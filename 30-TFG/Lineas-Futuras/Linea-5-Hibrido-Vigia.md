# Línea 5 · Híbrido con vigía: la red cuando la ventana llegó entera, CSP+LDA cuando llegó con hueco

> Nota de línea futura · 2026-09-27 · Sesión autónoma. Estado: **prototipo fuera de línea implementado y evaluado sobre las 855 ejecuciones de E2** en la notebook (rama `feat/robustez-modelo` del worktree `bci-fault-bench-futuro-robustez`); la integración en línea queda **diseñada, no implementada** (sección 5). Decisiones en [[_decisions-robustez]] (DA-R12, DA-R13). Línea hermana: [[Linea-4-Endurecer-EEGNet]].

## 1. Qué pregunta responde

E2 mostró dos decodificadores con fortalezas complementarias: EEGNet rinde más en la referencia (0,750 contra 0,708 de CSP+LDA) pero cae al azar con cualquier corte dentro de la ventana del ensayo (0,583 / 0,583 / 0,500), mientras CSP+LDA solo pierde en la severidad máxima (0,667). La pregunta es de ingeniería, no de modelos: **si el pipeline ya sabe, por su propia telemetría, que la ventana llegó con un hueco, ¿alcanza con elegir el decodificador en el momento de la decisión para quedarse con lo mejor de cada uno?** Y, del lado del objetivo 5 de la tesis: un detector de salud que no solo avisa sino que **actúa**.

## 2. Diseño

Por ensayo, antes de decodificar, un **vigía** lee dos señales de la ventana [2, 6) s (ambas salen de las marcas de tiempo de las muestras recibidas, que el consumidor ya tiene en el búfer):

- `n_samples`: muestras presentes en la ventana (1000 si llegó completa a 250 Hz);
- `max_gap_ms`: mayor intervalo entre muestras presentes **contando los bordes de la ventana** (un hueco que empieza en el borde, como la desconexión en el ensayo, también cuenta).

| Regla | La ventana va a EEGNet si… | Si no |
|---|---|---|
| `complete` | `n_samples == 1000` | CSP+LDA |
| `gap40` | `max_gap_ms <= 40` (un bloque de transporte de 10 muestras) | CSP+LDA |
| `gap200` | `max_gap_ms <= 200` | CSP+LDA |

Cada regla se probó con la EEGNet original (`hybrid_<regla>`) y con la endurecida de la Línea 4 (`hybrid_<regla>_gapaug`). La rama CSP usa la decisión de CSP+LDA fuera de línea sobre el mismo segmento (DA-R13). La regla de validez no cambia (125 muestras en la ventana).

## 3. Resultados

Celda: mediana entre sujetos de la balanced accuracy (cada sujeto = mediana de sus 5 corridas) con (p Holm; r) contra la referencia **de la propia columna**. n = 9 sujetos en todas las columnas.

| Condición | CSP en línea | CSP fuera de línea | EEGNet | híbrido `complete` | híbrido `gap40` | híbrido `gap200` | híbrido `gap40` + gapaug |
|:--|:--|:--|:--|:--|:--|:--|:--|
| referencia | 0,708 | 0,708 | 0,750 | 0,750 | 0,750 | 0,750 | 0,833 |
| pérdida de muestras 0,01 | 0,708 (,750; 0,38) | 0,708 (,812; 0,11) | 0,750 (1; 0,22) | **0,708** (,477; 0,24) | 0,750 (1; 0,22) | 0,750 (1; 0,22) | 0,792 (1; 0,22) |
| pérdida de muestras 0,05 | 0,708 (1; 0,11) | 0,708 (,188; 0,62) | 0,750 (1; 0,11) | **0,708** (,117; 0,69) | 0,750 (1; 0,11) | 0,750 (1; 0,11) | 0,792 (1; 0,00) |
| desconexión 0,5 / 1 / 3 s | 0,708 / 0,708 / 0,708 | 0,708 / 0,708 / 0,708 | 0,750 / 0,750 / 0,750 | 0,792 / 0,750 / 0,792 | 0,792 / 0,750 / 0,792 | 0,792 / 0,750 / 0,792 | 0,792 / 0,792 / 0,833 |
| pérdida contigua 0,10 | 0,708 (,375; 0,30) | 0,708 (,250; 0,38) | 0,750 (,594; 0,19) | 0,708 (,344; 0,43) | 0,708 (,344; 0,43) | 0,708 (,344; 0,43) | 0,708 (,641; 0,24) |
| pérdida contigua 0,25 | 0,750 (,250; 0,51) | 0,750 (,250; 0,51) | 0,750 (,594; 0,35) | 0,750 (,344; 0,46) | 0,750 (,344; 0,46) | 0,750 (,344; 0,46) | 0,750 (,641; 0,33) |
| pérdida contigua 0,40 | 0,667 (,012; 0,96) | 0,667 (,023; 0,89) | 0,708 (,023; 0,89) | 0,667 (,023; 0,89) | 0,667 (,023; 0,89) | 0,667 (,023; 0,89) | 0,667 (,047; 0,81) |
| desconexión en el ensayo 0,5 s | 0,750 (,062; 0,72) | 0,667 (,016; 0,89) | **0,583** (,012; 0,96) | **0,667** (,012; 0,96) | **0,667** (,012; 0,96) | **0,667** (,012; 0,96) | **0,667** (,012; 0,96) |
| desconexión en el ensayo 1 s | 0,750 (,062; 0,72) | 0,667 (,016; 0,89) | **0,583** (,012; 0,96) | **0,667** (,012; 0,96) | **0,667** (,012; 0,96) | **0,667** (,012; 0,96) | **0,667** (,012; 0,96) |
| desconexión en el ensayo 2 s | 0,667 (,012; 0,96) | 0,667 (,012; 0,96) | **0,500** (,012; 0,96) | **0,667** (,012; 0,89) | **0,667** (,012; 0,89) | **0,667** (,012; 0,89) | **0,667** (,031; 0,72) |

Jitter y retraso: sin diferencias en ninguna columna (todas iguales a su referencia, p = 1). Pérdida de muestras 0,10 y desconexión uniforme: sin diferencias significativas. Tabla completa (19 condiciones) en `results/robustez/tabla_variantes_hibrido.md`.

**Desempeño sin fallo** (ensayos válidos de las 5 corridas de referencia por sujeto, agrupados; mediana de 9 sujetos): CSP 0,725 · EEGNet 0,742 · híbridos con EEGNet original 0,742 · híbrido `gap40` + gapaug 0,808. Ningún ensayo de la referencia se envía a CSP con ninguna regla: **el vigía no tiene falsas alarmas en limpio**.

### 3.1 Ruteo: fracción de ensayos válidos enviados a CSP+LDA

| Condición | `complete` | `gap40` | `gap200` |
|:--|--:|--:|--:|
| referencia, jitter (3), retraso (3) | 0,000 | 0,000 | 0,000 |
| pérdida de muestras 0,01 / 0,05 / 0,10 | **1,000** / 1,000 / 1,000 | 0,000 / 0,000 / 0,000 | 0,000 / 0,000 / 0,000 |
| desconexión 0,5 / 1 / 3 s | 0,069 / 0,062 / 0,079 | 0,069 / 0,060 / 0,078 | 0,065 / 0,057 / 0,071 |
| pérdida contigua 0,10 / 0,25 / 0,40 | 1,000 / 1,000 / 1,000 | 1,000 / 1,000 / 1,000 | 1,000 / 1,000 / 1,000 |
| desconexión en el ensayo 0,5 / 1 / 2 s | 1,000 / 1,000 / 1,000 | 1,000 / 1,000 / 1,000 | 1,000 / 1,000 / 1,000 |

### 3.2 Lectura

1. **Sí recupera el nivel de CSP bajo desconexión en el ensayo sin perder el de la red en la referencia.** Con cualquier regla, el híbrido pasa de 0,583 / 0,583 / 0,500 (EEGNet) a 0,667 / 0,667 / 0,667, y mantiene 0,750 en la referencia y en jitter/retraso. Con la red endurecida de la Línea 4 la mediana de la referencia figura 0,833 y la caída bajo corte queda en el mismo 0,667; ojo: ese 0,833 es un efecto de la mediana de medianas, porque apareado por sujeto la red endurecida no mejora la referencia (diferencia mediana 0,000; 3 sujetos mejoran y 3 empeoran; p = 1). Contra EEGNet, apareado por sujeto, el híbrido `gap40` gana en el corte de 2 s en 8 de 9 sujetos (+0,083, Wilcoxon sin corregir p = ,008) y no pierde ninguno en la referencia.
2. **Sigue habiendo diferencia significativa contra su propia referencia** (p Holm = ,012), porque la referencia del híbrido es la de la red (0,750) y bajo corte decide CSP (0,667): el híbrido hereda el piso de CSP, no lo supera. La caída (mediana de las diferencias por sujeto contra la referencia) se achica de −0,125 / −0,125 / −0,208 (EEGNet) a −0,083 / −0,083 / −0,083 (`gap40`); con la red endurecida, de −0,083 / −0,083 / −0,167 (`gapaug` sola) a −0,083 / −0,083 / −0,125.
3. **La regla `complete` es demasiado sensible**: la pérdida aleatoria de muestras sueltas (1 %) deja todas las ventanas con menos de 1000 muestras y el híbrido manda el 100 % a CSP, bajando a 0,708 sin necesidad (EEGNet no perdía nada ahí). `gap40` y `gap200` dan resultados idénticos en esta campaña: los huecos de la pérdida aleatoria son de 8-12 ms y los estructurados de 404 ms en adelante, no hay nada entre medio. **Regla recomendada: `gap40`**, por ser la menos arbitraria (un bloque de transporte) y la que más temprano detecta.
4. **Donde el híbrido pierde**: pérdida contigua 0,40 (1,6 s en posición aleatoria), EEGNet original 0,708 y el híbrido 0,667, porque CSP cae igual. Con la red endurecida es peor: `gapaug` sola ya había recuperado esa condición (0,708, p = ,328) y el híbrido la manda a CSP (0,667, p = ,047). El vigía decide por "hay hueco", no por "este hueco daña a la red": un hueco a mitad de ventana no daña a la red endurecida y el vigía igual la aparta (ver la sonda de posición en [[Linea-4-Endurecer-EEGNet]]).

## 4. Límites

- Es un prototipo fuera de línea sobre los segmentos guardados; ambos decodificadores son deterministas, así que la decisión es la que habría salido en vivo, **salvo la latencia**, que no se midió en el pipeline (sección 5).
- La rama CSP es la fuera de línea (grilla con ceros); en línea CSP filtra la señal compactada y en desconexión en el ensayo de 0,5 y 1 s dio 0,750, mejor que 0,667. Un híbrido en línea usaría esa cadena y probablemente rendiría algo más: no se afirma sin medirlo.
- El umbral de 40 ms está atado a este transporte (bloques de 10 muestras cada 40 ms).
- Los huecos de la campaña no ejercitan la zona entre 40 y 200 ms; no se puede elegir entre `gap40` y `gap200` con estos datos.

## 5. Integración en línea (diseño, no implementado)

**Dónde lee el vigía.** En `consumer.py`, dentro de `_decode(onset)`: `_segment()` ya devuelve `ts` (marcas de tiempo de las muestras recibidas en [onset+1, onset+7) s). El vigía es una función pura de `ts` que corre **antes** de filtrar:

```python
def sentinel(ts, onset, sf=250.0):
    w = ts[(ts >= onset + data.TMIN) & (ts < onset + data.TMAX)]
    edges = np.concatenate([[onset + data.TMIN - 1 / sf], w, [onset + data.TMAX]])
    return len(w), float(np.diff(edges).max() * 1e3)        # n_samples, max_gap_ms
```

`_decode` pasa a elegir: si `max_gap_ms <= 40` → grilla nominal + filtro + EEGNet; si no → filtro de la señal compactada + CSP+LDA (la cadena actual). La fila de `trials.csv` suma dos columnas, `route` (`net`/`csp`) y `max_gap_ms`, para que el análisis pueda separar los ensayos por rama. La telemetría por segundo (`telemetry.csv`) no sirve para esto: tiene resolución de 1 s y no se alinea con la ventana del ensayo (DA-R12).

**Qué cuesta.** Ambos modelos cargados a la vez: 18 kB (EEGNet, *state dict*) + 10 kB (CSP+LDA) por sujeto, más el import de torch (del orden de cientos de MB de memoria del proceso, el costo real). Latencia medida en la notebook (CPU, 1 ventana, promedio de 200 llamadas, con otros entrenamientos corriendo): vigía 0,06 ms · filtro 8-30 Hz de 22 × 1500 muestras 13,5 ms · EEGNet 6,0 ms · CSP+LDA 1,2 ms. El vigía es gratis frente a la decisión; la rama de la red suma ≈ 5 ms respecto de CSP, despreciable frente al ≈ 1 s de retraso de decisión que ya impone el relleno de 1 s del filtro.

**Los dos modos de falla del vigía.**

| Modo | Qué pasa | Qué cuesta | En E2 |
|---|---|---|---|
| **Falsa alarma**: ventana limpia enviada a CSP | se decide con el decodificador peor en limpio | si todo lo limpio fuera a CSP: 0,742 → 0,725 en la mediana limpia (−0,017; con la red endurecida, 0,808 → 0,725); en el sujeto 2 la falsa alarma incluso ayuda (CSP 0,617 vs EEGNet 0,492) | 0 % en referencia, jitter y retraso con `gap40`; 100 % de la pérdida aleatoria con `complete` |
| **Omisión**: ventana con hueco enviada a la red | la red decide sobre ceros | hasta −0,250 (EEGNet original, corte de 2 s) | 0 % con cualquier regla: todos los huecos estructurados miden ≥ 404 ms |

La asimetría de costos (falsa alarma barata, omisión cara) justifica un umbral bajo: `gap40`.

**Vínculo con el objetivo 5 (detectores).** El vigía es un detector de salud **por ensayo** con umbral fijo sobre la temporalidad del flujo, del mismo tipo que el detector por umbrales de E2 pero con otra granularidad (ensayo en lugar de segundo) y otra salida (una acción en lugar de una alarma). E2 mostró que el estado operativo por segundo diverge de la degradación funcional ("parece sano y decodifica mal"); el vigía ataca justamente esa divergencia desde el lado del pipeline: no intenta predecir la degradación, sino **evitar el decodificador que se degrada con esa falla concreta**. Es la traducción práctica de la conclusión de E2 de que la calidad del flujo sola no alcanza para saber si la decisión es buena: se usa para decidir **qué** decodificador es confiable con ese flujo.

## 6. Esfuerzo y reproducción

| Tarea | Estado | Esfuerzo restante |
|---|---|---|
| Vigía + híbrido fuera de línea, 3 reglas × 2 redes, análisis | hecho | — |
| Vigía en `consumer.py` (función pura + rama + 2 columnas) | diseñado | 0,5 día + prueba de humo |
| Campaña en línea del híbrido (VM) | pendiente | 9 × 5 × (referencia + 2 fallas estructuradas × 3) ≈ 315 ejecuciones ≈ 3 h con 12 workers |

En la notebook (no hace falta la VM), desde el worktree, después de los pasos de la Línea 4:

```bash
PY=../TESIS/TESIS/40-Prototipo/.venv/Scripts/python.exe
PYTHONPATH=src $PY scripts/hybrid_decoder.py --root results/campana2-eval --out results/robustez
for v in hybrid_complete hybrid_gap40 hybrid_gap200 hybrid_complete_gapaug hybrid_gap40_gapaug hybrid_gap200_gapaug; do
  PYTHONPATH=src $PY scripts/analyze.py --root results/campana2-eval --out results/analysis-$v \
    --window 8 --thr-rule min --trials-file trials_$v.csv --perf-only
done
PYTHONPATH=src $PY scripts/compare_variants.py --variants csp_online csp_offline eegnet eegnet_gapaug \
  hybrid_complete hybrid_gap40 hybrid_gap200 hybrid_gap40_gapaug --tag _hibrido
```

## Enlaces

- Código: `scripts/hybrid_decoder.py`, `scripts/redecode_variants.py` (escribe `trials_sentinel.csv`), `scripts/compare_variants.py`.
- Salidas: `results/robustez/tabla_variantes_hibrido.md`, `ruteo.md`, `ruteo_por_ejecucion.csv`.
- [[Linea-4-Endurecer-EEGNet]] · [[_decisions-robustez]] · [[_propuestas-robustez]] · [[_research-robustez]] · [[Trabajo-Futuro]]
