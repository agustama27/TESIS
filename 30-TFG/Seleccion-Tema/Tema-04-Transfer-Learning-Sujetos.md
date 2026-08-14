# Tema 4 — Transfer learning entre sujetos

> Estado: 🟢 En reserva (fue 4º del ranking histórico)

## Definiciones Iniciales (formato oficial)

- **Tipo de TFG**: Trabajo de Investigación · **Línea**: Transformación Digital

### Título tentativo (~12 palabras)

Estrategias de transferencia entre sujetos para reducir la calibración en interfaces cerebro-computadora

### Justificación de la línea (3 renglones)

Una BCI que exige media hora de calibración por sesión no se adopta. Reducir esa fricción mediante transferencia de conocimiento entre usuarios ataca directamente la barrera de adopción digital de la tecnología.

### Explicación del tema (5-15 renglones)

La señal EEG varía tanto entre personas que un modelo entrenado para un usuario no sirve para otro — el equivalente BCI del cold-start. Este trabajo mide cuánto puede reducirse la calibración de un usuario nuevo aprovechando datos de otros: alineación de covarianzas (Riemannian alignment), fine-tuning de EEGNet pre-entrenado en N-1 sujetos, y curvas de calibración con fracciones crecientes de datos del sujeto objetivo. Protocolo leave-one-subject-out sobre datasets públicos vía MOABB (148 datasets), con resultados comparables internacionalmente.

### Problema / pregunta (3-5 renglones)

¿Cuántos minutos de datos de un usuario nuevo se necesitan para alcanzar precisión utilizable (>70%) en imaginería motora, usando conocimiento transferido de otros sujetos? ¿Qué técnica de transferencia rinde mejor por minuto de calibración?

### Revisión de literatura (4 trabajos, APA)

1. Lawhern, V. J., et al. (2018). EEGNet. *Journal of Neural Engineering*. https://doi.org/10.1088/1741-2552/aace8c
2. *EEG-Reptile: An Automatized Reptile-Based Meta-Learning Library for BCIs*. *arXiv*. https://arxiv.org/abs/2412.19725
3. MOABB — Mother of All BCI Benchmarks (NeuroTechX). https://moabb.neurotechx.com
4. ⚠️ Jayaram, V., y Barachant, A. (2018). MOABB paper, *Journal of Neural Engineering* — verificar DOI.

### Justificación del TFG (borrador)

La pregunta operativa — cuántos minutos de calibración necesita un producto BCI — es un requisito no funcional cuantificado con método científico. Riesgo logístico cero (datasets públicos, benchmark estándar), mapeo directo a competencias de ML engineering (domain adaptation, evaluación reproducible). *(Expandir a 15-20 renglones si se activa.)*

## Ampliación

Ficha completa: [[../../20-Investigacion/Temas-Candidatos-TFG|lista maestra]] (ficha 4).
