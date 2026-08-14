# Tema 17 — Brain-to-text: benchmark de decodificadores (forma original)

> Estado: ❌ **Descartado en su forma original → EVOLUCIONÓ al [[Tema-19-Fidelidad-Brain-to-Text|Tema 19]]** (2026-08-14).
> Motivo: la validación adversarial mostró que la pregunta "¿por qué los Transformers no superan a la RNN?" se está cerrando — trabajos 2025-2026 (transformer multi-usuario, pre-entrenamiento, Brain-to-Text '25) muestran Transformers ganando con escala. Evidencia completa: [[../../20-Investigacion/Decodificacion-Brain-to-Text|Decodificacion-Brain-to-Text]] §"Estado de la pregunta".

## Definiciones Iniciales (abreviado, histórico)

- **Tipo**: Trabajo de Investigación · **Línea**: Transformación Digital
- **Título tentativo (histórico)**: Evaluación de arquitecturas de decodificación brain-to-text sobre datos intracorticales públicos
- **Explicación (resumen)**: reproducción del baseline RNN del Brain-to-Text Benchmark '24 (datasets públicos de Stanford en Dryad) + comparación de arquitecturas + ablación del modelo de lenguaje.
- **Literatura (4)**: Willett et al. (2021), *Nature* 593 · Willett et al. (2023), *Nature* 620 · Brain-to-Text Benchmark '24 (arXiv 2412.17227) · Card et al. (2024), *NEJM*.

**Qué sobrevive en el Tema 19**: los datasets, el pipeline, la reproducción del baseline y la ablación del modelo de lenguaje — reencuadrados bajo la pregunta de fidelidad, que sigue abierta y tiene mayor alcance.
