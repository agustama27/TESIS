# Temas candidatos para el TFG — BCI / NeuroIngeniería

> Investigación iniciada el 2026-08-12 · **Estado actualizado: 2026-08-14**
> Cada tema tiene su página de presentación en formato oficial en `30-TFG/Seleccion-Tema/` → [[../30-TFG/Seleccion-Tema/00-Indice|Índice]].

## ESTADO ACTUAL (2026-08-14) — rankings anteriores SUPERADOS

**🎯 EN FOCO — dos finalistas ELEGIDOS POR EL AUTOR (ejercicio de decisión, 2026-08-14):**
- **Tema 24: LLMs para comunicación asistida en español** (réplica de SpeakFaster/Nature Comms 2024, inexistente en español; stack diario del autor; sin hardware).
- **Tema 19: Fidelidad en la decodificación brain-to-text** (evolución del tema 17). Investigación de implementación: [[Fidelidad-Brain-to-Text]].
- 🧬 **Fusión posible** (ver Tema 24): construir la expansión en español Y auditar su fidelidad — un pipeline, las dos preguntas.
- Tema 23 (compresión) pasa a reserva alta con Word oficial ya generado.

**🟢 EN RESERVA** (elegibles si el foco cae): 1 (benchmark imaginería motora) · 2 (foundation models EEG) · 4 (transfer learning) · 7 (SDK BCI) · 10 (juego serio ACV) · 14 (tutor adaptativo) · 18 (neuroderechos) · **nuevos 2026-08-14, perfil Investigación+AI+SE**: **20 (drift/mantenimiento de decodificadores — MLOps neural, benchmark FALCON de NeurIPS)** · 21 (robustez adversarial) · 22 (datos sintéticos por difusión).

**❌ DESCARTADOS**:
- **3 · Speller P300** — decisión del usuario: "muy cliché, ya se ha realizado, no aportaría al CV".
- **16 · Compresión N1** — decisión del usuario: percibido como inviable ("si Neuralink no pudo…"); técnicamente era caracterización de frontera, pero sin convicción del autor no hay tesis.
- **17 · Brain-to-text benchmark (forma original)** — la pregunta "¿por qué los Transformers no ganan?" se está cerrando (evidencia 2025-26, ver [[Decodificacion-Brain-to-Text]]); **evolucionó al tema 19**.
- **11 · Validación Muse** — depende 100% de hardware importado.
- **5 · Neurofeedback / 9 · Domótica SSVEP / 13 · Teclado parpadeo** — dependencia de hardware sin equipo en mano.
- **6 · Somnolencia / 8 · Estrés / 12 · Emociones DEAP / 15 · Biometría** — dominados por opciones de mayor retorno con el mismo esfuerzo; sin interés del autor.

---

## Hallazgos de la investigación previa

**Repositorios locales relevados** (búsquedas indexadas, 2026-08-12):

- **Siglo 21** (`repositorio.uesiglo21.edu.ar`): no se encontraron tesis BCI/EEG indexadas. **Hay vacancia — tu tesis sería de las primeras del tema en la universidad.** Eso juega a favor en originalidad y en visibilidad (repositorio, Ciencia y Técnica, Open Lab).
- **UNC** (`rdu.unc.edu.ar`): sin tesis BCI de grado indexadas en las búsquedas; hay actividad en neurociencia/señales en FaMAF y FCEFyN pero no aparece BCI aplicado como TFG.
- **UTN** (`ria.utn.edu.ar`): aparece al menos un trabajo sobre señales EEG (bitstream indexado), sin explosión del tema.
- **Precedentes regionales de grado que demuestran factibilidad**: U. de Concepción (Chile) — BCI con Muse; Escuela Politécnica Nacional (Ecuador) — control IoT por parpadeos EEG para discapacidad motriz; PUCE (Ecuador) — procesamiento de señales encefalográficas. O sea: **esto se puede hacer como tesis de grado**, está probado.

**Restricciones duras de la universidad** (el tema DEBE cumplirlas):

- Tipo: **Prototipado Tecnológico** (prototipo del core + relevamiento + proceso de negocio) o **Trabajo de Investigación** (método científico, pregunta, hipótesis, datos).
- Línea temática (irreversible): **Transformación Digital** | **Plataformas de Desarrollo** | **Educación Digital**.
- 4 entregas en ~4 meses. El prototipo NO necesita estar 100% implementado.
- La presentación del tema exige: título ~12 palabras, justificación de línea (3 renglones), explicación (5-15), pregunta (3-5), **4 citas APA de fuentes confiables**, justificación (15-20 renglones).

**Criterio de factibilidad clave (Argentina, 4 meses)**: los temas basados en **datasets públicos** (BCI Competition IV, PhysioNet, DEAP, TUH) tienen riesgo logístico CERO. Los que requieren hardware EEG de consumo (Muse ~USD 250, OpenBCI ~USD 500-1000 + aduana) tienen riesgo de importación/tiempos. Cada ficha lo marca.

---

## Matriz resumen

| # | Tema | Tipo | Línea | Datos | Riesgo | CV posgrado/industria |
|---|------|------|-------|-------|--------|----------------------|
| 1 | Benchmark deep learning vs clásicos en imaginería motora | Investigación | TD | Público | 🟢 Bajo | ⭐⭐⭐⭐ |
| 2 | Foundation models de EEG: ¿sirven con pocos datos? | Investigación | TD | Público | 🟡 Medio | ⭐⭐⭐⭐⭐ |
| 3 | Speller P300 de bajo costo para comunicación asistiva | Prototipado | TD | Público + sim | 🟢 Bajo | ⭐⭐⭐⭐ |
| 4 | Transfer learning entre sujetos: calibración mínima | Investigación | TD | Público | 🟢 Bajo | ⭐⭐⭐⭐⭐ |
| 5 | Neurofeedback de atención para estudiantes | Prototipado | **ED** | Hardware | 🟡 Medio | ⭐⭐⭐⭐ |
| 6 | Detección de somnolencia del conductor con EEG | Prototipado | TD | Público | 🟢 Bajo | ⭐⭐⭐ |
| 7 | Framework/SDK abierto para pipelines BCI real-time | Prototipado | **PD** | Público | 🟡 Medio | ⭐⭐⭐⭐ |
| 8 | Detección de estrés/carga cognitiva (bienestar digital) | Investigación | TD | Público | 🟢 Bajo | ⭐⭐⭐ |
| 9 | Control domótico por SSVEP para movilidad reducida | Prototipado | TD | Sim + público | 🟡 Medio | ⭐⭐⭐ |
| 10 | Juego serio BCI para rehabilitación post-ACV | Prototipado | TD | Público + sim | 🟡 Medio | ⭐⭐⭐⭐ |
| 11 | Validación de EEG de consumo (Muse) para ERP/atención | Investigación | TD | Hardware | 🔴 Alto | ⭐⭐⭐⭐ |
| 12 | Reconocimiento de emociones: benchmark de arquitecturas | Investigación | TD | Público | 🟢 Bajo | ⭐⭐⭐ |
| 13 | Teclado virtual híbrido (parpadeo + atención) accesible | Prototipado | TD | Hardware/sim | 🟡 Medio | ⭐⭐⭐ |
| 14 | Tutor adaptativo que regula dificultad según carga cognitiva | Prototipado | **ED** | Público + sim | 🟡 Medio | ⭐⭐⭐⭐ |
| 15 | Autenticación biométrica con señales EEG | Investigación | TD | Público | 🟡 Medio | ⭐⭐⭐ |

TD = Transformación Digital · PD = Plataformas de Desarrollo · ED = Educación Digital

---

## Fichas detalladas

### 1 · Benchmark de deep learning vs métodos clásicos en imaginería motora

**Título tentativo**: "Evaluación comparativa de redes neuronales profundas y métodos clásicos para clasificación de imaginería motora en interfaces cerebro-computadora"

- **Tipo**: Trabajo de Investigación · **Línea**: Transformación Digital
- **Pregunta**: ¿Las arquitecturas profundas compactas (EEGNet) superan significativamente a los pipelines clásicos (CSP+LDA/SVM) en datasets públicos de imaginería motora, y a qué costo computacional?
- **Datos**: BCI Competition IV-2a, PhysioNet Motor Movement/Imagery — públicos, gratis, estándar del campo.
- **Pros**: riesgo logístico cero; metodología calcada del método científico (perfecta para el tipo Investigación); reproducible; te obliga a dominar TODO el pipeline BCI (el conocimiento más transferible del campo); resultados comparables con literatura internacional.
- **Contras**: sin demo "wow" para la defensa (gráficos y tablas, no un dispositivo); tema muy transitado a nivel mundial (la originalidad está en el análisis local: costo computacional, hardware accesible).
- **CV**: ⭐⭐⭐⭐ — es exactamente el tipo de trabajo que un comité de maestría en neuroingeniería/ML espera saber leer y hacer. Base perfecta para un paper corto.
- **Literatura ancla** (✅ = verificada hoy):
  - ✅ Lawhern et al. (2018). *EEGNet: a compact convolutional neural network for EEG-based brain–computer interfaces*. J. Neural Engineering. https://iopscience.iop.org/article/10.1088/1741-2552/aace8c
  - ✅ Survey GNN/DL para clasificación EEG (arXiv 2310.02152)
  - ⚠️ SIN VERIFICAR: Tangermann et al. (2012), review del BCI Competition IV — verificar DOI antes de usar.

### 2 · Foundation models de EEG: ¿sirven cuando hay pocos datos?

**Título tentativo**: "Modelos fundacionales de EEG frente a modelos entrenados desde cero en escenarios de datos limitados"

- **Tipo**: Trabajo de Investigación · **Línea**: Transformación Digital
- **Pregunta**: ¿El fine-tuning de un foundation model de EEG pre-entrenado (LaBraM, ~2.500 hs de EEG) supera a modelos entrenados desde cero cuando solo hay minutos de datos del usuario final?
- **Datos**: LaBraM es open source (ICLR 2024 spotlight, código en GitHub) + datasets públicos para fine-tuning.
- **Pros**: es LA frontera del campo (2024-2026) — la intersección exacta de tu perfil AI Engineer con BCI; casi nadie lo está haciendo como tesis de grado; máxima señal para posgrado; sin hardware.
- **Contras**: requiere GPU decente (Colab Pro alcanza); riesgo técnico de que el fine-tuning no converja fácil; literatura muy reciente (menos red de contención metodológica); necesitás sostenerlo vos en la defensa ante una CAE que quizás no conozca el tema.
- **CV**: ⭐⭐⭐⭐⭐ — "evalué foundation models de EEG en régimen de pocos datos" es una frase que abre puertas en cualquier lab de neurotecnología o entrevista de ML. Es lo más parecido a investigación de posgrado que podés hacer en el TFG.
- **Literatura ancla**:
  - ✅ Jiang et al. (2024). *Large Brain Model (LaBraM)*. ICLR 2024 spotlight. https://github.com/935963004/labram
  - ✅ *Are Large Brainwave Foundation Models Capable Yet? Insights from Fine-tuning* (arXiv 2507.01196)
  - ✅ *What Do EEG Foundation Models Capture from Human Brain Signals?* (arXiv 2605.11410)
  - ✅ Lawhern et al. (2018), EEGNet como baseline.

### 3 · Speller P300 de bajo costo para comunicación asistiva

**Título tentativo**: "Prototipo de comunicador P300 de bajo costo para personas con discapacidad motora severa"

- **Tipo**: Prototipado Tecnológico · **Línea**: Transformación Digital
- **Explicación**: sistema web que presenta la matriz clásica de letras parpadeantes; el usuario deletrea palabras atendiendo a la letra deseada y el sistema detecta el potencial P300. El core: presentación de estímulos + pipeline de detección + interfaz. Se desarrolla y valida con datasets públicos de P300; la demo en vivo puede ser simulada (reproducción de señal grabada) — el prototipo NO exige hardware.
- **Pros**: impacto social evidente (ELA, síndrome de enclaustramiento) → justificación fortísima; paradigma más robusto y documentado del campo; encaja perfecto en la estructura de Prototipado (organización modelada: centro de rehabilitación); demo visual para la defensa.
- **Contras**: tema clásico (la novedad va por el ángulo bajo costo + español + web); sin hardware real la validación en vivo queda como trabajo futuro.
- **CV**: ⭐⭐⭐⭐ — demuestra dominio de ERP + sistema completo end-to-end. Muy citable en el repositorio institucional.
- **Literatura ancla**:
  - ✅ Revisión sistemática de spellers P300 (ACM ICAAI 2024). https://dl.acm.org/doi/10.1145/3704137.3704196
  - ✅ Framework ensemble para Locked-In Syndrome (Scientific Reports, Nature). https://www.nature.com/articles/s41598-026-47041-4
  - ⚠️ SIN VERIFICAR: Farwell & Donchin (1988), paper fundacional del speller — verificar DOI (es real, pero confirmar referencia exacta).

### 4 · Transfer learning entre sujetos: hacia BCIs sin calibración

**Título tentativo**: "Estrategias de transferencia entre sujetos para reducir la calibración en interfaces cerebro-computadora"

- **Tipo**: Trabajo de Investigación · **Línea**: Transformación Digital
- **Pregunta**: ¿Cuánto se puede reducir el tiempo de calibración de una BCI de imaginería motora usando datos de otros sujetos (domain adaptation), manteniendo una precisión utilizable (>70%)?
- **Datos**: públicos (BCI Competition, PhysioNet, MOABB como framework de benchmark).
- **Pros**: problema REAL y abierto del campo (la no-estacionariedad entre sujetos es EL cuello de botella de las BCI prácticas); mapea 1:1 con conceptos ML que ya dominás (domain shift, few-shot); riesgo logístico cero; MOABB da benchmark reproducible listo.
- **Contras**: como el 1, sin demo física; requiere rigor estadístico (validación cruzada entre sujetos bien hecha).
- **CV**: ⭐⭐⭐⭐⭐ — transfer learning en EEG es tema de paper de maestría. Si sale bien, es publicable en Ciencia y Técnica sin esfuerzo extra.
- **Literatura ancla**:
  - ✅ EEGNet (Lawhern et al., 2018) — arquitectura base.
  - ✅ EEG-Reptile: meta-learning para BCIs (arXiv 2412.19725)
  - ⚠️ SIN VERIFICAR: Jayaram & Barachant (2018), MOABB (J. Neural Eng.) — verificar DOI.

### 5 · Neurofeedback de atención para estudiantes

**Título tentativo**: "Sistema de neurofeedback EEG para entrenamiento de la atención en estudiantes universitarios"

- **Tipo**: Prototipado Tecnológico · **Línea**: **Educación Digital** (encaje perfecto y natural)
- **Explicación**: aplicación que mide un índice de atención con EEG de consumo (banda theta/beta), lo muestra en tiempo real y gamifica sesiones de entrenamiento. Core: adquisición → índice de atención → feedback visual → registro de progreso.
- **Pros**: es EL tema BCI que mejor encaja en Educación Digital (la línea menos competida); literatura 2023-2025 activa y favorable; demo en vivo espectacular para la defensa; la universidad misma es la organización a modelar (relevamiento fácil).
- **Contras**: **requiere hardware** (Muse ~USD 250 + importación) — riesgo logístico real en Argentina; si además querés probarlo con estudiantes reales, necesitás consentimiento informado (sumale burocracia; para el TFG alcanza con demo sobre vos mismo).
- **CV**: ⭐⭐⭐⭐ — neurotecnología aplicada a educación es un nicho creciente (ed-tech + neuro). Diferenciador fuerte.
- **Literatura ancla**:
  - ✅ *Exploring Neural Evidence of Attention in Classroom Environments: A Scoping Review* (PMC12384261)
  - ✅ Estudio cuasi-experimental de neurofeedback en aulas reales (Research Square rs-9662086)
  - ✅ Krigolson et al. (2017). *Choosing MUSE: Validation of a Low-Cost, Portable EEG System for ERP Research*. Frontiers in Neuroscience. (PMC5344886)
  - ✅ Review de juegos de neurofeedback y habilidades cognitivas (ScienceDirect S0001691825007188)

### 6 · Detección de somnolencia del conductor con EEG

**Título tentativo**: "Sistema de detección temprana de somnolencia en conductores mediante señales EEG"

- **Tipo**: Prototipado Tecnológico · **Línea**: Transformación Digital
- **Explicación**: clasificador de estados de vigilia/somnolencia sobre EEG + alerta en tiempo real. Datasets públicos de fatiga al volante existen; el prototipo corre sobre señal reproducida.
- **Pros**: justificación social contundente (siniestralidad vial argentina); problema de clasificación bien definido; datasets públicos disponibles.
- **Contras**: la versión "real" necesitaría hardware wearable — queda como trabajo futuro; el aporte es más aplicación que ciencia.
- **CV**: ⭐⭐⭐ — sólido pero menos distintivo para posgrado; muy bueno para industria (safety-tech, automotive).
- **Literatura ancla**: ⚠️ SIN VERIFICAR — hay datasets y literatura de drowsiness detection (SEED-VIG y similares) pero no los verifiqué hoy; requiere pasada de bci-explorer antes de presentar.

### 7 · Framework/SDK abierto para prototipar pipelines BCI en tiempo real

**Título tentativo**: "Plataforma de desarrollo para prototipado rápido de interfaces cerebro-computadora en tiempo real"

- **Tipo**: Prototipado Tecnológico · **Línea**: **Plataformas de Desarrollo** (el ÚNICO tema natural en esta línea)
- **Explicación**: un SDK/framework (Python) que abstrae adquisición (BrainFlow/reproducción de datasets), filtrado, extracción de features, clasificación y salida de eventos — para que un desarrollador arme una BCI en pocas líneas. Core: arquitectura de streaming + plugins + ejemplo funcional (ej. speller P300 armado sobre el framework).
- **Pros**: es puro Software Engineering (tu fortaleza hoy) aplicado a BCI; encaja literal en la definición de la línea PD ("herramientas que acompañen nuevas metodologías de desarrollo"); open source = portfolio en GitHub con visibilidad internacional.
- **Contras**: competís mentalmente con MNE/BrainFlow/BCI2000 (tu defensa: capa de developer experience que hoy no existe unificada); riesgo de scope creep — hay que recortar el alcance con crueldad.
- **CV**: ⭐⭐⭐⭐ — para industria es oro (systems + neuro). Para maestría académica, algo menos directo que 2/4.
- **Literatura ancla**: ✅ Systematic review de headsets EEG low-cost (Frontiers in Neuroinformatics 2020); ⚠️ SIN VERIFICAR: papers de BCI2000 y BrainFlow/MNE como antecedentes — verificar antes de presentar.

### 8 · Detección de estrés y carga cognitiva con EEG

**Título tentativo**: "Clasificación de estrés y carga cognitiva mediante EEG y aprendizaje profundo"

- **Tipo**: Trabajo de Investigación · **Línea**: Transformación Digital
- **Pregunta**: ¿Qué arquitecturas y features detectan mejor estados de estrés/carga cognitiva en EEG, y son transferibles entre sujetos?
- **Datos**: DEAP y similares — públicos.
- **Pros**: bienestar digital/burnout es tema caliente; datasets maduros; sin hardware.
- **Contras**: DEAP es chico para deep learning (limitación metodológica conocida — hay que reconocerla); el "affective computing" tiene crítica metodológica fuerte (etiquetas subjetivas).
- **CV**: ⭐⭐⭐ — correcto, no distintivo.
- **Literatura ancla**:
  - ✅ *Deep Learning-Based EEG Emotion Recognition: A Review* (MDPI Brain Sciences 2026 / PMC12839272)
  - ✅ Review PRISMA 2020-2025, 233 artículos (PMC12825124)
  - ✅ Brain2Vec: CNN-LSTM-Attention para estrés (arXiv 2506.11179)

### 9 · Control domótico por SSVEP para personas con movilidad reducida

**Título tentativo**: "Prototipo de control domótico mediante potenciales evocados visuales para movilidad reducida"

- **Tipo**: Prototipado Tecnológico · **Línea**: Transformación Digital
- **Explicación**: panel de estímulos parpadeando a frecuencias distintas; mirar un estímulo dispara el comando (luz, ventilador, TV). SSVEP es el paradigma con mejor SNR y menos entrenamiento del usuario.
- **Pros**: SSVEP tiene precisiones >85% documentadas en domótica; demo llamativa; IoT + BCI = combinación vendible.
- **Contras**: la validación seria requiere EEG occipital real (los headsets de consumo frontal como Muse NO sirven bien para SSVEP — limitación técnica que hay que conocer); sin hardware queda en simulación.
- **CV**: ⭐⭐⭐ — buen proyecto de ingeniería, menos profundidad científica.
- **Literatura ancla**: ✅ SSVEP-BCI smart home (ResearchGate 317801658); ✅ SSVEP wheelchair (arXiv 2307.08703); ✅ drone multiclase con EEG de consumo (IJEEEMI).

### 10 · Juego serio controlado por BCI para rehabilitación post-ACV

**Título tentativo**: "Juego serio controlado por imaginería motora para apoyo a la neurorrehabilitación de miembro superior"

- **Tipo**: Prototipado Tecnológico · **Línea**: Transformación Digital
- **Explicación**: juego donde el avatar se mueve por imaginería motora del paciente; gamifica la terapia post-ACV. Evidencia clínica 2023-2025 respalda que MI-BCI mejora la recuperación del miembro superior. Core: clasificador MI (dataset público) + motor del juego + adaptación de dificultad.
- **Pros**: combinación salud + gaming + BCI con evidencia clínica REAL detrás (meta-análisis 2024-2025 favorables); organización modelada obvia (centro de neurorrehabilitación); emotivo y potente para la defensa.
- **Contras**: no vas a validar con pacientes reales (alcance: demo con dataset/usuario sano — hay que decirlo desde el día 1); dominio clínico exige leer más.
- **CV**: ⭐⭐⭐⭐ — salud digital + BCI es el área con más demanda laboral del campo.
- **Literatura ancla**:
  - ✅ *Brain-Computer Interfaces for Stroke Motor Rehabilitation* (MDPI Bioengineering 2025 / PMC12383906)
  - ✅ Meta-análisis MI vs motor attempt (J. Neurological Sciences 2025)
  - ✅ RCT de BCI-MI en hemiplejia (PMC10064693)

### 11 · Validación de EEG de consumo (Muse) para investigación de atención/ERP

**Título tentativo**: "Validación de un sistema EEG de consumo para medición de atención en contextos reales"

- **Tipo**: Trabajo de Investigación · **Línea**: Transformación Digital
- **Pregunta**: ¿Un headset de consumo (~USD 250) puede replicar hallazgos de atención/ERP obtenidos con equipos de laboratorio (~USD 20.000)?
- **Pros**: replicación = ciencia de la buena; Krigolson ya demostró que es viable (N200, P300 con Muse); democratización de la neurociencia como narrativa.
- **Contras**: **DEPENDE 100% del hardware** — si el Muse no llega por aduana, no hay tesis. Riesgo inaceptable con el calendario si no tenés ya el dispositivo. Solo elegible si conseguís el equipo YA.
- **CV**: ⭐⭐⭐⭐ — metodológicamente muy formativo.
- **Literatura ancla**: ✅ Krigolson et al. (2017), Frontiers in Neuroscience; ✅ systematic review de headsets low-cost (Frontiers in Neuroinformatics 2020).

### 12 · Reconocimiento de emociones en EEG: benchmark de arquitecturas

**Título tentativo**: "Evaluación comparativa de arquitecturas de aprendizaje profundo para reconocimiento de emociones en EEG"

- **Tipo**: Trabajo de Investigación · **Línea**: Transformación Digital
- **Pregunta**: ¿Qué familia de arquitecturas (CNN, RNN, Transformers, GNN) rinde mejor en DEAP bajo un protocolo de evaluación honesto (subject-independent)?
- **Pros**: datasets públicos; literatura abundante; ejercita todo tu stack ML.
- **Contras**: campo saturado de papers con evaluación dudosa (data leakage entre sujetos es epidémico — tu aporte puede ser justamente el protocolo limpio, pero es un aporte "negativo" difícil de vender a la CAE).
- **CV**: ⭐⭐⭐ — sólido, no distintivo.
- **Literatura ancla**: ✅ las mismas reviews del tema 8 (PMC12839272, PMC12825124, Frontiers 2023).

### 13 · Teclado virtual híbrido (parpadeo EEG + atención) para discapacidad motriz

**Título tentativo**: "Teclado virtual accesible controlado por señales electrofisiológicas para discapacidad motriz severa"

- **Tipo**: Prototipado Tecnológico · **Línea**: Transformación Digital
- **Explicación**: los artefactos de parpadeo (que todo el mundo filtra como ruido) se usan acá como SEÑAL de comando — precedente directo en la tesis de la EPN (Ecuador) para control IoT. Robusto y detectable incluso con hardware muy barato.
- **Pros**: técnicamente el más simple y robusto de los prototipos con hardware; precedente de grado regional documentado; costo mínimo.
- **Contras**: científicamente es el menos "neuro" (parpadeo es EMG/EOG más que EEG) — un evaluador exigente puede señalarlo; menos brillo para posgrado.
- **CV**: ⭐⭐⭐ — buen proyecto de accesibilidad, ciencia liviana.
- **Literatura ancla**: ✅ tesis EPN — BCI de parpadeos para IoT (bibdigital.epn.edu.ec/handle/15000/21787); ⚠️ complementar con literatura de hybrid BCI verificada.

### 14 · Tutor adaptativo que regula dificultad según carga cognitiva

**Título tentativo**: "Sistema de aprendizaje adaptativo basado en carga cognitiva estimada mediante EEG"

- **Tipo**: Prototipado Tecnológico · **Línea**: **Educación Digital**
- **Explicación**: plataforma de ejercicios que estima la carga cognitiva del estudiante (índices espectrales EEG) y adapta la dificultad en tiempo real — el sueño del aprendizaje personalizado llevado a fisiología. Core: estimador de carga + motor de adaptación + contenido demo.
- **Pros**: encaja en ED con un ángulo más novedoso que el neurofeedback clásico; intersección adaptive learning + neuro casi sin competencia local; puede desarrollarse con datasets públicos de workload y demo simulada.
- **Contras**: la estimación de carga cognitiva con EEG es menos robusta que P300/SSVEP (honestidad metodológica obligatoria); validación real requeriría estudio con estudiantes.
- **CV**: ⭐⭐⭐⭐ — ed-tech + neuroadaptive computing es nicho emergente con literatura creciente.
- **Literatura ancla**: ✅ Bibliometric systematic review de EEG en educación (arXiv 2509.26083); ✅ scoping review de atención en aulas (PMC12384261); ⚠️ verificar literatura específica de "neuroadaptive learning systems".

### 15 · Autenticación biométrica con señales EEG

**Título tentativo**: "Evaluación de señales EEG como factor de autenticación biométrica continua"

- **Tipo**: Trabajo de Investigación · **Línea**: Transformación Digital
- **Pregunta**: ¿Las respuestas cerebrales individuales (ERP ante estímulos conocidos) son suficientemente estables y únicas para autenticar usuarios?
- **Pros**: ciberseguridad + neuro = combinación llamativa y poco explotada; datasets públicos utilizables; conversación garantizada en la defensa.
- **Contras**: aplicación práctica lejana (nadie va a loguearse con un gorro EEG pronto) — la justificación de "beneficio" es más débil; literatura más chica.
- **CV**: ⭐⭐⭐ — curioso y diferenciador, pero nicho.
- **Literatura ancla**: ✅ *Enhancing User Authentication Through EEG Based P300 Speller Response* (Springer, 978-3-031-75543-9_10); ⚠️ ampliar con survey de EEG biometrics verificado.

---

## [SUPERADO — ver "ESTADO ACTUAL" arriba] Recomendación inicial (2026-08-12, histórico)

**🥇 Tema 2 — Foundation models de EEG** si tu prioridad es el posgrado/carrera en neuroingeniería. Es frontera 2024-2026, intersecta EXACTAMENTE tu perfil de AI Engineer, no depende de hardware, y te posiciona donde el campo va — no donde estuvo. Riesgo técnico real pero manejable (LaBraM open source + baseline EEGNet como red de seguridad: si el fine-tuning no converge, el benchmark comparativo YA es la tesis).

**🥈 Tema 4 — Transfer learning entre sujetos** como variante más segura del mismo espíritu: problema abierto real, cero hardware, benchmark reproducible con MOABB, y sigue siendo nivel-maestría para el CV.

**🥉 Tema 3 — Speller P300** si preferís el tipo Prototipado (demo visible, impacto social, estructura de entregas más guiada por la universidad). Es el clásico por una razón: funciona.

**Mención para Educación Digital**: si querés la línea menos competida en la universidad, el **Tema 5 (neurofeedback)** es el encaje más natural — pero su dependencia de hardware importado lo hace riesgoso con tu calendario. Solo si ya tenés (o conseguís YA) un Muse.

**Regla de descarte rápido**: con <4 meses y sin hardware en mano, descartá 11 (depende 100% del equipo) y bajá prioridad a 5, 9 y 13 (hardware o validación comprometida).

---

## Plantilla de presentación (formato del PDF oficial)

Cuando elijas, el documento `Apellido_Nombre - Tipo TFG.docx` debe contener:

1. **Datos**: nombre, DNI, legajo.
2. **Tipo de TFG**: Prototipado Tecnológico ▢ / Trabajo de Investigación ▢
3. **Línea temática**: Transformación Digital ▢ / Plataformas de Desarrollo ▢ / Educación Digital ▢
4. **Título tentativo** (~12 palabras) — cada ficha ya trae uno.
5. **Justificación de la línea elegida** (3 renglones).
6. **Explicación del tema** (5-15 renglones) — usar la sección "Explicación/Pregunta" de la ficha.
7. **Problema o pregunta de investigación** (3-5 renglones).
8. **Revisión de literatura**: **4 trabajos en APA** — usar SOLO las marcadas ✅; las ⚠️ requieren verificación de DOI antes de citar (regla del harness: ninguna cita sin fuente verificada).
9. **Justificación del TFG** (15-20 renglones): por qué importa, cómo se aborda, qué tecnologías (si es Prototipado).

**Siguiente paso al elegir**: correr `bci-explorer` sobre el tema elegido para armar las 4 citas APA completas y verificadas + redactar el documento juntos (yo verifico, vos firmás las ideas).

---

## Ampliación: encuadre justificado y metodología por tema (2026-08-12, 2ª pasada)

> Versión navegable completa en el deck interactivo (artifact). Resumen de encuadre + fases acá para portabilidad.
> Datasets adicionales verificados hoy: **SEED-VIG** (SJTU, 23 sujetos, PERCLOS), **STEW** (IEEE DataPort, DOI 10.21227/44r8-ya50, 48 sujetos), **MOABB** (148 datasets, NeuroTechX).

### Estructura común de los 4 meses

- **Prototipado**: E1 relevamiento + marco teórico + metodología (Scrum/UML) → E2 análisis y diseño + mockups SIN código → E3 seguridad, costos, riesgos, conclusión → E4 codificación del core + demo.
- **Investigación**: M1 marco teórico + hipótesis + diseño experimental → M2 pipeline y baselines → M3 experimento principal + estadística → M4 robustez + redacción final.

### Encuadre y metodología (síntesis)

1. **Benchmark DL vs clásicos (Investigación · TD)** — Por qué: respuesta validada estadísticamente, no sistema. Método: BCI IV-2a + PhysioNet; CSP+LDA/SVM vs EEGNet; Wilcoxon por sujeto; costo computacional. Stack: MNE, scikit-learn, PyTorch, MOABB.
2. **Foundation models EEG (Investigación · TD)** — Por qué: experimento controlado sobre adoptabilidad (calibración). Método: curvas de aprendizaje 1-100% de datos, LaBraM fine-tuned vs EEGNet desde cero. Stack: PyTorch, LaBraM, Colab Pro.
3. **Speller P300 (Prototipado · TD)** — Por qué: sistema con organización modelable (centro de rehabilitación) y proceso (sesión de comunicación). Método: E1 relevamiento → E2 UML + mockups matriz 6×6 → E3 seguridad datos biométricos → E4 front estimulador + detección P300 sobre dataset BNCI en replay. Stack: React, FastAPI, MNE, MOABB.
4. **Transfer learning entre sujetos (Investigación · TD)** — Por qué: pregunta cuantificable con protocolo LOSO estándar. Método: baselines → Riemannian alignment → fine-tuning EEGNet con fracciones crecientes; curvas de calibración. Stack: MOABB, pyRiemann, PyTorch.
5. **Neurofeedback atención (Prototipado · ED)** — Por qué: producto educativo, organización = la universidad; línea ED menos competida. Método: E1 relevamiento + COMPRAR MUSE YA → E2 arquitectura Muse→BrainFlow→índice→UI → E3 consentimiento/datos neurales → E4 core con feedback en vivo (N=1 declarado). Stack: BrainFlow, Muse 2, React/Electron.
6. **Somnolencia conductor (Prototipado · TD)** — Por qué: sistema para empresa de transporte modelada. Método: SEED-VIG con replay tiempo real, features espectrales → regresor vs PERCLOS, dashboard supervisor + alerta. Stack: MNE, FastAPI, React.
7. **Framework/SDK BCI (Prototipado · PD)** — Por qué: producto PARA desarrolladores — único encaje natural en PD. Método: API Source→Filter→Feature→Classifier→Sink, plugins, v1 = replay + 2 paradigmas + speller ejemplo + PyPI. Riesgo: scope creep. Stack: Python asyncio, BrainFlow adapter, GitHub Actions.
8. **Estrés/carga cognitiva (Investigación · TD)** — Por qué: comparación experimental pura. Método: STEW principal (workload 1-9), protocolo subject-independent declarado, PSD+SVM vs CNN-LSTM; el gap dependent/independent es el hallazgo. Stack: MNE, PyTorch.
9. **Domótica SSVEP (Prototipado · TD)** — Por qué: hogar asistido modelable. Método: estimulador web de frecuencias → CCA/FBCCA sobre dataset SSVEP en replay → MQTT a Home Assistant simulado. Limitación: Muse frontal NO sirve para SSVEP. Stack: MNE/NumPy, MQTT.
10. **Juego serio post-ACV (Prototipado · TD)** — Por qué: centro de neurorrehabilitación modelable, evidencia clínica 2024-25 real. Método: clasificador MI (BCI IV-2a replay) → juego (Phaser/Godot) via WebSocket → panel kinesiólogo. Alcance declarado: sin pacientes reales. Stack: Python, Phaser/Godot.
11. **Validación Muse (Investigación · TD)** — Por qué: replicación experimental con datos propios (oddball, N 10-15). SOLO con hardware en mano — descartado por calendario. Stack: PsychoPy, BrainFlow, MNE.
12. **Emociones DEAP (Investigación · TD)** — Por qué: benchmark metodológico contra el data leakage del campo. Método: splits subject-independent públicos, spectral+SVM vs CNN/LSTM/Transformer. Stack: MNE, PyTorch.
13. **Teclado parpadeo (Prototipado · TD)** — Por qué: asistivo de costo mínimo con precedente EPN. Método: detector de parpadeo voluntario (umbral+duración) + teclado por barrido web; métrica palabras/minuto. Stack: Python, JS.
14. **Tutor adaptativo por carga (Prototipado · ED)** — Por qué: cierra el loop pedagógico (contenido se adapta a fisiología); ED sin hardware. Método: estimador workload sobre STEW → replay como estudiante simulado → motor de adaptación + banco de ejercicios → panel docente. Stack: MNE+sklearn, React, FastAPI.
15. **Biometría EEG (Investigación · TD)** — Por qué: evaluación FAR/FRR/EER de estabilidad y unicidad de ERP. Método: verificación 1:1, estabilidad multi-sesión como hallazgo central. Stack: MNE, sklearn.

---

## Ampliación 2: pitch al tutor (2026-08-12, 3ª pasada)

Cada ficha del deck ahora incluye la sección **"Pitch al tutor"**: problema con cifras, por qué ahora, dónde está la Ingeniería en Software, y objeción probable con respuesta.

### El argumento madre (aplica a los 15 temas)

**"¿Y esto qué tiene que ver con Ingeniería en Software?"** — Una BCI es un sistema de software intensivo: pipeline de adquisición streaming, procesamiento con presupuesto de latencia, ML en línea, arquitectura event-driven, UX de accesibilidad extrema y atributos de calidad duros (tiempo real, confiabilidad, seguridad de datos biométricos). **La neurociencia es el dominio; la Ingeniería en Software es la disciplina** — como fintech no es economía ni salud digital es medicina. Al mercado BCI (USD 3,4 → 6,5 mil millones 2025→2030, Grand View Research) no le faltan neurocientíficos: le faltan ingenieros de software.

### Cifras verificadas para justificaciones (2026-08-12)

- **Mercado BCI**: USD ~3,44 mil millones (2025) → 6,52 mil millones (2030), CAGR 18,15% — Grand View Research.
- **Somnolencia al volante**: 17,6% de choques fatales involucran conductor somnoliento (AAA Foundation 2017-2021, ~30.000 muertes/5 años); costo social USD 109 mil millones/año (NHTSA).
- **ACV**: 12,2 millones/año en el mundo (World Stroke Organization); hasta 80% de sobrevivientes con déficit de miembro superior; persiste a 6 meses en 30-66%.
- **Síndrome de enclaustramiento**: 80% de supervivencia a 10 años con buen cuidado (Neurology 2023); 62% usa tecnología asistiva — décadas de vida con necesidad de comunicación.
- **Calibración BCI**: ~20-30 min por usuario/sesión — el bloqueo #1 de productización (motiva temas 2 y 4).

---

## Ampliación 3: bloque Neuralink — temas 16-18 (2026-08-14)

A pedido del usuario se investigó qué es factible como tesis de Ingeniería en Software en relación a los avances de Neuralink y BCI invasiva. Hallazgo central: **la frontera invasiva es accesible con datos públicos** — sin hardware ni quirófano.

### 16 · Compresión de telemetría neural (Neuralink Compression Challenge) — Investigación · TD · 🟢 · ⭐⭐⭐⭐⭐

- **Verificado**: Neuralink publicó 1 hora de grabaciones crudas del implante N1 (corteza motora de primate) en content.neuralink.com/compression-challenge. Reto: compresión lossless 200x, <1 ms, <10 mW. El N1 genera ~200 Mbps y transmite ~1 Mbps. Estado del arte: zip ≈ 2,2x — problema ABIERTO.
- **Tesis**: caracterizar la frontera ratio-latencia-potencia con predictores adaptativos, codificación entrópica (rANS) y variantes aprendidas. Un resultado negativo bien argumentado (por qué 200x choca con la entropía de la señal) ES aporte.
- **SE**: algoritmia, sistemas de bajo nivel, benchmarking — ingeniería de performance. Stack: C/C++/Rust + Python.
- **CV**: "trabajé con datos reales del implante N1" — la línea más distintiva posible apuntando a neurotech.

### 17 · Decodificación brain-to-text sobre datos intracorticales públicos — Investigación · TD · 🟡 · ⭐⭐⭐⭐⭐

- **Verificado**: datasets de Stanford públicos en Dryad — handwriting BCI (Willett 2021, 192 electrodos, ~90 caracteres/min) y speech neuroprosthesis (Willett 2023, doi:10.5061/dryad.x69p8czpq). Benchmark internacional activo: Brain-to-Text '24.
- **Tesis**: reproducir el baseline RNN, comparar arquitecturas (GRU vs Transformer) y ablacionar el aporte del language model. Métricas CER/WER comparables internacionalmente.
- **SE**: ML de secuencias + integración con LMs + evaluación rigurosa + latencia de inferencia. Es el problema EXACTO del equipo de decodificación de Neuralink.
- **Objeción resuelta**: los datos ya existen y son públicos — el trabajo es 100% computacional (los cirujanos implantan; los ingenieros de software decodifican).

### 18 · Seguridad y neuroderechos: threat modeling para sistemas BCI — Prototipado · TD · 🟢 · ⭐⭐⭐⭐

- **Verificado**: Chile = primer país con neuroderechos constitucionales (2021); fallo de Corte Suprema 2023 contra empresa BCI estadounidense real (PMC10929545); Neuroprotection Bill 2023 trata neurodatos como tejido orgánico; UNESCO debatiendo marco global. Argentina: vacío legal — oportunidad.
- **Tesis (prototipo)**: herramienta de threat modeling específica de BCI — catálogo de amenazas de neurodatos (inferencia de salud, replay, manipulación de estímulos), mapeo amenaza→control→neuroderecho, generador de reportes. Caso de estudio: la arquitectura del dispositivo del fallo chileno.
- **SE**: threat modeling, privacy-by-design, compliance tooling — seguridad informática, área núcleo de la carrera. ÚNICO tema sin datos ni GPU ni hardware: riesgo técnico mínimo absoluto.

**Actualización del ranking**: para el objetivo declarado "trabajar en Neuralink o similar", los temas 16 y 17 compiten de igual a igual con el 🥇 (tema 2). El 16 si te tira el software de sistemas/bajo nivel; el 17 si te tira el ML de secuencias. El 18 es el outsider de máxima factibilidad.

---

## [SUPERADO — ver "ESTADO ACTUAL" arriba] Ranking Top 5 (2026-08-14, histórico)

Criterio: impacto en CV para maestría/neurotech (peso máximo) · factibilidad 4 meses sin hardware · encaje con perfil AI Engineer · encuadre institucional limpio. Los cinco son cero-hardware con datasets públicos.

1. **🥇 Tema 17 — Decodificación brain-to-text** (Investigación · TD): el problema exacto de Neuralink con datasets públicos de Stanford y benchmark internacional. Encaje milimétrico con el perfil AI Engineer.
2. **🥈 Tema 2 — Foundation models de EEG** (Investigación · TD): frontera no invasiva, red de seguridad por diseño (benchmark vs EEGNet ya es tesis).
3. **🥉 Tema 16 — Compresión de telemetría neural N1** (Investigación · TD): el CV más distintivo; tercero solo porque exige perfil de sistemas (C/C++/Rust).
4. **Tema 4 — Transfer learning entre sujetos** (Investigación · TD): la opción más segura sin resignar nivel de posgrado.
5. **Tema 3 — Speller P300** (Prototipado · TD): el mejor Prototipado; demo visible e impacto social.

**Desempate por perfil**: ML de secuencias → 17 · EEG frontera con seguridad → 2 · sistemas/performance → 16 · mínimo riesgo → 4 · construir > experimentar → 3.
**Menciones fuera del top**: 18 (neuroseguridad, máxima factibilidad) y 14 (mejor Educación Digital sin hardware).
