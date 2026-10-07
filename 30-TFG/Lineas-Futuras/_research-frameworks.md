# Research: BciPy vs MEDUSA como consumidor LSL para la línea futura

> Fecha de relevamiento: 2026-09-27. Todo dato viene de una fuente primaria consultada ese día (GitHub API vía `gh api`, raw.githubusercontent.com, PyPI JSON API, Crossref API, sitios oficiales). Lo que no pude verificar queda marcado **⚠️ SIN VERIFICAR**. Las inferencias propias (lectura de código, no dichas por el proyecto) quedan marcadas **(inferencia)**.

## 0. TL;DR

- **Recomendación: BciPy, pero usando SOLO su capa de adquisición** (`bcipy.acquisition`: `LslAcquisitionClient` + `ClientManager`), no la aplicación completa. Es BSD-3, es una librería, su capa de adquisición no importa GUI, y el buffer es un ring buffer acotado que se consulta por rango de timestamps: encaja casi 1:1 con el segmentado `[onset+2, onset+6]`.
- **El problema es Python**: `pyproject.toml` declara `requires-python = ">3.8,<3.11"` y fija `numpy==1.24.4`, `scipy==1.10.1`, `PsychoPy==2025.1.1` (sin wheels para 3.12). En Python 3.12 **no se instala el paquete completo**; hay que instalar con `--no-deps --ignore-requires-python` (y aportar `pylsl`, `pandas`, `numpy`) o crear un venv 3.10. Ojo: el README dice "Python 3.9, 3.10 or 3.11" y el pyproject dice `<3.11`; el CI (`.github/workflows/main.yml`) sólo prueba 3.9 y 3.10.6. Me quedo con el pyproject + CI.
- **MEDUSA queda descartado para esta línea**: licencia **CC BY-NC-ND 2.0** (NoDerivs, tanto kernel como platform), la plataforma es una app de escritorio PySide6 que exige **login contra medusabci.com**, no está en PyPI, y la capa LSL (`LSLStreamReceiver`, `LSLStreamAppWorker`) vive en la plataforma, no en `medusa-kernel`. Aun así su código es muy interesante como **objeto de estudio**: tiene una política explícita de reintentos (timeout 1,5 s, >5 timeouts ⇒ excepción) que sería justamente lo que la tesis quiere medir.
- **DOI de MEDUSA provisto era INCORRECTO**: `10.1016/j.cmpb.2023.107501` es otro paper (partículas en vías respiratorias). El correcto es **`10.1016/j.cmpb.2023.107357`**.

---

## 1. BciPy (CAMBI-tech/BciPy)

### 1.1 Estado del repositorio

| Campo | Valor | Fuente |
|---|---|---|
| Rama por defecto | `main` | `gh api repos/CAMBI-tech/BciPy` |
| Último commit en `main` | 2025-10-17T14:34:16Z (`67df8e17`, "Merge pull request #398 … dependency-fix / Adjust PyTables dependen…") | `gh api repos/CAMBI-tech/BciPy/commits?per_page=1` |
| `pushed_at` (cualquier rama) | 2026-07-30T15:47:34Z | `gh api repos/CAMBI-tech/BciPy` |
| Último release GitHub | `v2.0.0`, 2025-08-25 | `gh api .../releases?per_page=1` |
| Tags más recientes | `v2.0.1.rc4`, `v2.0.1rc3`, `v2.0.1rc2` | `gh api .../tags` |
| PyPI | `bcipy 2.0.1`, subido 2025-10-17T17:22:10, `requires_python <3.11,>3.8` | https://pypi.org/pypi/bcipy/json |
| Issues abiertos | 5 | `gh api` (`open_issues_count`, incluye PRs) |
| Stars | 157 | `gh api` |
| Licencia | SPDX `BSD-3-Clause`; `LICENSE.md` es texto BSD-3 "Copyright 2025 (CAMBI)". Detalle: el classifier del pyproject dice `License :: Other/Proprietary License` (inconsistencia de metadatos, el texto manda) | `gh api`, `LICENSE.md` |
| Python | `requires-python = ">3.8,<3.11"` (pyproject); README: "requires Python 3.9, 3.10 or 3.11"; CI: `[3.9, 3.10.6]` | `pyproject.toml`, `README.md`, `.github/workflows/main.yml` |
| SO | README: "windows (10, 11), linux (ubuntu 22.04) and macos (Sonoma)"; CI en `ubuntu-latest` (con `xvfb-run`), `windows-latest`, `macos-14` | README, workflow |
| Tipo | **Librería pip + app**. Entry points CLI: `bcipy`, `bcipy-sim`, `bcipy-train`, `bcipy-replay`… La app completa usa PsychoPy/PyQt6 (necesita display; en CI Linux se corre con `xvfb`). La **capa de adquisición es headless** (ver 1.5). | `pyproject.toml [project.scripts]` |

### 1.2 Cómo recibe LSL

Archivo: `bcipy/acquisition/protocols/lsl/lsl_client.py` (clase `LslAcquisitionClient`).

- **Librería**: `pylsl` (`from pylsl import StreamInlet, local_clock, resolve_byprop`), pin `pylsl==1.16.2`. No usa mne-lsl.
- **Resolución del stream**: `connect.py::resolve_device_stream` resuelve **por `type`, no por nombre**, y **sin timeout**:
  ```python
  streams = resolve_stream('type', content_type)
  ```
  ⇒ con varios streams `EEG` en la red toma `streams[0]`. Para `<exec>-eeg` hay que subclasear o inyectar el `StreamInfo` (inferencia).
- **Creación del inlet**:
  ```python
  self.inlet = StreamInlet(stream_info, max_buflen=MAX_PAUSE_SECONDS, max_chunklen=1)
  ```
  `MAX_PAUSE_SECONDS = 365` (`bcipy/config.py`). **No pasa `recover`** ⇒ queda el default de pylsl, `recover=True` (verificado en `pylsl v1.16.2/pylsl/pylsl.py` línea 668: `def __init__(self, info, max_buflen=360, max_chunklen=0, recover=True, processing_flags=0)`). Sin `processing_flags` (sin clocksync/dejitter).
- **Pulling**: por chunk, no bloqueante, **bajo demanda** (no hay hilo en el cliente):
  ```python
  samples, timestamps = self.inlet.pull_chunk(timeout=0.0, max_samples=self.max_samples)
  ```
  `get_latest_data()` vacía el inlet en un loop `while count == self.max_samples` y devuelve el buffer.
- **Buffer**: `bcipy/gui/viewer/ring_buffer.py::RingBuffer`, **lista Python de objetos `Record(sample, timestamp)`** (no numpy), tamaño fijo `max_samples = int(max_buffer_len * sample_rate)` (para irregular: `max_buffer_len` = n° de muestras). `max_buffer_len` default = 1 s; en la app se fija con `task_buffer_length` (`helpers/acquisition.py::init_lsl_client`). Sobrescribe lo más viejo al llenarse.
- **Hilos**: el cliente no usa hilo; sólo el grabador opcional `LslRecordingThread(StoppableProcess)` (**proceso**, no hilo) en `lsl_recorder.py`, que abre **su propio** `StreamInlet(stream_info, max_chunklen=1)` y hace `pull_chunk(timeout=0.0)` cada `sleep_seconds = 0.2`.
- **Stream que desaparece**: **no hay lógica de reconexión ni manejo de excepción propio**. Todo queda delegado a `recover=True` de liblsl. `open_stream(timeout=LSL_TIMEOUT)` con `LSL_TIMEOUT = 5.0` sólo al arrancar. En `get_data()` hay:
  ```python
  assert start is not None and start >= data_start, 'Start time out of range'
  assert end is not None and end <= data_end, 'End time out of range'
  ```
  ⇒ si tras un corte la ventana pedida cae fuera del buffer, **falla con `AssertionError`** (inferencia sobre el efecto; el código es literal).

**Lectura para la tesis (inferencia)**: BciPy es "pasivo": no amortigua ni amplifica por diseño propio; el costo de reconexión lo decide liblsl. Lo que sí agrega es (a) un buffer de 365 s en el inlet que puede retener datos si el outlet sigue vivo, y (b) un punto de falla duro (assert) si falta ventana. Eso es medible y comparable contra el consumidor propio.

### 1.3 Dónde se enchufa un decodificador propio

- `bcipy/signal/model/base_model.py::SignalModel(ABC)` — métodos abstractos: `reshaper`, `fit(training_data, training_labels)`, `evaluate(test_data, test_labels)`, `predict(data, inquiry: List[str], symbol_set: List[str])`, `save(path)`, `load(path)`. La firma de `predict` está pensada para **spellers RSVP** (inquiry/símbolos), no para MI de 4 clases.
- Para un consumidor headless **no hace falta** `SignalModel`: se usa directamente `LslAcquisitionClient.get_data(start, end)` / `ClientManager.get_data_by_device(start, seconds, content_types)` y se llama al pipeline sklearn pickleado.

### 1.4 Marcadores como segundo inlet

- `bcipy/acquisition/multimodal.py::ContentType` define `EEG`, `EYETRACKER` y `MARKERS` (sinónimo `'switch'`). `ClientManager` maneja **un `LslAcquisitionClient` por content type** y `get_data_by_device()` aplica `start + device_spec.static_offset` por dispositivo.
- Para irregular rate (`IRREGULAR_RATE`) el buffer se dimensiona en muestras y **no** aplica los asserts de rango.
- Alineación: ambos clientes usan timestamps LSL del inlet (sin `proc_clocksync`), en el mismo reloj si todo corre en la misma máquina; `clock_offset()` convierte reloj de experimento (PsychoPy) a `local_clock()`. En la app nativa BciPy **genera** sus marcadores (`marker_writer.py::LslMarkerWriter`, stream `"Markers"` tipo `string`), no consume uno externo tipo `int32`. Consumir `<exec>-markers` int32 funciona con el mismo cliente, pero ⚠️ SIN VERIFICAR en ejecución (no lo corrí).

### 1.5 Instalabilidad en Windows 11 + Python 3.12 + CPU + headless

Chequeo de wheels en PyPI (JSON API) de los pins de `pyproject.toml`:

| Pin | `requires_python` | wheel cp312 Windows |
|---|---|---|
| `numpy==1.24.4` | >=3.8 | **No** |
| `scipy==1.10.1` | <3.12 | **No** |
| `PsychoPy==2025.1.1` | **<3.11** | No |
| `pyo==1.0.5` | >=3.7,<4 | **No** (sí cp310) |
| `torch==2.2.0` | >=3.8 | Sí |
| `tables==3.9.1` | >=3.9 | Sí |

Además `PyQt6==6.7.1`, `WxPython==4.2.1` (no Linux), README pide **Microsoft Visual C++ Build Tools** en Windows.

**Conclusión**: `pip install bcipy` en 3.12 **falla** por `requires-python`. Camino viable: la capa `bcipy.acquisition` sólo importa `bcipy.config`, `pylsl`, `pandas`, `numpy` y stdlib (verifiqué los imports de `lsl_client.py`, `connect.py`, `multimodal.py`, `devices.py`, `record.py`, `helpers/clock.py`, `gui/viewer/ring_buffer.py`), así que:
1. `pip install bcipy==2.0.1 --no-deps --ignore-requires-python` + `pip install pylsl pandas numpy`, **o**
2. vendorizar esos ~8 archivos (BSD-3 lo permite con atribución), **o**
3. venv Python 3.10 con install completo (pesado: torch, psychopy).

Que el import de `bcipy.acquisition` no arrastre GUI en 3.12 es ⚠️ SIN VERIFICAR en ejecución (lo inferí de los imports).

### 1.6 Esfuerzo estimado (consumidor headless)

| Tarea | Días-persona |
|---|---|
| Instalación en 3.12 (`--no-deps`) o vendorizado + smoke test | 0,5–1 |
| Resolver por **nombre** (`<exec>-eeg`/`<exec>-markers`): subclase de `LslAcquisitionClient` o `DeviceSpec` custom | 0,5 |
| Loop de polling (el cliente no tiene hilo): hilo propio que llama `get_latest_data()` y detecta cues 1..4, 100, 200 | 1 |
| Segmentado `[onset+2, onset+6]` con `get_data(start,end)`, `max_buffer_len` ≥ 8–10 s, manejo del `AssertionError` como evento de telemetría | 1 |
| CSP+LDA pickleado + `trials.csv` / `telemetry.csv` / `segments.npz` (reusar esquema actual) | 0,5–1 |
| Instrumentar la reconexión (timestamps de gap, muestras perdidas) y validar contra el consumidor propio | 1–2 |
| **Total** | **≈ 4,5–6,5 días** |

---

## 2. MEDUSA (medusabci)

### 2.1 Estado del repositorio

| Campo | medusa-kernel | medusa-platform | Fuente |
|---|---|---|---|
| Rama por defecto | `master` | `master` | `gh api` |
| Último commit | 2026-02-04T16:37:37Z (`37b709d2`, "Fixed 10-20 montages") | 2026-07-06T16:46:37Z (`23d4019a`, "Added cookies to app_info…") | `gh api …/commits?per_page=1` |
| `pushed_at` | 2026-09-24 | 2026-07-06 | `gh api` |
| Último release | `v1.4.3`, 2025-12-03 | `v2025.0.1`, 2025-12-04 | `gh api …/releases` |
| PyPI | `medusa-kernel 1.4.3` (2025-12-03), `requires_python <3.14,>=3.10` | **No está en PyPI** (HTTP 404) | PyPI JSON |
| Issues abiertos | 7 | 20 | `gh api` |
| Stars | 23 | 23 | `gh api` |
| Licencia | SPDX `NOASSERTION`; `LICENSE` = **Creative Commons Attribution-NonCommercial-NoDerivs 2.0**; `setup.py license='CC Attribution-NonCommercial-NoDerivs 2.0'` | `LICENSE.txt` = **CC BY-NC-ND 2.0** | archivos LICENSE |
| Python | `python_requires='>=3.10, <3.14'` ⇒ **3.12 OK** | `requirements.txt` fija `numpy==2.3.5`, `PySide6==6.10.1`, `pylsl==1.17.6`, `scikit-learn==1.7.2`, `medusa-kernel>=1.4,<1.5` | `setup.py`, `requirements.txt` |
| Tipo | Librería pip (procesamiento), pero **depende de `PySide6`** en `install_requires` | **App de escritorio GUI** ("MEDUSA© Platform is a desktop application… modern graphic user interface", README) | README |

Extras de la plataforma: `src/user_session.py` apunta a `url_server = 'https://www.medusabci.com/api'` y `main_window.py` abre `LoginDialog` si `accounts_manager.check_session()` falla ⇒ **requiere cuenta online**. README: "MEDUSA Platform is under heavy development!".

SO: ⚠️ SIN VERIFICAR (el README consultado no lista SO; la plantilla Unity incluye DLLs Windows).

### 2.2 Cómo recibe LSL

**Importante**: `medusa-kernel` **no contiene código LSL** (árbol de 126 archivos, ningún `lsl`). Todo está en la plataforma:

- `src/acquisition/lsl_utils.py::LSLStreamWrapper.set_inlet()`:
  ```python
  self.lsl_stream_inlet = pylsl.StreamInlet(self.lsl_stream, processing_flags=processing_flags)
  ```
  `pylsl` (1.17.6), sin `recover` explícito ⇒ **`recover=True`** y `max_buflen=360` por default (verificado en `pylsl v1.17.6/src/pylsl/inlet.py`). Flags por defecto: sólo `proc_threadsafe=True`.
- `LSLStreamReceiver` (mismo archivo): `min_chunk_size = max(int(0.01*fs), 1)`, `max_chunk_size = max(2*min_chunk_size, int(fs))`, y
  ```python
  timeout = 1.5 * self.max_chunk_size / self.fs if self.fs > 0 else np.inf
  ```
  Para EEG 250 Hz ⇒ min_chunk 2, max_chunk 250, **timeout 1,5 s** (inferencia aritmética). Para marcadores irregulares (fs=0) ⇒ **timeout infinito**. `auto_mode=True` agranda `max_chunk_size`/`timeout` si `samples_available()` lo supera.
- `get_chunk()`: loop `while True` con `pull_chunk(max_samples=...)` (timeout 0.0 por default de pylsl ⇒ **busy-wait sin sleep**, inferencia) hasta juntar `min_chunk_size`; convierte a tiempo local con `time_correction()` + offset Unix; si pasa el timeout: `raise exceptions.LSLStreamTimeout()`.
- `src/resources.py::LSLStreamAppWorker(th.Thread)` — **un hilo por stream**:
  ```python
  except exceptions.LSLStreamTimeout as e:
      error_counter += 1
      if error_counter > 5:
          raise exceptions.MedusaException(... 'Is the device connected?' ...)
      else:
          self.medusa_interface.log(msg='... Trying to reconnect.', style='warning')
          continue
  ```
  `error_counter` **nunca se resetea** tras un chunk exitoso ⇒ el 6.º timeout **acumulado** de la sesión mata el worker (lectura de código; es un hallazgo relevante para fault injection). El "reconnect" es sólo un `continue`, la reconexión real la hace liblsl.
- **Buffer**: `numpy` **sin límite**: `self.data = np.vstack((self.data, chunk_data))` y `np.append` de timestamps, protegido por `th.Lock()`. Crece toda la corrida y copia todo el array en cada chunk (O(n²) en copias, inferencia). Sólo acumula si `app_state == APP_STATE_ON` y `run_state == RUN_STATE_RUNNING`.

**Lectura para la tesis (inferencia)**: con cortes de ≈570 ms MEDUSA **no dispara** su timeout (1,5 s), así que absorbería el corte en silencio; cortes >1,5 s generan warnings y, a partir del 6.º acumulado, la muerte del hilo. Es decir: **amortigua cortes cortos y amplifica fallas repetidas** — un contraste muy lindo con BciPy, pero no es usable en la tesis por licencia/GUI (ver 2.5).

### 2.3 Dónde se enchufa un decodificador

- Plataforma: `src/resources.py::AppSkeleton(mp.Process)` — el usuario implementa `main()`, `manager_thread_worker()`, `process_event(event)`, `check_lsl_config()`, `check_settings_config()`; consume datos con `self.lsl_workers[uid].get_data()` → `(timestamps, data)`. Plantillas: `src/templates/qt_template/`, `src/templates/unity_template/`.
- Kernel: `medusa/components.py::Algorithm(ProcessingMethod)` con `add_method()`; `medusa/bci/mi_paradigms.py::MIModel(Algorithm)` con `configure()`, `build()`, `fit_dataset(dataset)`, `predict(times, signal, fs, l_cha, x_info)`; **ya existe `MIModelCSP`** (`predict(times, signal, fs, channel_set, x_info)`, `x_info` con `"onsets"` y `"mi_labels"`).

### 2.4 Marcadores como segundo inlet

No hay concepto de "marker stream" de primera clase: cualquier stream LSL se configura en la GUI (`src/gui/lsl_config/`) y obtiene su `LSLStreamAppWorker`. En los paradigmas MEDUSA los onsets los genera la propia app (Unity/Qt) y se pasan en `x_info["onsets"]`. Un stream irregular int32 funcionaría con timeout infinito (inferencia). Alineación: cada chunk se lleva a tiempo Unix local (`lsl_times + lsl_clock_offset + unix_clock_offset`), con corrección de aliasing opcional (desactivada: `self.aliasing_correction = False`).

### 2.5 Instalabilidad Windows 11 + 3.12 + headless

- `medusa-kernel`: instala en 3.12 (rango `>=3.10,<3.14`), pero arrastra `PySide6`. Útil sólo para procesamiento (tiene `MIModelCSP`), **no trae LSL**.
- `medusa-platform`: no es paquete pip; `resources.py` hace `from PySide6.QtWidgets import *` al importar; la app se lanza desde la GUI y exige login online. **No corre headless** en una VM Linux sin display (inferencia fuerte: Qt + login).
- **Licencia CC BY-NC-ND 2.0**: la cláusula NoDerivs impide distribuir una versión modificada/adaptada (p. ej. un consumidor headless derivado de `resources.py`) en el repo público de la tesis. ⚠️ Interpretación legal no verificada con el titular; pero es un riesgo real para un repo público v1.0.

### 2.6 Esfuerzo estimado

| Opción | Días-persona |
|---|---|
| A. Usar la plataforma tal cual (GUI + cuenta + app custom desde `qt_template`), en Windows con display | 5–8 (y no automatizable en la VM de AWS) |
| B. Extraer `LSLStreamReceiver`/`LSLStreamAppWorker` a un consumidor headless | 4–6 técnicos, **pero bloqueado por NoDerivs** si se publica |
| **Veredicto** | No recomendable para la línea |

---

## 3. Alternativas (sólo para justificar exclusión)

- **Timeflux** (MIT; `gh api repos/timeflux/timeflux`): último commit en `master` **2024-09-23**, último release `v0.17.2` (2024-12-04), 25 issues abiertos, 189 stars. `setup.cfg` fija `numpy==1.26.4` (sin wheels cp313, sí cp312 ⚠️ SIN VERIFICAR). Su nodo `timeflux/nodes/lsl.py::Receive` crea `StreamInlet(streams[0], processing_flags=clocksync|dejitter)` y hace `pull_chunk` en `update()`; si el stream no está, `resolve_byprop(..., timeout=1.0)` y `return`. Es un grafo YAML de nodos, headless — técnicamente viable, pero **~2 años sin commits** y es un framework de flujo (pandas DataFrames por tick), no un framework BCI con capa de adquisición+buffer para comparar. Excluido por mantenimiento.
- **BCI2000**: la wiki oficial documenta el módulo `LSLSource` ("uses Labstreaminglayer to acquire data…", en `/src/contrib/SignalSource/LSLSource`) y dice "operates on most Windows systems". Implementación C++ y licencia: ⚠️ SIN VERIFICAR (las páginas de licencia consultadas dieron 404). Excluido: C++/Windows, arquitectura de módulos por proceso, esfuerzo de integración muy superior al de un consumidor Python.
- **OpenViBE**: licencia **AGPL-3.0** desde 0.16.0 (http://openvibe.inria.fr/license/); repo `openvibe/extras` en gitlab.inria.fr es 87 % C++ (API de lenguajes) con última actividad 2026-09-04; tiene cajas `CBoxLSLCommunication` y `CBoxLSLExport` (`plugins/processing/network-io`) y la extensión de servidor `lsl-output`. Excluido: C++, diseñador gráfico de escenarios, AGPL.
- **NeuroPype**: sitio oficial: software **propietario/comercial** con "30-day free trial", "free academic license" y ediciones "Enterprise and Deployment" (https://www.neuropype.io/). Excluido: cerrado, no auditable a nivel de código (clave para fault injection).

---

## 4. Tabla comparativa

| Criterio | BciPy 2.0.1 | MEDUSA (kernel 1.4.3 + platform v2025.0.1) |
|---|---|---|
| Licencia | BSD-3-Clause | CC BY-NC-ND 2.0 (ambos) |
| Último commit rama default | 2025-10-17 | kernel 2026-02-04 / platform 2026-07-06 |
| Stars / issues abiertos | 157 / 5 | 23 / 7 (kernel), 23 / 20 (platform) |
| Python declarado | >3.8,<3.11 (CI: 3.9, 3.10) | kernel >=3.10,<3.14 |
| Instala en Win11 + 3.12 | No el paquete completo; sí la capa de adquisición con `--no-deps` | kernel sí; platform no es pip |
| Headless | Capa de adquisición sí; app no (PsychoPy/PyQt6) | No (PySide6 + login online) |
| Dónde está el LSL | `bcipy/acquisition/protocols/lsl/lsl_client.py` | `medusa-platform/src/acquisition/lsl_utils.py` + `src/resources.py` |
| Resolución | por `type`, sin timeout | por propiedades, config en GUI |
| Inlet | `max_buflen=365`, `max_chunklen=1`, `recover` default (True) | `max_buflen` default (360), `recover` default (True), `proc_threadsafe` |
| Pulling | `pull_chunk(timeout=0.0)` bajo demanda, sin hilo | hilo por stream, `pull_chunk` en busy loop |
| Buffer | `RingBuffer` (lista de `Record`), acotado a `max_buffer_len*fs` | `np.vstack` sin límite |
| Manejo de corte | Nada propio; `AssertionError` si la ventana no está | Timeout 1,5 s @250 Hz; >5 timeouts acumulados ⇒ `MedusaException` |
| Marcadores | `ContentType.MARKERS` + `ClientManager` | stream genérico; onsets en `x_info` |
| Punto de enchufe del decoder | `SignalModel` (orientado a RSVP) o directo sobre `get_data()` | `AppSkeleton.main()` + `MIModelCSP` |
| Paper (verificado en Crossref) | 10.1080/2326263X.2021.1878727 | **10.1016/j.cmpb.2023.107357** |
| Esfuerzo consumidor headless | ≈4,5–6,5 días | 5–8 días (GUI) o bloqueado por licencia |

---

## 5. Recomendación

**Usar BciPy (capa `bcipy.acquisition`) como framework de la línea futura.** Razones: licencia BSD-3 compatible con el repo público; librería con capa de adquisición desacoplada de la GUI; buffer acotado consultable por timestamps (encaja con el segmentado por onset); `ClientManager` ya modela EEG + MARKERS; paper con revisión por pares y DOI verificado.

Tradeoffs honestos:
- **Python**: hay que romper el `requires-python` (`--ignore-requires-python`) o fijar un venv 3.10 sólo para este experimento. Eso es una amenaza a la validez que hay que declarar ("se usó la capa de adquisición de BciPy 2.0.1 fuera de su rango soportado").
- **No se usa el "BciPy completo"**: se usa su capa de adquisición y buffer. Para la pregunta de la tesis ("¿el buffer/manejo de errores del framework amortigua o amplifica?") es exactamente la capa relevante, pero hay que decirlo así, sin vender "framework completo".
- **BciPy casi no tiene manejo de errores propio**: el resultado esperable (hipótesis) es "neutro respecto de liblsl + fallo duro si falta ventana". Si se quiere contraste con un framework que **sí** tiene política propia, MEDUSA es el caso ideal pero no se puede usar/publicar; se puede **describir** su política (timeout 1,5 s, >5 acumulados ⇒ excepción) en Discusión/Trabajo futuro como análisis estático, citando el código.
- La cadencia de BciPy bajó (último commit en `main` 2025-10-17, ~11 meses), pero con release 2.0.x reciente y 157 stars.

---

## 6. Párrafos para la Introducción (con cita primaria verificada)

**BciPy.** BciPy es un framework de código abierto en Python para el desarrollo de interfaces cerebro-computadora, mantenido por el consorcio CAMBI y distribuido bajo licencia BSD-3. Integra adquisición de datos vía Lab Streaming Layer, presentación de estímulos, modelado de señales y paradigmas como RSVP Keyboard, con una capa de adquisición que mantiene un buffer circular consultable por marca temporal (Memmott et al., 2021).

- Cita (Crossref): Memmott, T., Koçanaoğulları, A., Lawhead, M., Klee, D., Dudy, S., Fried-Oken, M., & Oken, B. (2021). *BciPy: brain–computer interface software in Python*. **Brain-Computer Interfaces**, 8(4), 137–153. https://doi.org/10.1080/2326263X.2021.1878727 (Crossref: online 2021-02-02, print 2021-10-02).
- Complementar con software: BciPy v2.0.1, https://github.com/CAMBI-tech/BciPy, PyPI 2025-10-17.

**MEDUSA.** MEDUSA© es un ecosistema en Python para investigación en BCI y neurociencia cognitiva, compuesto por una librería de procesamiento de bioseñales (MEDUSA Kernel) y una plataforma de escritorio (MEDUSA Platform) que adquiere señales vía LSL y ejecuta paradigmas como aplicaciones independientes. Su arquitectura asigna un hilo de recepción por stream LSL con una política explícita de timeouts, lo que la vuelve un contrapunto de diseño relevante frente a consumidores sin manejo de errores propio (Santamaría-Vázquez et al., 2023).

- Cita (Crossref): Santamaría-Vázquez, E., Martínez-Cagigal, V., Marcos-Martínez, D., Rodríguez-González, V., Pérez-Velasco, S., Moreno-Calderón, S., & Hornero, R. (2023). *MEDUSA©: A novel Python-based software ecosystem to accelerate brain-computer interface and cognitive neuroscience research*. **Computer Methods and Programs in Biomedicine**, 230, 107357. https://doi.org/10.1016/j.cmpb.2023.107357 (Crossref: 2023-03).
- **El DOI candidato `10.1016/j.cmpb.2023.107501` es incorrecto**: Crossref lo resuelve a Kuga, Kizuka, Khoa & Ito (2023), "Effect of transient breathing cycle on the deposition of micro and nanoparticles on respiratory walls", CMPB 236. No usar.
- Afirmaciones sobre timeout/hilos: citar además el código (medusa-platform `src/acquisition/lsl_utils.py`, commit `23d4019a`, 2026-07-06), porque el paper no fue verificado en ese nivel de detalle.

---

## 7. Fuentes consultadas

- `gh api repos/{CAMBI-tech/BciPy, medusabci/medusa-kernel, medusabci/medusa-platform, timeflux/timeflux}` (+ `/commits`, `/releases`, `/tags`, `/git/trees`)
- raw.githubusercontent.com: BciPy `pyproject.toml`, `README.md`, `LICENSE.md`, `.github/workflows/main.yml`, `bcipy/config.py`, `bcipy/acquisition/{protocols/lsl/lsl_client.py, connect.py, lsl_recorder.py, multimodal.py, marker_writer.py, devices.py, record.py}`, `bcipy/gui/viewer/ring_buffer.py`, `bcipy/signal/model/base_model.py`, `bcipy/helpers/{acquisition.py, clock.py}`; MEDUSA kernel `setup.py`, `LICENSE`, `medusa/components.py`, `medusa/bci/mi_paradigms.py`; MEDUSA platform `README.md`, `LICENSE.txt`, `requirements.txt`, `dependencies.txt`, `src/acquisition/lsl_utils.py`, `src/resources.py`, `src/gui/main_window.py`, `src/user_session.py`; Timeflux `timeflux/nodes/lsl.py`, `setup.cfg`; pylsl `v1.16.2/pylsl/pylsl.py`, `v1.17.6/src/pylsl/inlet.py`
- PyPI JSON: `bcipy`, `medusa-kernel`, `medusa-platform` (404), `timeflux`, `pylsl/1.16.2`, `numpy/1.24.4`, `scipy/1.10.1`, `PsychoPy/2025.1.1`, `torch/2.2.0`, `tables/3.9.1`, `PySide6/6.10.1`, `pyo/1.0.5`
- Crossref: `works/10.1080/2326263X.2021.1878727`, `works/10.1016/j.cmpb.2023.107501`, `works/10.1016/j.cmpb.2023.107357`, búsqueda bibliográfica MEDUSA
- Web: bci2000.org (Main_Page, Contributions:LSLSource), openvibe.inria.fr (home, license), gitlab.inria.fr API (`openvibe/extras`), neuropype.io
