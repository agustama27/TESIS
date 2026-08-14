# Tema 2 — Foundation models de EEG con pocos datos

> Estado: 🟢 En reserva (fue 🥈 del ranking histórico)

## Definiciones Iniciales (formato oficial)

- **Tipo de TFG**: Trabajo de Investigación · **Línea**: Transformación Digital

### Título tentativo (~12 palabras)

Modelos fundacionales de EEG frente a modelos entrenados desde cero con datos limitados

### Justificación de la línea (3 renglones)

Toda BCI práctica exige una calibración por usuario que bloquea su adopción como herramienta digital cotidiana. Los modelos fundacionales prometen eliminar esa barrera: evaluarlos rigurosamente es evaluar la adoptabilidad de la tecnología.

### Explicación del tema (5-15 renglones)

Los foundation models de EEG (LaBraM, ICLR 2024, pre-entrenado con ~2.500 horas de señal) prometen trasladar a las señales cerebrales el salto que GPT dio en lenguaje: aprender representaciones generales y adaptarse a cada tarea con pocos datos. Este trabajo evalúa esa promesa donde importa: régimen de pocos datos del usuario final. Se construyen curvas de aprendizaje (1%, 5%, 10%, 50%, 100% de los datos) comparando LaBraM fine-tuneado contra EEGNet entrenado desde cero, sobre datasets públicos, midiendo dónde el pre-entrenamiento paga y dónde no.

### Problema / pregunta (3-5 renglones)

¿El fine-tuning de un foundation model de EEG supera a modelos entrenados desde cero cuando solo hay minutos de datos del usuario? ¿Dónde se cruzan las curvas de aprendizaje y qué costo computacional tiene cada camino?

### Revisión de literatura (4 trabajos, APA)

1. Jiang, W., et al. (2024). Large Brain Model for learning generic representations with tremendous EEG data in BCI. *ICLR 2024* (spotlight). https://github.com/935963004/labram
2. *Are Large Brainwave Foundation Models Capable Yet? Insights from Fine-tuning*. *arXiv*. https://arxiv.org/abs/2507.01196
3. *What Do EEG Foundation Models Capture from Human Brain Signals?* *arXiv*. https://arxiv.org/abs/2605.11410
4. Lawhern, V. J., et al. (2018). EEGNet. *Journal of Neural Engineering*. https://doi.org/10.1088/1741-2552/aace8c

### Justificación del TFG (borrador)

La calibración de 20-30 minutos por usuario es el bloqueo #1 de la productización BCI. Los foundation models son la apuesta del campo para eliminarla, pero su evaluación en régimen de pocos datos es incipiente. Este trabajo la aporta con diseño experimental de red de seguridad: el benchmark contra EEGNet es publicable converja o no el fine-tuning. Es MLOps de frontera: gestión de fine-tuning, tracking de experimentos, evaluación sistemática. *(Expandir a 15-20 renglones si se activa.)*

## Ampliación

Ficha completa: [[../../20-Investigacion/Temas-Candidatos-TFG|lista maestra]] (ficha 2).
