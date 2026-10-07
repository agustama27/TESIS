# Línea 2 · Trazas reales: reemplazar las fallas sintéticas por comportamiento medido de enlaces

> Nota de línea futura · 2026-09-27 · Sesión autónoma. Estado del código: **modo `trace` implementado y probado en la notebook** (rama `feat/trazas-reales` del clon `bci-fault-bench-futuro`). Estado de las fuentes: ver sección 2 (se completa con `_research-trazas.md`). Decisiones en [[Decisiones-Autonomas|DA-04]].

## 1. Qué pregunta responde

El Entregable 2 midió cuatro modelos de fallo uniformes y dos estructurados con severidades ancladas a la escala del ensayo (Tabla 1 de Métodos). La objeción prevista en [[Fundamentos-Diseno-Estadistico]] es "fallas de laboratorio": ¿un enlace real se comporta como jitter gaussiano y cortes de duración fija? La línea reemplaza los modelos paramétricos por **trazas**: series temporales del estado de un enlace medido (Bluetooth de un casco EEG, Wi-Fi congestionado), reproducidas 1:1 en el tiempo sobre la misma interfaz de transporte del banco. La pregunta nueva es si la **forma** de las fallas reales (ráfagas de pérdida, cortes con reconexión, retraso variable) produce efectos que los modelos paramétricos no mostraron.

## 2. Fuentes verificadas de comportamiento de enlaces

Resumen del informe `_research-trazas.md` (DOI verificados en Crossref y cifras tomadas del texto completo salvo ⚠️; ahí están las citas APA completas).

**Bluetooth / EEG inalámbrico**

| Fuente | Equipo | Cifra medida |
|---|---|---|
| Krigolson et al. (2017), *Front. Neurosci.*, 10.3389/fnins.2017.00109 | Muse por Bluetooth | retraso medio 40 ms (± 20 ms), con pocas muestras de latencia extrema |
| Dasenbrock et al. (2022), *Front. Neurosci.*, 10.3389/fnins.2022.904003 | SMARTING → Bluetooth → Android → LSL, 250 Hz | jitter ≈ 3 ms; el retraso cambia hasta 52 ms entre sesiones; muestras sueltas de hasta 150 ms |
| Arpaia et al. (2025), *IEEE TNSRE*, 10.1109/TNSRE.2025.3575695 | tres EEG inalámbricos | retraso medio 20 / 102 (88) / 47 ms según el equipo; sin pérdida de paquetes en las pruebas |
| Epinat-Duclos et al. (2026), *PeerJ*, 10.7717/peerj.20416 | EPOC Flex (Bluetooth) vs LiveAmp (Wi-Fi) vs cable | dos sesiones con pérdida total de conexión; disparadores perdidos 4,10 [0-19] vs 0,05 vs 0 |
| Mahmud et al. (2023), informe INL/RPT-23-74719, 10.2172/2242485 | BLE con Wi-Fi interfiriendo | PER de BLE entre 2 y 9 % |

Ya citado en el manuscrito (E1/E2, verificado entonces): Gemborn Nilsson et al. (2023), casco inalámbrico 20-40 ms de retraso y 5 ms de jitter.

**Wi-Fi congestionado**

| Fuente | Contexto | Cifra medida |
|---|---|---|
| Aguayo et al. (2004), *SIGCOMM CCR*, 10.1145/1030194.1015482 | Roofnet 802.11b | la pérdida es independiente por debajo de ≈ 0,1 s; en enlaces malos está correlacionada hasta ≥ 1 s |
| Jardosh et al. (2005), *IMC*, 10.1145/1330107.1330140 | red de la reunión IETF 62 | congestión por encima de 84 % de uso del canal; throughput de 4,9 a 2,8 Mbps |
| Sui et al. (2016), *MobiSys*, 10.1145/2906388.2906393 | campus, > 47.000 dispositivos | latencia de cola larga: p90 ≈ 20 ms, p99 ≈ 250 ms (⚠️ solo resumen) |

**Ninguna fuente publica duraciones de *dropout* en ms** ni una traza de pérdida de un casco EEG: eso es lo que falta y se lista en la sección 6.

**Sobre LSL** (liblsl 1.18, código y documentación oficial): al cortarse el flujo, el inlet con `recover` busca el flujo durante al menos 1,0 s y luego espera 500 ms fijos antes de reconectar; el *watchdog* de 15 s no interviene en cortes breves. Los ≈ 570 ms de reconexión medidos en la campaña se explican por esa espera fija más la búsqueda, TCP y el primer bloque (inferencia sobre el código; LSL no lo documenta). **Predicción verificada en los datos de E2** (`results/analysis/execs.csv`, medianas de 9 sujetos): intervalo máximo sin datos de 1.561 / 1.560 / 3.598 ms para cortes de 0,5 / 1 / 3 s, es decir, un exceso de **1.061 / 560 / 598 ms**. El corte de 0,5 s paga casi el doble que los otros porque cae dentro de la primera ronda de búsqueda de 1 s de liblsl: el costo de reconexión no es proporcional al corte sino que está cuantizado por el ciclo de búsqueda de LSL. Es un resultado nuevo para la Discusión (ver [[Propuestas-Manuscrito]]). Ninguna *issue* del proyecto mide el tiempo de reconexión (#35, #195, #299 lo mencionan): la medición es un aporte original y sostiene el punto 7 de [[Trabajo-Futuro]].

### 2.1 Trazas obtenidas

| Traza (`traces/`) | Origen | Qué reproduce | Qué NO reproduce |
|---|---|---|---|
| `ble-muse-s.csv` (66,9 s, cíclica) | grabación real de un Muse S por BLE exportada por Mind Monitor (Iwendi et al., 2026, Zenodo 10.5281/zenodo.22093536, CC BY 4.0, sin registro; MD5 verificado) | retraso y jitter de llegada reales del enlace BLE: 17.136 llegadas, reloj ajustado 256,04 Hz, retraso p50 31,6 ms, p99 53 ms, máximo 111 ms, jitter medio 13,5 ms | pérdida (no observable: llegan 17.136 muestras contra ≈ 17.081 esperadas) ni cortes; ⚠️ no se verificó cómo Mind Monitor marca el tiempo de cada muestra (agrupa 12 por paquete) |
| `ge-wifi-ble.csv` (420 s) | **modelo** de Gilbert-Elliott parametrizado con Mahmud (PER 2-9 %), Aguayo (correlación ≈ 1 s) y Sui (p50 5 ms, p99 250 ms, lognormal) | pérdida correlacionada en ráfagas y latencia de cola larga | **no es una medición**; se usa solo si el autor lo acepta como reemplazo declarado de la pérdida i.i.d. |
| `ejemplo-sintetico.csv` | generado | prueba de humo | — |

Reproducción de `ble-muse-s` en la notebook (60 s): latencia media 40,6 ms, desvío del intervalo entre llegadas 12,6 ms, 0 huecos, 7/7 ensayos válidos. **Coincide con los 40 ms de Krigolson et al. (2017) para el mismo casco**, medidos por otro método. Reproducción de `ge-wifi-ble` (60 s): recibido 0,963, 8,7 huecos por segundo, latencia media 24 ms y máxima 1,1 s: la cola lognormal produce bloques que llegan más de un segundo tarde y, como la entrega es en orden, arrastran a los siguientes (el reproductor lo registra como error de temporización p99 = 482 ms).

## 3. Diseño del modo `trace` (implementado)

### 3.1 Formato de archivo

`traces/<nombre>.csv`, UTF-8, con cabecera de procedencia obligatoria:

```
# source: <URL o DOI de la medición de origen>
# license: <licencia de la fuente>
# resolution_s: <duración típica del intervalo>
# notes: <cómo se convirtió; supuestos declarados>
t_s,up,delay_ms,loss[,jitter_ms]
```

| Columna | Significado | Dónde actúa en el banco |
|---|---|---|
| `t_s` | inicio del intervalo (s desde el inicio de la traza, creciente) | — |
| `up` | 1 enlace operativo · 0 corte | transporte real: se destruye y recrea el *outlet* (igual que `disconnect`) |
| `delay_ms` | retraso adicional de entrega de los bloques del intervalo | instante de entrega (igual que `delay`) |
| `loss` | fracción de muestras omitidas en el intervalo | contenido del flujo (igual que `loss`) |
| `jitter_ms` | (opcional) desviación estándar del retraso dentro del intervalo | instante de entrega (igual que `jitter`) |

La traza es el **formato común** al que se convierten fuentes heterogéneas. Tres convertidores en `scripts/trace_tools.py`:

- `from-timestamps`: a partir de las marcas de tiempo por muestra de una grabación real (LSL/XDF exportado a CSV): hueco > 1,5 períodos = muestras perdidas; hueco > 0,5 s = corte. El retraso no es observable en una grabación (queda 0) salvo que exista una columna de instante de llegada.
- `from-arrivals`: a partir del instante de **llegada** de cada muestra (Mind Monitor, Muse por BLE): se ajusta un reloj nominal lineal por mínimos cuadrados, el residuo llegada − nominal referido a su percentil 1 es el retraso; por intervalo se guarda media (retraso) y desvío (jitter). La pérdida no es observable en esa fuente.
- `synth-gilbert-elliott`: modelo de dos estados con parámetros publicados (ver 2.1); no es una medición.
- `from-ping`: a partir de un registro de `ping` (o CSV `seq,rtt_ms`): retraso de un sentido = (RTT − base)/2 con base = percentil 1; paquete perdido = `loss` 1; ≥ 3 pérdidas seguidas = corte. Supuesto declarado en la cabecera.
- `synth-example`: traza sintética de 60 s **solo para pruebas de humo** (no es una medición).

### 3.2 Anclaje a la escala del ensayo

- **Tiempo 1:1.** Un segundo de traza es un segundo de corrida; la traza no se estira ni se comprime (cambiaría la duración de cortes y ráfagas, que es lo que se quiere reproducir). Si es más corta que la corrida (≈ 6,5 min) se repite en forma cíclica.
- **Punto de entrada.** Al azar desde la semilla de la ejecución (así las cinco corridas de un sujeto no ven el mismo tramo), o fijo con `<nombre>@<offset_s>`. Queda registrado en `producer.json` (`trace_offset_s`) y en `fault_log.jsonl` (cortes planificados y efectivos), de modo que la realización es repetible.
- **Severidad = factor de escala** sobre `delay_ms` y `loss`; 1 = tal como se midió. Los cortes no se escalan. El criterio de la Tabla 1 (severidad anclada al ensayo) se sustituye por "tal como se midió" como condición principal; ×2 o ×4 quedan como estrés, declarado.
- **Análisis.** Cada traza es su propio tipo de fallo (`trace:<nombre>`) y se compara, como las demás familias, contra la referencia de la misma corrida (Wilcoxon apareado, Holm). `analyze.py` y `metrics.py` ya lo hacen sin cambios de interfaz.

### 3.3 Qué se probó en la notebook (2026-09-27)

Prueba de humo de 60 s (`scripts/smoke_run.py --fault trace --mode ejemplo-sintetico@0`), sujeto 1, corrida 0:

| Tramo de la traza | Qué debía pasar | Qué registró la telemetría |
|---|---|---|
| 10-20 s: retraso 0→60 ms, jitter 5 ms | latencia creciente | `lat_mean` 3 → 19 → 37 → 62 ms |
| 25,0-25,8 s: corte | 0 muestras, reconexión | `n_samples` = 0 en el segundo 25; intervalo máximo 1,56 s (0,8 s de corte + ≈ 0,76 s de reconexión de LSL) |
| 30-40 s: pérdida 3 % | ≈ 241 de 250 muestras | 241 muestras, 9 huecos por segundo |

7 ensayos, 7 válidos, sin excepciones; `producer.json` registra `trace`, `trace_offset_s` y la cabecera de procedencia. Una mini-campaña (sujetos 1, 3 y 8 × referencia + traza, 90 s, 3 en paralelo, 6/6 ok) pasó por `analyze.py` completo (tablas, divergencia y figuras) sin cambios: la traza aparece como tipo de fallo "traza ejemplo-sintetico" con recibido 0,962, 132 huecos, latencia media 7,8 ms y 2 s sin datos frente a la referencia.

## 4. Esfuerzo estimado

| Tarea | Estado | Esfuerzo restante |
|---|---|---|
| Modo `trace` (inyector, reproductor, ejecutor, análisis) | hecho | — |
| Convertidores desde marcas de tiempo y desde ping | hechos, probados con datos sintéticos | 0,5 día para probar con la fuente real elegida |
| Obtener trazas reales con licencia (ver `_research-trazas.md`) | ver informe | 1-3 días según disponibilidad |
| Campaña en la VM: 9 sujetos × 5 corridas × (referencia + *k* trazas) | pendiente | con *k* = 2: 270 ejecuciones ≈ 4,5 h con 12 workers |
| Métodos y Resultados (ver [[Propuestas-Manuscrito]]) | redactado como propuesta | 1 día |

## 5. Comando exacto para la VM

Preparación (una vez): la rama debe estar en la VM. Si v2.0 ya está en `main`, primero reubicar la rama: `git rebase --onto main feat/base-v2-snapshot feat/trazas-reales`.

```bash
# en la notebook: subir la rama (ya pusheada) y desplegar en la VM
ssh -i ~/.ssh/tfg-bench.pem ubuntu@<IP> "cd ~/bcibench && git fetch origin && git checkout feat/trazas-reales && git pull"
# copiar las trazas reales (si no están en la rama)
scp -i ~/.ssh/tfg-bench.pem traces/*.csv ubuntu@<IP>:~/bcibench/traces/
```

Prueba de humo en la VM (2 min):

```bash
cd ~/bcibench && .venv/bin/python scripts/smoke_run.py --fault trace --mode ejemplo-sintetico@0 --max-seconds 60
```

Campaña con las dos trazas disponibles (la traza real BLE y, si el autor acepta el modelo declarado, la Gilbert-Elliott):

```bash
cd ~/bcibench && tmux new -s trazas
PYTHONPATH=src .venv/bin/python -m bcibench.runner --plan trazas --subjects 1 2 3 4 5 6 7 8 9 --runs 0 1 2 3 4 \
  --workers 12 --out results/campana-trazas --family trace --traces ble-muse-s ge-wifi-ble --trace-scales 1
# análisis (misma ventana y regla que la campaña principal)
.venv/bin/python scripts/analyze.py --root results/campana-trazas --out results/analysis-trazas --window 8 --thr-rule min
```

Estimación: 9 × 5 × 3 = 135 ejecuciones ≈ 2,3 h con 12 workers (≈ 6,5 min cada una). Solo con la traza real: `--traces ble-muse-s` → 90 ejecuciones ≈ 1,6 h. Con escalas `1 2` (estrés declarado): 225 ejecuciones ≈ 3,8 h.

## 5 bis. Lo que falta (lista honesta)

1. **Una traza de pérdida/cortes de un casco EEG real.** Ninguna fuente publicada trae duraciones de *dropout*; la grabación del Muse no muestra pérdida. Opciones: (a) medirla con un casco propio (Muse o Ganglion) y `pylsl`, registrando marcas de tiempo del dispositivo y de llegada; (b) pedir a los autores de Epinat-Duclos et al. (2026) el registro del EPOC Flex con las desconexiones; (c) aceptar el modelo Gilbert-Elliott declarado como tal.
2. **Una traza de Wi-Fi congestionado descargable.** CRAWDAD `ucsb/ietf2005` exige cuenta IEEE DataPort (gratuita): el autor puede registrarse y convertirla con `from-ping` o un convertidor nuevo a partir de sus paquetes. Alternativa barata y honesta: un `ping -i 0.2` de 10 minutos a un router doméstico con descargas simultáneas, convertido con `from-ping`; se declara como medición propia.
3. **Modo calendario** (opcional): reproducir el agrupamiento en paquetes de 12 muestras del BLE liberando bloques según los instantes de llegada de la traza, en vez de media y desvío por intervalo (0,5 día).
4. **Verificar la predicción de LSL** sobre los datos de E2 (`disconnect-0.5` debería mostrar ≈ 1 s de exceso): una consulta sobre `results/analysis/execs.csv`.

## 6. Tradeoffs y límites

- **Fidelidad vs. capa.** Reproducir la traza en el inyector (dentro del proceso emisor) mantiene la comparabilidad con las otras familias, pero no reproduce el comportamiento de TCP ante pérdida de paquetes (retransmisión → retraso). Una traza de Wi-Fi convertida con `from-ping` modela la pérdida de paquetes como retraso solo si se declara así en la conversión; la alternativa fiel (netem/tc en Linux) queda fuera de la interfaz de transporte del banco.
- **Lo que una grabación no muestra.** Las marcas de tiempo de una grabación Bluetooth revelan huecos y cortes, no el retraso: para el retraso se necesitan mediciones con instante de llegada (ping, o LSL con `time_correction`).
- **Licencias.** Solo se convierten fuentes con licencia que permita redistribuir la traza derivada; la cabecera `# license` lo documenta y el análisis la copia a `producer.json`.

## Enlaces

- Código: `bci-fault-bench-futuro` rama `feat/trazas-reales` (`src/bcibench/trace.py`, `injector.py`, `scripts/trace_tools.py`, `traces/`).
- Informe de fuentes: `_research-trazas.md`.
- Manuscrito: [[Propuestas-Manuscrito]] · Decisiones: [[Decisiones-Autonomas]] · Contexto: [[Trabajo-Futuro]] n.º 5.
