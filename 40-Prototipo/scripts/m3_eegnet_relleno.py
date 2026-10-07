"""¿La fragilidad de EEGNet se debe a la arquitectura o a cómo se le entregan los huecos?

Re-evalúa EEGNet sobre los mismos segmentos guardados de la campaña definitiva con tres
formas de completar las muestras faltantes en la grilla nominal, antes de filtrar:
  ceros    la forma usada en el Entregable 2 (debe reproducir trials_eegnet.csv)
  interp   interpolación lineal por canal entre las muestras presentes
  hold     repetición de la última muestra presente (muestreo y retención, como el
           receptor de Simeral et al., 2021); las faltantes iniciales toman la primera presente
Misma regla de validez que en línea (al menos 125 muestras en la ventana).
No sobrescribe nada: escribe <exec>/trials_eegnet_<modo>.csv y un resumen en
results/vm/analysis-m3-eegnet/.

Uso: .venv/Scripts/python scripts/m3_eegnet_relleno.py --root results/vm/campana2 --models results/models
"""
import argparse
import csv
import glob
import os
import sys
import warnings

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from mne.filter import filter_data  # noqa: E402

from bcibench import data  # noqa: E402
from bcibench.eegnet import EEGNetDecoder  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("--root", required=True)
ap.add_argument("--models", required=True)
ap.add_argument("--out", default="results/vm/analysis-m3-eegnet")
a = ap.parse_args()

SF = data.SFREQ
TMIN, TMAX, PAD = data.TMIN, data.TMAX, 1.0
N_WIN = int(round((TMAX - TMIN) * SF))
N_PAD = int(round((TMAX - TMIN + 2 * PAD) * SF))
W0 = int(PAD * SF)
MODES = ("ceros", "interp", "hold")


def grid(ts_rel, x, n_ch):
    g = np.zeros((n_ch, N_PAD), dtype=np.float64)
    idx = np.round((ts_rel - (TMIN - PAD)) * SF).astype(int)
    ok = (idx >= 0) & (idx < N_PAD)
    g[:, idx[ok]] = x[ok].T
    present = np.zeros(N_PAD, dtype=bool)
    present[idx[ok]] = True
    return g, present


def fill(g, present, mode):
    if mode == "ceros" or present.all() or not present.any():
        return g
    pos = np.flatnonzero(present)
    out = g.copy()
    if mode == "interp":
        allpos = np.arange(N_PAD)
        for c in range(g.shape[0]):
            out[c] = np.interp(allpos, pos, g[c, pos])
        return out
    # hold: índice de la última presente a la izquierda (o la primera presente si no hay)
    last = np.maximum.accumulate(np.where(present, np.arange(N_PAD), -1))
    last[last < 0] = pos[0]
    return g[:, last]


nets = {}
os.makedirs(a.out, exist_ok=True)
dirs = sorted(glob.glob(os.path.join(a.root, "s*/")))
n = 0
for d in dirs:
    seg_p = os.path.join(d, "segments.npz")
    if not os.path.exists(seg_p):
        continue
    if all(os.path.exists(os.path.join(d, f"trials_eegnet_{m}.csv")) for m in MODES):
        n += 1
        continue
    subject = int(os.path.basename(d.rstrip("/\\")).split("-")[0][1:])
    if subject not in nets:
        nets[subject] = EEGNetDecoder.load(os.path.join(a.models, f"eegnet_s{subject:02d}.pkl"))
    net = nets[subject]
    z = np.load(seg_p)
    meta = z["meta"]
    rows = {m: [] for m in MODES}
    for k in range(len(meta)):
        onset, label = float(meta[k][0]), int(meta[k][1])
        ts, x = z[f"t{k}_ts"], z[f"t{k}_x"]
        rec = dict(onset=round(onset, 4), label=label)
        if len(ts) == 0:
            for m in MODES:
                rows[m].append(dict(rec, pred="", proba="", n_samples=0, valid=0))
            continue
        g, present = grid(ts.astype(float), x.astype(np.float64) * 1e-6, x.shape[1])
        n_in = int(present[W0:W0 + N_WIN].sum())
        valid = int(n_in >= int(0.5 * SF))
        for m in MODES:
            if not valid:
                rows[m].append(dict(rec, pred="", proba="", n_samples=n_in, valid=0))
                continue
            gf = filter_data(fill(g, present, m), SF, data.FMIN, data.FMAX, method="iir", verbose=False)
            pn = net.predict_proba(gf[:, W0:W0 + N_WIN][None].astype(np.float32))[0]
            rows[m].append(dict(rec, pred=int(net.classes[int(pn.argmax())]), proba=round(float(pn.max()), 4),
                                n_samples=n_in, valid=1))
    for m in MODES:
        with open(os.path.join(d, f"trials_eegnet_{m}.csv"), "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["onset", "label", "pred", "proba", "n_samples", "valid"])
            w.writeheader()
            w.writerows(rows[m])
    n += 1
    if n % 100 == 0:
        print(n, flush=True)
print("ejecuciones:", n)

# ---------------- resumen ----------------
from sklearn.metrics import balanced_accuracy_score  # noqa: E402


def parse(eid):
    s, r, *rest = eid.split("-")
    return int(s[1:]), r, "-".join(rest)


recs, trials = [], []
for d in dirs:
    eid = os.path.basename(d.rstrip("/\\"))
    if not os.path.exists(os.path.join(d, "trials_eegnet_ceros.csv")):
        continue
    subj, run, label = parse(eid)
    base = pd.read_csv(os.path.join(d, "trials_eegnet.csv")) if os.path.exists(os.path.join(d, "trials_eegnet.csv")) else None
    for m in MODES:
        t = pd.read_csv(os.path.join(d, f"trials_eegnet_{m}.csv"))
        t["mode"], t["subject"], t["run"], t["cond"] = m, subj, run, label
        trials.append(t)
        v = t[t.valid == 1]
        ba = balanced_accuracy_score(v.label, v.pred.astype(int)) if len(v) else np.nan
        same = np.nan
        if m == "ceros" and base is not None and len(base) == len(t):
            same = float((base.pred.astype(str) == t.pred.astype(str)).mean())
        recs.append(dict(exec_id=eid, subject=subj, run=run, cond=label, mode=m, bacc=ba, reproduce_e2=same))
E = pd.DataFrame(recs)
E.to_csv(os.path.join(a.out, "por_ejecucion.csv"), index=False)
T = pd.concat(trials, ignore_index=True)

# BA: mediana de las corridas por sujeto, luego mediana entre sujetos; diferencia contra la referencia
M = E.groupby(["cond", "mode", "subject"]).bacc.median().reset_index()
ref = M[M.cond == "ref"][["mode", "subject", "bacc"]].rename(columns={"bacc": "ref"})
M = M.merge(ref, on=["mode", "subject"])
M["diff"] = M.bacc - M.ref
res = M.groupby(["cond", "mode"]).agg(bacc=("bacc", "median"), diff=("diff", "median")).reset_index()
tab_ba = res.pivot(index="cond", columns="mode", values="diff").round(3)
tab_ba.to_csv(os.path.join(a.out, "diferencia_bacc.csv"))

# Cambio de decisión respecto del mismo ensayo en la referencia, por fracción de ventana recibida
refT = T[T.cond == "ref"][["mode", "subject", "run", "onset", "pred"]].rename(columns={"pred": "pred_ref"})
J = T[T.cond != "ref"].merge(refT, on=["mode", "subject", "run", "onset"], how="inner")
J["cambio"] = (J.pred.astype(str) != J.pred_ref.astype(str)).astype(float)
bins = [-1, 124, 499, 749, 899, 999, 1000]
labels = ["inválido", "125-499", "500-749", "750-899", "900-999", "1000"]
J["bin"] = pd.cut(J.n_samples, bins=bins, labels=labels)
tab_dosis = (J.groupby(["bin", "mode"], observed=True).cambio.mean() * 100).unstack().round(1)
tab_dosis.to_csv(os.path.join(a.out, "dosis_cambio.csv"))
J.groupby(["cond", "mode"]).cambio.mean().unstack().mul(100).round(1).to_csv(os.path.join(a.out, "cambio_por_condicion.csv"))

print("\nreproduce el E2 (ceros vs trials_eegnet.csv):", round(E[E["mode"] == "ceros"].reproduce_e2.mean(), 4))
print("\n% de decisiones que cambian respecto de la referencia, por muestras recibidas:\n", tab_dosis)
print("\nDiferencia de balanced accuracy contra la referencia (mediana entre sujetos):\n", tab_ba)
