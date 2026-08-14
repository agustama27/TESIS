# Tema 18 — Seguridad y neuroderechos: threat modeling para BCI

> Estado: 🟢 En reserva (máxima factibilidad; sinergia con el tema 19 en foco)

## Definiciones Iniciales (formato oficial)

- **Tipo de TFG**: Prototipado Tecnológico · **Línea**: Transformación Digital

### Título tentativo (~12 palabras)

Framework de modelado de amenazas para sistemas de interfaz cerebro-computadora conforme a neuroderechos

### Justificación de la línea (3 renglones)

La neurotecnología solo se adopta masivamente si es confiable. Construir las herramientas de ingeniería que garanticen seguridad y cumplimiento de los neuroderechos emergentes es construir la infraestructura de confianza de esa transformación digital.

### Explicación del tema (5-15 renglones)

Los dispositivos BCI de consumo ya recolectan datos neurales capaces de revelar salud y estados emocionales. Chile se convirtió en el primer país con neuroderechos constitucionales (2021) y su Corte Suprema falló en 2023 contra una empresa BCI real por el manejo de datos neuronales; Argentina aún no legisla. No existen herramientas de ingeniería para diseñar sistemas BCI conformes a ese marco. Este trabajo prototipa un framework de threat modeling específico: catálogo de amenazas de neurodatos (inferencia de salud, replay de señal, manipulación de estímulos), mapeo amenaza→control→neuroderecho, y una herramienta web que guía el análisis y genera el reporte de riesgos. Caso de estudio: la arquitectura del dispositivo del fallo chileno.

### Problema / pregunta (3-5 renglones)

¿Cómo sistematizar el análisis de amenazas de un sistema BCI — con las amenazas específicas de los datos neurales — en una herramienta de ingeniería que produzca controles accionables y trazabilidad hacia los neuroderechos vigentes?

### Revisión de literatura (4 trabajos, APA)

1. Fallo de la Corte Suprema de Chile sobre protección de actividad cerebral: neurorights, protección de datos y neurodata. *PMC*. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10929545/
2. *Neurorights in the Constitution: from neurotechnology to ethics and politics*. *Philosophical Transactions of the Royal Society B*. https://royalsocietypublishing.org/doi/10.1098/rstb.2023.0098
3. Reforma constitucional chilena (2021) y Neuroprotection Bill (2023) — fuentes legislativas primarias.
4. ⚠️ Survey de ataques a BCIs (adversarial/replay) — verificar referencia específica.

### Justificación del TFG (borrador)

Seguridad informática es área núcleo de la carrera; la intersección seguridad×BCI×regulación no tiene herramientas y la región (Chile) lidera el marco legal mundial. Único tema sin datos, sin GPU y sin hardware: riesgo técnico mínimo absoluto. *(Expandir a 15-20 renglones si se activa.)*

## Ampliación

Ficha completa: [[../../20-Investigacion/Temas-Candidatos-TFG|lista maestra]] (ficha 18). Sinergia: la dimensión de agencia del usuario del [[Tema-19-Fidelidad-Brain-to-Text|tema 19]] conecta ambos temas — el 18 puede aportar el capítulo ético/regulatorio del marco teórico del 19.
