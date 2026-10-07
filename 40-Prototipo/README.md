# Banco de experimentación Software-in-the-Loop (TFG, Entregable 2)

Implementa el instrumento descrito en Métodos: reproduce EEG público (BCI Competition IV 2a)
como flujo LSL a su tasa original, inyecta fallos en la interfaz de transporte, decodifica con
CSP+LDA congelado y registra telemetría por segundo.

## Componentes (`src/bcibench/`)

| Módulo | Componente de Métodos |
|---|---|
| `data.py` | carga MOABB, eventos desde `STI`, artefactos anotados |
| `decoder.py` | decodificador de referencia CSP(6)+LDA, entrenado en sesión 1 y congelado |
| `replay.py` | servicio de reproducción (flujo EEG + flujo de marcadores) |
| `injector.py` | inyector de fallos: `loss` (random/burst), `jitter`, `delay`, `disconnect` |
| `consumer.py` | pipeline bajo prueba + recolector de telemetría (`trials.csv`, `telemetry.csv`) |
| `runner.py` | ejecutor de campañas: bloques, semillas, paralelismo, reanudación (`done.json`) |
| `metrics.py`, `stats.py`, `scripts/analyze.py` | variables dependientes, ventana móvil, umbral, Friedman/Wilcoxon/Holm, divergencia, detectores LOSO, tablas y figuras |

## Puesta en marcha local (Windows, desarrollo)

```bash
python -m venv .venv && .venv/Scripts/pip install -r requirements.txt
.venv/Scripts/python scripts/poc1_offline.py 1 2 3 4 5 6 7 8 9     # entrena y guarda los 9 decodificadores
.venv/Scripts/python scripts/smoke_run.py --fault loss --severity 0.05 --max-seconds 60
```

## VM Linux (campaña)

```bash
bash scripts/deploy.sh <IP> <ruta/tfg-bench.pem>          # copia, instala, verifica reloj, descarga dataset
ssh -i <pem> ubuntu@<IP>
cd ~/bcibench && tmux new -s bench
# piloto: corrida 6 (índice 5) de 3 sujetos, 13 condiciones, 6 en paralelo (~45 min)
PYTHONPATH=src .venv/bin/python -m bcibench.runner --plan piloto --subjects 1 5 8 --runs 5 --workers 6 --out results/piloto
# control de paralelismo: la misma referencia sola
PYTHONPATH=src .venv/bin/python -m bcibench.runner --plan piloto1 --subjects 1 --runs 5 --workers 1 --out results/piloto-solo --only ref
# análisis del piloto (elige W y q)
.venv/bin/python scripts/analyze.py --root results/piloto --out results/analysis-piloto --window 8 --q 5
# campaña: 9 sujetos × corridas 0 y 1 × 13 condiciones = 234 ejecuciones (~4,2 h con 6 workers)
PYTHONPATH=src .venv/bin/python -m bcibench.runner --plan campana --subjects 1 2 3 4 5 6 7 8 9 --runs 0 1 --workers 6 --out results/campana
.venv/bin/python scripts/analyze.py --root results/campana --out results/analysis --window <W> --q <q>
```

Si la campaña se interrumpe, se relanza el mismo comando: las ejecuciones con `done.json` se saltean.

## Salidas por ejecución (`results/<campaña>/<exec_id>/`)

- `producer.json`: condición, semilla, muestras emitidas/omitidas, cortes, error de temporización.
- `fault_log.jsonl`: eventos del inyector (cortes planificados y efectivos).
- `trials.csv`: por ensayo izquierda/derecha: etiqueta, predicción, confianza, muestras, validez, retardo de decisión.
- `telemetry.csv`: por segundo: muestras esperadas/recibidas, huecos, latencia, intervalos entre llegadas, predicciones, excepciones.
- `consumer.json`: resumen (balanced accuracy, válidos, excepciones).
