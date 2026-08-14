# Tema 22 — Datos sintéticos para decodificación neural (IA generativa)

> Estado: 🟢 En reserva — agregado 2026-08-14 tras validación. IA generativa × data-centric AI.

## Definiciones Iniciales (formato oficial)

- **Tipo de TFG**: Trabajo de Investigación · **Línea**: Transformación Digital

### Título tentativo (~12 palabras)

Aumento de datos con modelos de difusión para decodificación EEG en escenarios de escasez

### Justificación de la línea (3 renglones)

La escasez de datos neurales es el freno estructural del campo: recolectarlos es caro e invasivo. Si la IA generativa puede sintetizarlos con fidelidad útil, se destraba el desarrollo de aplicaciones BCI accesibles — multiplicador directo de la transformación digital.

### Explicación del tema (5-15 renglones)

Los modelos de difusión — la tecnología detrás de los generadores de imágenes — se están aplicando a sintetizar señal EEG: trabajos 2024-2026 (EEGDiffuser, DDPM mejorados) reportan que aumentar datasets reales con señal sintética mejora la decodificación en regímenes de pocos datos. Pero las evaluaciones son heterogéneas y la pregunta incómoda persiste: ¿la señal generada contiene información neurofisiológica real o solo estadística superficial que infla métricas? Este trabajo evalúa sistemáticamente cuánto mejora la decodificación con aumento por difusión bajo protocolo honesto (subject-independent, sin fugas), y audita la señal sintética con métricas de fidelidad espectral y de contenido — el espíritu del tema 19 aplicado a datos generados.

### Problema / pregunta (3-5 renglones)

¿El aumento con datos sintéticos de difusión mejora la decodificación EEG en pocos datos bajo evaluación honesta, y qué contienen realmente esas señales generadas: neurofisiología o estadística superficial?

### Revisión de literatura (4 trabajos, APA)

1. *Generative modeling and augmentation of EEG signals using improved diffusion probabilistic models*. (2025). *Journal of Neural Engineering*. https://iopscience.iop.org/article/10.1088/1741-2552/ada0e4
2. *EEGDiffuser: Label-guided EEG signals synthesis via diffusion model for BCI applications*. (2026). *Neurocomputing*. https://www.sciencedirect.com/science/article/abs/pii/S0925231226000330
3. *EEG-GAN: A Generative EEG Augmentation Toolkit for Enhancing Neural Classification*. (2025). *bioRxiv*. ⚠️ preprint.
4. Lawhern, V. J., et al. (2018). EEGNet. *Journal of Neural Engineering*. https://doi.org/10.1088/1741-2552/aace8c

### Justificación del TFG (borrador)

IA generativa (el corazón del stack actual del autor) aplicada al problema estructural del campo, con la capa de auditoría que evita el error metodológico típico (métricas infladas por fugas). Datasets públicos, GPU moderada. *(Expandir a 15-20 renglones si se activa.)*

## Ampliación

Pariente metodológico del [[Tema-19-Fidelidad-Brain-to-Text|tema 19]]: ambos auditan qué hay "adentro" de un número que parece bueno.
