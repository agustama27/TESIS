# ¿Dónde debe correr el decodificador? — adentro vs afuera del implante

> Nota de investigación · 2026-08-14 · **verificación de la premisa del [[../30-TFG/Seleccion-Tema/Tema-25-Decodificadores-SNN-Neuromorficos|Tema 25]]**
> Origen: el autor cuestionó si "el futuro es decodificar todo adentro" es un hecho o una suposición. Respuesta: **es una suposición, y no hay que apoyarse en ella.**

## Veredicto en una frase

**No existe consenso de que el futuro sea "decodificar todo adentro".** Lo que existe es un **compromiso de diseño abierto** — cuánto cómputo poner adentro y cuánto afuera — que la literatura trata explícitamente como una decisión de arquitectura con dos caminos legítimos. La premisa correcta para la tesis no es predecir el futuro, sino **cuantificar una de las variables que determinan ese compromiso**.

---

## Evidencia A FAVOR de decodificar adentro

1. **Ya existe comercialmente, en otro dominio.** Los dispositivos de neuroestimulación en lazo cerrado **decodifican dentro del implante hoy, en pacientes reales, aprobados por la FDA**:
   - **NeuroPace RNS**: analiza continuamente la señal intracraneal y detecta crisis epilépticas con algoritmos embebidos (line length, área, half-wave) para estimular en respuesta.
   - **Medtronic Percept**: análisis espectral + clasificador lineal sobre 4 canales de sensado para estimulación adaptativa en Parkinson.
   > **Esto es clave**: prueba que decodificar dentro del implante no es ciencia ficción. Es realidad clínica — con algoritmos simples.
2. **Hay investigación específica de decodificadores en el implante**: un procesador de spikes de 96 canales a **6,3 nanovatios por canal** diseñado para decodificar intención de movimiento en el implante ([arXiv 2009.05210](https://arxiv.org/pdf/2009.05210)).
3. **Y hay trabajo específico con redes de impulsos para ese fin**: [Combining SNNs with Filtering for Efficient Neural Decoding in Implantable BMIs](https://arxiv.org/pdf/2312.15889) · [Architectural Exploration of Hybrid Neural Decoders for Neuromorphic Implantable BMI](https://arxiv.org/pdf/2505.05983).
4. **Motivación energética confirmada**: la literatura establece que **la transmisión de datos del implante a la prótesis es el consumidor dominante de energía**, y que integrar cómputo en el implante reduce esa demanda porque la salida del cómputo es mucho más chica que los datos crudos.

## Evidencia EN CONTRA (o de matiz) — esto es lo que faltaba

1. **La literatura describe DOS caminos vigentes, no uno.** Textual: *"Algunos sistemas BCI integran cómputo en el implante, reduciendo la demanda de comunicación inalámbrica... Por el contrario, otros sistemas integran el cómputo en el dispositivo vestible, asumiendo que reducir la comunicación inalámbrica todavía no es necesario y aprovechando las restricciones de potencia más relajadas de los vestibles."* → **Es un compromiso de diseño, no una dirección única.**
2. **El cómputo dentro del implante es hoy severamente limitado.** Los recursos de RNS y Percept **restringen el análisis a unas pocas características simples de la señal** — nada parecido a una red profunda. La brecha entre "decodificar simple" y "decodificar con IA moderna" adentro es enorme.
3. **Poca exploración académica**: *"Solo unos pocos estudios exploraron la decodificación en el chip para aplicaciones BCI"*, por la dificultad de procesar datos de alta dimensión con electrodos densos.
4. **La práctica real es HÍBRIDA, no binaria.** La tarea se reparte: parte adentro (detección de spikes, decodificación parcial) y parte afuera (el filtro de Kalman, el modelo grande). No es "todo adentro o todo afuera".
5. **Razones no energéticas para dejar el decodificador afuera** (y son fuertes):
   - **Actualización del modelo sin cirugía**: si el decodificador vive en el teléfono, se mejora con un update. Si vive en el implante, cambiar el modelo es un problema serio.
   - **Recalibración**: el drift neural exige reajustes frecuentes — más fácil afuera.
   - **Aprobación regulatoria**: un algoritmo embebido en un dispositivo implantado enfrenta un camino regulatorio mucho más pesado.
   - **Capacidad de cómputo**: un teléfono tiene órdenes de magnitud más potencia que cualquier chip implantable.

---

## 🔧 Reformulación de la premisa (esto es lo que hay que corregir)

### ❌ Premisa frágil (la que teníamos)

> "El futuro es decodificar todo dentro del implante; mi tesis evalúa la tecnología que lo habilita."

**Problema**: apuesta a una predicción. Si el campo va hacia decodificadores externos más potentes, la justificación se debilita.

### ✅ Premisa robusta (la correcta)

> "Cuánto cómputo poner dentro del implante y cuánto afuera es un **compromiso de diseño abierto**, y la literatura documenta ambos caminos. Ese compromiso se resuelve conociendo **cuánto cuesta computar adentro**. Mi tesis mide exactamente eso para un paradigma emergente: cuánta precisión de decodificación se obtiene por unidad de cómputo con redes de impulsos frente a redes convencionales."

**Por qué es robusta**: el resultado sirve **en los tres escenarios**.

| Escenario del futuro | ¿Sirve mi medición? |
|---|---|
| Se decodifica todo adentro | Sí — dice si el paradigma alcanza |
| Se sigue con esquema híbrido (lo actual) | Sí — un cómputo más barato permite hacer **más** adentro con el mismo presupuesto: mejor extracción de características, decodificación parcial más rica |
| El decodificador queda afuera, en un vestible | Sí — los vestibles también son dispositivos a batería; la eficiencia sigue importando |

> **Regla general para tesis**: nunca apoyes la justificación en una predicción sobre el futuro. Apoyala en **una pregunta abierta del presente**. Las predicciones envejecen mal; las mediciones no.

---

## Cómo responderlo si el tutor pregunta

> "No parto de que el futuro sea decodificar todo dentro del implante — de hecho, la literatura muestra dos caminos vigentes y la práctica actual es híbrida. Lo que sí está establecido es que la transmisión de datos es el mayor consumidor de energía del implante, y que por eso el procesamiento migra hacia adentro cuando el cómputo lo permite: los dispositivos de neuroestimulación en lazo cerrado, como el NeuroPace RNS, ya decodifican dentro del cuerpo, aunque con algoritmos muy simples. La pregunta abierta es cuánto se puede decodificar adentro con la energía disponible, y eso depende del costo del cómputo. Mi tesis mide ese costo para un paradigma emergente. El resultado es útil se resuelva el compromiso como se resuelva."

## Fuentes

- Compromiso adentro/afuera y reparto de tareas: [Architectural Exploration of Hybrid Neural Decoders for Neuromorphic Implantable BMI (arXiv 2505.05983)](https://arxiv.org/pdf/2505.05983)
- Decodificador de intención en el implante, 6,3 nW/canal: [arXiv 2009.05210](https://arxiv.org/pdf/2009.05210)
- SNN para decodificación en BMI implantables: [arXiv 2312.15889](https://arxiv.org/pdf/2312.15889)
- Límites de cómputo en dispositivos en lazo cerrado (RNS, Percept): [Closed-Loop Neural Prostheses with On-Chip Intelligence (arXiv 2109.05848)](https://arxiv.org/pdf/2109.05848) · [Cloud Computing for Seizure Detection in Implanted Neural Devices (PMC6711163)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6711163/) · [Responsive Neurostimulation Device (ScienceDirect Topics)](https://www.sciencedirect.com/topics/medicine-and-dentistry/responsive-neurostimulation-device)
- IA en el extremo del borde para señales neurales: [Machine-Learning-Powered Neural Interfaces (arXiv 2505.02516)](https://arxiv.org/pdf/2505.02516)

## Enlaces

[[../10-Fundamentos/Como-Funciona-un-Implante-Intracortical|Arquitectura del implante]] · [[../10-Fundamentos/Cadena-de-Senal-Neural|Cadena de señal]] · [[../30-TFG/Seleccion-Tema/Tema-25-Decodificadores-SNN-Neuromorficos|Tema 25]]
