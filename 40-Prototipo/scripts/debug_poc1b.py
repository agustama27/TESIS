import sys, warnings; warnings.filterwarnings("ignore")
sys.path.insert(0, "src")
import numpy as np, mne
from bcibench import data
from moabb.paradigms import MotorImagery
from moabb.datasets import BNCI2014_001
sd = data.load_subject(1)
raw = sd["0train"]["0"]
ep = data.epochs_of(raw)
print("mine run0: n=", len(ep), "drop reasons:", [d for d in ep.drop_log if d][:5])
print("mine y:", ep.events[:,2][:12])
p = MotorImagery(n_classes=2, events=["left_hand","right_hand"], fmin=8, fmax=30)
X, y, meta = p.get_data(BNCI2014_001(), subjects=[1])
print("meta cols:", list(meta.columns), "runs:", meta.run.unique()[:6])
m = (meta.session=="0train") & (meta.run==meta.run.unique()[0])
Xm, ym = X[m], y[m]
print("moabb run0: n=", len(ym), "y:", ym[:12])
Xe = ep.get_data(copy=False)
print("shapes mine/moabb:", Xe.shape, Xm.shape)
n = min(len(Xe), len(Xm))
print("max abs diff first trial:", np.max(np.abs(Xe[0]-Xm[0])), " scale:", np.max(np.abs(Xm[0])))
print("corr first trial ch0:", np.corrcoef(Xe[0,0], Xm[0,0])[0,1])
# probar con tmin/tmax de MOABB internos
print("paradigm tmin/tmax:", p.tmin, p.tmax, "dataset interval:", BNCI2014_001().interval)
