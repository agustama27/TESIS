# Tema 12 — Reconocimiento de emociones (DEAP)

> Estado: ❌ **Descartado** — campo saturado con evaluación dudosa; dominado por el tema 19, que ataca un problema análogo (inflación de rendimiento) en un dominio de mayor impacto. Borrador abreviado.

## Definiciones Iniciales (abreviado)

- **Tipo**: Trabajo de Investigación · **Línea**: Transformación Digital
- **Título tentativo**: Evaluación comparativa de arquitecturas de aprendizaje profundo para reconocimiento de emociones en EEG
- **Justificación de línea (3 renglones)**: computación afectiva como capa de las interfaces digitales que responden al estado del usuario.
- **Explicación (resumen)**: benchmark de CNN/RNN/Transformers/GNN sobre DEAP con protocolo subject-independent limpio; el aporte es cuantificar cuánto caen las precisiones publicadas cuando se evalúa sin data leakage.
- **Pregunta**: ¿qué arquitecturas rinden mejor bajo evaluación honesta, y cuánta de la precisión publicada del campo es artefacto de protocolo?
- **Literatura (4)**: reviews PMC12839272 y PMC12825124 · *Frontiers in Psychology* (2023) · hybrid models sobre DEAP (PMC11946828).
- **Justificación (esbozo)**: la crisis de reproducibilidad del subcampo es real, pero el mismo espíritu (auditar rendimiento inflado) tiene más impacto aplicado al brain-to-text (tema 19).
