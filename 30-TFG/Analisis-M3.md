# Análisis M3: piso de reconexión, exposición de la ventana, IC de las diferencias y fuentes

> 2026-10-07. Campaña definitiva `campaign-2026-09-27` (855 ejecuciones = 9 sujetos x 5 corridas x 19 condiciones). Nota nueva; no modifica el manuscrito ni el código del banco. Relacionada con [[Mejoras-Redaccion-M3]], [[Fundamentos-Diseno-Estadistico]] y [[Trabajo-Futuro]].
>
> **Convenciones.** Rutas base: `B = C:\Users\agustin.tamagusuku\Desktop\bci-fault-bench`; datos `D = B\campaign-2026-09-27`; resultados intermedios en `D\analysis-m3\`. Scripts en `B\scripts\m3_*.py`, ejecutados con `C:\Users\agustin.tamagusuku\.venvs\bcibench\Scripts\python`. Las tablas usan punto decimal. "Diferencia" = condición menos referencia (negativo = degradación). BA = balanced accuracy. Cada cifra lleva entre corchetes `[script -> archivo]`.
>
> **Estado de lo producido.** Todo lo de las tareas 1 a 3 se calculó sobre los CSV de la campaña (no se ejecutó nada en VM). La lectura del código de liblsl (tarea 1) y las citas (tarea 4) vienen de la web y están marcadas con su URL.

## 0. Resumen ejecutivo

1. **Piso de reconexión.** En los 7.154 cortes de `disconnect` y `disconnect_trial` el hueco de datos (tiempo de muestra) es **max(1,52; d + 0,52) s**, con error de 0 a 40 ms (un bloque) en el 100 % de los cortes. La espera extra del receptor es r = 0,52 s para d >= 1 s y 1,00-1,04 s para d = 0,5 s. No depende del sujeto, de la corrida ni del instante del corte.
2. **Atribución: LSL, no el banco.** El código de liblsl explica las dos constantes: espera mínima de 1,0 s del primer intento de resolución + `sleep` fijo de 500 ms antes de reconectar = 1,5 s (+ 20 ms de reconexión). `consumer.py` no tiene lógica de reconexión. Falta verificar la versión de liblsl que empaqueta mne-lsl y la forma funcional exacta para d no múltiplo de 0,5 s (diagnóstico opcional de unos 30 min en VM, sección 1.6).
3. **Exposición.** En desconexión uniforme se toca el 6,2-8,7 % de los ensayos (global) y la ventana se pierde por más de la mitad solo con 3 s (4,2 %). El modelo E = N(d + r + w)/T con la r de la tarea 1 da 7,1 / 7,1 / 9,7 % y la versión con zona de guarda 7,0 / 6,9 / 9,6 %: dentro de 1,3 errores estándar de lo observado.
4. **Exposición vs. caída.** La caída de BA sigue la fracción de ventana perdida (Spearman -0,94 CSP+LDA y -0,93 EEGNet entre 18 condiciones; -0,99 y -0,85 en las 7 con pérdida >5 %), no la proporción de ventanas tocadas. En desconexión uniforme, con E <= 8,7 %, la caída máxima posible (peor caso: exactitud al azar en lo tocado) es de 1,6-2,4 puntos, por eso ninguna diferencia media cae fuera de +-0,03 por dilución (el IC exacto de CSP+LDA a 3 s llega a -0,042 por la resolución discreta, ver 3.4).
5. **IC (HL, exacto de Wilcoxon, nivel real 96,1 %, n = 9).** CSP+LDA: 8 de 18 condiciones con IC dentro de +-0,03 (jitter, retraso, desconexión 0,5 y 1 s). EEGNet: 11 de 18 (las anteriores más pérdida 1 y 10 %, desconexión 3 s). Fuera en ambos: pérdida contigua (10/25/40 %) y desconexión en el ensayo (0,5/1/2 s). Solo 6 de los 36 intervalos excluyen el cero.
6. **Límite de los IC.** La BA por sujeto avanza de a 1/24 = 0,042 (24 ensayos, mediana de 5 corridas): el margen +-0,03 es menor que un escalón. Los IC "dentro" de jitter y retraso son degenerados [0;0] porque las decisiones son idénticas (9/9 sujetos con diferencia exactamente 0), no por precisión estadística.
7. **EEGNet vs. CSP+LDA.** Con la misma pérdida de ventana (38 %) un corte al inicio de la ventana cuesta -0,130 a EEGNet y -0,051 a CSP+LDA; una pérdida contigua al azar del 40 % cuesta -0,079 y -0,065. Es una observación sin explicar (hipótesis, no probada: posición del hueco al inicio de la ventana).
8. **Fuentes.** Gallego et al. (2020) y Karpowicz et al. (2025) verificados con Crossref y Europe PMC. **El número de artículo de Karpowicz es 4662, no 4283.** Ambos son registros intracorticales en primates: respaldan "la señal registrada cambia y los decodificadores fijos se degradan sin falla del sistema", pero no se pueden extrapolar sin más a EEG de superficie.

---

## 1. Piso de reconexión

### 1.1 Método

- **Qué se mide.** Para cada corte (evento `outage_start`/`outage_end` de `fault_log.jsonl`) se toma la fila de telemetría con `n_gaps > 0` donde se reanuda el flujo y su `gap_s`. `gap_s` es la suma de (salto de marca de tiempo - 1/250 s) que calcula `consumer.py` (clase `Telemetry.on_chunk`): es el tiempo de muestra transcurrido entre la última muestra recibida antes del corte y la primera recibida después, **en escala nominal y con resolución de 40 ms** (los bloques son de 10 muestras). Es mejor que `ia_max` porque no depende del reloj de llegada del receptor. Se conserva `ia_max` como segundo estimador.
- **Duración del corte d.** `outage_end - outage_start` del log, alineada a la grilla de bloques de 40 ms (por eso un corte nominal de 0,5 s vale 0,48 o 0,52 s según la fase). `espera_receptor r = hueco - d`.
- **Apareamiento corte-fila.** En las 270 ejecuciones el número de filas con `n_gaps > 0` coincide con el de `outage_end` y siempre `n_gaps = 1` (0 discrepancias). 7.154 cortes: 674 uniformes (una corrida planificó 4 cortes) y 6.480 en el ensayo.
- Script `[B\scripts\m3_reconexion.py -> D\analysis-m3\m3_cortes.csv, m3_espera_resumen.csv, m3_grilla.csv]`.

### 1.2 Distribución del hueco y de la espera por duración de corte

`[m3_reconexion.py -> m3_espera_resumen.csv]` (segundos; p5 y p95 sobre todos los cortes de la condición)

| Condición | Cortes | d registrada (mediana) | Hueco: mediana | p5 | p95 | Espera r = hueco - d: mediana | r p5 | r p95 | ia_max - d: mediana |
|---|---|---|---|---|---|---|---|---|---|
| desconexión uniforme 0,5 s | 225 | 0.520 | 1.520 | 1.520 | 1.520 | 1.000 | 1.000 | 1.040 | 1.045 |
| desconexión uniforme 1 s | 224 | 1.000 | 1.520 | 1.520 | 1.520 | 0.520 | 0.520 | 0.520 | 0.560 |
| desconexión uniforme 3 s | 225 | 3.000 | 3.520 | 3.520 | 3.560 | 0.520 | 0.520 | 0.560 | 0.561 |
| desconexión en el ensayo 0,5 s | 2160 | 0.480 | 1.520 | 1.520 | 1.520 | 1.040 | 1.000 | 1.040 | 1.079 |
| desconexión en el ensayo 1 s | 2160 | 1.000 | 1.520 | 1.520 | 1.520 | 0.520 | 0.520 | 0.520 | 0.560 |
| desconexión en el ensayo 2 s | 2160 | 2.000 | 2.520 | 2.520 | 2.520 | 0.520 | 0.520 | 0.520 | 0.559 |

- El hueco toma **un solo valor** en casi todos los cortes: 1,52 s (d <= 1), 2,52 s (d = 2; 99,7 %, el resto 2,56) y 3,52 s (d = 3; 88,4 %, el resto 3,56). Máximo apartamiento: un bloque de 40 ms. `[m3_reconexion.py -> consola, "valores distintos de hueco_ts"; reproducible desde m3_cortes.csv]`
- `ia_max` supera a `gap_s` en un bloque (0,04 s): por eso el hallazgo previo de 1,56 / 2,56 / 3,6 s es el mismo fenómeno medido en llegadas, y 1,56 s en tiempo de muestra son 1,52 s.
- Para d = 0,5 s, r vale 1,00 o 1,04 s según d sea 0,52 o 0,48 s: el hueco es constante (1,52 s), r es el resto del piso, no una espera propia.
- Por sujeto, la mediana de r es idéntica en los 9 sujetos (0,52 s; 1,00-1,04 s para 0,5 s). `[m3_reconexion.py -> consola, "espera_ts por (kind, severity, subject)"]`

### 1.3 Pruebas de la forma funcional y de la "grilla"

`[m3_reconexion.py -> m3_grilla.csv y consola]`

- **Modelo hueco = max(c0, d + c1).** Ajuste por mínimos cuadrados con búsqueda en grilla de 0,01 s: c0 = 1,52 s, c1 = 0,52 s, error absoluto medio 0,2 ms, máximo 40 ms, **100 % de los 7.154 cortes dentro de un bloque**. En la escala de llegadas el modelo del enunciado, max(1,56; d + 0,56), acierta dentro de 40 ms en el 99,9 %.
- **Grilla en tiempo absoluto: no.** El instante de reanudación (inicio_corte + hueco) módulo 0,5 s y módulo 1 s toma 21-25 valores distintos por condición (frecuencia de la moda 7-15 %; uniforme sobre la grilla de 40 ms daría 4 %); lo mismo que el propio inicio del corte. No hay concentración en valores discretos del reloj; el retardo está anclado al **instante de pérdida** (relativo), no a una grilla global.
- **Dependencia del instante del corte.** Spearman entre r y el instante de inicio: |rho| <= 0,14 en cinco condiciones y -0,445 (p < 0,001) en la desconexión uniforme de 3 s, donde el 11,6 % de los cortes dura 3,56 s en vez de 3,52 s. La diferencia es de un bloque y no se pudo explicar con estos datos.

### 1.4 Qué dice liblsl (fuentes primarias, rama `master`)

Leído con WebFetch el 2026-10-07. **No es la versión que empaqueta mne-lsl** (no hay `mne_lsl` en el venv local, no se pudo consultar `library_version()`); verificar antes de afirmarlo en el manuscrito.

| Elemento | Qué hace | Fuente |
|---|---|---|
| `data_receiver::data_thread` | Tras cualquier error de conexión llama a `try_recover_from_error()` y **después duerme 500 ms** (comentario en el código: evitar "spam" de reconexiones al proveedor) antes de reintentar la conexión. | https://raw.githubusercontent.com/sccn/liblsl/master/src/data_receiver.cpp (`std::this_thread::sleep_for(std::chrono::milliseconds(500))`) |
| `inlet_connection::try_recover` | Consulta por `name`, `type`, `source_id`, `channel_count` y `channel_format`; llama `resolver_.resolve_oneshot(query.str(), 1, FOREVER, attempt == 0 ? 1.0 : 5.0)`: el primer intento **no puede terminar antes de 1,0 s** (`minimum_time`), los siguientes esperan 5,0 s. | https://raw.githubusercontent.com/sccn/liblsl/master/src/inlet_connection.cpp |
| `resolver_impl::resolve_oneshot` / `next_resolve_wave` | Fija `wait_until_ = lsl_clock() + minimum_time` y emite ondas de consulta cada `multicast_min_rtt` (0,5 s en modo rápido); termina cuando hay >= `minimum_` resultados y `lsl_clock() >= wait_until_`. | https://raw.githubusercontent.com/sccn/liblsl/master/src/resolver_impl.cpp |
| `resolve_attempt_udp::handle_receive_outcome` | Comprueba el criterio de cancelación **cada vez que llega una respuesta**: la resolución termina en cuanto el outlet recreado responde (si ya pasó el mínimo). | https://raw.githubusercontent.com/sccn/liblsl/master/src/resolve_attempt_udp.cpp |
| `lsl_api.cfg`, sección `[tuning]` | Valores por defecto: `MulticastMinRTT = 0.5`, `MulticastMaxRTT = 3.0`, `UnicastMinRTT = 0.75`, `ContinuousResolveInterval = 0.5`, `WatchdogCheckInterval = 15.0`, `WatchdogTimeThreshold = 15.0`. La página remite a `api_config.h` para las descripciones. | https://labstreaminglayer.readthedocs.io/info/lslapicfg.html y https://github.com/sccn/liblsl/blob/master/src/api_config.h (líneas 138-161) |
| Bandera `recover` | Solo recuperables los flujos con `source_id`; `replay.py` lo fija (`source_id = "<exec_id>-eeg"`), por eso el inlet se reconecta. | https://raw.githubusercontent.com/sccn/liblsl/master/include/lsl/inlet.h (doc de `lsl_create_inlet`) |

**Lo que no explica.** El watchdog (15 s) queda descartado: el hueco es de 1,5 s. `ContinuousResolveInterval` no interviene (el resolve de recuperación es en modo rápido).

### 1.5 Descarte del receptor propio y del emisor

- `consumer.py`: el bucle principal usa `pull_chunk(timeout=0.0)` (no bloquea) y `time.sleep(0.005)`; el inlet se crea con `recover=True`; **no hay lógica de reconexión, de espera ni de reintento**. El único temporizador que toca la espera es `TRIAL_TIMEOUT_S = 3.0` (decide cuándo decodificar con lo que haya), que no afecta al hueco de datos medido. Las excepciones del bucle se cuentan (`exceptions`) y valen 0 en las 855 ejecuciones `[D\analysis\execs.csv]`.
- `replay.py`: el outlet se destruye al primer bloque dentro del corte (`del outlet; gc.collect()`) y se recrea, con el mismo `StreamInfo`, en el primer bloque posterior (`outage_end`); reanuda el envío en ese mismo bloque. El instante de recreación es el planificado a menos de un bloque.

### 1.6 Mecanismo propuesto y conclusión

> **Actualización 07/10 (verificado en el código).** El modelo escalonado (M2) queda confirmado por la campaña exploratoria ([[Analisis-M3-campana-exploratoria]] §1) y su mecanismo se verificó en la fuente de **liblsl v1.17.7**, la versión que empaqueta mne-lsl 1.14 (`lsl_library_info()` = `git:v1.17.7`, en la notebook y en la VM); las líneas clave son idénticas en `master`. Tres piezas: (a) espera mínima de **1,0 s** del primer intento (`inlet_connection.cpp`, `attempt == 0 ? 1.0 : 5.0`, fija); (b) ondas de consulta cada `multicast_min_rtt` (`resolver_impl.cpp`, modo rápido; `MulticastMinRTT = 0.5` por defecto, **configurable** en `lsl_api.cfg` o con la variable `LSLAPICFG`): **es la grilla de 0,5 s**; (c) `sleep_for(500 ms)` después de recuperar y antes de reconectar (`data_receiver.cpp`, fijo): **es el +0,5 constante**. Prueba experimental en curso (07/10): `MulticastMinRTT = 0.25` debería bajar el hueco de d = 1,25 s de 2,02 a 1,77 s y dejar igual el de 0,5 s.

**Cadena de eventos (inferida del código, no medida en el banco).** Se destruye el outlet en t = 0 -> el hilo de datos del inlet recibe el error -> `try_recover` lanza una resolución con espera mínima de 1,0 s -> si el outlet ya volvió responde a la primera onda posterior a su recreación (ondas cada 0,5 s) -> el hilo **duerme 500 ms** -> reconecta (~20 ms) y llega el primer bloque. De ahí:

- hueco ≈ max(1,0 s; instante de visibilidad del outlet) + 0,5 s + 0,02 s.
- Para d <= 1,0 s: 1,0 + 0,5 + 0,02 = **1,52 s** (el piso). Para d = 2 y 3 s: d + 0,5 + 0,02 = 2,52 y 3,52 s. Todo coincide con lo observado (error <= 40 ms).
- Entonces r = 0,52 s ya no es "espera de una onda de búsqueda", sino el sleep fijo de 500 ms más la reconexión; y el piso es 1,0 + 0,5 s.

**Qué queda sin discriminar con estos datos.** Todas las d observadas son múltiplos de 0,5 s (salvo 0,48/0,52). Dos formas funcionales son compatibles:

- **M1 (continua):** hueco = max(1,52; d + 0,52).
- **M2 (ondas de 0,5 s):** hueco = 0,5 + max(1,0; 0,5·ceil(d/0,5)) + 0,02; es decir, el outlet es visible recién en la próxima onda de consulta.

Predicciones distintas solo para d no múltiplo de 0,5 s (predicciones propias, **no probadas**):

| d (s) | 0,1 | 0,25 | 0,75 | 1,25 | 1,75 | 2,25 |
|---|---|---|---|---|---|---|
| M1 (s) | 1,52 | 1,52 | 1,52 | 1,77 | 2,27 | 2,77 |
| M2 (s) | 1,52 | 1,52 | 1,52 | 2,02 | 2,52 | 3,02 |

**Conclusión: atribuible a LSL (mecanismo de recuperación del inlet en liblsl), con confianza alta pero no demostrada experimentalmente.** A favor: (a) dos constantes del código (1,0 s y 500 ms) suman exactamente el piso observado; (b) `consumer.py` y `replay.py` no imponen ninguna espera; (c) el valor es idéntico entre sujetos, corridas e instantes. En contra o pendiente: (i) versión de liblsl del banco no verificada; (ii) forma funcional entre M1 y M2 no discriminada; (iii) no se midió el instante de pérdida detectada por el inlet.

**Prueba de diagnóstico recomendada (NO ejecutada).** Opcional, solo si el manuscrito quiere afirmar la forma funcional; para el argumento principal (el piso es de LSL y no una propiedad del decodificador) alcanza con citar el código. Diseño: VM con el mismo entorno; script mínimo con liblsl (emisor que destruye y recrea el outlet con `source_id` fijo; receptor con `recover=True` que registra marcas de llegada, sin decodificador ni EEG); d en {0,1; 0,25; 0,5; 0,75; 1,0; 1,25; 1,5; 1,75; 2,0; 2,25}, 20 cortes por valor con inicios aleatorios, ~30 min; registrar `library_version()`. Comparar con M1 y M2 y repetir un brazo con el emisor y receptor del banco para confirmar que no agregan nada.

---

## 2. Exposición de la ventana de decodificación

### 2.1 Método

Por ensayo decodificado (24 por corrida) `n_samples` de `trials.csv` = muestras recibidas en [onset + 2 s, onset + 6 s] (1000 si íntegra; 0 si el ensayo fue inválido por <125 muestras). "Tocada" = `n_samples < 1000`; "mayoritaria" = `n_samples < 500`. Proporción por ejecución sobre 24; **mediana entre sujetos** = mediana de las 9 medianas por sujeto (sobre sus 5 corridas); **global** = proporción agrupada sobre los 1.080 ensayos de la condición. `[B\scripts\m3_exposicion.py -> D\analysis-m3\m3_exposicion_exec.csv, m3_exposicion_cond.csv]`. El `n_samples` es el mismo para ambos decodificadores (la ventana recibida es la misma); se leyó `trials.csv` y se comprobó que `trials_eegnet.csv` tiene los mismos 24 ensayos y onsets.

### 2.2 Resultados por condición

`[m3_exposicion.py -> m3_exposicion_cond.csv]`

| Condición | < 1000, mediana entre sujetos (%) | < 1000, global (%) | < 500, mediana entre sujetos (%) | < 500, global (%) | Inválidos, global (%) | Fracción de ventana perdida (media, %) |
|---|---|---|---|---|---|---|
| ref | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| loss-random-0.01 | 100.0 | 100.0 | 0.0 | 0.0 | 0.0 | 1.0 |
| loss-random-0.05 | 100.0 | 100.0 | 0.0 | 0.0 | 0.0 | 5.0 |
| loss-random-0.1 | 100.0 | 100.0 | 0.0 | 0.0 | 0.0 | 10.0 |
| jitter-0.01 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| jitter-0.05 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| jitter-0.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| delay-0.05 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| delay-0.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| delay-0.25 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| disconnect-0.5 | 8.3 | 6.9 | 0.0 | 0.0 | 0.0 | 1.9 |
| disconnect-1 | 8.3 | 6.2 | 0.0 | 0.0 | 0.0 | 1.8 |
| disconnect-3 | 8.3 | 8.7 | 4.2 | 4.2 | 0.8 | 4.2 |
| burst_trial-0.1 | 100.0 | 100.0 | 0.0 | 0.0 | 0.0 | 10.0 |
| burst_trial-0.25 | 100.0 | 100.0 | 0.0 | 0.0 | 0.0 | 25.0 |
| burst_trial-0.4 | 100.0 | 100.0 | 0.0 | 0.0 | 0.0 | 40.0 |
| disconnect_trial-0.5 | 100.0 | 100.0 | 0.0 | 0.0 | 0.0 | 38.0 |
| disconnect_trial-1 | 100.0 | 100.0 | 0.0 | 0.0 | 0.0 | 38.0 |
| disconnect_trial-2 | 100.0 | 100.0 | 100.0 | 100.0 | 0.0 | 63.0 |

Lectura:

- **Jitter y retraso no tocan la ventana** (0 %): las marcas de tiempo son nominales y el consumidor espera a tener el segmento; el contenido decodificado es idéntico al de la referencia.
- **Pérdida aleatoria toca el 100 % de las ventanas por construcción** (con p >= 1 % siempre cae alguna muestra): el umbral `< 1000` no discrimina y la medida útil es la fracción perdida (1, 5, 10 %).
- **Desconexión uniforme**: 6-9 % de los ensayos, mediana entre sujetos de 2 de 24 ensayos (8,3 %) en las tres severidades. Solo 3 s deja ventanas con menos de la mitad (4,2 %, 45 de 1.080) y 9 ensayos inválidos (0,8 %; <125 muestras).
- **Condiciones por ensayo**: 100 % de ventanas tocadas por diseño; 620 muestras (38 % perdido) para 0,5 y 1 s, 370 (63 %) para 2 s. Estas dos condiciones de 0,5 y 1 s son **idénticas en pérdida** porque el hueco es 1,52 s en ambas (tarea 1): la severidad nominal no es la efectiva.

### 2.3 Modelo E ≈ N·(d + r + w)/T para la desconexión uniforme

N = `outages` de cada corrida (5), w = 4 s, T = `secs_total` = 387 s, d + r = hueco de la tarea 1. `[m3_exposicion.py -> m3_exposicion_cond.csv, columnas E_r0, E_modelo, E_guarda_mean, obs_mean_exec, obs_se_exec]`

| Condición | d (s) | r (tarea 1, s) | Observado: media entre ejecuciones (%) | EE (%) | E con r = 0 (%) | E = N(d+r+w)/T (%) | E con zona de guarda (%) |
|---|---|---|---|---|---|---|---|
| disconnect-0.5 | 0.5 | 1.02 | 6.9 | 0.7 | 5.8 | 7.1 | 7.0 |
| disconnect-1 | 1.0 | 0.52 | 6.2 | 0.7 | 6.5 | 7.1 | 6.9 |
| disconnect-3 | 3.0 | 0.52 | 8.7 | 0.7 | 9.0 | 9.7 | 9.6 |

- "E con zona de guarda" es un refinamiento propio: misma esperanza, pero con los cortes confinados a [15 s, T - 15 s - d] (regla del inyector, `injector.py`, `GUARD_S`) y con los inicios de ventana reales de cada corrida.
- El modelo con r (versión con guarda) **acierta**: observado menos modelo = 0,0, -1,1 y -1,3 errores estándar (6,9 vs 7,0; 6,2 vs 6,9; 8,7 vs 9,6). **No se puede decir que r mejore al modelo con r = 0**: éste subestima a 0,5 s (observado menos modelo = +1,6 EE) y queda a -0,4 y -0,5 EE para 1 y 3 s. Con 45 ejecuciones por condición y EE de 0,7 puntos, las dos versiones no se distinguen; el aporte de r es de 0,7 a 1,3 puntos porcentuales.
- Para `disconnect_trial` el modelo E no aplica (el corte está anclado al inicio de la ventana): la exposición es 100 % y lo que cambia es cuánta ventana queda (620 / 620 / 370 muestras).

### 2.4 Exposición y caída de BA por condición, CSP+LDA y EEGNet

`ΔBA` = diferencia por sujeto (medianas de 5 corridas) condición - referencia, **promedio** y **mediana** entre los 9 sujetos; p de Holm de `t_desempeno.csv` (Wilcoxon apareado, corrección de Holm dentro de cada tipo). `[m3_exposicion.py -> m3_exposicion_cond.csv; p_holm de D\analysis\t_desempeno.csv y D\analysis-eegnet\t_desempeno.csv]`. BA de referencia (mediana entre sujetos): CSP+LDA 0,708, EEGNet 0,750 (`t_desempeno.csv`, `median_ref`).

| Condición | Ventana tocada (%) | Fracción perdida (%) | ΔBA CSP+LDA (media) | ΔBA CSP+LDA (mediana) | p Holm CSP+LDA | ΔBA EEGNet (media) | ΔBA EEGNet (mediana) | p Holm EEGNet |
|---|---|---|---|---|---|---|---|---|
| loss-random-0.01 | 100.0 | 1.0 | -0.014 | 0.000 | 0.750 | -0.009 | 0.000 | 1.000 |
| loss-random-0.05 | 100.0 | 5.0 | -0.014 | 0.000 | 1.000 | -0.009 | 0.000 | 1.000 |
| loss-random-0.1 | 100.0 | 10.0 | -0.014 | 0.000 | 1.000 | -0.005 | 0.000 | 1.000 |
| jitter (3 severidades) | 0.0 | 0.0 | 0.000 | 0.000 | 1.000 | 0.000 | 0.000 | 1.000 |
| delay (3 severidades) | 0.0 | 0.0 | 0.000 | 0.000 | 1.000 | 0.000 | 0.000 | 1.000 |
| disconnect-0.5 | 6.9 | 1.9 | -0.009 | 0.000 | 1.000 | -0.009 | 0.000 | 1.000 |
| disconnect-1 | 6.2 | 1.8 | 0.000 | 0.000 | 1.000 | -0.005 | 0.000 | 1.000 |
| disconnect-3 | 8.7 | 4.2 | -0.017 | 0.000 | 0.375 | -0.001 | 0.000 | 1.000 |
| burst_trial-0.1 | 100.0 | 10.0 | -0.014 | 0.000 | 0.375 | -0.014 | 0.000 | 0.594 |
| burst_trial-0.25 | 100.0 | 25.0 | -0.032 | -0.042 | 0.250 | -0.037 | -0.042 | 0.594 |
| burst_trial-0.4 | 100.0 | 40.0 | -0.065 | -0.042 | 0.012 | -0.079 | -0.083 | 0.023 |
| disconnect_trial-0.5 | 100.0 | 38.0 | -0.051 | -0.042 | 0.062 | -0.130 | -0.125 | 0.012 |
| disconnect_trial-1 | 100.0 | 38.0 | -0.051 | -0.042 | 0.062 | -0.130 | -0.125 | 0.012 |
| disconnect_trial-2 | 100.0 | 63.0 | -0.097 | -0.083 | 0.012 | -0.222 | -0.208 | 0.012 |

(Jitter y retraso se agrupan: las tres severidades dan exactamente 0 en ambos decodificadores y en las 9 diferencias.)

**Asociación entre condiciones** (n = 18, sin la referencia; condiciones de una misma familia no son independientes, la correlación es descriptiva). `[m3_exposicion.py -> m3_exposicion_vs_caida.csv]`

| Decodificador | Variable de exposición | Spearman | p | Pendiente por el origen (ΔBA por unidad de fracción) |
|---|---|---|---|---|
| CSP+LDA | proporción de ventanas tocadas (mediana entre sujetos) | -0.856 | <0.001 | -0.039 |
| CSP+LDA | proporción de ventanas < 500 (global) | -0.431 | 0.074 | -0.098 |
| CSP+LDA | fracción de ventana perdida (media global) | **-0.942** | <0.001 | -0.148 |
| EEGNet | proporción de ventanas tocadas (mediana entre sujetos) | -0.905 | <0.001 | -0.071 |
| EEGNet | proporción de ventanas < 500 (global) | -0.229 | 0.360 | -0.222 |
| EEGNet | fracción de ventana perdida (media global) | **-0.931** | <0.001 | -0.302 |

Restringido a las 7 condiciones con pérdida >5 % (pérdida 10 %, ráfagas, desconexión en el ensayo): Spearman -0,991 (CSP+LDA) y -0,847 (EEGNet, p = 0,016). **Lectura.**

- **La dosis es la fracción de la ventana perdida**, no si se la tocó: 100 % de ventanas tocadas con 1 % de pérdida y con 40 % dan caídas de -0,01 y -0,07.
- La pendiente por el origen sugiere unos **-1,5 puntos de BA por cada 10 % de ventana perdida en CSP+LDA y -3,0 en EEGNet**, pero es un resumen de 18 puntos heterogéneos: con el mismo 10 % de pérdida, la distribuida al azar cuesta -0,014 (CSP+LDA) y -0,005 (EEGNet) y la ráfaga contigua -0,014 y -0,014.
- **Anomalía a investigar.** A igual pérdida (38-40 %), la desconexión en el ensayo cuesta -0,130 en EEGNet y la ráfaga contigua -0,079; en CSP+LDA ocurre lo contrario (-0,051 frente a -0,065). Las dos condiciones difieren en dónde cae el hueco (inicio de la ventana frente a posición aleatoria) y en que la desconexión es real (outlet cerrado). No se probó la causa.

**Por qué la desconexión uniforme casi no mueve la BA (cota de peor caso).** Con exposición E y exactitud condicional entre la de referencia y el azar (0,5), la caída máxima es E·(a_ref - 0,5). Con a_ref = 0,759 (CSP+LDA, `trials.csv`, 1.080 ensayos de referencia) y 0,774 (EEGNet, `trials_eegnet.csv`) y E global observado de 6,9 / 6,2 / 8,7 %:

| | 0,5 s | 1 s | 3 s |
|---|---|---|---|
| Cota CSP+LDA (puntos) | 1,8 | 1,6 | 2,3 |
| Cota EEGNet (puntos) | 1,9 | 1,7 | 2,4 |

**Estas cotas son aritmética propia, sobre datos agrupados (no por sujeto), y suponen que los ensayos tocados no caen por debajo del azar.** Todas las caídas observadas en desconexión uniforme (<= 1,7 puntos en media) están por debajo. La exactitud por ensayo tocado vs. no tocado `[m3_exposicion.py -> m3_condicional.csv]`:

| Condición | Decodificador | Tocados (n) | Exactitud tocados | IC95 Wilson | No tocados (n) | Exactitud no tocados | IC95 Wilson |
|---|---|---|---|---|---|---|---|
| disconnect-0.5 | CSP+LDA | 75 | 0.773 | [0.67; 0.85] | 1005 | 0.756 | [0.73; 0.78] |
| disconnect-1 | CSP+LDA | 67 | 0.821 | [0.71; 0.89] | 1013 | 0.754 | [0.73; 0.78] |
| disconnect-3 | CSP+LDA | 85 | 0.718 | [0.61; 0.80] | 986 | 0.757 | [0.73; 0.78] |
| disconnect-0.5 | EEGNet | 75 | 0.653 | [0.54; 0.75] | 1005 | 0.779 | [0.75; 0.80] |
| disconnect-1 | EEGNet | 67 | 0.746 | [0.63; 0.84] | 1013 | 0.770 | [0.74; 0.79] |
| disconnect-3 | EEGNet | 85 | 0.694 | [0.59; 0.78] | 986 | 0.775 | [0.75; 0.80] |

Con 67-85 ensayos tocados por condición los IC son anchos (±10 puntos): CSP+LDA no muestra pérdida de exactitud en los ensayos tocados; EEGNet sí tiende a ser menor (0,65-0,75 frente a 0,77-0,78) pero el IC de 1 s incluye el valor sin tocar. Agrupar ensayos de sujetos y corridas distintos ignora la correlación intra-sujeto; es indicativo, no inferencial.

---

## 3. IC del 95 % de la diferencia apareada (condición - referencia) en BA

### 3.1 Método

Unidad = sujeto (n = 9), mediana de las 5 corridas: `D\analysis\medianas_por_sujeto.csv` (CSP+LDA en línea) y `D\analysis-eegnet\medianas_por_sujeto.csv` (EEGNet). `[B\scripts\m3_ic.py -> D\analysis-m3\m3_ic.csv]`

- **Estimador:** Hodges-Lehmann (HL), mediana de los 45 promedios de Walsh de las 9 diferencias.
- **IC principal (exacto):** intervalo de Wilcoxon de rangos con signo, a partir de los promedios de Walsh ordenados, [W(k+1), W(45-k)] con k = 5, el mayor entero con P(T+ <= k) <= 0,025 bajo H0 (distribución exacta por programación dinámica sobre los 2^9 signos). **Por la discreción de la distribución con n = 9 el nivel real es 96,09 %, no 95 %**: es ligeramente conservador. Los empates y ceros no invalidan el intervalo, que sigue siendo válido bajo simetría.
- **Contraste:** bootstrap por sujetos (remuestreo de las 9 diferencias, 10.000 réplicas, `numpy.random.default_rng(20261007)`), percentiles 2,5 y 97,5 de HL.
- **Criterio de equivalencia:** el IC exacto contenido en [-0,03; +0,03].

### 3.2 CSP+LDA

`[m3_ic.py -> m3_ic.csv]`; "−/0/+" = sujetos con diferencia negativa/nula/positiva.

| Condición | Diferencia media | HL | IC95 exacto (Wilcoxon) | IC95 bootstrap (HL) | −/0/+ | IC exacto dentro de ±0,03 | IC boot dentro de ±0,03 |
|---|---|---|---|---|---|---|---|
| loss-random-0.01 | -0.0139 | -0.0208 | [-0.0417; 0.0000] | [-0.0208; 0.0000] | 3/6/0 | NO | sí |
| loss-random-0.05 | -0.0139 | 0.0000 | [-0.0625; +0.0208] | [-0.0625; 0.0000] | 2/5/2 | NO | NO |
| loss-random-0.1 | -0.0139 | 0.0000 | [-0.0625; +0.0417] | [-0.0625; +0.0208] | 3/3/3 | NO | NO |
| jitter-0.01 | 0.0000 | 0.0000 | [0.0000; 0.0000] | [0.0000; 0.0000] | 0/9/0 | sí | sí |
| jitter-0.05 | 0.0000 | 0.0000 | [0.0000; 0.0000] | [0.0000; 0.0000] | 0/9/0 | sí | sí |
| jitter-0.1 | 0.0000 | 0.0000 | [0.0000; 0.0000] | [0.0000; 0.0000] | 0/9/0 | sí | sí |
| delay-0.05 | 0.0000 | 0.0000 | [0.0000; 0.0000] | [0.0000; 0.0000] | 0/9/0 | sí | sí |
| delay-0.1 | 0.0000 | 0.0000 | [0.0000; 0.0000] | [0.0000; 0.0000] | 0/9/0 | sí | sí |
| delay-0.25 | 0.0000 | 0.0000 | [0.0000; 0.0000] | [0.0000; 0.0000] | 0/9/0 | sí | sí |
| disconnect-0.5 | -0.0093 | 0.0000 | [-0.0208; 0.0000] | [-0.0208; 0.0000] | 2/7/0 | sí | sí |
| disconnect-1 | 0.0000 | 0.0000 | [-0.0208; +0.0208] | [-0.0208; +0.0208] | 1/7/1 | sí | sí |
| disconnect-3 | -0.0167 | -0.0208 | [-0.0417; 0.0000] | [-0.0333; 0.0000] | 4/5/0 | NO | NO |
| burst_trial-0.1 | -0.0139 | -0.0208 | [-0.0417; 0.0000] | [-0.0417; 0.0000] | 4/4/1 | NO | NO |
| burst_trial-0.25 | -0.0324 | -0.0208 | [-0.0833; 0.0000] | [-0.0625; 0.0000] | 5/3/1 | NO | NO |
| burst_trial-0.4 | -0.0648 | -0.0625 | [-0.0833; -0.0417] | [-0.0833; -0.0417] | 9/0/0 | NO | NO |
| disconnect_trial-0.5 | -0.0509 | -0.0417 | [-0.0833; 0.0000] | [-0.0833; -0.0208] | 7/1/1 | NO | NO |
| disconnect_trial-1 | -0.0509 | -0.0417 | [-0.0833; 0.0000] | [-0.0833; -0.0208] | 7/1/1 | NO | NO |
| disconnect_trial-2 | -0.0972 | -0.0833 | [-0.1458; -0.0417] | [-0.1250; -0.0417] | 9/0/0 | NO | NO |

### 3.3 EEGNet

| Condición | Diferencia media | HL | IC95 exacto (Wilcoxon) | IC95 bootstrap (HL) | −/0/+ | IC exacto dentro de ±0,03 | IC boot dentro de ±0,03 |
|---|---|---|---|---|---|---|---|
| loss-random-0.01 | -0.0093 | 0.0000 | [-0.0208; 0.0000] | [-0.0208; 0.0000] | 2/7/0 | sí | sí |
| loss-random-0.05 | -0.0093 | 0.0000 | [-0.0417; +0.0208] | [-0.0208; 0.0000] | 3/5/1 | NO | sí |
| loss-random-0.1 | -0.0046 | 0.0000 | [-0.0208; 0.0000] | [-0.0208; 0.0000] | 1/7/1 | sí | sí |
| jitter-0.01 | 0.0000 | 0.0000 | [0.0000; 0.0000] | [0.0000; 0.0000] | 0/9/0 | sí | sí |
| jitter-0.05 | 0.0000 | 0.0000 | [0.0000; 0.0000] | [0.0000; 0.0000] | 0/9/0 | sí | sí |
| jitter-0.1 | 0.0000 | 0.0000 | [0.0000; 0.0000] | [0.0000; 0.0000] | 0/9/0 | sí | sí |
| delay-0.05 | 0.0000 | 0.0000 | [0.0000; 0.0000] | [0.0000; 0.0000] | 0/9/0 | sí | sí |
| delay-0.1 | 0.0000 | 0.0000 | [0.0000; 0.0000] | [0.0000; 0.0000] | 0/9/0 | sí | sí |
| delay-0.25 | 0.0000 | 0.0000 | [0.0000; 0.0000] | [0.0000; 0.0000] | 0/9/0 | sí | sí |
| disconnect-0.5 | -0.0093 | 0.0000 | [-0.0208; 0.0000] | [-0.0208; 0.0000] | 2/6/1 | sí | sí |
| disconnect-1 | -0.0046 | 0.0000 | [-0.0208; 0.0000] | [-0.0208; 0.0000] | 1/8/0 | sí | sí |
| disconnect-3 | -0.0013 | 0.0000 | [-0.0038; 0.0000] | [-0.0038; 0.0000] | 2/7/0 | sí | sí |
| burst_trial-0.1 | -0.0139 | -0.0208 | [-0.0417; 0.0000] | [-0.0417; 0.0000] | 4/3/2 | NO | NO |
| burst_trial-0.25 | -0.0370 | -0.0417 | [-0.1042; 0.0000] | [-0.0833; 0.0000] | 6/1/2 | NO | NO |
| burst_trial-0.4 | -0.0787 | -0.0833 | [-0.1250; -0.0417] | [-0.1250; -0.0417] | 8/0/1 | NO | NO |
| disconnect_trial-0.5 | -0.1296 | -0.1250 | [-0.2083; -0.0625] | [-0.1875; -0.0833] | 9/0/0 | NO | NO |
| disconnect_trial-1 | -0.1296 | -0.1250 | [-0.2083; -0.0625] | [-0.1875; -0.0833] | 9/0/0 | NO | NO |
| disconnect_trial-2 | -0.2222 | -0.2083 | [-0.3750; -0.1250] | [-0.3542; -0.1250] | 9/0/0 | NO | NO |

### 3.4 Resumen y límites

| | IC exacto dentro de ±0,03 | IC exacto fuera de ±0,03 |
|---|---|---|
| **CSP+LDA** (8 de 18) | jitter 0,01/0,05/0,1; retraso 0,05/0,1/0,25; desconexión 0,5 y 1 s | pérdida 1/5/10 %; desconexión 3 s; ráfaga 10/25/40 %; desconexión en el ensayo 0,5/1/2 s |
| **EEGNet** (11 de 18) | pérdida 1 y 10 %; jitter x3; retraso x3; desconexión 0,5/1/3 s | pérdida 5 %; ráfaga x3; desconexión en el ensayo x3 |

- **IC que excluyen el cero (exacto):** CSP+LDA, ráfaga 40 % y desconexión en el ensayo de 2 s; EEGNet, ráfaga 40 % y desconexión en el ensayo (las tres). En CSP+LDA la desconexión en el ensayo de 0,5 y 1 s tiene el extremo superior en 0,0000 (el bootstrap sí excluye el cero: [-0,083; -0,021]); es un caso límite, coherente con su p de Holm de 0,062.
- **Resolución.** La BA por sujeto (mediana de 5 corridas de 24 ensayos) avanza de a 1/24 = 0,0417 (casi todos los valores de `medianas_por_sujeto.csv` son múltiplos de 1/24; unos pocos intermedios provienen de ejecuciones con ensayos inválidos). Los promedios de Walsh avanzan de a 1/48 = 0,0208. **El margen ±0,03 cae entre 1 y 2 de esos escalones**: un IC con extremo en -0,0417 queda "fuera" por un solo paso discreto. Por eso el criterio ±0,03 es más una convención que una frontera con significado; con 24 ensayos por corrida no se puede resolver una diferencia de 0,03. Ejemplo: CSP+LDA con desconexión de 3 s tiene diferencia media de -0,017 (por debajo de la cota de dilución de 2,3 puntos de la sección 2.4) y aun así su IC exacto [-0,042; 0] queda "fuera" por un escalón.
- **IC degenerados.** Los "sí" de jitter y retraso son [0; 0] porque las 9 diferencias son exactamente 0: el contenido recibido es idéntico a la referencia y las decisiones también (los ensayos tocados son 0 %, sección 2.2). No es una estimación precisa de un efecto pequeño sino la ausencia de efecto por construcción de ese fallo.
- **Bootstrap con n = 9 y muchos ceros subestima el ancho** (p. ej. CSP+LDA pérdida 1 %: bootstrap "sí", exacto "NO"; EEGNet pérdida 5 %: igual). Se informa como análisis de sensibilidad; **se debe priorizar el IC exacto**.
- **Nivel real 96,1 %, no 95 %.** Con n = 9 no existe un intervalo exacto de nivel 95 %.
- **Múltiples comparaciones.** 36 intervalos sin ajuste por multiplicidad (el ajuste de Holm de `t_desempeno.csv` es para los p, no para estos IC); no se deben leer como una familia con 95 % conjunto.
- La referencia de CSP+LDA es la decisión en línea; la de EEGNet es la re-decodificación fuera de línea de los segmentos guardados (`trials_eegnet.csv`): las dos comparan condición con referencia dentro del mismo decodificador, no entre decodificadores.

---

## 4. Fuentes

Verificación realizada el 2026-10-07. El DOI resuelve a nature.com, pero la página del editor no se pudo leer con la herramienta (redirección a un portal de cookies/identidad que no entrega el contenido). Los metadatos se verificaron con **Crossref** (registro del DOI) y **Europe PMC** (PMID), que coinciden entre sí. Nada proviene de memoria.

### 4.1 Gallego et al. (2020)

> Gallego, J. A., Perich, M. G., Chowdhury, R. H., Solla, S. A., y Miller, L. E. (2020). Long-term stability of cortical population dynamics underlying consistent behavior. *Nature Neuroscience, 23*(2), 260-270. https://doi.org/10.1038/s41593-019-0555-4

- Metadatos verificados: 5 autores, volumen 23, número 2, páginas 260-270, 2020, PMID 31907438. Coinciden con la cita solicitada (el número 2 no estaba en la solicitud y se agregó).
- Qué muestra: registran poblaciones neuronales de corteza premotora, motora primaria y somatosensorial de monos durante una tarea de alcance, hasta 2 años. Las neuronas registradas cambian de forma sostenida (recambio), pero la dinámica latente de baja dimensión se mantiene estable. Con esa estabilidad se puede decodificar la conducta durante todo el período, mientras que los decodificadores fijos basados directamente en la actividad registrada se degradan de forma sustancial.
- **Uso correcto para el TFG:** respalda que la señal *registrada* cambia entre días (no estacionariedad del registro) y que un decodificador fijo se degrada sin que falle el sistema. **Matiz:** su tesis es que la dinámica latente es estable; la inestabilidad está en lo que el registro captura, no en la actividad cortical subyacente.

### 4.2 Karpowicz et al. (2025)

> Karpowicz, B. M., Ali, Y. H., Wimalasena, L. N., Sedler, A. R., Keshtkaran, M. R., Bodkin, K., Ma, X., Rubin, D. B., Williams, Z. M., Cash, S. S., Hochberg, L. R., Miller, L. E., y Pandarinath, C. (2025). Stabilizing brain-computer interfaces through alignment of latent dynamics. *Nature Communications, 16*(1), Artículo 4662. https://doi.org/10.1038/s41467-025-59652-y

- **Discrepancia con la cita pedida: el número de artículo es 4662, no 4283.** Coinciden Crossref y Europe PMC (PMID 40389429). El título, la revista, el volumen y el año coinciden con lo pedido. Conviene corregirlo en la bibliografía del manuscrito. Además la cita pedida decía "et al."; APA 7 enumera hasta 20 autores y este artículo tiene 13, por lo que se listan todos.
- Qué muestra: en las interfaces cerebro-computadora intracorticales actuales, las inestabilidades en la interfaz neural degradan el desempeño del decodificador y obligan a recalibrar con frecuencia con datos etiquetados. Presentan NoMAD, que alinea sin supervisión los datos neuronales no estacionarios a una dinámica latente consistente (con modelos recurrentes), de modo que el decodificador reciba una entrada estable. Con datos de corteza motora de monos logran decodificación precisa y estable durante semanas a meses sin recalibración supervisada.
- **Uso correcto para el TFG:** respalda "no estacionariedad de la señal entre sesiones degrada decodificadores fijos sin falla del sistema" y que se mitiga por alineación sin recalibración.

### 4.3 Límite de ambas citas

Los dos trabajos son sobre registros **intracorticales invasivos en primates**, no sobre EEG de superficie. Sirven como evidencia de que la no estacionariedad del registro y la degradación de decodificadores fijos son fenómenos documentados en BCI; **no sirven, por sí solos, para afirmar su magnitud en EEG de superficie ni en el dataset del banco** (el dato del banco es de una sola sesión de prueba reproducida). Si el manuscrito necesita ese punto para EEG, hace falta una fuente EEG verificada (`bci-explorer`); no se agregó ninguna aquí.

---

## 5. Trazabilidad

| Cifra | Script | Archivo de origen |
|---|---|---|
| Hueco, espera r, modelo max(c0, d+c1), grilla | `B\scripts\m3_reconexion.py` | `D\raw\<exec>\fault_log.jsonl`, `D\raw\<exec>\telemetry.csv`, `D\analysis\execs.csv` -> `D\analysis-m3\m3_cortes.csv`, `m3_espera_resumen.csv`, `m3_grilla.csv` |
| Exposición, modelo E, ΔBA, cota, exactitud tocado/no tocado | `B\scripts\m3_exposicion.py` | `D\raw\<exec>\trials.csv`, `trials_eegnet.csv`, `D\analysis\medianas_por_sujeto.csv`, `D\analysis-eegnet\medianas_por_sujeto.csv`, `t_desempeno.csv` -> `D\analysis-m3\m3_exposicion_exec.csv`, `m3_exposicion_cond.csv`, `m3_exposicion_vs_caida.csv`, `m3_condicional.csv` |
| IC (HL, exacto, bootstrap) | `B\scripts\m3_ic.py` | `D\analysis\medianas_por_sujeto.csv`, `D\analysis-eegnet\medianas_por_sujeto.csv` -> `D\analysis-m3\m3_ic.csv` |
| Tablas Markdown de esta nota | `B\scripts\m3_tablas.py` | CSV de `D\analysis-m3\` -> `D\analysis-m3\m3_tablas.md` |
| Código de liblsl, `lsl_api.cfg` | (WebFetch, 2026-10-07) | URLs de la sección 1.4 |
| Citas | (WebFetch, 2026-10-07) | Crossref `api.crossref.org/works/<doi>` y Europe PMC `ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:<doi>` |

**Reproducción:** `C:\Users\agustin.tamagusuku\.venvs\bcibench\Scripts\python B\scripts\m3_reconexion.py`, luego `m3_exposicion.py` (necesita `m3_cortes.csv`), `m3_ic.py` y `m3_tablas.py`. Semilla del bootstrap: 20261007.

**Pendiente de decisión del autor:** (1) ejecutar o no el diagnóstico de la sección 1.6; (2) corregir el número de artículo de Karpowicz en la bibliografía; (3) si el manuscrito conserva el margen ±0,03 sabiendo que es menor que el paso mínimo de la BA por sujeto; (4) verificar la versión de liblsl empaquetada por mne-lsl.
