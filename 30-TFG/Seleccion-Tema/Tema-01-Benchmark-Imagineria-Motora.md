# Tema 1 — Benchmark deep learning vs clásicos en imaginería motora

> Estado: 🟢 En reserva

## Definiciones Iniciales (formato oficial)

- **Tipo de TFG**: Trabajo de Investigación · **Línea**: Transformación Digital

### Título tentativo (~12 palabras)

Evaluación comparativa de redes profundas y métodos clásicos para clasificación de imaginería motora

### Justificación de la línea (3 renglones)

Las BCI de imaginería motora habilitan el control digital sin movimiento para personas con discapacidad motora. Evaluar qué clasificadores rinden mejor en hardware accesible es condición para que esa tecnología se adopte fuera del laboratorio.

### Explicación del tema (5-15 renglones)

La imaginería motora es el paradigma BCI donde el usuario imagina un movimiento y el sistema lo clasifica desde la señal EEG. La literatura reporta precisiones de modelos profundos (EEGNet) frente a pipelines clásicos (CSP+LDA/SVM), pero rara vez mide el costo computacional — el dato que define qué se puede desplegar en hardware accesible. Este trabajo compara ambas familias sobre los datasets públicos estándar (BCI Competition IV-2a, PhysioNet) con protocolo reproducible, midiendo precisión Y costo (tiempo de entrenamiento, inferencia, parámetros).

### Problema / pregunta (3-5 renglones)

¿Las arquitecturas profundas compactas superan significativamente a los métodos clásicos en imaginería motora, y a qué costo computacional? ¿Cuál es el mejor equilibrio precisión-recursos para sistemas BCI ejecutables en hardware de consumo?

### Revisión de literatura (4 trabajos, APA)

1. Lawhern, V. J., et al. (2018). EEGNet: A compact convolutional neural network for EEG-based brain-computer interfaces. *Journal of Neural Engineering*. https://doi.org/10.1088/1741-2552/aace8c
2. Survey de deep learning para clasificación EEG. *arXiv*. https://arxiv.org/abs/2310.02152
3. MOABB — Mother of All BCI Benchmarks (NeuroTechX). https://moabb.neurotechx.com
4. ⚠️ Tangermann, M., et al. (2012). Review of the BCI Competition IV — verificar DOI antes de presentar.

### Justificación del TFG (borrador)

El mercado BCI crece hacia los USD 6,5 mil millones en 2030 pero las decisiones de arquitectura de sistemas reales se toman sin datos de ingeniería: la literatura optimiza precisión ignorando recursos. Este trabajo produce esa evidencia con benchmarks reproducibles — ingeniería de software empírica sobre datasets públicos, sin riesgo logístico, con resultados comparables internacionalmente. *(Expandir a 15-20 renglones si se activa.)*

## Ampliación

Ficha completa con metodología por entregas y pitch: [[../../20-Investigacion/Temas-Candidatos-TFG|lista maestra]] (ficha 1) y deck interactivo.
