# Análisis M3c: campaña exploratoria (reconexión, exposición, retención vs. borrado, fallas silenciosas)

> 2026-10-07. Campaña **exploratoria post hoc** `campaign-m3/campana3` (387 ejecuciones, 0 fallidas: 45 ref + 4 x 45 barrido de exposición + 3 x 45 `hold_trial` + 3 x 9 diagnóstico del piso de reconexión). Nota nueva; no modifica el manuscrito ni el código del banco (`src/bcibench`). Complementa a [[Analisis-M3]] y [[Analisis-M3-ensayos-divergencia]].
>
> **Esta campaña y todos estos análisis son EXPLORATORIOS y post hoc.** Se diseñó y se analizó después de ver los resultados de la campaña definitiva (`campaign-2026-09-27`, 855 ejecuciones) para poner a prueba tres explicaciones que quedaron abiertas. No hay corrección por multiplicidad entre tablas; los p valores son descriptivos (con n = 9 sujetos el p exacto bilateral mínimo de Wilcoxon es 0,0039). Dentro de cada tipo de fallo se aplica Holm como en el estudio.
>
> **Convenciones.** `B = C:\Users\agustin.tamagusuku\Desktop\bci-fault-bench`; campaña nueva `N = B\campaign-m3\campana3`; campaña anterior `A = B\campaign-2026-09-27` (`A\raw`, `A\analysis`); salidas en `B\campaign-m3\analysis\` (CSV, tablas `m3c_tablas.md`, figuras `m3c_exp_curva.png`, `m3c_ret_fig.png`); scripts en `B\scripts\m3c_*.py`, ejecutados con `C:\Users\agustin.tamagusuku\.venvs\bcibench\Scripts\python` (el EEGNet se re-evaluó con `40-Prototipo\.venv` y `40-Prototipo\scripts\m3_eegnet_relleno.py`, salida en `B\campaign-m3\analysis-eegnet\` y `N\<exec>\trials_eegnet_{ceros,interp,hold}.csv`). Las tablas usan punto decimal; en el texto, coma. Cada cifra lleva `[script -> archivo]`. **Unidad estadística = sujeto** (mediana de sus corridas; 9 sujetos), pruebas no paramétricas apareadas: Friedman sobre {ref, severidades}, Wilcoxon de cada severidad contra la referencia con Holm dentro del tipo y r = |Z|/sqrt(n) (`bcibench.stats.by_kind_tests`, el mismo código del estudio). Decodificadores: CSP+LDA en línea (`trials.csv`) y EEGNet fuera de línea sobre los segmentos recibidos; **EEGNet estándar = modo "ceros"** (`trials_eegnet_ceros.csv`), que reproduce `trials_eegnet.csv` del Entregable 2 en el 99,96 % de las decisiones de las 855 ejecuciones de la campaña anterior (`40-Prototipo\results\vm\analysis-m3-eegnet\por_ejecucion.csv`, columna `reproduce_e2`; mínimo 91,7 % en una ejecución). "Cambio" = la decisión difiere de la que tomó el mismo decodificador en el mismo ensayo (mismo sujeto, corrida, índice y onset) de la referencia de su campaña; un ensayo inválido cuenta como cambio y como error. "pp" = puntos porcentuales; "Δ" = condición − referencia.
>
> **Datos de partida.** `N\plan.json` solo lista las 360 ejecuciones del plan principal (la corrida de 27 ejecuciones del piso de reconexión se hizo aparte; sus carpetas están en `N`). Los 24 ensayos por corrida y la telemetría por segundo (`telemetry.csv`) tienen el mismo formato que en la campaña anterior. En `hold_trial` `fault_log.jsonl` trae `interval_planned` (índices de muestra del tramo retenido); en `burst_trial` de la campaña anterior queda vacío.

## 0. Resumen ejecutivo

1. **Tarea 1. La regla lineal `hueco = max(1,52; d + 0,52)` NO se cumple para d > 1 s.** Con d = 1 s se cumple en los 1.665 cortes (todos dentro de ±40 ms). Con d = 1,25 / 1,75 / 2,25 s el hueco real es 2,04 / 2,52 / 3,04 s en los 45 cortes de cada condición (sin dispersión), contra 1,77 / 2,27 / 2,77 s predichos: error de +270 / +250 / +270 ms, 0 de 135 dentro de ±40 ms. La espera tras recrear el outlet es 0,76-0,80 s, no 0,52 s. La regla previa se ajustó con d = 0,5 / 1 / 2 / 3 s, todos múltiplos de 0,5 s, y por eso no podía distinguirse de un escalón.
2. **Tarea 1. Modelo escalonado (post hoc).** `hueco = max(1,52; 0,52 + 0,5 · ceil(d / 0,5))` (reanudación en el primer reintento de 0,5 s posterior a la vuelta del outlet) reproduce los 1.800 cortes nuevos (error absoluto medio 1,1 ms, máximo 40 ms = un bloque) y los 7.154 de la campaña anterior (idéntico a la lineal allí). Está inferido de tres valores de d (los tres a 0,25 s de la grilla): es una hipótesis consistente, no una ley confirmada; la atribución al código de liblsl no se verificó contra su fuente.
3. **Tarea 2. La proporción de ensayos tocados escala con K como predice el modelo de ocupación** (2,4 / 7,6 / 14,4 / 27,4 % de los ensayos para K = 2 / 5 / 10 / 20; modelo `K (1,52 + 4) / 387` = 2,9 / 7,1 / 14,3 / 28,5 %), pero **no se detecta caída de balanced accuracy en ningún K** ni en CSP+LDA ni en EEGNet (p Holm = 1,000 en los ocho contrastes; Friedman p = 0,478 y 0,671). Δ medio a K = 20: -1,4 pp (CSP+LDA) y -1,4 pp (EEGNet), mediana 0 y -4,2 pp. Con 24 ensayos por corrida y 9 sujetos la resolución de la BA es de 4,2 pp por ensayo: el barrido no tiene potencia para ver el efecto esperado (< 1 pp).
4. **Tarea 2. Los ensayos no tocados casi no cambian (1 cambio en 3.760 por decodificador); los tocados sí** (10,9 % CSP+LDA, 18,9 % EEGNet), pero casi en igual número a favor y en contra (31 acertaban→fallan vs. 30 fallaban→aciertan en CSP+LDA; 55 vs. 51 en EEGNet). Los 2 únicos cambios en no tocados tienen un corte dentro del relleno de filtrado de 1 s alrededor de la ventana. El daño neto aparece solo con menos de 750 muestras en la ventana (-2,5 pp CSP+LDA, -2,2 pp EEGNet).
5. **Tarea 3. Retener no es más inocuo que borrar.** Mismo patrón de tramo contiguo, mismas severidades: Δ de BA (mediana entre sujetos, severidades 10 / 25 / 40 %) 0 / -4,2 / -8,3 pp en hold (ambos decodificadores) y 0 / -4,2 / -4,2 pp (CSP+LDA) o 0 / -4,2 / -8,3 pp (EEGNet) en burst. Comparación directa Δhold − Δburst: sin diferencias (p Holm ≥ 0,961). Contra su referencia, hold alcanza significación solo en EEGNet 25 % (p Holm = 0,023); burst en CSP+LDA 40 % (0,012) y EEGNet 40 % (0,023); el resto no (todas con n = 9, descriptivo).
6. **Tarea 3. A nivel de ensayo la retención cambia tantas o más decisiones.** Cambio por ensayo (hold / burst) en CSP+LDA: 5,7 / 6,0 % (10 %), 12,3 / 9,0 % (25 %), 19,3 / 14,0 % (40 %); en EEGNet: 8,6 / 7,9 %, 15,8 / 15,1 %, 22,5 / 24,2 %. La diferencia entre hold y burst por sujeto no es significativa (p Holm ≥ 0,56). El 100 % de los ensayos de ambas familias están tocados por diseño.
7. **Tarea 4. La retención produce fallas silenciosas genuinas.** Con la definición del estudio (operativo = llegaron muestras y sin excepciones; degradado = BA móvil W = 8 < umbral del sujeto) hay 797 segundos "operativos y degradados" de 38.250 evaluables en hold (2,08 %; 15 de 135 ejecuciones) contra 929 de 38.250 en burst (2,43 %; 22 de 135). El **100 %** de los segundos degradados de hold son operativos (en burst 93,8-100 %). La mediana entre sujetos de la proporción sigue siendo 0 (como en el estudio): la cola es real (hasta 9,4 % en un sujeto con hold 25 %).
8. **Tarea 4. La telemetría no ve la retención.** Recepción, huecos, `ia_std`, `ia_max`, segundos sin datos y excepciones son indistinguibles de la referencia; única diferencia estadística: latencia media +0,016 a +0,025 ms (2,675 → 2,69-2,70 ms; 9 de 9 sujetos, p Holm = 0,012), que no depende de que el segundo contenga el tramo retenido (AUC 0,55 en ambos casos) y es inservible como alarma. El detector por umbrales del estudio alarma en el 2,7 % de los segundos de hold y de ref (recall sobre los degradados: 2,6 %), contra 27,6 % en burst.
9. **Tarea 5. Control de máquina: ref nueva = ref anterior.** 1.080 de 1.080 decisiones idénticas en CSP+LDA y en EEGNet (45 ejecuciones, 0 con alguna diferencia); misma BA. Latencia media 2,675 vs. 2,664 ms (+0,016 ms, p = 0,008, 8 de 9 sujetos mayores): un corrimiento de sesión de 0,6 %, del mismo orden que el efecto de hold. Las decisiones no dependen de la máquina.
10. **Límites principales.** n = 9 sujetos y BA con granularidad de 4,2 pp; todo exploratorio y post hoc; el modelo escalonado salió de tres puntos; hold no tiene ensayos "no tocados" internos (el diseño toca todos); el umbral de degradación sale de las mismas referencias (la ref nunca lo cruza por construcción y además es idéntica a la anterior); burst se compara con otra campaña (cada familia contra su propia referencia); la mediana entre sujetos oculta una cola en la falla silenciosa.
11. **Implicancias para el manuscrito.** (a) No citar `d + 0,52` como ley general: es válida para d múltiplo de 0,5 s; con otros d la espera depende de la fase del reintento. (b) El barrido de exposición no permite afirmar una curva dosis-respuesta por K; sí confirma el modelo de ocupación y que el daño queda confinado al ensayo tocado. (c) La retención de la última muestra (Simeral et al., 2021) no evita la degradación y es invisible a la telemetría: refuerza la divergencia entre estado operativo y desempeño.

---

## 1. Tarea 1: piso de reconexión

### 1.1 Método

- Cortes de `disconnect-n{2,5,10,20}-1` (d = 1 s; 90 + 225 + 450 + 900 = 1.665 cortes) y de `disconnect-n5-{1.25,1.75,2.25}` (9 sujetos x r0 x 5 cortes = 45 por condición; 135 en total). Total 1.800 cortes en 207 ejecuciones.
- Por corte: `d_log` = `outage_end − outage_start` de `fault_log.jsonl` (grilla de 40 ms); `d_plan` = nominal de `outage_planned`; **hueco** = `gap_s` de la fila de telemetría donde se reanuda el flujo (tiempo de muestra faltante entre la última muestra previa y la primera posterior; resolución 40 ms = un bloque de 10 muestras; es la magnitud a la que se ajustó la regla previa); `ia_max` de la misma fila (intervalo entre llegadas en reloj de pared del receptor, que incluye el periodo del propio bloque: ≈ hueco + 0,04 s); **espera** = hueco − d_log.
- Cada corte se asocia con una fila de telemetría con `n_gaps > 0`, en orden. En las 207 ejecuciones el número de filas, de `outage_start` y de `outage_end` coincide y todas las filas tienen `n_gaps = 1`: 0 emparejamientos dudosos, 0 cortes excluidos. `[m3c_reconexion.py -> m3c_ejecuciones_problema.csv (vacío), m3c_cortes.csv]`
- Regla a poner a prueba: hueco = max(1,52; d + 0,52) s, tolerancia ±40 ms (un bloque), con d nominal (`d_plan`; con `d_log` el error medio cambia en ≤ 10 ms y el resultado es el mismo).

### 1.2 Resultado: la regla lineal falla para d > 1 s

| Condición | d nominal (s) | Cortes | Hueco (s) mediana [mín–máx] | Hueco ia_max (s) mediana | Espera = hueco − d (s) mediana [mín–máx] | Regla lineal: predicción (s) | Lineal: dentro de ±40 ms | Escalonada: predicción (s) | Escalonada: dentro de ±40 ms |
|---|---|---|---|---|---|---|---|---|---|
| disconnect-n2-1 | 1.000 | 90 | 1.52 [1.52–1.56] | 1.560 | 0.52 [0.52–0.56] | 1.52 | 90/90 | 1.52 | 90/90 |
| disconnect-n5-1 | 1.000 | 225 | 1.52 [1.52–1.56] | 1.560 | 0.52 [0.52–0.56] | 1.52 | 225/225 | 1.52 | 225/225 |
| disconnect-n10-1 | 1.000 | 450 | 1.52 [1.52–1.56] | 1.560 | 0.52 [0.52–0.56] | 1.52 | 450/450 | 1.52 | 450/450 |
| disconnect-n20-1 | 1.000 | 900 | 1.52 [1.52–1.56] | 1.560 | 0.52 [0.52–0.56] | 1.52 | 900/900 | 1.52 | 900/900 |
| disconnect-n5-1.25 | 1.250 | 45 | 2.04 [2.04–2.04] | 2.080 | 0.80 [0.76–0.80] | 1.77 | 0/45 | 2.02 | 45/45 |
| disconnect-n5-1.75 | 1.750 | 45 | 2.52 [2.52–2.52] | 2.559 | 0.76 [0.76–0.80] | 2.27 | 0/45 | 2.52 | 45/45 |
| disconnect-n5-2.25 | 2.250 | 45 | 3.04 [3.04–3.04] | 3.079 | 0.80 [0.76–0.80] | 2.77 | 0/45 | 3.02 | 45/45 |

`[m3c_reconexion.py -> m3c_espera_resumen.csv, m3c_modelo_escalonado.csv, m3c_regla.csv]`

- d = 1 s (1.665 cortes): hueco 1,52 s en 1.660 cortes y 1,56 s en 5; los 1.665 caen dentro de ±40 ms de la regla (error máximo 40 ms, tolerado).
- d = 1,25 / 1,75 / 2,25 s: hueco 2,04 / 2,52 / 3,04 s **idéntico en los 45 cortes** de cada condición. Predicción lineal 1,77 / 2,27 / 2,77 s: error +270 / +250 / +270 ms (nominal), **0 de 135 dentro de ±40 ms**. La espera es 0,76-0,80 s (no 0,52 s).
- Dato clave: dentro de cada condición `d_log` toma dos valores que difieren en 40 ms (1,24 y 1,28 s: 34 y 11 cortes; 1,72 y 1,76 s: 16 y 29; 2,24 y 2,28 s: 34 y 11) y el hueco no cambia. El hueco **no depende de forma continua de d**. `[m3c_reconexion.py -> consola, m3c_cortes.csv]`
- Con d = 1 s el hueco no depende de K (2 a 20 cortes por corrida): 1,52 s en todas las condiciones.
- La medida alternativa `ia_max` (sin corregir) da hueco + 0,04 s y por eso cae dentro de ±40 ms de la regla solo en 47-58 % de los cortes de 1 s; descontando el periodo del bloque (−0,04 s) coincide en 99,6-100 %. Para d > 1 s ambas medidas rechazan la regla lineal (0 %).

| Condición | ia_max sin corregir | ia_max − 0,04 s | hueco_ts (gap_s) |
|---|---|---|---|
| disconnect-n10-1 | 48.9 | 99.8 | 100.0 |
| disconnect-n2-1 | 57.8 | 100.0 | 100.0 |
| disconnect-n20-1 | 49.4 | 99.9 | 100.0 |
| disconnect-n5-1 | 46.7 | 99.6 | 100.0 |
| disconnect-n5-1.25 | 0.0 | 0.0 | 0.0 |
| disconnect-n5-1.75 | 0.0 | 0.0 | 0.0 |
| disconnect-n5-2.25 | 0.0 | 0.0 | 0.0 |

(% de cortes dentro de ±40 ms de la regla lineal, según la medida del hueco. `[m3c_reconexion.py -> m3c_regla.csv]`)

### 1.3 Modelo escalonado (post hoc)

Los tres valores nuevos (y los de d = 1 s) siguen `hueco = max(1,52; 0,52 + 0,5 · ceil(d / 0,5))`: la reanudación ocurre en el primer reintento de 0,5 s posterior a la vuelta del outlet, más 0,52 s fijos, con piso de 1,52 s. Para d múltiplo de 0,5 s coincide con la regla lineal (d + 0,52), por eso la campaña anterior (d = 0,5 / 1 / 2 / 3 s; 7.154 cortes) no podía distinguirlas.

| Campaña | Modelo | Cortes | MAE (ms) | Error máx. (ms) | Dentro de ±40 ms (%) |
|---|---|---|---|---|---|
| campaña nueva | lineal max(1,52; d+0,52) | 1800 | 19.86 | 270.00 | 92.50 |
| campaña nueva | escalonado max(1,52; 0,52+0,5*ceil(d/0,5)) | 1800 | 1.11 | 40.00 | 100.00 |
| campaña anterior | lineal max(1,52; d+0,52) | 7154 | 0.21 | 40.00 | 100.00 |
| campaña anterior | escalonado max(1,52; 0,52+0,5*ceil(d/0,5)) | 7154 | 0.21 | 40.00 | 100.00 |

`[m3c_reconexion.py -> m3c_modelo_escalonado.csv]`

> **Actualización 07/10 (verificado en el código).** El modelo escalonado (M2) queda confirmado por la campaña exploratoria ([[Analisis-M3-campana-exploratoria]] §1) y su mecanismo se verificó en la fuente de **liblsl v1.17.7**, la versión que empaqueta mne-lsl 1.14 (`lsl_library_info()` = `git:v1.17.7`, en la notebook y en la VM); las líneas clave son idénticas en `master`. Tres piezas: (a) espera mínima de **1,0 s** del primer intento (`inlet_connection.cpp`, `attempt == 0 ? 1.0 : 5.0`, fija); (b) ondas de consulta cada `multicast_min_rtt` (`resolver_impl.cpp`, modo rápido; `MulticastMinRTT = 0.5` por defecto, **configurable** en `lsl_api.cfg` o con la variable `LSLAPICFG`): **es la grilla de 0,5 s**; (c) `sleep_for(500 ms)` después de recuperar y antes de reconectar (`data_receiver.cpp`, fijo): **es el +0,5 constante**. Prueba experimental en curso (07/10): `MulticastMinRTT = 0.25` debería bajar el hueco de d = 1,25 s de 2,02 a 1,77 s y dejar igual el de 0,5 s.

**Estatus (texto original, antes de la verificación del 07/10).** Es una hipótesis inferida **después** de ver estos datos y con solo tres valores de d, los tres a 0,25 s de la grilla de 0,5 s; el error de 20 ms en 1,25 y 2,25 s es la cuantización de 40 ms del hueco (2,02 s predicho, 2,04 s observado). La coincidencia de 0,5 s con el "sleep fijo de 500 ms" que se atribuyó al código de liblsl es sugerente, pero **no se verificó contra el código fuente de liblsl**. Prueba discriminante pendiente: d = 1,1 y 1,4 s (el modelo escalonado predice 2,02 s para ambos; una espera constante de ~0,78 s predice 1,88 y 2,18 s).

---

### 1.4 Confirmación experimental del mecanismo: `MulticastMinRTT` (07/10)

**Diseño.** Familia `m3rtt` (`runner.py`): `disconnect` con 5 cortes estratificados de d = 0,5 / 1,1 / 1,25 / 1,75 s, sujetos 1-9, corrida 0, bajo dos archivos `lsl_api.cfg` (variable `LSLAPICFG`): `[tuning] MulticastMinRTT = 0.5` (valor por defecto) y `0.25`. 72 ejecuciones, 0 fallidas, 360 cortes, 0 descartados por emparejamiento. liblsl v1.17.7 en la VM (`lsl_library_info()` = `git:v1.17.7`, compilada con GNU 14.2.1). d = 1,1 s se eligió porque **no** está cerca de ningún punto de la grilla de 0,5 s: la regla lineal predice 1,62 s y el modelo escalonado 2,02 s. `[bci-fault-bench/scripts/m3d_rtt.py -> campaign-m3/analysis/m3d_rtt_cortes.csv, m3d_rtt_resumen.csv]`

**Resultado (hueco en s, n = 45 cortes por celda; entre paréntesis, d registrada en la grilla de bloques de 40 ms):**

| d nominal | `MulticastMinRTT` = 0,5 | `MulticastMinRTT` = 0,25 |
|---|---|---|
| 0,5 | 1,52 (45) | 1,52 (45) |
| 1,1 | 2,04 (45) | **1,80** (45) |
| 1,25 | 2,04 (45) | **1,80** (33, d = 1,24) / 2,04 (12, d = 1,28) |
| 1,75 | 2,52 (45) | **2,28** (6 de 6 con d = 1,72) / 2,52 (37 de 39 con d = 1,76) |

**Lectura.**
1. **El parámetro configurable controla la grilla.** Con d = 1,1 s el hueco baja de 2,04 a 1,80 s en los 45 cortes al pasar `MulticastMinRTT` de 0,5 a 0,25 s: es una intervención causal, no una correlación.
2. **El piso de 1,52 s no se mueve** (d = 0,5 s: 1,52 s con ambos valores): el mínimo de 1,0 s y la pausa de 500 ms son fijos, como dice el código.
3. **La regla lineal queda refutada** también con d = 1,1 s (2,04 observado contra 1,62 predicho, configuración por defecto).
4. **La mezcla en 1,25 y 1,75 s no es ruido, es la fase.** El corte real dura d registrada (múltiplo de 40 ms: 1,24 o 1,28; 1,72 o 1,76). Con grilla de 0,25 s, un outlet que vuelve en 1,24 s alcanza la consulta de 1,25 s (hueco 1,77-1,80) y uno que vuelve en 1,28 s la pierde y espera la de 1,50 s (2,02-2,04). Ídem 1,72 frente a 1,76 s respecto de la consulta de 1,75 s. Con grilla de 0,5 s esos valores quedan lejos de un punto de la grilla y no hay ambigüedad.

**Modelo final (con d registrada):** `hueco = max(1,52; 0,52 + RTT · ceil(d / RTT))`, con RTT = `MulticastMinRTT`. Ajusta **359 de 360** cortes de esta prueba dentro de ±40 ms; el único fuera (d = 1,76 s, hueco 2,28 s) es un caso de frontera en el que la consulta de 1,75 s salió unos milisegundos tarde y alcanzó al outlet. Con RTT = 0,5 s reproduce además los 1.800 cortes de §1.3 y los 7.154 de la campaña anterior.

**Conclusión para el manuscrito.** El piso de reconexión está **explicado y demostrado**: 1,0 s de espera mínima fija + la próxima consulta de búsqueda (cada `MulticastMinRTT`, configurable, 0,5 s por defecto) + 0,5 s de pausa fija + unos 20 ms de reconexión. Con la configuración por defecto cada desconexión cuesta al menos 1,52 s; bajar `MulticastMinRTT` acorta solo la parte que depende de la grilla (hasta 0,25 s en este ensayo), y los 1,5 s fijos no bajan sin modificar liblsl. **Estatus**: exploratorio y posterior a los datos del E2; la prueba de intervención se diseñó con predicciones escritas antes de correrla (tabla del 07/10 en la conversación y en `runner.py`).

---

## 2. Tarea 2: barrido de exposición (K = 2 / 5 / 10 / 20 cortes de 1 s)

### 2.1 Método

Condiciones `disconnect-n{K}-1` (225 ejecuciones + 45 ref). **Tocado** = `n_samples < 1000` o inválido (en la ventana [onset+2, onset+6] s). Balanced accuracy de CSP+LDA (en línea) y de EEGNet (ceros); mediana de las 5 corridas por sujeto; pruebas por sujeto (ref, K = 2, 5, 10, 20). Emparejamiento por ensayo con la ref de la misma corrida (1.080 ensayos por condición; 24 ensayos x 45 ejecuciones). `[m3c_exposicion.py -> m3c_exp_exec.csv, m3c_exp_subject.csv, m3c_exp_cond.csv, m3c_exp_tests.csv, m3c_exp_trials.csv]`

### 2.2 Exposición

| Condición | K | Tocados, mediana entre sujetos [Q1–Q3] (%) | Tocados, global (%) (k/n) | Modelo K(1,52+4)/387 (%) | Ensayos inválidos | Muestras perdidas (% de la ventana, global) |
|---|---|---|---|---|---|---|
| ref | 0 | 0.0 [0.0–0.0] | 0.0 (0/1080) | 0.0 | 0 | 0.00 |
| disconnect-n2-1 | 2 | 4.2 [0.0–4.2] | 2.4 (26/1080) | 2.9 | 0 | 0.62 |
| disconnect-n5-1 | 5 | 8.3 [8.3–8.3] | 7.6 (82/1080) | 7.1 | 0 | 2.09 |
| disconnect-n10-1 | 10 | 12.5 [12.5–16.7] | 14.4 (156/1080) | 14.3 | 0 | 4.07 |
| disconnect-n20-1 | 20 | 29.2 [25.0–29.2] | 27.4 (296/1080) | 28.5 | 0 | 7.66 |

`[m3c_exposicion.py -> m3c_exp_cond.csv]`. El modelo de ocupación (cada corte deja tocados los ensayos cuya ventana de 4 s solapa el hueco de 1,52 s, sin solapes ni zona de guarda) acierta la proporción global (modelo − observado entre -0,5 y +1,1 pp). Ningún ensayo quedó inválido: el hueco de 1,52 s deja siempre ≥ 620 de 1.000 muestras (mínimo observado 620; un ensayo con 1.001 por redondeo de borde).

### 2.3 Balanced accuracy

| Decodificador | Condición | BA mediana | Δ vs ref, mediana | Δ vs ref, media | Sujetos peor/igual/mejor | p Wilcoxon | p Holm | r | Friedman p |
|---|---|---|---|---|---|---|---|---|---|
| CSP+LDA | ref | 0.7083 |  |  |  |  |  |  |  |
| CSP+LDA | disconnect-n2-1 | 0.7083 | +0.0000 | +0.0000 | 0/9/0 | n.d. | 1.000 | n.d. | 0.478 |
| CSP+LDA | disconnect-n5-1 | 0.7083 | +0.0000 | -0.0046 | 1/8/0 | 1.000 | 1.000 | 0.00 | 0.478 |
| CSP+LDA | disconnect-n10-1 | 0.7083 | +0.0000 | -0.0046 | 1/8/0 | 1.000 | 1.000 | 0.00 | 0.478 |
| CSP+LDA | disconnect-n20-1 | 0.7083 | +0.0000 | -0.0139 | 2/7/0 | 0.500 | 1.000 | 0.22 | 0.478 |
| EEGNet | ref | 0.7500 |  |  |  |  |  |  |  |
| EEGNet | disconnect-n2-1 | 0.7500 | +0.0000 | +0.0000 | 0/9/0 | n.d. | 1.000 | n.d. | 0.671 |
| EEGNet | disconnect-n5-1 | 0.7500 | +0.0000 | +0.0046 | 0/7/2 | 0.500 | 1.000 | 0.22 | 0.671 |
| EEGNet | disconnect-n10-1 | 0.7083 | +0.0000 | -0.0185 | 3/4/2 | 0.312 | 1.000 | 0.34 | 0.671 |
| EEGNet | disconnect-n20-1 | 0.7500 | -0.0417 | -0.0139 | 5/0/4 | 1.000 | 1.000 | 0.00 | 0.671 |

`[m3c_exposicion.py -> m3c_exp_cond.csv, m3c_exp_tests.csv]`. **No hay caída detectable en ningún K**: p Holm = 1,000 en los ocho contrastes, Friedman p = 0,478 (CSP+LDA) y 0,671 (EEGNet), con 9 sujetos. El Δ medio a K = 20 es -1,4 pp en ambos decodificadores, pero en CSP+LDA 2 de 9 sujetos empeoran y 7 quedan igual, y en EEGNet 5 empeoran y 4 mejoran: ruido de la granularidad de la BA (1 ensayo = 4,2 pp en una corrida). La relación entre la caída y la exposición no es monótona (EEGNet: +0,5 pp a K = 5, -1,9 pp a K = 10, -1,4 pp a K = 20; Spearman entre las 4 condiciones con fallo no informativo con n = 4). **Esto es ausencia de evidencia, no evidencia de ausencia**: con el efecto por ensayo observado (siguiente sección) la caída esperada a K = 20 es < 1 pp, por debajo de la resolución del diseño. Figura: `m3c_exp_curva.png`.

### 2.4 Cambio de decisión: tocados vs. no tocados

| Condición | Decodificador | Grupo | Ensayos | Cambios | Cambio (%) | IC95 Wilson (%) | Acertaba→falla | Fallaba→acierta | Acierto cond. (%) | Acierto ref. (%) |
|---|---|---|---|---|---|---|---|---|---|---|
| disconnect-n2-1 | CSP+LDA | tocado | 26 | 0 | 0.0 | 0.0–12.9 | 0 | 0 | 80.8 | 80.8 |
| disconnect-n2-1 | CSP+LDA | no tocado | 1054 | 0 | 0.0 | 0.0–0.4 | 0 | 0 | 75.8 | 75.8 |
| disconnect-n2-1 | EEGNet | tocado | 26 | 4 | 15.4 | 6.1–33.5 | 1 | 3 | 80.8 | 73.1 |
| disconnect-n2-1 | EEGNet | no tocado | 1054 | 0 | 0.0 | 0.0–0.4 | 0 | 0 | 77.5 | 77.5 |
| disconnect-n5-1 | CSP+LDA | tocado | 82 | 9 | 11.0 | 5.9–19.6 | 4 | 5 | 73.2 | 72.0 |
| disconnect-n5-1 | CSP+LDA | no tocado | 998 | 0 | 0.0 | 0.0–0.4 | 0 | 0 | 76.3 | 76.3 |
| disconnect-n5-1 | EEGNet | tocado | 82 | 15 | 18.3 | 11.4–28.0 | 5 | 10 | 76.8 | 70.7 |
| disconnect-n5-1 | EEGNet | no tocado | 998 | 0 | 0.0 | 0.0–0.4 | 0 | 0 | 78.0 | 78.0 |
| disconnect-n10-1 | CSP+LDA | tocado | 156 | 22 | 14.1 | 9.5–20.4 | 12 | 10 | 71.8 | 73.1 |
| disconnect-n10-1 | CSP+LDA | no tocado | 924 | 0 | 0.0 | 0.0–0.4 | 0 | 0 | 76.4 | 76.4 |
| disconnect-n10-1 | EEGNet | tocado | 156 | 34 | 21.8 | 16.0–28.9 | 20 | 14 | 74.4 | 78.2 |
| disconnect-n10-1 | EEGNet | no tocado | 924 | 0 | 0.0 | 0.0–0.4 | 0 | 0 | 77.3 | 77.3 |
| disconnect-n20-1 | CSP+LDA | tocado | 296 | 30 | 10.1 | 7.2–14.1 | 15 | 15 | 73.6 | 73.6 |
| disconnect-n20-1 | CSP+LDA | no tocado | 784 | 1 | 0.1 | 0.0–0.7 | 1 | 0 | 76.7 | 76.8 |
| disconnect-n20-1 | EEGNet | tocado | 296 | 53 | 17.9 | 14.0–22.7 | 29 | 24 | 74.3 | 76.0 |
| disconnect-n20-1 | EEGNet | no tocado | 784 | 1 | 0.1 | 0.0–0.7 | 0 | 1 | 78.1 | 77.9 |
| TODAS | CSP+LDA | tocado | 560 | 61 | 10.9 | 8.6–13.7 | 31 | 30 | 73.4 | 73.6 |
| TODAS | CSP+LDA | no tocado | 3760 | 1 | 0.0 | 0.0–0.2 | 1 | 0 | 76.2 | 76.3 |
| TODAS | EEGNet | tocado | 560 | 106 | 18.9 | 15.9–22.4 | 55 | 51 | 75.0 | 75.7 |
| TODAS | EEGNet | no tocado | 3760 | 1 | 0.0 | 0.0–0.2 | 0 | 1 | 77.7 | 77.7 |

`[m3c_exposicion.py -> m3c_exp_cambio.csv]`

- **No tocados: 1 cambio en 3.760 ensayos por decodificador** (los de K = 20; son dos ensayos distintos: s02-r4 y s04-r1). Ambos tienen un corte dentro del relleno de filtrado de 1 s que el consumidor agrega a cada lado de la ventana (`consumer.py`, `PAD_S = 1.0`): en s02-r4 el corte empieza 0,20 s después de que cierra la ventana; en s04-r1 el hueco (corte de 1 s + reanudación en 1,52 s) cubre el segundo previo al inicio de la ventana. La definición de "tocado" por `n_samples` de la ventana no captura ese relleno: es un límite de la definición, no una dependencia entre ensayos.
- **Tocados: 10,9 % de las decisiones cambian en CSP+LDA y 18,9 % en EEGNet**, sin crecer con K (el cambio es por ensayo, no por corrida). Pero casi en igual número en ambos sentidos (31 vs. 30 en CSP+LDA; 55 vs. 51 en EEGNet): el acierto de los tocados es 73,4 % vs. 73,6 % (CSP+LDA) y 75,0 % vs. 75,7 % (EEGNet).

### 2.5 Dosis: muestras recibidas en la ventana

| Muestras en la ventana | Decodificador | Ensayos | Cambios | Cambio (%) | IC95 (%) | Acertaba→falla | Fallaba→acierta | Acierto cond. (%) | Acierto ref. (%) |
|---|---|---|---|---|---|---|---|---|---|
| 500-749 | CSP+LDA | 365 | 49 | 13.4 | 10.3–17.3 | 29 | 20 | 71.5 | 74.0 |
| 500-749 | EEGNet | 365 | 82 | 22.5 | 18.5–27.0 | 45 | 37 | 74.0 | 76.2 |
| 750-899 | CSP+LDA | 110 | 9 | 8.2 | 4.4–14.8 | 2 | 7 | 73.6 | 69.1 |
| 750-899 | EEGNet | 110 | 16 | 14.5 | 9.2–22.3 | 6 | 10 | 74.5 | 70.9 |
| 900-999 | CSP+LDA | 85 | 3 | 3.5 | 1.2–9.9 | 0 | 3 | 81.2 | 77.6 |
| 900-999 | EEGNet | 85 | 8 | 9.4 | 4.8–17.5 | 4 | 4 | 80.0 | 80.0 |
| >=1000 | CSP+LDA | 3760 | 1 | 0.0 | 0.0–0.2 | 1 | 0 | 76.2 | 76.3 |
| >=1000 | EEGNet | 3760 | 1 | 0.0 | 0.0–0.2 | 0 | 1 | 77.7 | 77.7 |

`[m3c_exposicion.py -> m3c_exp_dosis.csv]`. Cambio monótono con la pérdida (EEGNet siempre más sensible: 22,5 % vs. 13,4 % a 500-749 muestras). Solo con 500-749 muestras el acierto baja de forma apreciable (-2,5 pp CSP+LDA, -2,2 pp EEGNet; IC amplios, n = 365), y esos ensayos son el 8 % del total en el barrido.

---

## 3. Tarea 3: retención (`hold_trial`) vs. borrado (`burst_trial`)

### 3.1 Método

Mismo patrón de tramo contiguo ubicado al azar dentro de la ventana 2-6 s de cada ensayo (10 / 25 / 40 % de la ventana = 100 / 250 / 400 muestras): en `burst_trial` las muestras se **borran**; en `hold_trial` se **reemplazan por la última muestra válida** (llegan todas: `n_samples = 1000`). Cada familia se compara con su propia referencia (hold contra la ref de la campaña nueva; burst contra la ref de la campaña anterior; el control de la Tarea 5 muestra que ambas refs son equivalentes). Comparación directa: Wilcoxon apareado por sujeto sobre (Δhold − Δburst), Holm sobre las 3 severidades. **Tocado en hold** = `interval_planned` de `fault_log.jsonl` solapa la ventana de decodificación: **3.240 de 3.240 ensayos** (el intervalo cae completo dentro de la ventana en todos; solape medio 100 / 250 / 400 muestras; 24 intervalos por ejecución). En burst: `n_samples < 1000` en 3.240 de 3.240 (media 900 / 750 / 600). Consecuencia: **no hay ensayos no tocados dentro de estas condiciones**. `[m3c_retencion.py -> consola, m3c_ret_trials.csv]`

Control de consistencia: con las mismas funciones sobre `A\raw` se reproducen exactamente el p Holm y la diferencia de `burst_trial` de `A\analysis\t_desempeno.csv` y `analysis-eegnet\t_desempeno.csv` (p Holm 0,375 / 0,250 / 0,0117 en CSP+LDA; 0,594 / 0,594 / 0,0234 en EEGNet). `[m3c_retencion.py -> consola]`

### 3.2 Balanced accuracy contra la referencia

| Familia | Decodificador | Severidad | BA ref (mediana) | BA cond. (mediana) | Δ mediana | Δ media | Sujetos peor/igual/mejor | p Wilcoxon | p Holm | r | Friedman p |
|---|---|---|---|---|---|---|---|---|---|---|---|
| retención (hold) | CSP+LDA | 10 % | 0.7083 | 0.7500 | +0.0000 | -0.0278 | 4/4/1 | 0.188 | 0.188 | 0.44 | 0.063 |
| retención (hold) | CSP+LDA | 25 % | 0.7083 | 0.7083 | -0.0417 | -0.0556 | 6/2/1 | 0.047 | 0.141 | 0.66 | 0.063 |
| retención (hold) | CSP+LDA | 40 % | 0.7083 | 0.7500 | -0.0833 | -0.0417 | 5/1/3 | 0.086 | 0.172 | 0.57 | 0.063 |
| retención (hold) | EEGNet | 10 % | 0.7500 | 0.7500 | +0.0000 | +0.0046 | 2/4/3 | 0.625 | 0.625 | 0.16 | 0.010 |
| retención (hold) | EEGNet | 25 % | 0.7500 | 0.6667 | -0.0417 | -0.0509 | 8/0/1 | 0.008 | 0.023 | 0.89 | 0.010 |
| retención (hold) | EEGNet | 40 % | 0.7500 | 0.7500 | -0.0833 | -0.0648 | 7/0/2 | 0.051 | 0.102 | 0.65 | 0.010 |
| borrado (burst) | CSP+LDA | 10 % | 0.7083 | 0.7083 | +0.0000 | -0.0139 | 4/4/1 | 0.375 | 0.375 | 0.30 | 0.003 |
| borrado (burst) | CSP+LDA | 25 % | 0.7083 | 0.7500 | -0.0417 | -0.0324 | 5/3/1 | 0.125 | 0.250 | 0.51 | 0.003 |
| borrado (burst) | CSP+LDA | 40 % | 0.7083 | 0.6667 | -0.0417 | -0.0648 | 9/0/0 | 0.004 | 0.012 | 0.96 | 0.003 |
| borrado (burst) | EEGNet | 10 % | 0.7500 | 0.7500 | +0.0000 | -0.0139 | 4/3/2 | 0.562 | 0.594 | 0.19 | 0.007 |
| borrado (burst) | EEGNet | 25 % | 0.7500 | 0.7500 | -0.0417 | -0.0370 | 6/1/2 | 0.297 | 0.594 | 0.35 | 0.007 |
| borrado (burst) | EEGNet | 40 % | 0.7500 | 0.7083 | -0.0833 | -0.0787 | 8/0/1 | 0.008 | 0.023 | 0.89 | 0.007 |

`[m3c_retencion.py -> m3c_ret_cond.csv, m3c_ret_tests.csv]`. Δ en puntos de BA (0,0417 = 4,2 pp). Las medianas de los Δ son iguales en ambas familias en 5 de 6 celdas; las medias son del mismo orden (EEGNet: +0,5 / -5,1 / -6,5 pp en hold y -1,4 / -3,7 / -7,9 pp en burst). Figura: `m3c_ret_fig.png`.

### 3.3 Comparación directa hold vs. burst

| Decodificador | Severidad | n | Δ hold (mediana) | Δ burst (mediana) | Δhold − Δburst (mediana) | p Wilcoxon | p Holm | r | Sujetos con menos caída en hold / más |
|---|---|---|---|---|---|---|---|---|---|
| CSP+LDA | 10 % | 9 | 0.0000 | 0.0000 | 0.0000 | 0.344 | 0.961 | 0.32 | 3/4 |
| CSP+LDA | 25 % | 9 | -0.0417 | -0.0417 | -0.0417 | 0.391 | 0.961 | 0.29 | 2/6 |
| CSP+LDA | 40 % | 9 | -0.0833 | -0.0417 | 0.0000 | 0.320 | 0.961 | 0.33 | 5/3 |
| EEGNet | 10 % | 9 | 0.0000 | 0.0000 | 0.0000 | 0.531 | 1.000 | 0.21 | 4/2 |
| EEGNet | 25 % | 9 | -0.0417 | -0.0417 | 0.0000 | 0.719 | 1.000 | 0.12 | 2/4 |
| EEGNet | 40 % | 9 | -0.0833 | -0.0833 | 0.0000 | 0.469 | 1.000 | 0.24 | 4/2 |

`[m3c_retencion.py -> m3c_ret_directo.csv]`. **Sin diferencias** (p Holm ≥ 0,961, r ≤ 0,33). La retención no protege el desempeño.

### 3.4 Cambio de decisión por ensayo

| Familia | Decodificador | Severidad | Grupo | Ensayos | Cambios | Cambio (%) | IC95 (%) | Acertaba→falla | Fallaba→acierta | Acierto cond. (%) | Acierto ref. (%) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | CSP+LDA | 10 % | tocado | 1080 | 62 | 5.7 | 4.5–7.3 | 33 | 29 | 75.6 | 75.9 |
| hold | EEGNet | 10 % | tocado | 1080 | 93 | 8.6 | 7.1–10.4 | 46 | 47 | 77.5 | 77.4 |
| hold | CSP+LDA | 25 % | tocado | 1080 | 133 | 12.3 | 10.5–14.4 | 88 | 45 | 71.9 | 75.9 |
| hold | EEGNet | 25 % | tocado | 1080 | 171 | 15.8 | 13.8–18.1 | 105 | 66 | 73.8 | 77.4 |
| hold | CSP+LDA | 40 % | tocado | 1080 | 208 | 19.3 | 17.0–21.7 | 132 | 76 | 70.7 | 75.9 |
| hold | EEGNet | 40 % | tocado | 1080 | 243 | 22.5 | 20.1–25.1 | 158 | 85 | 70.6 | 77.4 |
| burst | CSP+LDA | 10 % | tocado | 1080 | 65 | 6.0 | 4.7–7.6 | 37 | 28 | 75.1 | 75.9 |
| burst | EEGNet | 10 % | tocado | 1080 | 85 | 7.9 | 6.4–9.6 | 51 | 34 | 75.8 | 77.4 |
| burst | CSP+LDA | 25 % | tocado | 1080 | 97 | 9.0 | 7.4–10.8 | 59 | 38 | 74.0 | 75.9 |
| burst | EEGNet | 25 % | tocado | 1080 | 163 | 15.1 | 13.1–17.4 | 103 | 60 | 73.4 | 77.4 |
| burst | CSP+LDA | 40 % | tocado | 1080 | 151 | 14.0 | 12.0–16.2 | 106 | 45 | 70.3 | 75.9 |
| burst | EEGNet | 40 % | tocado | 1080 | 261 | 24.2 | 21.7–26.8 | 171 | 90 | 69.9 | 77.4 |

`[m3c_retencion.py -> m3c_ret_cambio.csv]`. Los 1.080 ensayos de cada celda están tocados. En CSP+LDA la retención cambia más decisiones que el borrado a 25 y 40 % (12,3 vs. 9,0 % y 19,3 vs. 14,0 %; IC95 del 40 % sin solape: 17,0-21,7 vs. 12,0-16,2) pero el efecto neto sobre el acierto es parecido: a 40 %, 132 aciertos perdidos y 76 ganados en hold (-56 de 1.080) contra 106 y 45 en burst (-61), con acierto de 70,7 % vs. 70,3 % (ref 75,9 %). En EEGNet son equivalentes. Por sujeto la diferencia no es significativa:

| Decodificador | Severidad | n | Cambio hold (mediana entre sujetos) | Cambio burst (mediana entre sujetos) | Dif. (mediana) | p Wilcoxon | p Holm | r |
|---|---|---|---|---|---|---|---|---|
| CSP+LDA | 10 % | 9 | 0.0500 | 0.0417 | 0.0083 | 0.672 | 1.000 | 0.14 |
| CSP+LDA | 25 % | 9 | 0.1000 | 0.0833 | 0.0250 | 0.188 | 0.562 | 0.44 |
| CSP+LDA | 40 % | 9 | 0.1250 | 0.1250 | 0.0083 | 0.578 | 1.000 | 0.19 |
| EEGNet | 10 % | 9 | 0.0917 | 0.0500 | 0.0083 | 0.570 | 1.000 | 0.19 |
| EEGNet | 25 % | 9 | 0.1167 | 0.1333 | 0.0000 | 0.641 | 1.000 | 0.16 |
| EEGNet | 40 % | 9 | 0.2083 | 0.2583 | -0.0083 | 0.215 | 0.645 | 0.41 |

`[m3c_retencion.py -> m3c_ret_cambio_directo.csv]`

---

## 4. Tarea 4: fallas silenciosas con `hold_trial`

### 4.1 Método (misma definición del estudio)

`bcibench.metrics`: **operativo** (por segundo) = llegaron muestras (`n_samples > 0`) y `exceptions == 0`; **degradado** = última BA móvil W = 8 ensayos de CSP+LDA en línea (inválido = error) **<** umbral del sujeto de `A\analysis\thresholds.json` (mínimo de la móvil en sus 5 referencias de la campaña anterior); **silenciosa** = operativo y degradado, como proporción de los segundos evaluables (con móvil disponible). Se informa la mediana entre sujetos de la proporción por ejecución y los conteos totales. `[m3c_silenciosa.py -> m3c_sil_exec.csv, m3c_sil_cond.csv]`

**Controles.** (a) La ref nueva no cruza el umbral: 0 de 12.750 segundos evaluables degradados; el mínimo de la móvil por sujeto coincide exactamente con el umbral en los 9 sujetos (consistente con la Tarea 5: las decisiones son idénticas). (b) Recalculada sobre la campaña anterior (ref + burst, 69.660 segundos) reproduce `windows.csv` al 100,000 % (`degraded` y `operational`). `[m3c_silenciosa.py -> m3c_sil_control.csv]`

### 4.2 Resultado

| Campaña | Condición | Evaluables (s) | Degradados (s) | Operativos y degradados (s) | Proporción por ejecución, mediana entre sujetos | Máx. entre sujetos | Global (%) | Degradado que es silencioso (%) | Ejecuciones con ≥1 s (de 45) | Sujetos con ≥1 s (de 9) | Segundos sin muestras |
|---|---|---|---|---|---|---|---|---|---|---|---|
| nueva | ref | 12750 | 0 | 0 | 0.0000 | 0.0000 | 0.00 | n.d. | 0 | 0 [] | 0 |
| nueva | hold_trial-0.1 | 12750 | 40 | 40 | 0.0000 | 0.0000 | 0.31 | 100.0 | 2 | 1 [5] | 0 |
| nueva | hold_trial-0.25 | 12750 | 416 | 416 | 0.0000 | 0.0935 | 3.26 | 100.0 | 8 | 4 [4, 5, 7, 9] | 0 |
| nueva | hold_trial-0.4 | 12750 | 341 | 341 | 0.0000 | 0.0000 | 2.67 | 100.0 | 5 | 5 [1, 5, 7, 8, 9] | 0 |
| anterior | ref | 12750 | 0 | 0 | 0.0000 | 0.0000 | 0.00 | n.d. | 0 | 0 [] | 0 |
| anterior | burst_trial-0.1 | 12750 | 124 | 124 | 0.0000 | 0.0000 | 0.97 | 100.0 | 4 | 3 [5, 6, 7] | 0 |
| anterior | burst_trial-0.25 | 12750 | 370 | 369 | 0.0000 | 0.0839 | 2.89 | 99.7 | 10 | 6 [1, 3, 4, 5, 7, 9] | 13 |
| anterior | burst_trial-0.4 | 12750 | 465 | 436 | 0.0000 | 0.0000 | 3.42 | 93.8 | 8 | 6 [3, 4, 5, 6, 7, 9] | 1308 |

`[m3c_silenciosa.py -> m3c_sil_cond.csv]`

- **Hold: 40 / 416 / 341 segundos operativos y degradados (0,31 / 3,26 / 2,67 % de los segundos evaluables)**; 797 en total (2,08 %) en 15 de 135 ejecuciones y en 1 / 4 / 5 sujetos. **El 100 % de los segundos degradados son operativos**: en hold no hay un solo segundo sin muestras ni con excepción (0 segundos sin datos, 0 excepciones en las 135 ejecuciones).
- Burst (campaña anterior, recalculado): 124 / 369 / 436 (0,97 / 2,89 / 3,42 %), 929 en total (2,43 %) en 22 de 135 ejecuciones; 93,8-100 % de los degradados son operativos (solo `burst_trial-0.4`, con tramo de 1,6 s, tiene segundos sin datos: 1.308).
- La **mediana entre sujetos de la proporción por ejecución es 0** en todas las condiciones, de hold y de burst (como en el estudio); la cola es real: máximo por sujeto 9,4 % (hold 25 %) y 8,4 % (burst 25 %). Con n = 9 las pruebas de Wilcoxon sobre esa proporción no son informativas (casi todas las diferencias son 0: p no definido o 1,000; `m3c_sil_tests.csv`); el resultado se lee en los conteos.
- Hold vs. burst: sin diferencia detectable en la proporción silenciosa (p Holm = 1,000; `m3c_sil_directo.csv`). Es decir, **la retención produce tantas fallas silenciosas como el borrado, pero las produce sin ninguna señal de telemetría ni siquiera parcial**.
- Otras condiciones de la campaña nueva (para contexto): `disconnect-n10-1` 26 segundos silenciosos (2 ejecuciones), `disconnect-n5-1.75` 16 (1 ejecución), el resto 0. `[m3c_silenciosa.py -> m3c_sil_cond.csv]`

| Condición | Evaluables (s) | Degradados (s) | Operativos y degradados (s) | Mediana entre sujetos | Ejecuciones con ≥1 s | Segundos sin muestras |
|---|---|---|---|---|---|---|
| disconnect-n10-1 | 12750 | 27 | 26 | 0.0000 | 2 | 246 |
| disconnect-n2-1 | 12750 | 0 | 0 | 0.0000 | 0 | 56 |
| disconnect-n20-1 | 12750 | 0 | 0 | 0.0000 | 0 | 501 |
| disconnect-n5-1 | 12750 | 0 | 0 | 0.0000 | 0 | 132 |
| disconnect-n5-1.25 | 2822 | 0 | 0 | 0.0000 | 0 | 48 |
| disconnect-n5-1.75 | 2822 | 16 | 16 | 0.0000 | 1 | 72 |
| disconnect-n5-2.25 | 2822 | 0 | 0 | 0.0000 | 0 | 91 |

### 4.3 ¿La telemetría ve algo en hold?

Pruebas por sujeto (mediana de 5 corridas), ref vs. hold, Holm dentro del tipo `hold_trial`:

| Variable | Severidad | Ref (mediana entre sujetos) | Hold (mediana entre sujetos) | Diferencia | p Wilcoxon | p Holm | r |
|---|---|---|---|---|---|---|---|
| recv_ratio | 10 % | 0.99984 | 0.99984 | 0.00000 | n.d. | 1.000 | n.d. |
| recv_ratio | 25 % | 0.99984 | 0.99984 | 0.00000 | n.d. | 1.000 | n.d. |
| recv_ratio | 40 % | 0.99984 | 0.99984 | 0.00000 | n.d. | 1.000 | n.d. |
| n_gaps | 10 % | 0.00000 | 0.00000 | 0.00000 | n.d. | 1.000 | n.d. |
| n_gaps | 25 % | 0.00000 | 0.00000 | 0.00000 | n.d. | 1.000 | n.d. |
| n_gaps | 40 % | 0.00000 | 0.00000 | 0.00000 | n.d. | 1.000 | n.d. |
| gap_s | 10 % | 0.00000 | 0.00000 | 0.00000 | n.d. | 1.000 | n.d. |
| gap_s | 25 % | 0.00000 | 0.00000 | 0.00000 | n.d. | 1.000 | n.d. |
| gap_s | 40 % | 0.00000 | 0.00000 | 0.00000 | n.d. | 1.000 | n.d. |
| lat_mean_ms | 10 % | 2.67496 | 2.69977 | 0.02509 | 0.004 | 0.012 | 0.96 |
| lat_mean_ms | 25 % | 2.67496 | 2.69863 | 0.02344 | 0.004 | 0.012 | 0.96 |
| lat_mean_ms | 40 % | 2.67496 | 2.69339 | 0.01584 | 0.004 | 0.012 | 0.96 |
| lat_max_ms | 10 % | 20.12000 | 16.15000 | 4.01000 | 1.000 | 1.000 | 0.00 |
| lat_max_ms | 25 % | 20.12000 | 20.15000 | -1.96000 | 0.820 | 1.000 | 0.08 |
| lat_max_ms | 40 % | 20.12000 | 24.14000 | 4.00000 | 0.195 | 0.586 | 0.43 |
| ia_std_ms | 10 % | 1.88917 | 1.88806 | -0.00336 | 0.910 | 1.000 | 0.04 |
| ia_std_ms | 25 % | 1.88917 | 1.88284 | -0.00165 | 0.496 | 1.000 | 0.23 |
| ia_std_ms | 40 % | 1.88917 | 1.88920 | -0.00426 | 0.820 | 1.000 | 0.08 |
| ia_max_ms | 10 % | 42.84000 | 42.52000 | -0.32000 | 0.020 | 0.059 | 0.78 |
| ia_max_ms | 25 % | 42.84000 | 42.65000 | -0.10000 | 0.652 | 0.652 | 0.15 |
| ia_max_ms | 40 % | 42.84000 | 42.66000 | -0.21000 | 0.164 | 0.328 | 0.46 |
| secs_no_data | 10 % | 0.00000 | 0.00000 | 0.00000 | n.d. | 1.000 | n.d. |
| secs_no_data | 25 % | 0.00000 | 0.00000 | 0.00000 | n.d. | 1.000 | n.d. |
| secs_no_data | 40 % | 0.00000 | 0.00000 | 0.00000 | n.d. | 1.000 | n.d. |

`[m3c_silenciosa.py -> m3c_sil_telemetria.csv]`. Recepción, huecos, segundos sin datos y excepciones: idénticos (no definidos: todas las diferencias son 0). `lat_max`, `ia_std`, `ia_max`: sin diferencia tras Holm. **Única diferencia: latencia media +0,016 a +0,025 ms** (2,675 → 2,693-2,700 ms; 0,6-0,9 %; 9 de 9 sujetos, p Holm = 0,012, r = 0,96). Es específica de hold dentro de la campaña (las condiciones de desconexión de la misma campaña quedan entre -0,008 y +0,005 ms de media contra la ref, con 3 a 7 de 9 sujetos por encima; `m3c_sil_latencia_condiciones.csv`), pero no está ligada al tramo retenido ni sirve de alarma:

| variable | burst (anterior), todos los segundos | hold, segundos con tramo | hold, todos los segundos |
|---|---|---|---|
| exceptions | n.d. | n.d. | n.d. |
| gap_s | 0.574 | n.d. | n.d. |
| ia_max | 0.543 | 0.527 | 0.512 |
| ia_std | 0.553 | 0.519 | 0.509 |
| lat_max | 0.546 | 0.559 | 0.553 |
| lat_mean | 0.563 | 0.553 | 0.547 |
| n_gaps | 0.562 | n.d. | n.d. |
| recv_ratio | 0.623 | 0.502 | 0.500 |

(AUC de cada variable por segundo, separación = max(AUC, 1 − AUC); 0,5 = no separa. Hold, segundos que contienen el tramo vs. segundos de ref, y burst vs. su ref. `[m3c_silenciosa.py -> m3c_sil_auc.csv]`). En hold ninguna variable supera 0,56; la latencia media da 0,553 en los segundos con tramo y 0,547 en todos. En burst `recv_ratio` llega a 0,62.

El detector por umbrales del estudio (límites de la referencia de los otros 8 sujetos, 0,5-99,5 %, 8 variables):

| Grupo de segundos | Segundos | Alarmas | Tasa de alarma (%) | Degradados | Alarmas en degradados | Recall sobre degradados (%) | Silenciosos | Alarmas en silenciosos |
|---|---|---|---|---|---|---|---|---|
| ref nueva (LOSO) | 12750 | 340 | 2.7 | 0 | 0 | n.d. | 0 | 0 |
| hold_trial-0.1 (todos los segundos) | 12750 | 310 | 2.4 | 40 | 1 | 2.5 | 40 | 1 |
| hold_trial-0.25 (todos los segundos) | 12750 | 352 | 2.8 | 416 | 11 | 2.6 | 416 | 11 |
| hold_trial-0.4 (todos los segundos) | 12750 | 352 | 2.8 | 341 | 9 | 2.6 | 341 | 9 |
| hold (3 severidades, todos los segundos) | 38250 | 1014 | 2.7 | 797 | 21 | 2.6 | 797 | 21 |
| hold (segundos con tramo) | 9364 | 195 | 2.1 | 220 | 9 | 4.1 | 220 | 9 |
| ref anterior (LOSO) | 12750 | 334 | 2.6 | 0 | 0 | n.d. | 0 | 0 |
| burst_trial-0.1 (todos los segundos) | 12750 | 2465 | 19.3 | 124 | 20 | 16.1 | 124 | 20 |
| burst_trial-0.25 (todos los segundos) | 12750 | 3375 | 26.5 | 370 | 98 | 26.5 | 369 | 97 |
| burst_trial-0.4 (todos los segundos) | 12750 | 4271 | 33.5 | 465 | 147 | 31.6 | 436 | 118 |
| burst (3 severidades, todos los segundos) | 38250 | 10111 | 26.4 | 959 | 265 | 27.6 | 929 | 235 |

`[m3c_silenciosa.py -> m3c_sil_detector.csv]`. En hold la tasa de alarma (2,7 %) es la de la propia referencia (2,7 %) y el recall sobre los segundos degradados (2,6 %) es el nivel de falsa alarma; en burst es 27,6 % (porque el borrado deja huecos y baja `recv_ratio`). La retención hace exactamente lo que se quería probar: **todas las muestras llegan y la telemetría no ve nada**.

---

## 5. Tarea 5: control de máquina (ref nueva vs. ref anterior)

Las mismas 45 corridas (9 sujetos x 5 corridas), misma señal y mismo decodificador congelado, en dos campañas distintas. Decisión idéntica = ambos válidos y misma predicción (o ambos inválidos); EEGNet = "ceros" nueva vs. `trials_eegnet.csv` anterior. `[m3c_control.py -> m3c_ctl_ensayos.csv, m3c_ctl_resumen.csv, m3c_ctl_tests.csv]`

| Decodificador | Ejecuciones | Ensayos | Decisiones idénticas | % idénticas | Ejecuciones con alguna diferencia | % n_samples igual | |Δ proba| media |
|---|---|---|---|---|---|---|---|
| CSP+LDA | 45 | 1080 | 1080 | 100.0000 | 0 | 99.9074 | 0.0004 |
| EEGNet | 45 | 1080 | 1080 | 100.0000 | 0 | 100.0000 | 0.0000 |

**1.080 de 1.080 decisiones idénticas** en ambos decodificadores (45 de 45 ejecuciones sin ninguna diferencia); misma BA (CSP+LDA 0,7083, EEGNet 0,7500). `n_samples` igual en 99,9 % de los ensayos de CSP+LDA (1 ensayo difiere) y en el 100 % de EEGNet.

| Variable | Nueva (mediana entre sujetos) | Anterior (mediana entre sujetos) | Diferencia (mediana) | Dif. por ejecución mín. | Dif. por ejecución máx. | p Wilcoxon | r | Sujetos mayor/menor en la nueva |
|---|---|---|---|---|---|---|---|---|
| lat_mean_ms | 2.67496 | 2.66377 | 0.01561 | -0.01517 | 0.06227 | 0.008 | 0.89 | 8/1 |
| lat_max_ms | 20.12000 | 9.36000 | -1.75000 | -30.88000 | 30.92000 | 0.910 | 0.04 | 3/6 |
| ia_std_ms | 1.88917 | 1.88850 | 0.00486 | -0.06930 | 0.07276 | 0.820 | 0.08 | 5/4 |
| ia_max_ms | 42.84000 | 42.57000 | 0.47000 | -3.47000 | 5.20000 | 0.121 | 0.52 | 8/1 |
| recv_ratio | 0.99984 | 0.99984 | 0.00000 | 0.00000 | 0.00000 | n.d. | n.d. | 0/0 |
| decision_delay_ms | 1031.75000 | 1031.75000 | -0.00000 | -2.40000 | 3.05000 | 1.000 | 0.00 | 4/5 |
| bacc | 0.70833 | 0.70833 | 0.00000 | 0.00000 | 0.00000 | n.d. | n.d. | 0/0 |
| valid_rate | 1.00000 | 1.00000 | 0.00000 | 0.00000 | 0.00000 | n.d. | n.d. | 0/0 |
| timing_p99_ms | 0.00155 | 0.00136 | 0.00017 | -0.00010 | 0.00064 | 0.004 | 0.96 | 9/0 |
| bacc EEGNet (ceros vs E2) | 0.75000 | 0.75000 | 0.00000 | 0.00000 | 0.00000 | n.d. | n.d. | 0/0 |

Telemetría: la latencia media sube +0,016 ms en la campaña nueva (2,675 vs. 2,664 ms; 8 de 9 sujetos mayores, p = 0,008) y el p99 del error de temporización del productor +0,00017 ms (9 de 9); `ia_std`, `ia_max`, `decision_delay` y `lat_max` no difieren. El corrimiento de sesión (+0,016 ms) es del mismo orden que la diferencia de latencia de hold (+0,016 a +0,025 ms): con esta campaña **no se puede afirmar** que ese +0,02 ms de hold sea un efecto de la retención y no de la sesión, aunque dentro de la campaña las demás condiciones no lo muestran. En ningún caso afecta a las decisiones.

---

## 6. Límites

1. **Exploratorio y post hoc.** Los tres experimentos se diseñaron tras ver los resultados de la campaña definitiva; no hay corrección por multiplicidad entre tablas. Con n = 9 sujetos y p exacto mínimo de 0,0039, los p Holm de 0,012-0,023 son los únicos "significativos" y deben leerse como descriptivos.
2. **Resolución de la BA.** 24 ensayos por corrida: un ensayo = 4,2 pp en una corrida; la mediana por sujeto de 5 corridas toma valores discretos. El barrido de exposición no tiene potencia para efectos < 2-3 pp; la ausencia de significación no es equivalencia.
3. **Modelo escalonado de reconexión:** inferido de tres valores de d (1,25 / 1,75 / 2,25 s) más los de la campaña anterior, todos múltiplos de 0,5 s; no se discrimina de otras formas escalonadas ni se verificó contra el código de liblsl; los 135 cortes del diagnóstico son 45 por condición, 5 por ejecución (r0 únicamente, 9 sujetos) y el hueco es determinista (sin variación), así que el n efectivo es 9 ejecuciones x 5 cortes en un mismo mecanismo.
4. **Definición de "tocado" por `n_samples`.** No captura el relleno de filtrado de 1 s a cada lado de la ventana (2 de 3.760 ensayos "no tocados" cambiaron por esto). En hold, todos los ensayos están tocados por diseño: no hay control interno dentro de la condición; el control es la ref de la misma campaña.
5. **Burst vs. hold son campañas distintas.** Cada familia se compara con su propia ref (equivalentes: 100 % de decisiones idénticas) y las pruebas directas usan Δ contra la ref; la latencia difiere +0,016 ms entre sesiones. El EEGNet de la campaña anterior viene de `trials_eegnet.csv` (E2) y el de la nueva del modo "ceros" (reproduce E2 al 99,96 %, validado en la campaña anterior; no se repitió aquí porque `segments.npz` de la anterior no está en la copia local).
6. **Falla silenciosa.** El umbral (mínimo de la móvil W = 8 en las 5 referencias del sujeto) se calculó sobre las mismas corridas de la ref anterior y la ref nueva es idéntica: por construcción la ref no lo cruza (control (a)). La proporción depende de W y del umbral (la sensibilidad se estudió en [[Analisis-M3-ensayos-divergencia]] para la campaña anterior; no se repitió con hold). La mediana entre sujetos es 0; el resultado está en conteos y colas, con pocos sujetos por celda (1-5 de 9).
7. **Telemetría.** La latencia +0,02 ms de hold es específica de la condición dentro de la campaña pero no puede separarse de la deriva entre sesiones (+0,016 ms); no se identificó la causa. El detector por umbrales es el del estudio (límites LOSO de la ref, sin ajuste); otros detectores (modelos de aprendizaje) no se probaron en hold.
8. **Un solo patrón de retención** (tramo contiguo, última muestra válida) y 3 severidades; no se probó retención dispersa ni retención con estimación ("muestreo y retención" de un receptor real puede incluir otros pasos).
9. **Las 27 ejecuciones del piso** no están en `plan.json` (existen en `N`); su análisis usa el listado de carpetas.
10. **Efectos colaterales de la ejecución.** El script de EEGNet (`m3_eegnet_relleno.py`) escribió `trials_eegnet_{ceros,interp,hold}.csv` dentro de cada carpeta de `N` y sus resúmenes en `B\campaign-m3\analysis-eegnet\`; no se tocó nada más de la campaña, del banco ni del manuscrito.

## 7. Reproducción

```
cd B\scripts
# EEGNet (desde 40-Prototipo): m3_eegnet_relleno.py --root N --models 40-Prototipo\results\models --out B\campaign-m3\analysis-eegnet
python m3c_reconexion.py   # Tarea 1
python m3c_exposicion.py   # Tarea 2
python m3c_retencion.py    # Tarea 3
python m3c_silenciosa.py   # Tarea 4
python m3c_control.py      # Tarea 5
python m3c_tablas_md.py    # tablas de esta nota -> campaign-m3\analysis\m3c_tablas.md
```
Utilidades comunes en `m3c_common.py`.
