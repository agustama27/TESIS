# Investigación · Datasets intracorticales públicos y decodificadores de referencia

> Informe de investigación · 2026-09-27 · Sesión autónoma. Insumo para una línea futura: **¿la vulnerabilidad a fallas de transporte depende del tipo de señal?** (EEG no invasivo vs. actividad intracortical). Toda cifra sin ⚠️ fue leída de una fuente primaria en esta sesión: API de DANDI, API de Zenodo, API de Dryad, API de Crossref, resolución de DOI en doi.org (DataCite) o la página oficial. Lo marcado **⚠️ SIN VERIFICAR** no pudo confirmarse contra una fuente primaria.

---

## 0. Resumen ejecutivo

- **Hay datasets intracorticales abiertos, sin registro y con licencia permisiva, que entran en el banco sin pelearse con la infraestructura.** Los dos mejores candidatos son el de O'Doherty et al. (2017) en Zenodo (CC BY 4.0, MAT v7.3 por sesión, 84 MB a 1,9 GB) y MC_RTT del Neural Latents Benchmark en DANDI (CC BY 4.0, NWB, 50 MB). Son **el mismo mono (Indy) y la misma tarea**: MC_RTT es una sesión del dataset de O'Doherty reempaquetada.
- **Descargado para la prueba de concepto:** `indy_20161005_06.mat` (83.957.398 bytes; el MD5 coincide con Zenodo). Tiene 96 canales de M1, 249 unidades no vacías, 374 s de alcance continuo y la cinemática a 250 Hz.
- **Decodificador de referencia pragmático:** un **filtro de Kalman** sobre conteos en bins de 20 a 50 ms que regresa velocidad (Wu et al., 2006), con el **filtro de Wiener** como línea base. Los dos están implementados en `Neural_Decoding` (BSD 3-Clause; Glaser et al., 2020).
- **Qué cambia en el banco:** el flujo pasa a ser de conteos binneados (50 Hz si el bin es de 20 ms, 96 canales) en lugar de EEG a 250 Hz con 22 canales. La tarea pasa de **clasificación** a **regresión continua**, así que la métrica deja de ser la exactitud balanceada y pasa a ser R² o la correlación de Pearson. También hay que reescalar las severidades: el bin de 20 ms reemplaza al ensayo de 4 s como unidad.
- **Esfuerzo estimado:** entre **9 y 13 persona-días** para una PoC honesta (una sesión, un decodificador, los mismos seis modelos de fallo).
- **Recomendación:** en el Módulo 4 entra **solo como PoC exploratoria acotada** (anexo o sección de "extensión preliminar" con una sesión y sin pretensión inferencial). **El estudio comparativo completo** (varias sesiones, varios decodificadores y humano vs. primate) **es otra tesis.**

---

## 1. Relevamiento de datasets intracorticales públicos

### 1.1 Tabla comparativa

| # | Dataset | Repositorio · DOI | Licencia | ¿Registro? | Formato | Tamaño | Señal / resolución | Canales / unidades | Tarea · especie |
|---|---|---|---|---|---|---|---|---|---|
| A | O'Doherty, Cardoso, Makin y Sabes (2017) | Zenodo · 10.5281/zenodo.583331 | **CC BY 4.0** | **No** (verificado: `curl` descarga directo, HTTP 200) | MAT v7.3 (HDF5) | 47 archivos, 24,0 GB en total; de 84 MB a 1,96 GB por sesión | Tiempos de cruce de umbral ordenados en unidades (hasta 5 por canal, incluida la unidad "hash") y waveforms; cinemática a 250 Hz | 96 canales (M1) en la mayoría de las sesiones y 192 (M1 + S1) en algunas | Alcance autoguiado a una grilla de 8×8, sin retardos ni segmentación en ensayos · *Macaca mulatta* (Indy: 37 sesiones; Loco: 10) |
| A′ | Broadband crudo de A | Zenodo · una DOI por sesión (p. ej., 10.5281/zenodo.1419774 para `indy_20161005_06`) | ⚠️ SIN VERIFICAR (se asume la misma licencia) | ⚠️ SIN VERIFICAR | ⚠️ SIN VERIFICAR | ⚠️ SIN VERIFICAR (del orden de decenas de GB por sesión) | Broadband crudo (del que se extrajeron los spikes de A) | 96/192 | Igual que A |
| B | MC_RTT (NLB) | DANDI 000129 · 10.48324/dandi.000129/0.241017.1444 | **CC BY 4.0** | **No** (`dandi:OpenAccess`) | NWB | 50,97 MB (train: 49,76 MB; test: 1,20 MB) | Tiempos de spikes ordenados; NLB binnea a 5 ms por defecto (verificado en `nlb_tools`) | ⚠️ SIN VERIFICAR (130 unidades según el paper de NLB) | Igual que A (sesión de Indy) · macaco |
| C | MC_Maze (NLB) | DANDI 000128 · 10.48324/dandi.000128/0.220113.0400 | **CC BY 4.0** | **No** | NWB | 694,0 MB (train: 690,6 MB) | Tiempos de spikes ordenados, posición de mano, cursor y ojo | ⚠️ SIN VERIFICAR (182 unidades según NLB) | Alcance *center-out* con retardo, dentro de un laberinto, en M1 y PMd · macaco (Jenkins). Las variantes escaladas MC_Maze_Large, Medium y Small son los dandisets 000138, 000139 y 000140 (listados en el README de `nlb_tools`; no las inspeccioné) |
| D | Area2_Bump (NLB) | DANDI 000127 · 10.48324/dandi.000127/0.220113.0359 | **CC BY 4.0** | **No** | NWB | 1,82 GB | Tiempos de spikes ordenados, fuerza, cinemática muscular y articular | ⚠️ SIN VERIFICAR | *Center-out* con perturbaciones mecánicas (*bumps*) en S1, área 2 · macaco (Han) |
| E | DMFC_RSG (NLB) | DANDI 000130 · 10.48324/dandi.000130/0.241017.1448 | **CC BY 4.0** | **No** | NWB | 15,7 MB | Tiempos de spikes ordenados | ⚠️ SIN VERIFICAR | Reproducción de intervalos temporales (cognitiva, **no motora**) · macaco |
| F | Willett et al. (2021), handwriting | Dryad · 10.5061/dryad.wh70rxwmv | **CC0 1.0** | Para navegador, la página no indica login. **La descarga programática está bloqueada**: la API v2 respondió `Unauthorized, must have current bearer token` y `file_stream`, 403 del WAF | `.tar.gz` (contiene `.mat`, ver README en PDF) | 1,41 GB (un solo archivo) | Cruces de umbral binneados; bin de 10 ms ⚠️ SIN VERIFICAR | 2 × 96 electrodos (192) en el área de la mano de la corteza motora | Escritura a mano intentada, 1.000 oraciones, 10,7 h · humano (T5, BrainGate2) |
| G | Willett et al. (2023), habla | Dryad · 10.5061/dryad.x69p8czpq | **CC0 1.0** | Igual que F | `.tar.gz` con `.mat` | 80,4 GB en total; `competitionData.tar.gz`: 3,67 GB | Cruces de umbral y *spike band power* en **bins de 20 ms** (página de Dryad) | ⚠️ SIN VERIFICAR (256 electrodos) | Habla intentada, 12.100 oraciones · humano (T12, ELA) |
| H | Card et al. (2024), habla (base del *Brain-to-Text* '25) | Dryad · 10.5061/dryad.dncjsxm85 | **CC0 1.0** | Igual que F | `.pkl` y `.zip` (HDF5 dentro ⚠️) | 11,59 GB (neuronal: 11,05 GB; `t15_copyTask.pkl`: 57,8 MB, sin datos neuronales crudos) | Cruces de umbral (−4,5 RMS) y *spike band power*, **bins de 20 ms**, z-scoreados | **256 electrodos → 512 features** | Habla intentada, 45 sesiones en 20 meses · humano (T15, ELA) |
| I | FALCON H1 | DANDI 000954 (borrador, sin DOI de versión) | **CC BY 4.0** | **No** | NWB | 102,3 MB en 40 archivos | ⚠️ SIN VERIFICAR (bin) | 2 × 96 canales en la zona de la mano | Alcance y agarre de 7 grados de libertad en calibración de lazo abierto · humano (Pittsburgh, NCT01894802) |
| J | FALCON H2 | DANDI 000950 · 10.48324/dandi.000950/0.241029.1403 | **CC BY 4.0** | **No** | NWB | 1,22 GB en 47 archivos | ⚠️ SIN VERIFICAR | 2 × 96 canales | Escritura a mano (copia de oraciones) · humano (T5, BrainGate2) |
| K | FALCON M2 | DANDI 000953 (borrador) | **CC BY 4.0** | **No** | NWB | 37,1 MB en el borrador según `assetsSummary`. La búsqueda listó 15,9 GB: discrepancia entre versiones ⚠️ | Spiking multiunidad | ⚠️ SIN VERIFICAR | Movimiento de dos grupos de dedos, M1 · macaco |
| L | LINK (Temmar et al.) | DANDI 001201 · 10.48324/dandi.001201/0.251023.2336 | **CC BY 4.0** | **No** | NWB | 12,56 GB en 312 sesiones | Cruces de umbral multiunidad y *spiking band power* | 96 canales (Utah, M1) | Movimiento de dedos autoguiado, 303 días a lo largo de ~3,5 años · macaco. Ideal para estudiar deriva |
| M | Finger_RL / PPC_Finger (Guan et al.) | DANDI 000252 y 000147 | **CC BY 4.0** | 000252: **No**. 000147: el campo `access` está vacío en los metadatos ⚠️ | NWB | 38 MB / 78 MB | Tiempos de unidades ordenadas | 96 canales (Utah) en PPC, MC y SPL | Movimientos de dedos intentados, tarea por ensayos · humano |
| N | Perich, Lawlor, Kording y Miller (2018), pmd-1 | **CRCNS** · 10.6080/K0FT8J72 | Términos de CRCNS (exige citar a Lawlor et al., 2018 y la DOI del dataset) | **Sí**: "you must have an account (which is free)" | MAT | ~385 MB | Unidades bien aisladas ("tens" por sesión) | Utah en M1 y PMd; 4 sesiones de 2 monos | Alcance secuencial · macaco |
| O | Flint, Lindberg, Jordan, Miller y Slutzky (2012) | ⚠️ SIN VERIFICAR: presunto en CRCNS/DREAM (`crcns.org/data-sets/movements/dream`), que exige login | ⚠️ | **Sí** (DREAM: "must log in to view and download") | ⚠️ | ⚠️ | ⚠️ | ⚠️ | Alcance center-out con LFP y spikes · macaco. El paper sí está verificado (JNE 2012) |

### 1.2 Correcciones a supuestos del encargo (verificadas)

1. **`10.5061/dryad.xd2547dkt` NO es Perich et al. (2018).** DataCite y Dryad lo resuelven a *"Local field potentials reflect cortical population dynamics in a region-specific and frequency-dependent manner"* (Gallego-Carracedo, Perich, Chowdhury, Miller y Gallego, 2022; CC0; 9,57 GB). Contiene 24 `.mat` de *center-out* (monos Chewie, Han, Lando y Mihili, de 166 MB a 1,37 GB cada uno) **con LFP**. El dataset de Perich, Lawlor, Kording y Miller (2018) está en **CRCNS (pmd-1), DOI 10.6080/K0FT8J72, y exige cuenta.**
2. **Dryad es CC0 y no pide cuenta para descargar desde el navegador, pero desde script sí hay traba.** Desde esta sesión, la API v2 exigió *bearer token* y el endpoint web devolvió 403 (WAF anti-bot). Para el banco significa que la descarga de F, G y H **no es reproducible desde un script sin credenciales de API**. Hay que documentarlo si se usan.
3. **El DOI de DANDI solo existe para versiones publicadas.** Los borradores (`draft`) de 000954 y 000953 no tienen DOI. Para citar hay que usar una versión publicada.
4. **MC_RTT (NLB) y O'Doherty (Zenodo) son el mismo sujeto y la misma tarea.** Los contribuyentes de DANDI 000129 incluyen a O'Doherty, Makin, Cardoso y Sabes. Elegir uno u otro es una decisión de **formato** (NWB curado vs. MAT crudo por sesión), no de fenómeno.

### 1.3 Por qué Neuropixels y el Allen Brain Observatory no sirven para esta línea

Son sondas agudas, **en ratón y en corteza visual bajo estimulación pasiva** (Siegle et al., 2021). No hay intención motora ni cinemática que decodificar, no hay un decodificador BCI de referencia y el volumen está en otra escala (broadband a 30 kHz con cientos de canales por sonda). Sirven para neurociencia de sistemas, no como carga de trabajo de una interfaz cerebro-computadora.

---

## 2. Decodificadores de referencia para señales de spikes

| Decodificador | Referencia primaria (verificada en Crossref) | Qué hace | Estado |
|---|---|---|---|
| Vector poblacional | Georgopoulos, Schwartz y Kettner (1986), *Science*, 233(4771), 1416–1419 | Suma vectorial de direcciones preferidas ponderadas por la tasa | Histórico. Pedagógico, pero no competitivo |
| Filtro lineal (Wiener) | Serruya et al. (2002), *Nature*, 416, 141–142; Hochberg et al. (2006), *Nature*, 442, 164–171 | Regresión lineal de la cinemática sobre la historia de conteos (varios bins de retardo) | **Línea base obligatoria** |
| Filtro de Kalman | Kalman (1960); Wu, Gao, Bienenstock, Donoghue y Black (2006), *Neural Computation*, 18(1), 80–118 | Modelo de estado lineal-gaussiano: dinámica de la cinemática (A, W) y observación de la tasa (H, Q) | **Referencia pragmática para la PoC** |
| ReFIT-KF | Gilja et al. (2012), *Nature Neuroscience*, 15(12), 1752–1757 | Kalman reentrenado con la intención corregida en lazo cerrado | Requiere **lazo cerrado**, así que no se puede reproducir con datos grabados. Se cita como motivación |
| Redes (LSTM, GRU, etc.) | Glaser et al. (2020), *eNeuro*, 7(4), ENEURO.0506-19.2020 | Regresión no lineal con historia | Opcional, como comparación |
| RNN + modelo de lenguaje (habla y escritura) | Willett et al. (2021, 2023); Card et al. (2024) | Secuencia a caracteres o fonemas, con CTC y LM | Fuera de alcance: GPU, Kaldi o LM de 5-gramas y decenas de GB |

**Paquete `KordingLab/Neural_Decoding` (verificado en la API de GitHub y su README):**

- Licencia **BSD 3-Clause**.
- Incluye, para regresión, Wiener Filter, Wiener Cascade, **Kalman Filter**, Naive Bayes, SVR, XGBoost, DNN, RNN, GRU y **LSTM**.
- Tiene los notebooks `Examples_kf_decoder.ipynb` y `Examples_all_decoders.ipynb`, además de `pip install Neural-Decoding`.
- Los datos de ejemplo (M1, S1 e hipocampo) están en **Dropbox, sin licencia explícita** ⚠️. Para la tesis conviene usar los datos de Zenodo o DANDI (con licencia clara) y el paquete solo como código.
- Último *push*: 2023-07-03, así que es mantenimiento bajo. Conviene fijar la versión.

**Por qué el Kalman es la referencia pragmática:**

1. Es el decodificador **canónico de control de cursor** en la literatura BCI intracortical (Wu et al., 2006; base de ReFIT en Gilja et al., 2012).
2. Se entrena offline en segundos, por mínimos cuadrados cerrados, sin GPU.
3. Es **con estado**, y ahí está la oportunidad para esta tesis. Ante un bin perdido, el Kalman puede **hacer solo la predicción y omitir la actualización**, que es el manejo natural de las observaciones faltantes. Así, la pregunta "¿el tipo de señal cambia la vulnerabilidad?" se cruza con otra: "¿un decodificador con estado absorbe fallas que un clasificador por ventana (CSP+LDA) no absorbe?". Si se reporta, hay que declarar esa confusión entre variables (señal vs. arquitectura del decodificador).
4. El Wiener filter va al lado como control sin estado, para separar ese efecto.

---

## 3. Factibilidad en el banco de pruebas

### 3.1 Qué cambia al transmitir datos intracorticales por LSL

| Dimensión | EEG actual (BCI IV 2a) | Intracortical (A o B) | Consecuencia |
|---|---|---|---|
| Qué se transmite | Muestras continuas de voltaje | Hay tres opciones: (i) **conteos binneados** (recomendada), (ii) eventos de spike irregulares, (iii) broadband crudo | (i) es lo que consume un decodificador BCI real. (ii) en LSL es un *stream* irregular (`nominal_srate = 0`), así que "pérdida" y "jitter" cambian de semántica. (iii) a 30 kHz × 96 ch × float32 son ~11,5 MB/s: posible, pero implica meter la detección de spikes dentro del banco, que es otro proyecto |
| Tasa | 250 Hz | **50 Hz** con bin de 20 ms (o 200 Hz con 5 ms, como NLB) | 5 veces menos muestras por segundo. Cada muestra perdida pesa más |
| Canales | 22 | **96** (hasta 192) | Bloques LSL más anchos; tipo `int16` o `float32` |
| Estructura | Ensayos de 4 s con cue | **Continua, sin ensayos** (A está explícitamente sin segmentar) | Se evalúa sobre ventanas deslizantes o sobre toda la sesión, no ensayo a ensayo |
| Decodificador | CSP+LDA, 2 clases | **Kalman o Wiener**, regresión de velocidad 2D | — |
| Métrica | Exactitud balanceada | **R²** y **correlación de Pearson** por eje (velocidad x/y), más el error cuadrático medio | Hay que rehacer los modelos estadísticos del análisis: pasar de una proporción a una métrica continua acotada. R² puede ser negativo bajo falla severa |
| Duración de la sesión de la PoC | Sesiones de BCI IV 2a | `indy_20161005_06`: **374 s** (18.700 bins de 20 ms) | Alcanza para 5 folds de entrenamiento y test contiguos |

### 3.2 Reescalado de severidades

El Entregable 2 ancla las severidades a la escala del ensayo (ventana de 4 s). En intracortical **no hay ensayo**, así que hay que re-anclar:

- **Unidad temporal = el bin (20 ms)**, con horizonte de decisión = la **latencia del decodificador** (~la historia que usa el Wiener o la constante de tiempo del Kalman, del orden de 100 a 300 ms ⚠️ a medir con los datos).
- **Pérdida (`loss`):** se mantiene como fracción de muestras (%). Es comparable entre modalidades.
- **Retraso y jitter:** se expresan en **ms** (magnitud física del enlace) y además en **bins equivalentes**. Un jitter de 20 ms no pesa nada a 4 s por ensayo, pero equivale a un bin completo en intracortical. La comparación entre señales **tiene que hacerse en ms físicos** (el enlace no sabe qué transporta). La normalización por la escala de la señal va como análisis secundario.
- **Corte (`disconnect`) y ráfagas:** la duración va en ms, con la regla de que un corte de *k* bins elimina *k* observaciones del Kalman, que predice sin corregir.
- **Trazas reales (Línea 2):** se reusan tal cual, porque están en tiempo físico. Es un argumento a favor de esta línea: **la misma traza aplicada a dos señales** es el diseño más limpio para responder la pregunta.

### 3.3 Estimación de esfuerzo (persona-días, honesta)

| Tarea | Días | Notas |
|---|---|---|
| Loader (MAT v7.3 → conteos binneados + velocidad) y tests | 1,5 | Con h5py. Las celdas vacías de MATLAB llegan como `uint64 [0,0]` (verificado). Hay que decidir si se incluye la unidad hash (u1) |
| Replay LSL de conteos (50 Hz, 96 ch) | 1 | Reusa el *outlet* actual; cambian `nominal_srate`, el tipo y los metadatos |
| Kalman y Wiener entrenados offline, con CV temporal | 2 | `Neural_Decoding` o implementación propia (~80 líneas); falta el manejo de bins faltantes en el Kalman |
| Reescalado del inyector (ms ↔ bins; modo irregular opcional) | 1,5 | Configuración y validación de que las severidades equivalen a las de EEG en ms |
| Cambios de análisis (R² y CC, modelos continuos, figuras) | 2 | El modelo estadístico pasa de binomial a gaussiano o beta; nuevas curvas dosis-respuesta |
| Corridas, verificación y redacción de la PoC | 1–3 | Una sesión y 6 modelos de fallo × severidades × semillas, en local o en la VM |
| **Total** | **9–13** | Sin contar la revisión del director ni imprevistos |

### 3.4 Recomendación

**Módulo 4: sí, pero solo como PoC exploratoria y bien etiquetada.** Una sesión (`indy_20161005_06`), un Kalman y un Wiener, las mismas fallas en ms físicos y una figura que compare la pendiente dosis-respuesta de EEG contra la intracortical. Se presenta como **"extensión preliminar / evidencia de factibilidad"**, sin inferencia confirmatoria. Lo que justifica meterla es que demuestra que la arquitectura del banco (transporte agnóstico del contenido) **generaliza a otra modalidad**, y eso es un argumento de ingeniería de software, que es la línea de la tesis.

**Como estudio: otra tesis.** Responder en serio la pregunta necesita varias sesiones y sujetos, humano vs. primate (FALCON H1/H2, Card et al.), controlar la confusión entre señal y decodificador con estado, y probablemente lazo cerrado simulado. Eso excede un anexo.

Riesgo a vigilar: no dejar que la PoC contamine las líneas temáticas ya comprometidas. Va en Discusión o en Anexo, no en Resultados.

---

## 4. Prueba de concepto: archivo descargado

- **Archivo:** `C:\Users\agustin.tamagusuku\Desktop\bci-fault-bench-futuro\intracortical\raw\indy_20161005_06.mat`
- **Fuente:** `https://zenodo.org/records/583331/files/indy_20161005_06.mat?download=1`. `curl -sIL` devolvió HTTP 200, `content-length: 83957398`, sin registro.
- **Tamaño:** 83.957.398 bytes (80,1 MiB)
- **SHA-256:** `4b023e668d641960c7e3f4d277c781e606013125013a4cead1f4731951ff8eac`
- **MD5:** `5ea300952642e0fc54245144499db9bb`, que **coincide** con el checksum publicado por Zenodo
- **Formato:** `MATLAB 7.3 MAT-file` (HDF5), creado el 2017-05-25. Se lee con `h5py` 3.16.0; `scipy.io.loadmat` no sirve para v7.3.
- **Por qué no el `indy_20160627_01.mat` sugerido:** pesa 1.135.050.817 bytes, por encima del límite de 300 MB. Se eligió la sesión Indy más chica de la lista.

**Estructura (h5py; las formas son las almacenadas, transpuestas respecto de MATLAB):**

| Clave | Forma almacenada | dtype | Clase MATLAB | Contenido |
|---|---|---|---|---|
| `chan_names` | (1, 96) | object (refs) | cell | `"M1 001"` … `"M1 096"`: solo M1 |
| `cursor_pos` | (2, 93501) | float64 | double | x, y en mm |
| `finger_pos` | (3, 93501) | float64 | double | z, −x, −y en cm |
| `target_pos` | (2, 93501) | float64 | double | x, y en mm |
| `t` | (1, 93501) | float64 | double | 1288,000 → 1662,000 s; dt mediano 0,004 s (**250 Hz**); **374,0 s** |
| `spikes` | (5, 96) | object (refs) | cell | Tiempos de spike en s. Por ejemplo, `spikes[u0, ch0]` tiene forma (1, 1404) float64 |
| `wf` | (5, 96) | object (refs) | cell | Waveforms float32 de 64 muestras por spike, en µV. Por ejemplo, forma (64, 1404) |
| `#refs#` | grupo | — | — | Almacén interno HDF5 de las celdas |

**Unidades no vacías:** 249 en total. Por índice de unidad: u1 (hash) 85, u2 70, u3 60, u4 25, u5 9. Hay **323.237 spikes** en total. Los primeros spikes (≈1285,5 s) son anteriores a `t[0]` (1288 s), así que hay que recortar al rango de `t` al binnear.

---

## 5. Pendientes y dudas abiertas

- ⚠️ Confirmar el bin de F (handwriting): se asume 10 ms y hay que leerlo en `readme.pdf` del dataset.
- ⚠️ Canales y unidades de B, C y D: leerlos del NWB (no se descargó, para respetar el límite de un archivo).
- ⚠️ Localización y licencia exactas de los datos de Flint et al. (2012): DREAM/CRCNS exige login y no se pudo inspeccionar.
- ⚠️ Licencia y tamaño de los registros broadband de A′.
- Decidir con el director si la PoC entra en el Módulo 4 (ver 3.4).

---

## Referencias verificadas

Card, N. S., Wairagkar, M., Iacobacci, C., Hou, X., Singer-Clark, T., Willett, F. R., Kunz, E. M., Fan, C., Vahdati Nia, M., Deo, D. R., Srinivasan, A., Choi, E. Y., Glasser, M. F., Hochberg, L. R., Henderson, J. M., Shahlaie, K., Stavisky, S. D. y Brandman, D. M. (2024). An accurate and rapidly calibrating speech neuroprosthesis. *New England Journal of Medicine, 391*(7), 609–618. https://doi.org/10.1056/NEJMoa2314132

Card, N., Wairagkar, M., Iacobacci, C., Hou, X., Singer-Clark, T., Willett, F., Kunz, E., Fan, C., Vahdati Nia, M., Deo, D., Srinivasan, A., Choi, E. Y., Glasser, M., Hochberg, L., Henderson, J., Shahlaie, K., Stavisky, S. y Brandman, D. (2024). *Data for: An accurate and rapidly calibrating speech neuroprosthesis* [Conjunto de datos]. Dryad. https://doi.org/10.5061/dryad.dncjsxm85

Chowdhury, R. H., Glaser, J. I. y Miller, L. E. (2020). Area 2 of primary somatosensory cortex encodes kinematics of the whole arm. *eLife, 9*, e48198. https://doi.org/10.7554/eLife.48198

Chowdhury, R. y Miller, L. (2022). *Area2_Bump: Macaque somatosensory area 2 spiking activity during reaching with perturbations* (Versión 0.220113.0359) [Conjunto de datos]. DANDI Archive. https://doi.org/10.48324/dandi.000127/0.220113.0359

Churchland, M. M., Cunningham, J. P., Kaufman, M. T., Foster, J. D., Nuyujukian, P., Ryu, S. I. y Shenoy, K. V. (2012). Neural population dynamics during reaching. *Nature, 487*(7405), 51–56. https://doi.org/10.1038/nature11129

Churchland, M. y Kaufman, M. (2022). *MC_Maze: Macaque primary motor and dorsal premotor cortex spiking activity during delayed reaching* (Versión 0.220113.0400) [Conjunto de datos]. DANDI Archive. https://doi.org/10.48324/dandi.000128/0.220113.0400

Flint, R. D., Lindberg, E. W., Jordan, L. R., Miller, L. E. y Slutzky, M. W. (2012). Accurate decoding of reaching movements from field potentials in the absence of spikes. *Journal of Neural Engineering, 9*(4), 046006. https://doi.org/10.1088/1741-2560/9/4/046006

Gallego-Carracedo, C., Perich, M. G., Chowdhury, R. H., Miller, L. E. y Gallego, J. A. (2022). Local field potentials reflect cortical population dynamics in a region-specific and frequency-dependent manner. *eLife, 11*, e73155. https://doi.org/10.7554/eLife.73155

Gallego-Carracedo, C., Perich, M., Chowdhury, R., Miller, L. y Gallego, J. (2022). *Local field potentials reflect cortical population dynamics in a region-specific and frequency-dependent manner* [Conjunto de datos]. Dryad. https://doi.org/10.5061/dryad.xd2547dkt

Georgopoulos, A. P., Schwartz, A. B. y Kettner, R. E. (1986). Neuronal population coding of movement direction. *Science, 233*(4771), 1416–1419. https://doi.org/10.1126/science.3749885

Gilja, V., Nuyujukian, P., Chestek, C. A., Cunningham, J. P., Yu, B. M., Fan, J. M., Churchland, M. M., Kaufman, M. T., Kao, J. C., Ryu, S. I. y Shenoy, K. V. (2012). A high-performance neural prosthesis enabled by control algorithm design. *Nature Neuroscience, 15*(12), 1752–1757. https://doi.org/10.1038/nn.3265

Glaser, J. I., Benjamin, A. S., Chowdhury, R. H., Perich, M. G., Miller, L. E. y Kording, K. P. (2020). Machine learning for neural decoding. *eNeuro, 7*(4), ENEURO.0506-19.2020. https://doi.org/10.1523/ENEURO.0506-19.2020

Hochberg, L. R., Serruya, M. D., Friehs, G. M., Mukand, J. A., Saleh, M., Caplan, A. H., Branner, A., Chen, D., Penn, R. D. y Donoghue, J. P. (2006). Neuronal ensemble control of prosthetic devices by a human with tetraplegia. *Nature, 442*(7099), 164–171. https://doi.org/10.1038/nature04970

Kalman, R. E. (1960). A new approach to linear filtering and prediction problems. *Journal of Basic Engineering, 82*(1), 35–45. https://doi.org/10.1115/1.3662552

Karpowicz, B. M., Ye, J., Fan, C., Tostado-Marcos, P., Rizzoglio, F., et al. (2024). *Few-shot Algorithms for Consistent Neural Decoding (FALCON) Benchmark* [Preprint]. bioRxiv. https://doi.org/10.1101/2024.09.15.613126

Makin, J. G., O'Doherty, J. E., Cardoso, M. M. B. y Sabes, P. N. (2018). Superior arm-movement decoding from cortex with a new, unsupervised-learning algorithm. *Journal of Neural Engineering, 15*(2), 026010. https://doi.org/10.1088/1741-2552/aa9e95

O'Doherty, J. (2024). *MC_RTT: Macaque motor cortex spiking activity during self-paced reaching* (Versión 0.241017.1444) [Conjunto de datos]. DANDI Archive. https://doi.org/10.48324/dandi.000129/0.241017.1444

O'Doherty, J. E., Cardoso, M. M. B., Makin, J. G. y Sabes, P. N. (2017). *Nonhuman primate reaching with multichannel sensorimotor cortex electrophysiology* [Conjunto de datos]. Zenodo. https://doi.org/10.5281/zenodo.583331

Pei, F., Ye, J., Zoltowski, D., Wu, A., Chowdhury, R. H., Sohn, H., O'Doherty, J. E., Shenoy, K. V., et al. (2021). Neural Latents Benchmark '21: Evaluating latent variable models of neural population activity. En *Proceedings of the Neural Information Processing Systems Track on Datasets and Benchmarks*. https://doi.org/10.48550/arXiv.2109.04463

Perich, M. G., Gallego, J. A. y Miller, L. E. (2018). A neural population mechanism for rapid learning. *Neuron, 100*(4), 964–976.e7. https://doi.org/10.1016/j.neuron.2018.09.030

Perich, M. G., Lawlor, P. N., Kording, K. P. y Miller, L. E. (2018). *Extracellular neural recordings from macaque primary and dorsal premotor motor cortex during a sequential reaching task* [Conjunto de datos]. CRCNS.org. https://doi.org/10.6080/K0FT8J72

Serruya, M. D., Hatsopoulos, N. G., Paninski, L., Fellows, M. R. y Donoghue, J. P. (2002). Instant neural control of a movement signal. *Nature, 416*(6877), 141–142. https://doi.org/10.1038/416141a

Siegle, J. H., Jia, X., Durand, S., Gale, S., Bennett, C., Graddis, N., et al. (2021). Survey of spiking in the mouse visual system reveals functional hierarchy. *Nature, 592*(7852), 86–92. https://doi.org/10.1038/s41586-020-03171-x

Sohn, H. y Jazayeri, M. (2024). *DMFC_RSG: Macaque dorsomedial frontal cortex spiking activity during time interval reproduction task* (Versión 0.241017.1448) [Conjunto de datos]. DANDI Archive. https://doi.org/10.48324/dandi.000130/0.241017.1448

Willett, F. R., Avansino, D. T., Hochberg, L. R., Henderson, J. M. y Shenoy, K. V. (2021). High-performance brain-to-text communication via handwriting. *Nature, 593*(7858), 249–254. https://doi.org/10.1038/s41586-021-03506-2

Willett, F., Avansino, D., Hochberg, L., Henderson, J. y Shenoy, K. (2021). *Data from: High-performance brain-to-text communication via handwriting* [Conjunto de datos]. Dryad. https://doi.org/10.5061/dryad.wh70rxwmv

Willett, F. R., Kunz, E. M., Fan, C., Avansino, D. T., Wilson, G. H., Choi, E. Y., Kamdar, F., Glasser, M. F., Hochberg, L. R., Druckmann, S., Shenoy, K. V. y Henderson, J. M. (2023). A high-performance speech neuroprosthesis. *Nature, 620*(7976), 1031–1036. https://doi.org/10.1038/s41586-023-06377-x

Willett, F., Kunz, E., Fan, C., Avansino, D., Wilson, G., Choi, E. Y., Kamdar, F., Glasser, M., Hochberg, L., Druckmann, S., Shenoy, K. y Henderson, J. (2023). *Data for: A high-performance speech neuroprosthesis* [Conjunto de datos]. Dryad. https://doi.org/10.5061/dryad.x69p8czpq

Willett, F. R., Li, J., Le, T., Fan, C., Chen, M., Shlizerman, E., Chen, Y., Zheng, X., et al. (2024). *Brain-to-Text Benchmark '24: Lessons learned* [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2412.17227

Wu, W., Gao, Y., Bienenstock, E., Donoghue, J. P. y Black, M. J. (2006). Bayesian population decoding of motor cortical activity using a Kalman filter. *Neural Computation, 18*(1), 80–118. https://doi.org/10.1162/089976606774841585

**Software:** KordingLab. (2023). *Neural_Decoding* [Software; licencia BSD 3-Clause]. GitHub. https://github.com/KordingLab/Neural_Decoding · Neural Latents. (s. f.). *nlb_tools* [Software; licencia MIT]. GitHub. https://github.com/neurallatents/nlb_tools
