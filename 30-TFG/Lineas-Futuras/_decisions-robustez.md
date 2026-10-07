# Decisiones autónomas · Líneas 4 y 5 (robustez de EEGNet e híbrido con vigía)

> 2026-09-27 · Sesión autónoma. Para fusionar en [[Decisiones-Autonomas]] (este archivo no la edita). Código: worktree `bci-fault-bench-futuro-robustez`, rama `feat/robustez-modelo`. Notas: [[Linea-4-Endurecer-EEGNet]], [[Linea-5-Hibrido-Vigia]].

**DA-R1 · Intérprete de Python.**
- Qué: se usó `TESIS/40-Prototipo/.venv` (torch 2.14 CPU, mne 1.13, moabb 1.7, sklearn 1.9) y no `bci-fault-bench-futuro/.venv`.
- Por qué: el venv indicado **no tiene torch instalado** (verificado con `pip list`); el de 40-Prototipo tiene las mismas versiones de mne/moabb/sklearn/pandas más torch. Solo se ejecutó el intérprete; no se escribió nada dentro de 40-Prototipo.
- Descartado: instalar torch en el venv indicado (≈ 200 MB de descarga, cambio de entorno no pedido).

**DA-R2 · Espejo de evaluación en lugar de escribir en la campaña.**
- Qué: `results/campana2-eval/<exec>/` con copias de `producer.json`, `consumer.json`, `telemetry.csv`, `trials.csv`, `trials_csp_offline.csv` y el `trials_eegnet.csv` original renombrado `trials_eegnet_orig.csv`; los `segments.npz` se leen de la carpeta original.
- Por qué: la campaña es de solo lectura y `analyze.py` necesita todo junto en una carpeta por ejecución.
- Descartado: symlinks (Windows sin privilegios) o parametrizar `load_campaign` con dos raíces (más cambios en código ya publicado).

**DA-R3 · Control exacto antes de cualquier variante.**
- Qué: la variante `eegnet` se recalculó con el pipeline nuevo y se comparó ensayo por ensayo con el `trials_eegnet.csv` original: **0 diferencias** de predicción o validez en 20.520 ensayos (855 ejecuciones) y `t_desempeno.md` **idéntico byte a byte** al de `40-Prototipo/results/analysis-eegnet`. Lo mismo para CSP en línea (`trials.csv`) contra `analysis/t_desempeno.md`.
- Por qué: si el control no reproduce, cualquier diferencia entre variantes podría ser del pipeline.

**DA-R4 · Dónde se aplica el hueco del aumento: espacio crudo, antes del filtro.**
- Qué: el aumento borra el tramo en la época **cruda** con 1 s de relleno a cada lado (0 V), filtra 8-30 Hz y recorta [2, 6] s, exactamente la cadena de inferencia.
- Por qué: en inferencia la muestra faltante vale 0 V **antes** del filtro. Se verificó el temor de "-mu/sd ≠ 0": como la señal de entrenamiento está filtrada 8-30 Hz, mu es del orden de 1e-10 V y sd de 4e-6 V, así que **max |mu/sd| = 7·10⁻⁴** (sujetos 1 y 5): el silencio estandarizado es ≈ 0. Lo que sí difiere entre "cero crudo" y "cero estandarizado" es el **transitorio del filtro** en los bordes del hueco; borrar en crudo lo reproduce, borrar en espacio estandarizado no.
- Descartado: poner ceros después de la estandarización (entrenaría con bordes abruptos que la red nunca ve en inferencia).

**DA-R5 · Consecuencia de DA-R4: las variantes aumentadas se entrenan con ventanas filtradas por ensayo.**
- Qué: `eegnet_gapaug`/`_mask`/`_wide` ven ventanas filtradas sobre [1, 7) s (como en inferencia), mientras que el EEGNet original se entrenó con épocas recortadas de la corrida continua ya filtrada (`data.epochs_of`). Mismos ensayos (144 por sujeto, sin artefactos), mismas épocas (300), semilla 0, Adam 1e-3, lote 32, misma arquitectura.
- Por qué: es la única forma de que el hueco del entrenamiento tenga el mismo transitorio que en inferencia.
- Costo: confusión declarada. La variante endurecida difiere del original en dos cosas (aumento + filtrado por ventana). La sonda sin hueco y la tabla limpia permiten separarlo solo en parte (ver límites en la Línea 4).

**DA-R6 · Probabilidad del aumento p = 0,5.**
- Qué: en cada época, cada ensayo recibe un hueco con probabilidad 0,5 (nuevo sorteo por época: posición y largo).
- Por qué: la mayor parte del uso real (y 16 de las 19 condiciones de la campaña) es sin hueco en la ventana; con p = 1 la red nunca vería una ventana completa en el entrenamiento y se arriesga desempeño limpio, que es justamente lo que se pide no pagar. Con p = 0,5 el desempeño limpio no bajó (ver tabla limpia).
- Descartado: p = 1 (sin evidencia de que haga falta y con costo probable en limpio); barrer p (no entraba en el presupuesto).

**DA-R7 · Largo y posición del hueco: U(0,4; 1,6) s en posición uniforme dentro de la ventana.**
- Qué: se siguió la consigna. Se midió después que los huecos reales de la campaña son: pérdida contigua 0,40 / 1,00 / 1,60 s en posición aleatoria; desconexión en el ensayo **1,52 / 1,52 / 2,52 s y siempre al inicio de la ventana** (arranca a los 2,00-2,04 s).
- Consecuencia: el corte de 2 s (2,52 s) queda fuera del rango de entrenamiento; por eso se entrenó también `eegnet_gapaug_wide` con U(0,4; 2,6) s.
- Descartado (quedó como propuesta): un aumento **anclado al inicio** de la ventana, que es lo que la sonda de posición señala como causa.

**DA-R8 · Relleno alternativo aplicado en la grilla cruda, antes del filtro.**
- Qué: `interp` (np.interp por canal; bordes = valor más cercano) y `hold` (última muestra; hueco inicial = primer valor presente), en toda la grilla con relleno de 1500 muestras.
- Hallazgo: tras el filtro 8-30 Hz, **cualquier relleno suave se vuelve ≈ 0 dentro del hueco**: RMS en el interior del hueco (a más de 0,4 s de una muestra presente) / RMS de la señal presente = 0,001 para cero, interpolación y retención (medido en 30 ejecuciones de pérdida contigua 0,4 y corte en el ensayo 2 s). Solo cambia el borde (0,13 / 0,13 / 0,15 en los 0,4 s cercanos). Una recta o una constante no tienen energía en 8-30 Hz. Rellenar antes del filtro es, para la red, casi lo mismo que poner ceros.
- Descartado: rellenar después del filtro (no es lo que haría un pipeline real que filtra el flujo, y un relleno lineal del filtrado igual carece de contenido en banda).

**DA-R9 · Canal máscara: n_ch = 23, mu = 0 y sd = 1, sin filtrar.**
- Qué: canal 23 = 1 donde falta la muestra de la grilla nominal dentro de la ventana; la convolución espacial en profundidad abarca las 23 filas. Se entrena con el mismo aumento que `gapaug` (una máscara sin huecos en el entrenamiento sería constante e inútil).
- Por qué: es la forma más simple de "indicador de faltante" (Che et al., 2018) que no cambia la arquitectura salvo en el número de filas.
- Descartado: una rama separada para la máscara o multiplicarla dentro de la red (cambia la arquitectura de referencia).

**DA-R10 · Cobertura de sujetos.**
- Qué: `gapaug` 9/9, rellenos 9/9 (solo inferencia), `mask` en 1, 5 y 8 primero y luego extendida a 9/9 porque el tiempo medido lo permitió (≈ 5-6 min por sujeto con dos entrenamientos en paralelo de 5 hilos), `gapaug_wide` 9/9.
- Presupuesto usado: ver Línea 4 (tiempos por sujeto en `results/train_<variante>.csv`).

**DA-R11 · `analyze.py --perf-only`.**
- Qué: bandera nueva que corta el análisis después de desempeño e infraestructura (sección 1).
- Por qué: el análisis completo tardó 8,5 min por variante (la mayor parte en ventana móvil, divergencia y detectores LOSO, que no dependen de la variante en lo que aquí interesa); con ≈ 15 variantes eran más de 2 h. `t_desempeno.*` sale idéntico con y sin la bandera.
- Descartado: paralelizar el análisis (más memoria de la disponible).

**DA-R12 · Vigía: señales y reglas.**
- Qué: por ensayo, n.º de muestras en [2, 6) s y máximo intervalo entre muestras presentes **contando los bordes de la ventana** (un hueco que empieza en el borde también cuenta). Reglas `complete` (1000 muestras), `gap40` (≤ 40 ms = un bloque de transporte) y `gap200` (≤ 200 ms).
- Por qué los bordes: la desconexión en el ensayo empieza exactamente en el borde; sin contarlo, el vigía no la vería.
- Descartado: usar la telemetría por segundo (`telemetry.csv`): tiene resolución de 1 s y no se alinea con la ventana del ensayo.

**DA-R13 · Rama de respaldo del híbrido: CSP+LDA fuera de línea.**
- Qué: cuando el vigía detecta hueco se usa la decisión de `trials_csp_offline.csv` (misma grilla con ceros, filtrada, y CSP sobre las muestras presentes).
- Por qué: es la decisión que se obtiene del mismo segmento y con la misma cadena que la red; la de `trials.csv` filtra la señal compactada y es otra cadena. En la campaña ambas coinciden en las medianas de las condiciones estructuradas salvo desconexión en el ensayo 0,5 y 1 s (0,750 en línea vs 0,667 fuera de línea).
- Descartado: CSP en línea como respaldo (mezclaría dos cadenas de preprocesamiento en un mismo decodificador).

**DA-R14 · Sonda de posición del hueco.**
- Qué: `scripts/gap_position_probe.py` borra 1,52 s (el largo de la desconexión en el ensayo de 0,5 y 1 s) al inicio, al medio o al final de la ventana sobre la sesión 2 limpia y decodifica con cada modelo.
- Por qué: los números de la campaña mostraron que `gapaug` recupera la pérdida contigua de 1,6 s (posición aleatoria) pero no la desconexión de 1,52 s (siempre al inicio), aunque el largo está dentro del rango de entrenamiento. La sonda aísla la posición como variable.

**DA-R15 · Qué no se commitea.**
- `results/` está en `.gitignore` (modelos, espejo, análisis, tablas). Las tablas finales se copiaron como markdown a las notas del vault.

**DA-R16 · Comparación entre variantes apareada por sujeto, sin corrección.**
- Qué: además de cada variante contra su propia referencia (Holm, como en E2), `compare_variants.py` informa la diferencia apareada por sujeto contra EEGNet original (mediana, sujetos que mejoran/empeoran, Wilcoxon sin corregir).
- Por qué: la mediana de medianas engaña. La referencia de `gapaug` figura 0,833 contra 0,750, pero apareado por sujeto la diferencia es 0 (3 mejoran, 3 empeoran, p = 1). Sin esta tabla se habría reportado una mejora inexistente.
- Descartado: corregir por Holm sobre todas las variantes × condiciones (≈ 70 pruebas exploratorias; el objetivo es orientar, no confirmar).
