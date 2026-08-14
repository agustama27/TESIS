# Tema 20 — Drift y mantenimiento de decodificadores neuronales (MLOps neural)

> Estado: 🟢 En reserva ALTA — agregado 2026-08-14 tras validación. Encaje fuerte con perfil AI engineering + SE.

## Definiciones Iniciales (formato oficial)

- **Tipo de TFG**: Trabajo de Investigación · **Línea**: Transformación Digital

### Título tentativo (~12 palabras)

Degradación temporal y estrategias de recalibración en decodificadores neuronales: un estudio de mantenimiento

### Justificación de la línea (3 renglones)

Una BCI que exige recalibración diaria por un técnico no es un producto adoptable. Resolver el mantenimiento del modelo — que siga funcionando mientras el cerebro y los sensores cambian — es la condición operativa de la transformación digital que estas tecnologías prometen.

### Explicación del tema (5-15 renglones)

Los decodificadores neuronales se degradan con el tiempo: la señal cambia entre sesiones y días (movimiento de electrodos, plasticidad neuronal, fisiología), rompiendo la relación que el modelo aprendió — el caso más extremo de *concept drift* que existe en ML. Los sistemas actuales lo resuelven con recalibración diaria supervisada, inviable para uso real. Existe un benchmark público dedicado (FALCON, NeurIPS 2024) con datos multi-sesión para evaluar exactamente esto. Este trabajo cuantifica la degradación de decodificadores estándar a lo largo de sesiones y compara estrategias de recalibración (reentrenamiento completo, fine-tuning con pocos datos, métodos no supervisados) midiendo el trade-off precisión-vs-costo de mantenimiento — la pregunta central de MLOps aplicada al modelo que lee un cerebro.

### Problema / pregunta (3-5 renglones)

¿Cuánto y cómo se degrada un decodificador neuronal entre sesiones, y qué estrategia de recalibración recupera más rendimiento por unidad de datos y cómputo? ¿Puede formularse el mantenimiento de estos modelos con las herramientas estándar de MLOps (detección de drift, continuous training)?

### Revisión de literatura (4 trabajos, APA)

1. *Few-shot Algorithms for Consistent Neural Decoding (FALCON) Benchmark*. (2024). *NeurIPS Datasets and Benchmarks Track*. https://proceedings.neurips.cc/paper_files/paper/2024/file/8c2e6bb15be1894b8fb4e0f9bcad1739-Paper-Datasets_and_Benchmarks_Track.pdf
2. *Measuring instability in chronic human intracortical neural recordings towards stable, long-term brain-computer interfaces*. (2024). *Communications Biology*. https://www.nature.com/articles/s42003-024-06784-4
3. *Long-term unsupervised recalibration of cursor-based intracortical BCIs using a hidden Markov model*. (2025). *Nature Biomedical Engineering*. https://www.nature.com/articles/s41551-025-01536-z
4. Sculley, D., et al. (2015). Hidden technical debt in machine learning systems. *NeurIPS 28*. https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems

### Justificación del TFG (borrador)

El drift neural es el "changing external world" de Sculley en su versión más pura, con un benchmark público (FALCON) que lo vuelve medible sin hardware. El trabajo une la literatura BCI con el marco MLOps/SE4AI: detección de drift, políticas de reentrenamiento, costo de mantenimiento como atributo de calidad. Resultado útil en ambas direcciones: una guía cuantitativa de recalibración para el campo BCI y un caso de estudio extremo para la comunidad MLOps. *(Expandir a 15-20 renglones si se activa.)*

## Ampliación

Sinergia con [[Tema-19-Fidelidad-Brain-to-Text|tema 19]]: mismos pipelines, otra dimensión de confiabilidad (temporal en vez de composicional). Ambos son "auditoría de sistemas ML sobre datos neurales públicos".
