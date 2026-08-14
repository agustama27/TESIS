# Tema 25 — Decodificadores neuromórficos: redes de impulsos vs redes convencionales

> Estado: 🎯 **EN FOCO** (tercer finalista, junto a [[Tema-24-LLM-Comunicacion-Asistida-Espanol|24]] y [[Tema-19-Fidelidad-Brain-to-Text|19]]) · agregado 2026-08-14 a pedido del autor.

## La idea en palabras simples

Las redes neuronales comunes calculan con números continuos, todas las neuronas todo el tiempo — por eso gastan tanta energía. Las neuronas del cerebro no: están en silencio y solo disparan un impulso cuando algo importa; por eso el cerebro entero funciona con lo que consume una lamparita. Las **redes de impulsos (SNN)** copian ese truco, y son la gran apuesta para que el decodificador corra DENTRO de un implante (presupuesto de milivatios: un chip en el cráneo no puede calentar el tejido). Elegancia extra: la señal que graban los electrodos **ya son impulsos** — la SNN la procesa en su formato nativo. **Tu tesis: comparar con rigor decodificadores SNN contra los convencionales sobre los datasets públicos, midiendo precisión Y costo computacional (el proxy estándar de energía). La tabla del trade-off es la tesis.**

## Definiciones Iniciales (formato oficial)

- **Tipo de TFG**: ☑ Trabajo de Investigación
- **Línea Temática**: ☑ Transformación Digital

### Título tentativo (~12 palabras)

Evaluación de redes neuronales de impulsos como decodificadores neuronales eficientes en energía

### Justificación de la Línea Temática elegida (3 renglones)

Los implantes neurales solo escalarán a productos cotidianos cuando su software de decodificación pueda ejecutarse con consumo mínimo dentro del dispositivo. Evaluar el paradigma de cómputo que promete esa eficiencia es evaluar la viabilidad energética de la transformación digital neurotecnológica.

### Explicación del tema (5-15 renglones)

Los decodificadores neuronales actuales usan redes convencionales que computan con valores continuos y consumo elevado — aceptable en una workstation, inviable dentro de un implante cuyo presupuesto es de milivatios. Las redes neuronales de impulsos (SNN) computan como las neuronas biológicas: unidades que permanecen en silencio y disparan impulsos discretos solo ante actividad relevante, con un costo por operación muy inferior (sumas en lugar de multiplicaciones). La literatura 2024-2025 muestra trabajo activo en SNNs para decodificación intracortical, pero sin una comparación sistemática y reproducible contra los decodificadores convencionales sobre los benchmarks públicos del campo. Este trabajo la produce: entrena decodificadores convencionales (referencia) y SNNs (mediante frameworks abiertos sobre PyTorch con gradiente sustituto) sobre los mismos datasets públicos de movimiento (FALCON, Neural Latents Benchmark), y mide en cada caso la precisión de decodificación, el número de operaciones de cómputo — el proxy de energía estándar en la literatura — y la latencia. La señal intracortical ya está compuesta de impulsos, por lo que las SNN la procesan en formato nativo. El resultado es el mapa del trade-off precisión-energía entre ambos paradigmas de software.

### Problema / pregunta de investigación (3-5 renglones)

¿Pueden los decodificadores basados en redes de impulsos igualar la precisión de los decodificadores convencionales sobre señal intracortical pública, y con qué reducción de operaciones de cómputo lo logran? ¿En qué condiciones (tarea, cantidad de datos, arquitectura) el paradigma neuromórfico resulta preferible como software de decodificación?

### Revisión de literatura principal (4 trabajos, APA)

1. *Few-shot Algorithms for Consistent Neural Decoding (FALCON) Benchmark*. (2024). *NeurIPS Datasets and Benchmarks Track*. https://proceedings.neurips.cc/paper_files/paper/2024/file/8c2e6bb15be1894b8fb4e0f9bcad1739-Paper-Datasets_and_Benchmarks_Track.pdf
2. *Adaptively Pruned Spiking Neural Networks for Energy-Efficient Intracortical Neural Decoding*. (2025). *arXiv*. https://arxiv.org/abs/2504.11568
3. *A Scalable, Causal, and Energy Efficient Framework for Neural Decoding with Spiking Neural Networks*. (2025). *arXiv*. https://arxiv.org/abs/2510.20683
4. *Multiscale fusion enhanced spiking neural network for invasive BCI neural signal decoding*. (2025). *Frontiers in Neuroscience*. https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2025.1551656/full

### Justificación del Trabajo Final de Graduación (borrador — expandir al confirmar)

El consumo energético del software es hoy un atributo de calidad de primera clase (green software engineering), y en ningún dominio es tan crítico como dentro de un implante cerebral, donde el calor disipado tiene límite fisiológico. Las SNN prometen resolver exactamente eso, pero la evidencia comparativa contra los decodificadores convencionales está fragmentada: cada paper usa datasets y protocolos propios. Este trabajo aporta la comparación limpia que falta, con protocolo reproducible sobre benchmarks públicos, métricas declaradas (precisión, operaciones de cómputo, latencia) y diseño informativo en cualquier dirección: si las SNN igualan precisión con una fracción del cómputo, se aporta evidencia de viabilidad para el despliegue en implante; si pierden precisión, se cuantifica por primera vez el costo real del paradigma en este dominio. El abordaje es íntegramente de ingeniería de software: evaluación empírica de dos paradigmas de software para el mismo problema, con la energía como requisito no funcional cuantificado. Sin hardware especializado: entrenamiento en GPU estándar (frameworks abiertos sobre PyTorch) y energía estimada por conteo de operaciones, el método aceptado por la literatura. *(Expandir a 15-20 renglones al confirmar.)*

## Alcance — qué SÍ y qué NO (declarado)

**Incluye**: datasets públicos de movimiento (FALCON / NLB); decodificador convencional de referencia (GRU/Kalman) vs 1-2 arquitecturas SNN (snnTorch/SpikingJelly, gradiente sustituto); métricas precisión + operaciones sinápticas + latencia; análisis del trade-off.
**Excluye**: chips neuromórficos físicos (Loihi) — energía estimada, no medida con instrumentos; implantes reales; tiempo real estricto; segunda tarea solo si sobra tiempo.

## Plan de 4 meses

| Mes | Trabajo |
|---|---|
| 1 · E1 | Curva de aprendizaje SNN (tutoriales snnTorch, 2-3 semanas) + marco teórico + diseño experimental. **El mes de mayor riesgo — declarado.** |
| 2 · E2 | Baseline convencional reproducido y medido (precisión + operaciones + latencia). |
| 3 · E3 | Entrenar SNNs con gradiente sustituto, mismas condiciones; llenar la tabla comparativa; análisis estadístico. |
| 4 · E4 | Trade-off final, discusión de implicancias para implantes, redacción, código público. |

**Stack**: Python · PyTorch · snnTorch o SpikingJelly · FALCON/NLB · Colab (GPU moderada — los datasets de movimiento son livianos).

## Riesgo principal (honesto)

Es el tema con mayor curva de aprendizaje de los tres finalistas: ~1 mes siendo novato en un paradigma nuevo antes de ser productivo (los otros dos usan el stack actual del autor desde el día uno). A cambio, es el perfil más "investigador de frontera": las SNN para implantes son apuesta a 5-10 años y tema natural de doctorado — máxima señal para posgrado.

## Comparación rápida de los tres finalistas

| | 24 · LLM-AAC español | 19 · Fidelidad | 25 · SNN |
|---|---|---|---|
| Distancia de tu stack actual | Cero (LLMs = tu día a día) | Corta (ML general) | Un mes de curva |
| Riesgo técnico | Bajo | Medio | Medio-alto |
| Impacto social inmediato | Máximo (hispanohablantes con discapacidad) | Alto | Indirecto (habilita implantes futuros) |
| Señal para posgrado/frontera | Alta | Alta | Máxima |
| Método de Nature/NeurIPS a replicar | Sí (Nature Comms 2024) | Sí (protocolo 2025-26) | Parcial (papers dispersos) |
