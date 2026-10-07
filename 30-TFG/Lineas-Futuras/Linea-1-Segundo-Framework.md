# Línea 1 · Segundo marco de aplicación: consumidor sobre BciPy

> Nota de línea futura · 2026-09-27 · Sesión autónoma. Objetivo del Módulo 4: reemplazar el consumidor propio por la capa de un framework BCI completo y medir si sus búferes y su manejo de errores **amortiguan o amplifican** el costo de reconexión de LSL (≈ 570 ms por corte en la campaña; ver [[Linea-2-Trazas-Reales]] §2 por la explicación en liblsl). Informe de fuentes: `_research-frameworks.md`. Decisiones: [[Decisiones-Autonomas|DA-11]]. Código: rama `feat/framework-bcipy` del clon `bci-fault-bench-futuro`.

## 1. Comparación verificada (estado al 2026-09-27)

Todo lo que sigue sale de la API de GitHub, PyPI, los archivos de licencia y el código fuente descargado; los DOI se verificaron en Crossref.

| Criterio | BciPy 2.0.1 (CAMBI-tech/BciPy) | MEDUSA (medusa-kernel 1.4.3 + medusa-platform v2025.0.1) |
|---|---|---|
| Licencia | BSD-3-Clause | CC BY-NC-ND 2.0 (kernel y plataforma) |
| Último commit en la rama principal | 2025-10-17 (release v2.0.0 el 2025-08-25; PyPI 2.0.1 el 2025-10-17) | kernel 2026-02-04; plataforma 2026-07-06 |
| Estrellas / issues abiertos | 157 / 5 | 23 / 7 (kernel), 23 / 20 (plataforma) |
| Python declarado | > 3.8 y < 3.11 | kernel ≥ 3.10 y < 3.14; la plataforma no está en PyPI |
| Tipo | biblioteca pip + aplicación (PsychoPy/PyQt6); **la capa de adquisición es independiente de la GUI** | biblioteca de procesamiento (kernel, sin LSL) + **aplicación de escritorio** PySide6 con inicio de sesión en línea |
| Dónde recibe LSL | `bcipy/acquisition/protocols/lsl/lsl_client.py` (`LslAcquisitionClient`), pylsl 1.16.2 | `medusa-platform/src/acquisition/lsl_utils.py` + `src/resources.py` |
| Inlet | `StreamInlet(info, max_buflen=365, max_chunklen=1)`, `recover` por defecto (True) | `StreamInlet(stream, processing_flags=threadsafe)`, `recover` por defecto |
| Lectura | `pull_chunk(timeout=0)` a demanda, sin hilo propio | un hilo por flujo, `pull_chunk` en bucle ocupado |
| Búfer | anillo acotado (`RingBuffer`, lista de registros, `max_buffer_len × fs`), consultable por rango de marcas de tiempo (`get_data(start, end)`) | `np.vstack` sin límite (crece toda la corrida) |
| Política ante un corte | ninguna propia: delega en `recover` de liblsl; si la ventana pedida no está en el búfer, `AssertionError` | timeout = 1,5 × bloque máximo / fs = **1,5 s a 250 Hz**; más de 5 timeouts **acumulados** (el contador no se reinicia) matan el hilo con `MedusaException` |
| Marcadores | `ContentType.MARKERS` en `ClientManager` (un cliente por tipo) | flujo genérico; los onsets los genera la propia app |
| Enchufe del decodificador | `SignalModel` (orientado a RSVP) o directo sobre `get_data()` | `AppSkeleton.main()` + `MIModelCSP` del kernel |
| Artículo (Crossref) | Memmott et al. (2021), *Brain-Computer Interfaces*, 8(4), 137-153, 10.1080/2326263X.2021.1878727 | Santamaría-Vázquez et al. (2023), *CMPB*, 230, 107357, 10.1016/j.cmpb.2023.107357 (ya en Referencias del E2) |
| Esfuerzo de un consumidor sin GUI | 4,5-6,5 días-persona | 5-8 días con GUI en Windows, o bloqueado por *NoDerivs* si se publica una versión derivada |

Descartadas (verificado): **Timeflux** (MIT, último commit 2024-09-23, framework de flujo, no de BCI); **OpenViBE** (AGPL-3, C++); **BCI2000** (C++, Windows; licencia ⚠️ SIN VERIFICAR, páginas 404); **NeuroPype** (propietario). ⚠️ SIN VERIFICAR: sistemas operativos declarados por MEDUSA.

## 2. Elección: BciPy, solo su capa de adquisición

**Por qué BciPy**: licencia compatible con el repositorio público; capa `bcipy.acquisition` sin GUI; búfer acotado consultable por marca de tiempo (encaja con el segmentado por *onset* del banco); `ClientManager` ya modela EEG + marcadores; artículo con revisión por pares.

**Por qué no MEDUSA**: la recepción LSL vive en la aplicación de escritorio (Qt + cuenta en línea), no corre sin pantalla en la VM, y la cláusula *NoDerivs* impide publicar un consumidor derivado. Pero su **política de errores es el contrapunto de diseño ideal** y se describe en la Discusión: con cortes de ≈ 570 ms **no dispara** su timeout de 1,5 s (amortigua en silencio); con cortes largos repetidos, el sexto timeout acumulado mata el hilo (amplifica). Se cita como análisis estático del código (`lsl_utils.py`, `resources.py`, commit `23d4019a`, 2026-07-06).

**Tradeoffs declarados**:
- BciPy 2.0.1 declara Python < 3.11 y fija numpy 1.24 / scipy 1.10 / PsychoPy sin ruedas para 3.12. Se instaló **sin dependencias** (`--no-deps --ignore-requires-python`) más las que la capa de adquisición importa (`requirements-bcipy.txt`: pylsl 1.16.2, numpy, pandas, scipy, future, setuptools < 81, psutil, py-cpuinfo, pyglet, torch). Es una amenaza a la validez: "capa de adquisición de BciPy 2.0.1 fuera de su rango de Python soportado". Alternativa limpia para la VM: venv con Python 3.10 (`uv python install 3.10`), sin costo.
- No es "BciPy completo": es su capa de adquisición y búfer, que es exactamente la que responde la pregunta (¿el búfer del framework amortigua o amplifica?). Hay que decirlo así en Métodos.
- Hipótesis previa (del código, no del experimento): BciPy es **neutro** respecto de liblsl (mismo `recover`) y agrega un **punto de fallo duro** (aserción) si la ventana pedida cae fuera del búfer tras un corte. La medición dirá si eso se traduce en ensayos inválidos donde el consumidor propio decodifica.

## 3. Implementación (rama `feat/framework-bcipy`, hecha y probada)

Commits: `1b633c7` (telemetría a módulo propio), `4163793` (consumidor sobre BciPy), `8006e45` (ejecutor con `--consumer`), `2fcb51d` (comparador), `5c755a7` (README §10).

Diseño: `src/bcibench/consumer_bcipy.py` resuelve `<exec>-eeg` y `<exec>-markers` **por nombre** (BciPy resuelve por tipo y sin timeout), crea los inlets como BciPy (`max_buflen=365`, `max_chunklen=1`, `recover` por defecto), lee con el cliente a demanda, segmenta cada ensayo con `get_data(onset+1, onset+7)` sobre el búfer del framework, decodifica con el mismo CSP+LDA congelado y escribe **los mismos** `trials.csv`, `telemetry.csv`, `segments.npz` y `consumer.json` (con `"consumer": "bcipy"`), de modo que `runner.py`, `analyze.py` y `redecode_segments.py` sirven sin cambios. `runner.py` y `smoke_run.py` reciben `--consumer {own,bcipy}` y `--consumer-python` (el consumidor corre en `.venv-bcipy`, el reproductor en `.venv`). `scripts/compare_consumers.py` compara dos ejecuciones (propio vs BciPy) ensayo por ensayo.

## 4. Diseño experimental propuesto para la VM

Misma campaña que la v2 (9 sujetos × 5 corridas × 19 condiciones) con el consumidor BciPy: 855 ejecuciones ≈ 8 h con 12 workers. Comparación apareada **consumidor propio vs BciPy** por sujeto y condición sobre: intervalo máximo sin datos y segundos sin datos (¿el búfer del framework cambia el costo de reconexión?), tasa de ensayos válidos y excepciones (¿la aserción de BciPy convierte cortes en decisiones inválidas?), retardo de decisión, y *balanced accuracy*. Si el tiempo de VM es un límite: solo las familias `disconnect` y `disconnect_trial` más la referencia (7 condiciones, 315 ejecuciones ≈ 3 h), que son las únicas que ejercitan la reconexión.

## 5. Comando exacto para la VM

Preparación (una vez; Ubuntu 24.04 trae Python 3.12, misma solución que en la notebook):

```bash
ssh -i ~/.ssh/tfg-bench.pem ubuntu@<IP>
cd ~/bcibench && git fetch origin && git checkout feat/framework-bcipy && git pull
python3 -m venv .venv-bcipy && .venv-bcipy/bin/pip install -r requirements-bcipy.txt
.venv-bcipy/bin/pip install --no-deps --ignore-requires-python bcipy==2.0.1
.venv-bcipy/bin/python -c "from bcipy.acquisition import LslAcquisitionClient; print('ok')"
```

Prueba de humo (2 min) y campaña:

```bash
.venv/bin/python scripts/smoke_run.py --consumer bcipy --consumer-python .venv-bcipy/bin/python --fault disconnect --severity 1.0 --max-seconds 90
tmux new -s bcipy
PYTHONPATH=src .venv/bin/python -m bcibench.runner --plan bcipy --subjects 1 2 3 4 5 6 7 8 9 --runs 0 1 2 3 4 \
  --workers 12 --out results/campana-bcipy --family all --consumer bcipy --consumer-python .venv-bcipy/bin/python
.venv/bin/python scripts/analyze.py --root results/campana-bcipy --out results/analysis-bcipy --window 8 --thr-rule min
```

Versión corta (solo desconexiones, ≈ 3 h): agregar `--only ref disconnect-0.5 disconnect-1 disconnect-3 disconnect_trial-0.5 disconnect_trial-1 disconnect_trial-2`.

## 6. Resultados de la prueba en la notebook (sujeto 1, corrida 0)

Adaptaciones necesarias, documentadas en el módulo y que no cambian lo medido: resolución por nombre con tope de 90 s (BciPy resuelve por tipo y sin tope: con 12 ejecuciones en paralelo tomaría el flujo de otra); BciPy no tiene hilo de recepción, así que el bucle principal sondea `get_latest_data()` cada 5 ms; `start_acquisition` consume la primera muestra sin guardarla (el segundo 0 registra 249 muestras); `get_data` incluye ambos extremos y se descarta la muestra del borde para que la ventana sea idéntica; el búfer de BciPy se dimensiona en muestras (30 s = 7.500), no en segundos, así que durante un corte no se vacía.

| Condición | Ensayos válidos | Recibido | Latencia media | `AssertionError` de `get_data` |
|---|---|---|---|---|
| sin fallo, 60 s | 7/7 | 14.999 / 15.000 | 6,6 ms | 0 |
| retraso 0,25 s, 90 s | 9/9 | 0,99996 | 256 ms (retardo de decisión ≈ 1,29 s) | 0 |
| desconexión 1 s, 90 s | 9/9 | 0,93 | cuatro cortes, huecos de 1,52-1,56 s | 0 |
| desconexión 3 s, 90 s | **8/9** | — | — | **1** |

**Equivalencia** (sin fallo, 120 s, misma semilla, consumidor propio vs BciPy): 11/11 predicciones iguales, diferencia máxima de probabilidad 0, segmentos crudos idénticos bit a bit; recibido 1,000 vs 0,99997; latencia media 3,2 vs 6,5 ms; bloques por segundo 25 vs 28,5; retardo de decisión +4,8 ms en BciPy. El ejecutor con `--consumer bcipy` corrió 2/2 y `metrics.load_campaign` lee las salidas sin cambios.

**Hallazgo previo a la campaña** (una corrida, no inferencial): el búfer de BciPy **tolera en silencio los cortes cortos** (el corte se recupera antes del plazo y `get_data` entrega la ventana con menos muestras) e **invalida los cortes largos**: con un corte de 3 s la consulta por rango lanza `AssertionError: End time out of range` y el ensayo queda inválido, mientras el consumidor propio decodifica la parte recibida si hay ≥ 125 muestras. Es exactamente la diferencia de política que la campaña de la VM cuantificará por sujeto y severidad: para el framework, "amortiguar" y "amplificar" dependen de si el corte cabe dentro del plazo de decisión.

## Enlaces

- Informe de fuentes: `_research-frameworks.md` · Manuscrito: [[Propuestas-Manuscrito]] · Decisiones: [[Decisiones-Autonomas]] · Contexto: [[Trabajo-Futuro]] n.º 4.
