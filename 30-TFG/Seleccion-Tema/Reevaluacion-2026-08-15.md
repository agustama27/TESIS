# Reevaluación de finalistas con la vara correcta

> 2026-08-15 · Ejecuta los 3 pendientes de [[../../20-Investigacion/Calibracion-Alcance-Tesis-BCI|Calibración de alcance]]:
> (1) segundo referente de tesis de la disciplina, (2) exploración del ángulo QA/testing, (3) reevaluación de los finalistas.

---

## 1. Segundo referente de tesis (parcial)

- **PUCE (Ing. en Sistemas)**: repositorio caído (HTTP 503, mantenimiento) — ⏳ reintentar en unos días.
- **Uniandes (2013)**: metadatos confirmados vía navegador — *"Diseño e implementación de una interfaz cerebro-máquina (BCI) para la identificación de tareas cognitivas, a partir de señales de EEG adquiridas con sistemas portátiles"*, Gamba Cárdenas, **Ingeniería Electrónica, trabajo de grado de pregrado**, dirigida por dos profesores, PDF de 1 MB. El texto completo está tras protección anti-bot (⏳ pendiente); el patrón del título confirma la calibración: **"diseño e implementación"**, no "descubrimiento".

**Estado de la calibración**: confirmada con 1 tesis completa (UNSAM, 141 pp.) + 5 casos a nivel de metadatos. Suficiente para operar.

## 2. Ángulo QA/testing de sistemas BCI — explorado y CON sustancia

Lo que existe (verificado hoy) — y bajo la vara correcta, que exista es **bueno**: hay sobre qué construir.

| Recurso | Qué es | Referencia |
|---|---|---|
| **SzCORE** | Framework open-source de evaluación/validación para algoritmos de detección de convulsiones en EEG — con model cards, métricas y reproducibilidad | [arXiv 2402.13005](https://arxiv.org/pdf/2402.13005) |
| **DEEGMUX** | Emulador de señales EEG (hardware) para **testing reproducible hardware-in-the-loop** de clasificadores embebidos | [ScienceDirect 2026](https://www.sciencedirect.com/science/article/pii/S246806722600060X) |
| Framework OpenBCI para experimentos | Automatiza creación de bases, chequeos de integridad, debugging | [Sensors 2023](https://doi.org/10.3390/s23073763) |
| **MOABB reproducibility study** | El mayor estudio de reproducibilidad de BCIs basados en EEG | [arXiv 2404.15319](https://arxiv.org/html/2404.15319) |

**Tema candidato emergente (26, a desarrollar si interesa):**

> *"Diseño e implementación de un framework de pruebas automatizadas para pipelines BCI de código abierto"* — pruebas de regresión por reproducción de señal (replay), pruebas de integración del pipeline, benchmarks de latencia, integración continua. **Prototipado Tecnológico** natural, 100% Ingeniería de Software (testing es disciplina núcleo), sobre un proyecto open-source existente.

**El detalle valioso**: la tesis de UNSAM trabajó dentro de **OTTAA Project** — proyecto argentino de comunicación aumentativa, de código abierto. Ese modelo ("trabajar dentro de un proyecto OSS existente agregándole una capacidad") aplica acá directamente: un framework de QA aplicado a un pipeline BCI open source real. ⏳ Verificar el estado actual del código de OTTAA Project en GitHub antes de proponerlo.

## 3. Los finalistas, reevaluados

### Tema 19 — Fidelidad brain-to-text → 🟢 VIABLE (más de lo que se dijo)

- Con vara de paper se lo degradó porque "la ablación del LM ya existe y el resultado es previsible". **Con vara de TFG**: aplicar el protocolo de fidelidad (desarrollado en EEG no invasivo) a los datos intracorticales públicos, **declarando qué se replica y qué se aporta**, es un estudio bien delimitado y ejecutable — exactamente el tipo de trabajo que se aprueba.
- Debilidad real que queda: al autor no lo entusiasma ("muy de nicho, el sistema ya funciona bien").

### Tema 24 — LLM comunicación asistida en español → 🟢 EL MÁS SÓLIDO EN PAPEL

- Ya era el más fuerte con la vara exigente (ausencia verificable: no existe en español; precedente metodológico en portugués brasileño). Con la vara correcta, es casi sin riesgo: método publicado en Nature Comms para replicar/adaptar, stack diario del autor, validación por simulación offline.
- Debilidad real que queda: al autor no lo atrae ("no lo veo tan justificable, no me llama").

### Tema 25 — Decodificadores SNN → 🟢 REACTIVADO, con extensión propia identificada

- **Reformulación**: *implementación y evaluación comparativa de decodificadores convencionales y de impulsos sobre datos públicos*, con NeuroBench como **referente de contraste**.
- **La extensión propia concreta** (lo que NeuroBench NO hizo): NeuroBench evaluó sobre 6 sesiones de 2 primates (Indy/Loco). **FALCON aporta el protocolo multi-sesión y few-shot** — evaluar cómo se comportan ambos paradigmas **a través de sesiones** (robustez temporal, recalibración con pocos datos) es una dimensión que el benchmark de NeuroBench no cubre. Replicación declarada + extensión identificada = estructura honesta y estándar.
- Fortalezas: interés genuino del autor (único tema por el que preguntó repetidas veces); demo visual diseñada (tres trayectorias + contadores); materia prima verificada (FALCON, snnTorch, repo de Basilea, NeuroBench como herramienta).
- Debilidades: curva de aprendizaje (~1 mes); la justificación requiere el argumento fino (compromiso adentro/afuera, sin predicciones).

## El cuadro final

| Tema | Solidez del hueco | Ejecutabilidad 4 meses | Motivación del autor | Riesgo |
|---|---|---|---|---|
| 19 · Fidelidad | Media (replicación+extensión declarada) | Alta | **Baja** | Medio |
| 24 · LLM español | **Alta** (ausencia verificable) | **Máxima** | **Baja** | **Bajo** |
| 25 · SNN | Media (replicación+extensión FALCON) | Media-alta | **Alta** | Medio |
| 26 · QA de BCI (embrión) | A verificar | Alta (presunta) | ¿? | Bajo (presunto) |

**Lectura del cuadro**: en papel gana el 24; en motivación gana el 25 — y cuatro meses de tesis los sostiene la motivación, no el papel. El 26 queda como comodín a desarrollar solo si el autor muestra interés.

**La decisión sigue siendo del autor, y el instrumento sigue siendo el mismo**: la prueba de humo de 2 semanas del [[Roadmap-Tema-25]] — tres horas del primer sábado alcanzan para saber si el paradigma SNN engancha o no.

## Pendientes que quedan

- [ ] ⏳ Reintentar PUCE (Ing. en Sistemas) cuando el repositorio vuelva.
- [ ] ⏳ Texto completo de Uniandes (anti-bot).
- [ ] Verificar estado del código de OTTAA Project en GitHub (para el modelo "OSS existente" y el tema 26).
- [ ] Decisión del autor: prueba de humo del 25, o desarrollo del 26, o cerrar con 24/19.
