"""Figuras conceptuales y de resultados agregadas al Entregable 2 (versión con figuras).

Genera en fig/ ocho PNG en blanco y negro, con la misma tipografía serif que las
figuras del análisis. Las figuras de resultados (reconexión, retardo, divergencia)
leen sus cifras de numeros.json, de modo que se regeneran con los datos.

Uso:  python figuras.py
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

HERE = Path(__file__).parent
OUT = HERE / "fig"
N = json.loads((HERE / "numeros.json").read_text(encoding="utf-8"))

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 12,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "savefig.dpi": 300,
})
GRIS = "#d9d9d9"
GRIS_CLARO = "#f0f0f0"


def nums(key: str) -> list[float]:
    """'1.561, 1.560 y 3.598' -> [1561.0, 1560.0, 3598.0] (formato es-AR)."""
    txt = N[key].replace(" y ", ", ")
    return [float(t.strip().replace(".", "").replace(",", ".")) for t in txt.split(",")]


def lienzo(w_in: float, h_in: float, xmax: float = 100, ymax: float = 60):
    fig, ax = plt.subplots(figsize=(w_in, h_in))
    ax.set_xlim(0, xmax)
    ax.set_ylim(0, ymax)
    ax.axis("off")
    return fig, ax


def caja(ax, x, y, w, h, titulo, sub=None, fill="white", lw=1.0, dashed=False, size=12):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.8",
                                fc=fill, ec="black", lw=lw, ls="--" if dashed else "-"))
    if sub:
        ax.text(x + w / 2, y + h * 0.62, titulo, ha="center", va="center", size=size, weight="bold")
        ax.text(x + w / 2, y + h * 0.30, sub, ha="center", va="center", size=size - 2)
    else:
        ax.text(x + w / 2, y + h / 2, titulo, ha="center", va="center", size=size, weight="bold")


def flecha(ax, x1, y1, x2, y2, dashed=False):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", lw=1.0, color="black", ls="--" if dashed else "-",
                                shrinkA=0, shrinkB=0))


def guardar(fig, nombre):
    fig.savefig(OUT / nombre, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("OK", nombre)


# ---------------------------------------------------------------- Introducción
def fig_etapas():
    fig, ax = lienzo(10, 2.6, 100, 29)
    etapas = [("Adquisición", "electrodos, EEG"), ("Transporte", "LSL"),
              ("Preprocesamiento", "filtrado, ventanas"), ("Decodificación", "modelo entrenado"),
              ("Decisión", "acción")]
    w, gap, x0, y = 17.2, 3, 1.0, 12
    for i, (t, s) in enumerate(etapas):
        x = x0 + i * (w + gap)
        caja(ax, x, y, w, 11, t, s, fill=GRIS if t == "Transporte" else "white",
             lw=2.0 if t == "Transporte" else 1.0, size=9.5)
        if i:
            flecha(ax, x - gap, y + 5.5, x, y + 5.5)
    xt = x0 + (w + gap)
    ax.text(xt + w / 2, 26.5, "fallos inyectados", ha="center", va="center", size=10, style="italic")
    flecha(ax, xt + w / 2, 25, xt + w / 2, 23.2)
    xa, xb = xt, x0 + 4 * (w + gap) + w
    ax.plot([xa, xa, xb, xb], [10.5, 8.5, 8.5, 10.5], color="black", lw=1)
    ax.text((xa + xb) / 2, 5.5, "cadena de software: objeto de estudio", ha="center", va="center", size=10)
    guardar(fig, "fig_etapas.png")


def fig_capas():
    fig, ax = lienzo(10, 5.4, 100, 54)
    filas = [  # capa, origen, efecto en la capa
        ("Adquisición", "dispositivo inalámbrico\nque pierde alcance", "elimina muestras"),
        ("Transporte", "red congestionada;\nconexión que se corta", "más latencia y\nvariabilidad; cortes"),
        ("Procesamiento", "consumidor demorado,\nbúfer lleno", "descarta las muestras\nmás antiguas"),
    ]
    ys = [40, 24, 8]
    for (capa, origen, efecto), y in zip(filas, ys):
        ax.text(0, y + 5, capa, ha="left", va="center", size=10, weight="bold")
        caja(ax, 16, y, 23, 10, "", fill="white")
        ax.text(27.5, y + 5, origen, ha="center", va="center", size=9.5)
        caja(ax, 42, y, 21, 10, "", fill=GRIS_CLARO)
        ax.text(52.5, y + 5, efecto, ha="center", va="center", size=9.5)
        flecha(ax, 39, y + 5, 42, y + 5)
        flecha(ax, 63, y + 5, 66, 27)
    caja(ax, 66, 16, 13, 22, "", fill=GRIS, lw=2.0)
    ax.text(72.5, 27, "Interfaz\nde entrada\ndel pipeline", ha="center", va="center", size=9.5, weight="bold")
    modelos = ["Pérdida de\nmuestras", "Jitter", "Retraso", "Desconexión"]
    for i, m in enumerate(modelos):
        y = 43 - i * 11
        caja(ax, 82.5, y, 17, 8, m, size=9.5)
        flecha(ax, 79, 27, 82.5, y + 4)
    ax.text(52.5, 52, "efecto en la capa", ha="center", va="center", size=10, style="italic")
    ax.text(27.5, 52, "origen", ha="center", va="center", size=10, style="italic")
    ax.text(91.5, 52, "modelo de fallo", ha="center", va="center", size=10, style="italic")
    guardar(fig, "fig_capas.png")


def _mapa(ax, celdas, resaltada):
    ax.text(58, 59, "Estado de la infraestructura", ha="center", va="center", size=12, weight="bold")
    ax.text(37, 52, "Operativa", ha="center", va="center", size=11)
    ax.text(79, 52, "No operativa", ha="center", va="center", size=11)
    ax.text(0, 57, "Función del\ndecodificador", ha="left", va="center", size=11, weight="bold")
    ax.text(0, 38, "No degradada", ha="left", va="center", size=11)
    ax.text(0, 14, "Degradada", ha="left", va="center", size=11)
    pos = {(0, 0): (17, 27), (1, 0): (59, 27), (0, 1): (17, 3), (1, 1): (59, 3)}
    for key, (x, y) in pos.items():
        titulo, sub = celdas[key]
        hi = key == resaltada
        caja(ax, x, y, 40, 22, "", fill=GRIS if hi else "white", lw=2.0 if hi else 1.0)
        ax.text(x + 20, y + 15, titulo, ha="center", va="center", size=11, weight="bold")
        ax.text(x + 20, y + 7.5, sub, ha="center", va="center", size=10)


def fig_mapa():
    fig, ax = lienzo(8.5, 5.4, 100, 63)
    _mapa(ax, {
        (0, 0): ("Concordancia", "funciona y decide bien"),
        (1, 0): ("Divergencia: interrupción", "no operativa, decide bien"),
        (0, 1): ("Divergencia: falla silenciosa", "operativa, decide mal"),
        (1, 1): ("Concordancia", "falla visible y decide mal"),
    }, resaltada=(0, 1))
    guardar(fig, "fig_mapa.png")


# ---------------------------------------------------------------- Métodos
def fig_banco():
    fig, ax = lienzo(10, 5.8, 100, 58)
    caja(ax, 1, 25, 42, 22, "", dashed=True)
    ax.text(2, 45, "proceso emisor", ha="left", va="center", size=9, style="italic")
    caja(ax, 51, 9, 48, 38, "", dashed=True)
    ax.text(52, 45, "proceso consumidor", ha="left", va="center", size=9, style="italic")
    caja(ax, 3, 29, 17, 12, "Reproducción", "MOABB, LSL", size=10)
    caja(ax, 24, 29, 17, 12, "Inyector", "fallo y semilla", fill=GRIS, lw=2.0, size=10)
    flecha(ax, 20, 35, 24, 35)
    caja(ax, 55, 29, 22, 12, "Pipeline bajo prueba", "ventanas, CSP + LDA", size=10)
    flecha(ax, 41, 35, 55, 35)
    ax.text(48, 37, "flujo EEG", ha="center", va="bottom", size=9)
    ax.plot([11.5, 11.5], [29, 23], color="black", lw=1, ls="--")
    ax.plot([11.5, 59], [23, 23], color="black", lw=1, ls="--")
    flecha(ax, 59, 23, 59, 29, dashed=True)
    ax.text(27, 22, "marcadores (no se perturban)", ha="center", va="top", size=9)
    caja(ax, 80, 29, 17, 12, "Decisiones", "por ensayo", size=10)
    flecha(ax, 77, 35, 80, 35)
    caja(ax, 55, 11, 22, 9, "Recolector", "telemetría por segundo", size=10)
    flecha(ax, 70, 29, 70, 20)
    caja(ax, 80, 11, 17, 9, "Segmentos", "señal recibida", size=10)
    flecha(ax, 74, 29, 84, 20)
    caja(ax, 55, 0, 22, 8, "Detectores", "fuera de línea", size=10)
    flecha(ax, 66, 11, 66, 8)
    caja(ax, 80, 0, 17, 8, "EEGNet", "fuera de línea", size=10)
    flecha(ax, 88.5, 11, 88.5, 8)
    caja(ax, 12, 50, 76, 7, "Ejecutor: orquesta condiciones, semillas y ejecuciones en paralelo", size=10)
    flecha(ax, 22, 50, 22, 47)
    flecha(ax, 75, 50, 75, 47)
    guardar(fig, "fig_banco.png")


def fig_ensayo():
    fig, ax = plt.subplots(figsize=(10, 4.4))
    ax.set_xlim(-0.3, 10.3)
    ax.set_ylim(0, 6.2)
    ax.spines["left"].set_visible(False)
    ax.set_yticks([])
    ax.set_xticks(range(0, 11))
    ax.set_xlabel("Tiempo desde el marcador de inicio del ensayo (s)")

    def barra(y, x0, x1, fill="white", hatch=None, lw=1.0, ls="-", label=None):
        ax.add_patch(Rectangle((x0, y - 0.3), x1 - x0, 0.6, fc=fill, ec="black", lw=lw, ls=ls, hatch=hatch))
        if label:
            ax.text((x0 + x1) / 2, y, label, ha="center", va="center", size=10)

    filas = {"ventana": 5.2, "decision": 4.2, "contigua": 3.0, "desconexion": 2.0, "uniforme": 1.0}
    etiquetas = {"ventana": "Ventana", "decision": "Decisión",
                 "contigua": "Pérdida contigua\nen el ensayo", "desconexion": "Desconexión\nen el ensayo",
                 "uniforme": "Familia uniforme"}
    for k, y in filas.items():
        ax.text(-0.4, y, etiquetas[k], ha="right", va="center", size=10)
    ax.axvline(0, color="black", lw=1)
    y = filas["ventana"]
    barra(y, 1, 2, GRIS_CLARO, label="relleno")
    barra(y, 2, 6, GRIS, lw=1.5, label="ventana de decisión (2 a 6 s)")
    barra(y, 6, 7, GRIS_CLARO, label="relleno")
    y = filas["decision"]
    ax.plot([7.03, 7.03], [y - 0.3, y + 0.3], color="black", lw=2)
    ax.text(6.9, y, "decisión (≈ 1 s tras el fin del ensayo)", ha="right", va="center", size=10)
    barra(y, 7.03, 10.03, "white", ls="--", label="plazo: 3 s para recibir datos")
    y = filas["contigua"]
    ax.plot([2, 6], [y, y], color="black", lw=0.6, ls=":")
    barra(y, 3.3, 4.3, "white", hatch="///", label="")
    ax.text(6.3, y, "un bloque de 0,4 a 1,6 s en posición aleatoria", ha="left", va="center", size=10)
    y = filas["desconexion"]
    barra(y, 2, 3, "white", hatch="xxx")
    ax.text(3.3, y, "corte de 0,5, 1 o 2 s desde el inicio de la ventana", ha="left", va="center", size=10)
    y = filas["uniforme"]
    for x0, x1 in [(0.6, 0.9), (4.6, 5.1), (8.2, 8.5)]:
        barra(y, x0, x1, "white", hatch="///")
    ax.text(9.0, y, "en cualquier instante", ha="left", va="center", size=10)
    ax.text(5.1, 0.25, "Decisión válida si quedan al menos 125 muestras (0,5 s) dentro de la ventana",
            ha="center", va="center", size=10, style="italic")
    guardar(fig, "fig_ensayo.png")


# ---------------------------------------------------------------- Resultados
def fig_reconexion():
    uni = [v / 1000 for v in nums("ia_max_disc3")]
    ens = [v / 1000 for v in nums("ia_max_disct")]
    fig, ax = plt.subplots(figsize=(6.5, 4.6))
    ax.plot([0, 3.4], [0, 3.4], color="black", lw=1, ls="--", label="Intervalo igual a la duración del corte")
    ax.plot([0.47, 0.97, 3], uni, marker="o", ms=8, color="black", lw=1, label="Desconexión (familia uniforme)")
    ax.plot([0.53, 1.03, 2], ens, marker="s", ms=8, color="black", lw=1, ls=":", mfc="white",
            label="Desconexión en el ensayo")
    ax.set_xlim(0, 3.4)
    ax.set_ylim(0, 4.0)
    ax.set_xticks([0, 0.5, 1, 2, 3])
    ax.set_xticklabels(["0", "0,5", "1", "2", "3"])
    ax.set_yticks([0, 1, 2, 3, 4])
    ax.set_xlabel("Duración del corte inyectado (s)")
    ax.set_ylabel("Intervalo máximo entre llegadas (s)")
    ax.legend(frameon=False, fontsize=10, loc="upper left")
    guardar(fig, "fig_reconexion.png")


def fig_retardo():
    ref = nums("dd_ref")[0]
    dly = nums("dd_delay")
    jit = nums("dd_jitter")
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4.2), sharey=True)
    x = [0, 50, 100, 250]
    a1.plot([0, 250], [ref, ref + 250], color="black", lw=1, ls="--", label="Referencia + retraso inyectado")
    a1.plot(x, [ref] + dly, marker="^", ms=8, color="black", lw=1, label="Observado")
    a1.set_xticks(x)
    a1.set_xticklabels(["ref.", "50", "100", "250"])
    a1.set_xlabel("Retraso inyectado (ms)")
    a1.set_ylabel("Retardo de decisión (ms)")
    a1.set_title("Retraso", size=12)
    a1.legend(frameon=False, fontsize=10, loc="upper left")
    xj = [0, 10, 50, 100]
    a2.plot(xj, [ref] + jit, marker="s", ms=8, color="black", lw=1)
    a2.set_xticks(xj)
    a2.set_xticklabels(["ref.", "10", "50", "100"])
    a2.set_xlabel("Desviación del jitter inyectado (ms)")
    a2.set_title("Jitter", size=12)
    a1.set_ylim(1000, 1320)
    guardar(fig, "fig_retardo.png")


def fig_divergencia():
    fig, ax = lienzo(8.5, 5.4, 100, 63)
    loud_e = N["loud_disct"].split(" y ")[-1]
    _mapa(ax, {
        (0, 0): ("Concordancia", "resto de las ventanas"),
        (1, 0): ("Divergencia: interrupción", f"hasta {loud_e} según la condición"),
        (0, 1): ("Divergencia: falla silenciosa", f"{N['silent_max']} en las 18 condiciones"),
        (1, 1): ("Concordancia", "no se cuantificó por separado"),
    }, resaltada=(0, 1))
    guardar(fig, "fig_divergencia.png")


CAMPANA = Path(r"C:\Users\agustin.tamagusuku\Desktop\bci-fault-bench\campaign-2026-09-27")
ORDEN = [("loss", "Pérdida de muestras", lambda s: f"{s*100:g} %"),
         ("jitter", "Jitter", lambda s: f"{s*1000:g} ms"),
         ("delay", "Retraso", lambda s: f"{s*1000:g} ms"),
         ("disconnect", "Desconexión", lambda s: f"{s:g} s".replace(".", ",")),
         ("burst_trial", "Pérdida contigua en el ensayo", lambda s: f"{s*100:g} %"),
         ("disconnect_trial", "Desconexión en el ensayo", lambda s: f"{s:g} s".replace(".", ","))]


def fig_desempeno():
    """Balanced accuracy de los dos decodificadores por tipo y severidad (mediana e
    intervalo intercuartílico entre sujetos); asterisco: p de Holm < 0,05."""
    import pandas as pd
    series = []
    for sub, etiqueta, estilo in [("analysis", "CSP y LDA", dict(marker="o", ls="-", mfc="black")),
                                  ("analysis-eegnet", "EEGNet", dict(marker="s", ls="--", mfc="white"))]:
        med = pd.read_csv(CAMPANA / sub / "medianas_por_sujeto.csv")
        tst = pd.read_csv(CAMPANA / sub / "t_desempeno.csv")
        series.append((med, tst, etiqueta, estilo))
    fig, axes = plt.subplots(2, 3, figsize=(10, 6.2), sharey=True)
    for ax, (kind, titulo, fmt) in zip(axes.flat, ORDEN):
        for k, (med, tst, etiqueta, estilo) in enumerate(series):
            ref = med[med.kind == "none"].bacc
            sub = med[med.kind == kind]
            sevs = sorted(sub.severity.unique())
            grupos = [ref] + [sub[sub.severity == s].bacc for s in sevs]
            y = [g.median() for g in grupos]
            lo = [g.median() - g.quantile(0.25) for g in grupos]
            hi = [g.quantile(0.75) - g.median() for g in grupos]
            x = [i + (k - 0.5) * 0.2 for i in range(len(grupos))]
            ax.errorbar(x, y, yerr=[lo, hi], color="black", capsize=3, lw=1, ms=6, label=etiqueta, **estilo)
            for i, s in enumerate(sevs, start=1):
                row = tst[(tst.kind == kind) & (abs(tst.severity - s) < 1e-9)]
                if len(row) and row.p_holm.iloc[0] < 0.05:
                    ax.text(x[i], y[i] + hi[i] + 0.03, "*", ha="center", va="bottom", size=14)
        ax.set_xticks(range(4))
        ax.set_xticklabels(["ref."] + [fmt(s) for s in sevs], size=9)
        ax.set_title(titulo, size=11)
        ax.set_ylim(0.3, 1.05)
    for ax in axes[:, 0]:
        ax.set_ylabel("Balanced accuracy")
    axes[0, 0].legend(frameon=False, fontsize=9, loc="lower left")
    fig.tight_layout()
    guardar(fig, "fig_desempeno.png")


if __name__ == "__main__":
    fig_desempeno()
    fig_etapas()
    fig_capas()
    fig_mapa()
    fig_banco()
    fig_ensayo()
    fig_reconexion()
    fig_retardo()
    fig_divergencia()
