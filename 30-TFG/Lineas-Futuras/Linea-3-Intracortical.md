# Línea 3 · Señal intracortical: ¿la vulnerabilidad al transporte depende del tipo de señal?

> Nota de línea futura · 2026-09-27 · Sesión autónoma. Informe de fuentes: `_research-intracortical.md` (tabla de 15 datasets, 30 referencias verificadas en Crossref/DataCite). Decisiones: [[Decisiones-Autonomas|DA-08]]. Código: repositorio nuevo `agustama27/bci-fault-bench-intracortical` (PoC 1 fuera de línea).

## 1. Qué datasets públicos de implantes existen de verdad

Verificado en las páginas de los repositorios (licencia, registro, tamaño, formato). Resumen; la tabla completa está en `_research-intracortical.md` §1.1.

| Dataset | Dónde · DOI | Licencia · registro | Formato · tamaño | Señal | Tarea · especie |
|---|---|---|---|---|---|
| O'Doherty, Cardoso, Makin y Sabes (2017) | Zenodo 10.5281/zenodo.583331 | CC BY 4.0 · **sin registro** | MAT v7.3 por sesión, 84 MB a 1,96 GB (47 sesiones, 24 GB) | tiempos de cruce de umbral ordenados (hasta 5 unidades por canal) + cinemática a 250 Hz | alcance continuo autoguiado, sin ensayos · macaco (Indy, Loco); 96 canales M1 (192 con S1) |
| MC_RTT, Neural Latents Benchmark | DANDI 000129 · 10.48324/dandi.000129/0.241017.1444 | CC BY 4.0 · sin registro | NWB, 51 MB | tiempos de disparo ordenados | **la misma sesión de Indy** reempaquetada |
| MC_Maze (NLB) | DANDI 000128 | CC BY 4.0 · sin registro | NWB, 694 MB | disparos + mano, cursor, ojo | *center-out* con retardo en laberinto · macaco |
| Area2_Bump, DMFC_RSG (NLB) | DANDI 000127, 000130 | CC BY 4.0 | NWB, 1,8 GB / 16 MB | disparos | S1 con perturbaciones; tarea cognitiva (no motora) |
| Willett et al. (2021) escritura; Willett et al. (2023) y Card et al. (2024) habla | Dryad 10.5061/dryad.wh70rxwmv, .x69p8czpq, .dncjsxm85 | CC0 · sin cuenta en el navegador, **pero la descarga por script devuelve 403** | tar.gz / pkl, 1,4 GB a 80 GB | cruces de umbral en bins de 10-20 ms | escritura / habla intentada · humano (BrainGate2) |
| FALCON H1, H2 | DANDI 000954, 000950 | CC BY 4.0 · sin registro | NWB, 102 MB / 1,2 GB | ⚠️ bin sin verificar | alcance-agarre 7 GDL; escritura · **humano** |
| Perich, Lawlor, Kording y Miller (2018); Flint et al. (2012) | CRCNS 10.6080/K0FT8J72; DREAM | **exigen cuenta** | MAT | unidades aisladas | alcance · macaco |

Correcciones a supuestos previos: el DOI `10.5061/dryad.xd2547dkt` no es Perich 2018 sino Gallego-Carracedo et al. (2022, LFP); Neuropixels / Allen no sirven (ratón, corteza visual, estimulación pasiva: no hay intención motora que decodificar).

## 2. Decodificador de referencia para disparos neuronales

| Decodificador | Referencia verificada | Rol |
|---|---|---|
| Filtro de Wiener (regresión lineal sobre la historia de conteos) | Serruya et al. (2002), *Nature*, 10.1038/416141a; Hochberg et al. (2006), *Nature*, 10.1038/nature04970 | línea base sin estado |
| **Filtro de Kalman** sobre conteos en bins de 20 ms | Wu, Gao, Bienenstock, Donoghue y Black (2006), *Neural Computation*, 18(1), 80-118, 10.1162/089976606774841585 | **referencia pragmática** (canónico del control de cursor; se entrena en segundos por mínimos cuadrados) |
| ReFIT-KF | Gilja et al. (2012), *Nat. Neurosci.*, 10.1038/nn.3265 | requiere lazo cerrado: no reproducible con datos grabados |
| Redes (LSTM, GRU) | Glaser et al. (2020), *eNeuro*, 10.1523/ENEURO.0506-19.2020 | comparación opcional; paquete `KordingLab/Neural_Decoding` (BSD-3) trae Wiener, Kalman y LSTM (⚠️ sus datos de ejemplo están en Dropbox sin licencia) |
| RNN + modelo de lenguaje | Willett et al. (2021, 2023); Card et al. (2024) | fuera de alcance (GPU, decenas de GB) |

Punto metodológico importante: el Kalman **tiene estado**: ante un bin faltante puede predecir sin corregir. Eso mezcla dos variables (tipo de señal y arquitectura del decodificador), por lo que el Wiener va al lado como control sin estado. Esta misma confusión es la que las líneas 4 y 5 estudian en EEG (CSP promedia; EEGNet no).

## 3. Qué cambia en el banco

| Dimensión | EEG actual | Intracortical | Consecuencia |
|---|---|---|---|
| Contenido del flujo | voltaje continuo, 22 canales a 250 Hz | **conteos binneados** (20 ms → 50 Hz), 96 canales; alternativas: eventos irregulares (`nominal_srate = 0`, cambia la semántica de pérdida) o *broadband* a 30 kHz (11,5 MB/s: otro proyecto) | reproductor LSL casi igual (cambian tasa, tipo y metadatos); cada muestra perdida pesa 5 veces más |
| Estructura | ensayos de 4 s con *cue* | sesión continua sin ensayos (374 s en la sesión descargada) | evaluación por ventanas deslizantes o por *folds* temporales, no por ensayo |
| Decodificador | CSP+LDA, 2 clases | Kalman / Wiener, regresión de velocidad 2D | cargador y decodificador nuevos |
| Métrica | *balanced accuracy* | R² y correlación por eje, ECM | análisis estadístico distinto (métrica continua, R² puede ser negativo) |
| Escala de severidades | ensayo de 4 s (Tabla 1) | **ms físicos** (el enlace no sabe qué transporta) con equivalencia en bins: un jitter de 20 ms es un bin entero | las **trazas reales** ([[Linea-2-Trazas-Reales]]) se reutilizan tal cual: la misma traza aplicada a dos señales es el diseño más limpio |

## 4. Esfuerzo honesto y recomendación

| Tarea | Días |
|---|---|
| Cargador MAT v7.3 → conteos + velocidad (hecho en PoC 1) | 1,5 |
| Reproductor LSL de conteos (50 Hz, 96 canales) | 1 |
| Kalman y Wiener con validación temporal (hecho en PoC 1) | 2 |
| Reescalado del inyector (ms ↔ bins) | 1,5 |
| Análisis (R², correlación, curvas) | 2 |
| Corridas, verificación, redacción | 1-3 |
| **Total** | **9-13 días-persona** |

**Recomendación: Módulo 4 solo como PoC exploratoria acotada** (una sesión, un Kalman y un Wiener, las mismas fallas en ms físicos, una figura que compare la pendiente dosis-respuesta de EEG contra la intracortical), presentada como "extensión preliminar / evidencia de factibilidad" en Discusión o Anexo, sin inferencia confirmatoria. Lo que justifica incluirla es de ingeniería de software: demuestra que la arquitectura del banco (transporte agnóstico del contenido, objetivo 6) generaliza a otra modalidad. **El estudio completo es otra tesis** (varias sesiones y sujetos, humano vs primate con FALCON, control de la confusión señal/decodificador, lazo cerrado simulado). Riesgo a vigilar: no dejar que contamine las líneas temáticas comprometidas.

## 5. PoC 1 (cargar + decodificar fuera de línea)

Descargado sin registro: `indy_20161005_06.mat` (83.957.398 bytes; MD5 igual al publicado por Zenodo; SHA-256 `4b023e668d641960c7e3f4d277c781e606013125013a4cead1f4731951ff8eac`). 96 canales de M1, 249 unidades no vacías, 323.237 disparos, 374 s a 250 Hz de cinemática. Se eligió la sesión más chica de Indy (la sugerida, `indy_20160627_01`, pesa 1,1 GB).

Repositorio público: https://github.com/agustama27/bci-fault-bench-intracortical (MIT; commits `chore: project scaffold` → `docs: README with results`). Cargador `src/icbench/data.py` (h5py; 18.700 bins de 20 ms × 96 electrodos, unidad *hash* incluida por defecto, velocidad y posición del cursor; recorta los disparos anteriores a `t[0]`); decodificadores `src/icbench/decoders.py` en numpy desde cero: Wiener (historia de 10 bins, *ridge*, suavizado gaussiano causal opcional) y Kalman según Wu et al. (2006) (estado posición-velocidad-aceleración, √conteos, retardo neural de 3 bins; ante un bin faltante hace solo el paso de predicción). `scripts/poc1_offline.py`: 5 pliegues temporales contiguos, sin barajar; corre en ≈ 12 s.

| Decodificador | R² x | R² y | r x | r y |
|---|---|---|---|---|
| Wiener | 0,449 | 0,585 | 0,680 | 0,770 |
| Kalman | 0,378 | 0,425 | 0,636 | 0,672 |

Bins faltantes al azar (cambio del R² medio respecto de limpio): Wiener con ceros −0,007 (5 %) y −0,042 (20 %); Kalman solo predicción −0,006 y −0,027. En limpio rinde mejor el Wiener; con datos faltantes se degrada menos el Kalman: **la confusión entre tipo de señal y decodificador con estado aparece ya en la PoC** y hay que declararla en cualquier experimento con fallos.

Salvedades honestas: hiperparámetros elegidos a mano mirando un solo *split* (sin validación anidada); las caídas de bins son uniformes e independientes (chequeo de cordura, no el modelo de fallos del banco); el Kalman depende del retardo de 3 bins y de la aceleración en el estado (sin ellos R² ≈ 0,23-0,32). DOI de Wu et al. (2006) verificado en Crossref; el del dataset, en DataCite.

## 6. Comandos

No requiere VM. En la notebook:

```bash
cd ~/Desktop/bci-fault-bench-intracortical && .venv/Scripts/python.exe scripts/poc1_offline.py
```

## Enlaces

- Informe de fuentes: `_research-intracortical.md` · Manuscrito: [[Propuestas-Manuscrito]] · Decisiones: [[Decisiones-Autonomas]] · Contexto: [[Trabajo-Futuro]] n.º 6 · Fundamentos previos: [[Que-Es-BRAND]], [[Decodificadores-Estado-del-Arte]].
