# Línea 4 · Endurecer EEGNet: ¿la fragilidad ante cortes es por los ceros o por lo que se pierde?

> Nota de línea futura · 2026-09-27 · Sesión autónoma. Estado: **implementado y evaluado fuera de línea en la notebook** sobre los segmentos de las 855 ejecuciones de E2 (rama `feat/robustez-modelo` del worktree `bci-fault-bench-futuro-robustez`; no hace falta la VM). Decisiones en [[_decisions-robustez]] (DA-R1 a DA-R11, DA-R14). Fuentes en [[_research-robustez]]. Línea hermana: [[Linea-5-Hibrido-Vigia]].

## 1. Qué pregunta responde

En E2, EEGNet cae al azar con **cualquier** corte dentro de la ventana del ensayo (desconexión en el ensayo 0,5 / 1 / 2 s → 0,583 / 0,583 / 0,500 contra 0,750 de referencia, p Holm = ,012) mientras CSP+LDA solo pierde en la severidad máxima (0,667). La hipótesis de trabajo era que la red recibe **ceros** donde falta señal (tensor de tamaño fijo en la grilla nominal) y nunca vio silencios al entrenar, mientras CSP usa la covarianza de las muestras presentes. Si fuera así, habría tres remedios baratos: enseñarle huecos (aumento), no darle ceros (relleno alternativo) o decirle dónde está el hueco (canal máscara). La línea los prueba y, de paso, pone a prueba la hipótesis.

## 2. Método

**Control.** Antes de cualquier variante se re-decodificó con la cadena nueva el EEGNet original: 0 diferencias ensayo por ensayo en 20.520 ensayos y `t_desempeno.md` idéntico byte a byte al de E2; lo mismo para CSP+LDA en línea (DA-R3).

**Cadena de inferencia (igual para todas las variantes).** Muestras recibidas → grilla nominal [1, 7) s a 250 Hz → relleno de las posiciones faltantes → filtro IIR 8-30 Hz → recorte [2, 6) s (1000 muestras) → estandarización por canal → red. Regla de validez: 125 muestras en la ventana.

| Variante | Modelo | Relleno | Qué se entrena distinto | Sujetos |
|---|---|---|---|---|
| `eegnet` (control) | original | ceros | — | 9/9 |
| `eegnet_fill_interp` | original | interpolación lineal por canal (bordes: valor más cercano), en crudo antes del filtro | nada (solo inferencia) | 9/9 |
| `eegnet_fill_hold` | original | retención de la última muestra (hueco inicial: primer valor presente), en crudo antes del filtro | nada (solo inferencia) | 9/9 |
| `eegnet_gapaug` | aumentado | ceros | en cada época, cada ensayo con p = 0,5 pierde **un** tramo contiguo de U(0,4; 1,6) s en posición uniforme dentro de la ventana, borrado en **crudo** (0 V) antes del filtro | 9/9 |
| `eegnet_gapaug_fill_interp` | aumentado | interpolación | ídem | 9/9 |
| `eegnet_gapaug_wide` | aumentado | ceros | ídem con U(0,4; 2,6) s (cubre el corte de 2 s, que mide 2,52 s) | 9/9 |
| `eegnet_mask` | aumentado + máscara | ceros | canal 23 = 1 donde falta la muestra (mu = 0, sd = 1, sin filtrar); la convolución espacial abarca las 23 filas; mismo aumento que `gapaug` | 9/9 (1, 5 y 8 primero; se extendió porque alcanzó el tiempo) |

Todo lo demás igual que `eegnet.train`: sesión `0train` (144 ensayos izquierda/derecha sin artefactos), 300 épocas, semilla 0, Adam 1e-3, lote 32, F1 = 8, D = 2, F2 = 16. **Diferencia declarada** (DA-R5): las variantes aumentadas ven ventanas filtradas por ensayo, como en inferencia; el original se entrenó con la corrida continua filtrada.

**Por qué el hueco se borra en crudo.** En inferencia la muestra faltante vale 0 V antes del filtro. Se verificó el temor de que tras estandarizar valiera −mu/sd ≠ 0: con la señal filtrada 8-30 Hz, **max |mu/sd| = 7·10⁻⁴**, así que el silencio estandarizado es ≈ 0. Lo que sí importa es el transitorio del filtro en los bordes del hueco, y solo borrando en crudo el entrenamiento lo reproduce (DA-R4).

**Presupuesto usado.** Un entrenamiento midió 354 s (sujeto 1, con la re-decodificación corriendo al lado). Total: `gapaug` 46 min, `mask` 44 min, `gapaug_wide` 37 min de proceso (suma de `seconds_train`), en dos procesos paralelos de 5 hilos: **≈ 65 min de reloj** para 27 modelos. Re-decodificar las 855 ejecuciones: 2-7 min por tanda; `analyze.py --perf-only`: ≈ 20 s por variante.

## 3. Resultados

### 3.1 Tabla comparativa (condiciones con hueco en la ventana y referencia)

Celda: mediana entre sujetos de la balanced accuracy (cada sujeto = mediana de sus 5 corridas) con (p Holm; r) contra la referencia **de la propia variante**. n = 9 sujetos en todas las columnas. Jitter, retraso, pérdida aleatoria y desconexión uniforme: ninguna variante difiere de su referencia (p Holm ≥ ,375); tabla completa de 19 filas en `results/robustez/tabla_variantes.md`.

| Condición | CSP en línea | CSP fuera de línea | EEGNet | `gapaug` | `fill_interp` | `fill_hold` | `gapaug` + interp | `mask` | `gapaug_wide` |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| referencia | 0,708 | 0,708 | 0,750 | 0,833 | 0,750 | 0,750 | 0,833 | 0,833 | 0,750 |
| pérdida contigua 0,10 | 0,708 (,375; 0,30) | 0,708 (,250; 0,38) | 0,750 (,594; 0,19) | 0,792 (,562; 0,22) | 0,750 (,438; 0,26) | 0,750 (,875; 0,05) | 0,792 (,188; 0,51) | 0,792 (,562; 0,19) | 0,750 (,375; 0,30) |
| pérdida contigua 0,25 | 0,750 (,250; 0,51) | 0,750 (,250; 0,51) | 0,750 (,594; 0,35) | 0,708 (,562; 0,36) | 0,750 (,172; 0,57) | 0,750 (,625; 0,34) | 0,750 (,188; 0,56) | 0,708 (,562; 0,36) | 0,750 (,188; 0,56) |
| pérdida contigua 0,40 | 0,667 (**,012**; 0,96) | 0,667 (**,023**; 0,89) | 0,708 (**,023**; 0,89) | 0,708 (,328; 0,53) | 0,667 (**,023**; 0,89) | 0,708 (**,023**; 0,89) | 0,667 (,188; 0,62) | 0,708 (,422; 0,49) | 0,708 (**,023**; 0,89) |
| desconexión en el ensayo 0,5 s | 0,750 (,062; 0,72) | 0,667 (**,016**; 0,89) | 0,583 (**,012**; 0,96) | 0,583 (**,012**; 0,96) | 0,583 (**,012**; 0,96) | 0,625 (**,012**; 0,96) | 0,583 (**,023**; 0,89) | 0,667 (,094; 0,66) | 0,583 (**,012**; 0,96) |
| desconexión en el ensayo 1 s | 0,750 (,062; 0,72) | 0,667 (**,016**; 0,89) | 0,583 (**,012**; 0,96) | 0,583 (**,012**; 0,96) | 0,583 (**,012**; 0,96) | 0,625 (**,012**; 0,96) | 0,583 (**,023**; 0,89) | 0,667 (,094; 0,66) | 0,583 (**,012**; 0,96) |
| desconexión en el ensayo 2 s | 0,667 (**,012**; 0,96) | 0,667 (**,012**; 0,96) | 0,500 (**,012**; 0,96) | 0,542 (**,012**; 0,96) | 0,542 (**,012**; 0,96) | 0,500 (**,012**; 0,96) | 0,542 (**,023**; 0,89) | 0,583 (**,023**; 0,89) | 0,542 (**,012**; 0,96) |

### 3.2 Contra EEGNet, apareado por sujeto

La mediana de medianas engaña (la referencia de `gapaug` figura 0,833 contra 0,750). Apareado por sujeto (`results/robustez/tabla_vs_base.md`; diferencia mediana, sujetos que mejoran/empeoran, Wilcoxon sin corregir):

| Condición | `gapaug` | `mask` | `gapaug_wide` | `fill_hold` |
|:--|:--|:--|:--|:--|
| referencia | +0,000 (3/3; p = 1) | +0,000 (4/1; p = ,500) | +0,000 (4/2; p = ,281) | +0,000 (0/0) |
| pérdida contigua 0,40 | **+0,042 (8/1; p = ,027)** | +0,042 (5/1; p = ,125) | +0,000 (4/2; p = ,250) | +0,000 (1/1) |
| desconexión en el ensayo 0,5 s | +0,000 (3/2; p = ,312) | +0,042 (5/3; p = ,164) | +0,000 (3/4; p = ,688) | +0,000 (1/2) |
| desconexión en el ensayo 2 s | +0,042 (7/2; p = ,070) | +0,042 (6/2; p = ,227) | +0,042 (6/3; p = ,098) | +0,000 (1/1) |

**Desempeño sin fallo** (ensayos válidos de las 5 corridas de referencia, agrupados por sujeto; mediana de 9): EEGNet 0,742 · `gapaug` 0,808 · `mask` 0,800 · `gapaug_wide` 0,775 · rellenos 0,742 (idénticos al control: sin hueco no hay nada que rellenar) · CSP 0,725. **El endurecimiento no cuesta desempeño limpio**; tampoco lo mejora de forma demostrable (apareado: 3/3 sujetos en `gapaug`).

### 3.3 Por qué los rellenos no cambian nada: el filtro

Tras el filtro 8-30 Hz, cualquier relleno suave se vuelve ≈ 0 dentro del hueco: el RMS en el interior del hueco (a más de 0,4 s de una muestra presente) dividido por el RMS de la señal presente es **0,001** para ceros, interpolación y retención por igual (30 ejecuciones de pérdida contigua 0,4 y corte de 2 s). Una recta o una constante no tienen energía en 8-30 Hz. Solo difieren los 0,4 s junto a los bordes (0,13 / 0,13 / 0,15). **Rellenar antes de filtrar es, para la red, poner ceros con otro borde.** Por eso `fill_interp` y `fill_hold` repiten al control (salvo ±1 ensayo).

### 3.4 La sonda de posición: el problema no son los ceros, es lo que se pierde al principio

Los huecos de la campaña no son iguales (medidos en `trials_sentinel.csv`): la pérdida contigua borra 0,40 / 1,00 / 1,60 s en posición **aleatoria**; la desconexión en el ensayo borra 1,52 / 1,52 / 2,52 s **siempre al inicio** de la ventana (arranca a los 2,00-2,04 s del cue). `gapaug` recuperó la pérdida contigua de 1,60 s pero no la desconexión de 1,52 s, que está **dentro** de su rango de entrenamiento. Para aislar la posición se borró 1,52 s de la sesión 2 limpia al inicio, al medio o al final de la ventana (`scripts/gap_position_probe.py`, mediana de 9 sujetos):

| Decodificador | sin hueco | hueco al inicio | al medio | al final |
|:--|--:|--:|--:|--:|
| CSP+LDA (muestras presentes) | 0,722 | 0,715 | 0,660 | 0,715 |
| EEGNet | 0,750 | **0,604** | 0,750 | 0,701 |
| `gapaug` | 0,785 | **0,660** | 0,778 | 0,785 |
| `gapaug_wide` | 0,757 | 0,625 | 0,736 | 0,743 |
| `mask` | 0,806 | 0,674 | 0,708 | 0,785 |

EEGNet no pierde nada con 1,52 s de ceros **a mitad** de ventana y pierde 0,146 con los mismos ceros **al inicio**. La red apoya su decisión en el primer tramo de la imaginería (2 a 3,5 s desde el cue) y CSP, que integra la varianza de toda la ventana, no. La hipótesis "no vio silencios" explica una parte (el aumento sube el caso "inicio" de 0,604 a 0,660 y elimina el daño en posición aleatoria), pero la causa principal de la caída bajo desconexión en el ensayo es **pérdida de información en el tramo que la red usa**, no la forma de rellenarlo.

### 3.5 Por sujeto (condiciones estructuradas)

- **Corte de 2 s**: CSP+LDA decide mejor que EEGNet en 8 de 9 sujetos (empate en el 5). Sujeto 9: 0,417 con EEGNet, 0,708 con CSP (−0,29); `gapaug` no lo mueve (0,417), la máscara lo empeora (0,375). Sujeto 8: `gapaug` lo lleva de 0,583 a 0,792, igual que CSP.
- **Corte de 0,5 s**: la máscara ayuda justo donde EEGNet más pierde (sujeto 9: 0,667 → 0,875; sujeto 7: 0,542 → 0,667; sujeto 2: 0,458 → 0,583), y empeora levemente a 1 y 8.
- **Pérdida contigua 0,40**: `gapaug` mejora a 8 de 9 sujetos (solo empeora el 7: 0,708 → 0,667).
- **Referencia**: el sujeto 7 pierde con todas las variantes aumentadas (0,750 → 0,667 / 0,625 / 0,708) y el 4 gana (0,708 → 0,833): el efecto neto es nulo.

## 4. Recomendación

**Entrenar con huecos NO elimina la fragilidad frente a la desconexión dentro del ensayo**: con `gapaug`, 0,583 / 0,583 / 0,542 contra 0,833 de su referencia (p Holm = ,012 en las tres); con la versión ancha que cubre los 2,52 s, 0,583 / 0,583 / 0,542 (p = ,012). **Sí elimina la fragilidad frente a la pérdida contigua en posición aleatoria**: pérdida contigua 0,40 pasa de 0,708 con p Holm = ,023 (EEGNet) a 0,708 con p Holm = ,328 (`gapaug`), mejorando a 8 de 9 sujetos contra el original (p = ,027), sin costo en limpio (0,742 → 0,808 de mediana, neutro apareado). El canal máscara es la única variante que saca a la desconexión de 0,5 y 1 s de la significación (0,667, p Holm = ,094), pero no la de 2 s (0,583, p = ,023), y con n = 9 la mejora contra el original no es significativa (p = ,164). Rellenar distinto (interpolación, retención) **no sirve**: el filtro 8-30 Hz lo convierte en ceros.

Para el manuscrito: la vulnerabilidad de EEGNet a la desconexión dentro del ensayo es, sobre todo, de **información** (qué tramo de la ventana se pierde), no de **representación** (qué valor se pone en su lugar). La mitigación que sí funcionó en la campaña es de arquitectura del pipeline, no del modelo: el híbrido con vigía ([[Linea-5-Hibrido-Vigia]]) lleva el corte de 2 s de 0,500 a 0,667 (8 de 9 sujetos, p = ,008).

## 5. Esfuerzo y reproducción

| Tarea | Estado | Esfuerzo restante |
|---|---|---|
| Cadena de variantes, control, rellenos, 3 variantes entrenadas × 9 sujetos, sonda | hecho (≈ 65 min de entrenamiento) | — |
| Aumento **anclado al inicio** de la ventana (lo que señala la sonda) | propuesto | ≈ 30 min de entrenamiento + 10 min de evaluación |
| Barrido de p (0,25 / 0,5 / 1) | propuesto | ≈ 1,5 h |
| Llevar la red endurecida a una campaña en línea | no necesario para la conclusión | — |

Comandos exactos en la notebook, desde el worktree (`C:\Users\agustin.tamagusuku\Desktop\bci-fault-bench-futuro-robustez`), con el intérprete que tiene torch (DA-R1):

```bash
PY=../TESIS/TESIS/40-Prototipo/.venv/Scripts/python.exe
CAMP="C:/Users/agustin.tamagusuku/Desktop/TESIS/TESIS/40-Prototipo/results/vm/campana2"
# 1. entrenar (máximo 2 procesos a la vez; ≈ 5 min por sujeto)
PYTHONPATH=src $PY scripts/train_variants.py --variant gapaug      --subjects 1 2 3 4 5 6 7 8 9
PYTHONPATH=src $PY scripts/train_variants.py --variant mask        --subjects 1 5 8 2 3 4 6 7 9
PYTHONPATH=src $PY scripts/train_variants.py --variant gapaug_wide --subjects 1 2 3 4 5 6 7 8 9
# 2. re-decodificar (espejo en results/campana2-eval; no escribe en la campaña)
PYTHONPATH=src $PY scripts/redecode_variants.py --root "$CAMP" --models results/models --out results/campana2-eval \
  --variants eegnet eegnet_fill_interp eegnet_fill_hold eegnet_gapaug eegnet_gapaug_fill_interp eegnet_mask eegnet_gapaug_wide
# 3. tablas por variante (CSP: trials.csv y trials_csp_offline.csv)
for v in eegnet eegnet_fill_interp eegnet_fill_hold eegnet_gapaug eegnet_gapaug_fill_interp eegnet_mask eegnet_gapaug_wide; do
  PYTHONPATH=src $PY scripts/analyze.py --root results/campana2-eval --out results/analysis-$v --window 8 --thr-rule min \
    --trials-file trials_$v.csv --perf-only; done
PYTHONPATH=src $PY scripts/analyze.py --root results/campana2-eval --out results/analysis-csp_online  --window 8 --thr-rule min --trials-file trials.csv --perf-only
PYTHONPATH=src $PY scripts/analyze.py --root results/campana2-eval --out results/analysis-csp_offline --window 8 --thr-rule min --trials-file trials_csp_offline.csv --perf-only
# 4. comparación y sonda
PYTHONPATH=src $PY scripts/compare_variants.py --variants csp_online csp_offline eegnet eegnet_gapaug eegnet_fill_interp \
  eegnet_fill_hold eegnet_gapaug_fill_interp eegnet_mask eegnet_gapaug_wide hybrid_gap40 hybrid_gap40_gapaug
PYTHONPATH=src $PY scripts/gap_position_probe.py --variants eegnet eegnet_gapaug eegnet_gapaug_wide eegnet_mask
```

(Las columnas `hybrid_*` requieren antes `scripts/hybrid_decoder.py`, ver [[Linea-5-Hibrido-Vigia]].)

## 6. Límites

- **n = 9 y resolución gruesa**: con ≈ 24 ensayos por corrida la balanced accuracy se mueve de a 0,042; muchas diferencias entre variantes son de uno o dos ensayos por sujeto. Las comparaciones entre variantes (3.2) son exploratorias y sin corrección.
- **Confusión en el entrenamiento** (DA-R5): las variantes aumentadas se diferencian del original también en el filtrado por ventana. La sonda "sin hueco" (EEGNet 0,750 vs `gapaug` 0,785 con el mismo insumo) no permite atribuir esa diferencia a una u otra cosa.
- **Una sola semilla**: el orden de magnitud de la variación entre semillas de EEGNet en 144 ensayos no se midió; un cambio de 0,04 puede estar dentro de ella.
- **Probabilidad y rango fijos** (p = 0,5; U(0,4; 1,6) s por consigna): no se barrieron.
- **Fuera de línea**: la red endurecida no corrió en el pipeline en vivo; por ser determinista, la decisión es la misma, no así la latencia (≈ 6 ms por ventana en la notebook).

## Enlaces

- Código: `src/bcibench/robust.py`, `scripts/train_variants.py`, `scripts/redecode_variants.py`, `scripts/compare_variants.py`, `scripts/gap_position_probe.py`, `scripts/analyze.py --perf-only`.
- Salidas (no versionadas): `results/robustez/tabla_variantes.md`, `tabla_vs_base.md`, `tabla_por_sujeto.md`, `tabla_limpia.md`, `sonda_posicion.md`; `results/train_<variante>.csv`.
- [[Linea-5-Hibrido-Vigia]] · [[_decisions-robustez]] · [[_propuestas-robustez]] · [[_research-robustez]] · [[Trabajo-Futuro]]
