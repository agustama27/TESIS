# Tema 21 — Robustez adversarial de decodificadores neuronales

> Estado: 🟢 En reserva — agregado 2026-08-14 tras validación. Seguridad × AI reliability.

## Definiciones Iniciales (formato oficial)

- **Tipo de TFG**: Trabajo de Investigación · **Línea**: Transformación Digital

### Título tentativo (~12 palabras)

Robustez adversarial de decodificadores EEG: evaluación sistemática de ataques y defensas

### Justificación de la línea (3 renglones)

Las BCI entran en rehabilitación, dispositivos asistivos y consumo masivo. Su adopción segura exige saber qué tan frágiles son sus modelos ante manipulación — la infraestructura de confianza de la transformación digital neurotecnológica.

### Explicación del tema (5-15 renglones)

La literatura demostró que los clasificadores EEG son vulnerables a perturbaciones adversariales imperceptibles e incluso a ataques de backdoor por envenenamiento de datos de entrenamiento — en aplicaciones donde un error significa una silla de ruedas moviéndose mal o un diagnóstico alterado. Existe un benchmark de robustez adversarial para BCIs (FGCS 2023) y defensas recientes (adversarial training, arquitecturas jerárquicas, 2025). Este trabajo evalúa sistemáticamente ataques estándar (FGSM, PGD) y defensas sobre los decodificadores y datasets públicos de referencia, bajo protocolo honesto y reproducible, cuantificando el trade-off robustez-precisión.

### Problema / pregunta (3-5 renglones)

¿Qué tan robustos son los decodificadores EEG estándar frente a ataques adversariales de distinta potencia, y qué defensas recuperan robustez sin sacrificar precisión? ¿El trade-off cambia entre paradigmas (imaginería motora, P300)?

### Revisión de literatura (4 trabajos, APA)

1. *Adversarial robustness benchmark for EEG-based brain-computer interfaces*. (2023). *Future Generation Computer Systems*. https://www.sciencedirect.com/science/article/abs/pii/S0167739X23000353
2. *EEG-Based Brain-Computer Interfaces Are Vulnerable to Backdoor Attacks*. (ResearchGate/IEEE). ⚠️ verificar referencia de revista exacta.
3. *Adversarial robust EEG-based BCIs using a hierarchical convolutional neural network*. (2025). *Scientific Reports*. https://www.nature.com/articles/s41598-025-34024-0
4. *Making Brain-Computer Interfaces More Secure*. *arXiv*. https://arxiv.org/abs/2606.02597

### Justificación del TFG (borrador)

Security engineering aplicada a ML — dos áreas núcleo de la carrera — sobre el dominio más sensible. Sinergia natural con el tema 18 (neuroderechos: acá está la evidencia técnica de las amenazas que aquel marco regula). Datasets y benchmark públicos, sin hardware. *(Expandir a 15-20 renglones si se activa.)*

## Ampliación

Conecta [[Tema-18-Neuroderechos-Threat-Modeling|tema 18]] (el marco) con la evidencia técnica (los ataques). Juntos podrían formar un programa; separados, cada uno es tesis.
