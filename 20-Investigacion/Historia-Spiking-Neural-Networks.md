# Spiking Neural Networks — historia, aplicaciones y antecedentes en neuroingeniería

> Nota de investigación · 2026-08-14 · contexto para el [[../30-TFG/Seleccion-Tema/Tema-25-Decodificadores-SNN-Neuromorficos|Tema 25]]
> Todas las fuentes verificadas salvo las marcadas ⚠️.

## Síntesis

Las redes de impulsos (SNN) no son una moda reciente: son una línea de investigación de **casi 30 años** como paradigma formal, apoyada en neurociencia de los años 50 y en una industria de hardware que arrancó en los 80. Su momento comercial llegó con los chips neuromórficos (IBM 2014, Intel 2017-2024) y con las cámaras de eventos. **En neuroingeniería y BCI hay antecedentes claros y muy recientes (2024-2026), pero pocos y sin consolidación**: es un campo abierto con herramientas maduras — la posición ideal para un TFG.

---

## Línea de tiempo

### Los cimientos (1950s-1990s)

- **1952 — Hodgkin y Huxley** describen matemáticamente cómo una neurona real genera un impulso eléctrico (les valió el Nobel). Es la base biofísica de todo lo que vino después. ⚠️ *Completar cita APA exacta antes de usar en el TFG.*
- **1980s — Carver Mead** (Caltech) advierte que los sistemas nerviosos biológicos superan a las computadoras digitales en eficiencia, y empieza a construir circuitos analógicos VLSI que imitan neuronas. **En 1990 acuña el término "neuromorphic"** ([Wikipedia: Neuromorphic computing](https://en.wikipedia.org/wiki/Neuromorphic_computing); [SPIE, 2024](https://spie.org/news/photonics-focus/septoct-2024/inventing-the-integrated-circuit)). Nace la ingeniería neuromórfica: hardware inspirado en el cerebro.
- **1997 — Wolfgang Maass** publica *Networks of spiking neurons: The third generation of neural network models* (*Neural Networks*, 10(9), 1659-1671). **Este es el paper fundacional del campo**: formaliza las SNN como la "tercera generación" de redes neuronales y demuestra su potencia computacional.

**Las tres generaciones, para contarlo simple:**

| Generación | Qué son | Época |
|---|---|---|
| 1ª | Perceptrón: neuronas de umbral, salida binaria | 1950s-60s |
| 2ª | Redes con activaciones continuas y backpropagation — **las de hoy** (CNN, RNN, Transformers) | 1980s-presente |
| 3ª | **SNN**: neuronas que disparan impulsos discretos en el tiempo | 1997-presente |

Ojo con el matiz: la 3ª generación no reemplazó a la 2ª. Convive con ella y compite en el nicho donde la energía manda.

### El hardware que las hizo viables (2014-2024)

- **2014 — IBM TrueNorth**: chip digital neuromórfico con más de 1 millón de neuronas y 256 millones de sinapsis.
- **2017 — Intel Loihi** (septiembre): el chip que popularizó la investigación neuromórfica accesible.
- **2021 — Intel Loihi 2**: 1 millón de neuronas (7,8× la primera generación), 120 millones de sinapsis.
- **2024 — Intel Hala Point**: el primer sistema a gran escala basado en Loihi 2.
- **SpiNNaker** (Universidad de Manchester): arquitectura masivamente paralela para simular redes de impulsos, otra línea paralela.

Fuentes: [Open Neuromorphic — Loihi](https://open-neuromorphic.org/neuromorphic-computing/hardware/loihi-intel/) · [IBM — What is neuromorphic computing](https://www.ibm.com/think/topics/neuromorphic-computing) · [Conscium — Major neuromorphic projects](https://conscium.com/explainers/major-neuromorphic-computing-projects/)

---

## ¿Dónde se aplican HOY? (fuera de BCI)

El patrón es constante: **donde la energía, la latencia o los eventos asincrónicos importan más que la precisión bruta.**

**1. Visión por eventos (la aplicación estrella).** Las *cámaras de eventos* no sacan fotos completas 30 veces por segundo: cada píxel avisa solo cuando cambia la luz — igual que la retina. Salida asincrónica, natural para una SNN.
- Drones esquivando obstáculos con baja latencia y bajo consumo.
- Autos autónomos detectando vehículos en condiciones adversas (alto rango dinámico).
- Análisis de expresiones humanas con granularidad de microsegundos.
- Conteo de objetos a alta velocidad, detección de defectos, medición de vibraciones, estimación de tiempo-al-contacto para aterrizaje de naves.
- Programa **FAST** de DARPA dedicado a cámaras neuromórficas.
Fuentes: [Survey VSLAM con cámaras de eventos (MDPI Biomimetics, 2024)](https://www.mdpi.com/2313-7673/9/7/444) · [Review de sensores de visión neuromórfica (PMC12526923)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12526923/) · [DARPA FAST](https://www.darpa.mil/research/programs/fast-event-based-neuromorphic-camera-and-electronics)

**2. Audio y video de bajo consumo en Loihi 2** — procesamiento eficiente en el borde ([arXiv 2310.03251](https://arxiv.org/pdf/2310.03251)).

**3. Espacio y satélites**: cómputo con presupuesto energético crítico en órbita baja ([arkspace](https://arkspace.me/blog/neuromorphic-computing-in-space/)) y evaluación para radiotelescopios ([arXiv 2601.07130](https://arxiv.org/pdf/2601.07130)).

**4. Frontera reciente: LLMs con principios neuromórficos** en Loihi 2 ([arXiv 2503.18002](https://arxiv.org/pdf/2503.18002)) — el cruce entre tu mundo actual y este.

---

## ¿Hay antecedentes en neuroingeniería y BCI? SÍ — y son recientes

Esta es la pregunta que decide el encuadre de la tesis. La respuesta honesta: **existen, son de 2024-2026, y todavía no están consolidados.**

| Antecedente | Qué hizo | Referencia |
|---|---|---|
| **RSNN para velocidad de dedos** | Decodifica cinemática de la mano desde trenes de spikes corticales; publica `bigRSNN` (rendimiento) y `tinyRSNN` (eficiencia). **Código público.** | [github.com/fmi-basel/neural-decoding-RSNN](https://github.com/fmi-basel/neural-decoding-RSNN) |
| **SNN podadas para decodificación intracortical** | Poda adaptativa para eficiencia energética en decodificación intracortical | [arXiv 2504.11568](https://arxiv.org/abs/2504.11568) |
| **Framework causal y eficiente** | Decodificación neural escalable con SNN | [arXiv 2510.20683](https://arxiv.org/abs/2510.20683) |
| **SNN de fusión multiescala para BCI invasiva** | Decodificación de señal neural invasiva | [Frontiers in Neuroscience, 2025](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2025.1551656/full) |
| **Acumuladores Hebbianos de doble escala** | Decodificación SNN *online* en BMI intracorticales | [arXiv 2509.14447](https://arxiv.org/pdf/2509.14447) |
| **SNN + aprendizaje continuo** | Interfaces auto-adaptativas | [arXiv 2511.22108](https://www.arxiv.org/pdf/2511.22108) |
| **SNN sobre EEG en Loihi** | Implementación PyTorch + hardware neuromórfico para decodificar EEG | [github.com/combra-lab/snn-eeg](https://github.com/combra-lab/snn-eeg) |
| **NeuroBench** | Framework de benchmarking neuromórfico con conteo estandarizado de operaciones | [Nature Communications, 2025](https://www.nature.com/articles/s41467-025-56739-4) |

### Qué significa esto para la tesis (lectura honesta)

**Lo bueno**: no arrancás en el desierto. Hay código público del problema exacto, un framework de medición publicado en *Nature Communications*, y papers recientes que legitiman la línea ante cualquier tribunal.

**El desafío**: como hay antecedentes, la originalidad **no puede ser** "aplicar SNN a decodificación neural" — eso ya se hizo. Tiene que ser un hueco preciso. Candidatos plausibles (a confirmar en el mapeo del Mes 1):

- **Comparación limpia y unificada**: cada paper usa su dataset, su métrica y su protocolo. Una evaluación reproducible SNN-vs-convencional sobre el mismo benchmark público (FALCON) con NeuroBench como medidor estandarizado es exactamente el tipo de trabajo consolidador que un campo joven necesita — y que nadie hizo.
- **Condiciones no barridas**: robustez entre sesiones (drift), tamaño de datos, latencia bajo restricción de tiempo real.
- **El costo real del ahorro**: cuantificar el trade-off precisión-vs-operaciones como frontera, no como punto único.

Regla: **llegar a un campo con herramientas maduras y huecos identificables es la mejor posición posible para un TFG.** Lo riesgoso hubiera sido lo contrario — campo vacío, sin código, sin métricas.

---

## Para explicarlo en la reunión (30 segundos)

> "Las redes de impulsos no son una novedad de moda: son la 'tercera generación' de redes neuronales, formalizada por Maass en 1997, sobre hardware que Carver Mead empezó a construir en los 80. Hoy se usan comercialmente donde la energía manda: cámaras de eventos en drones y autos, procesamiento en satélites, chips como el Loihi de Intel. En interfaces cerebro-computadora los antecedentes son de 2024-2026: existen, hay código público y hasta un framework de medición en Nature Communications — pero cada trabajo usa su propio protocolo. Mi tesis aporta la comparación unificada y reproducible que el campo todavía no tiene."

## Enlaces

[[../30-TFG/Seleccion-Tema/Tema-25-Decodificadores-SNN-Neuromorficos|Tema 25]] · [[../30-TFG/Seleccion-Tema/Roadmap-Tema-25|Roadmap del Tema 25]] · [[Decodificacion-Brain-to-Text]] · [[Temas-Candidatos-TFG]]
