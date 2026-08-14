# Tema 14 — Tutor adaptativo por carga cognitiva

> Estado: 🟢 En reserva (mejor opción de Educación Digital sin hardware)

## Definiciones Iniciales (formato oficial)

- **Tipo de TFG**: Prototipado Tecnológico · **Línea**: Educación Digital

### Título tentativo (~12 palabras)

Sistema de aprendizaje adaptativo basado en carga cognitiva estimada mediante señales EEG

### Justificación de la línea (3 renglones)

Las plataformas educativas adaptan la dificultad según respuestas correctas — una señal tardía que llega después del fallo y la frustración. Estimar la carga cognitiva desde la fisiología permite adaptar ANTES: personalización educativa real mediante herramientas digitales.

### Explicación del tema (5-15 renglones)

El e-learning es masivo pero su "personalización" reacciona tarde: solo ve aciertos y errores. La carga cognitiva medible en EEG (índices espectrales validados sobre el dataset público STEW, 48 sujetos con etiquetas de esfuerzo mental) es la señal temprana. Este trabajo prototipa una plataforma de ejercicios con arquitectura de dos loops desacoplados: un estimador de carga (entrenado sobre STEW, con señal en reproducción como estudiante simulado) y un motor pedagógico que ajusta la dificultad. Decisión de diseño central: el sistema es agnóstico del estimador — si la ciencia mejora el índice, se enchufa sin tocar el resto.

### Problema / pregunta (3-5 renglones)

¿Cómo diseñar un sistema educativo que adapte la dificultad en tiempo real a partir de la carga cognitiva estimada por EEG, con una arquitectura que aísle la incertidumbre del estimador fisiológico del resto de la plataforma?

### Revisión de literatura (4 trabajos, APA)

1. Lim, W. L., Sourina, O., y Wang, L. (2018). STEW: Simultaneous Task EEG Workload dataset. *IEEE Transactions on Neural Systems and Rehabilitation Engineering*. IEEE DataPort: https://doi.org/10.21227/44r8-ya50
2. Bibliometric-enhanced systematic literature review of EEG in education. *arXiv*. https://arxiv.org/abs/2509.26083
3. *Exploring Neural Evidence of Attention in Classroom Environments: A Scoping Review*. *PMC*. https://pmc.ncbi.nlm.nih.gov/articles/PMC12384261/
4. ⚠️ Literatura de neuroadaptive learning systems — verificar referencia específica.

### Justificación del TFG (borrador)

Educación Digital es la línea menos competida; adaptive learning + neuro casi no tiene sistemas construidos localmente. Sin hardware (STEW + demo simulada). La limitación científica del estimador se convierte en argumento de diseño (arquitectura desacoplada). *(Expandir a 15-20 renglones si se activa.)*

## Ampliación

Ficha completa: [[../../20-Investigacion/Temas-Candidatos-TFG|lista maestra]] (ficha 14).
