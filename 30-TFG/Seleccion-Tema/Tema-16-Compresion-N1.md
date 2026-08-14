# Tema 16 — Compresión de telemetría neural (Neuralink N1)

> Estado: ❌ **Descartado** (2026-08-14) — decisión del autor: percibido como inviable ("si Neuralink no pudo resolverlo…"). Nota técnica: el planteo era caracterizar la frontera, no ganar el desafío — pero sin convicción del autor no hay tesis. Análisis completo preservado en [[../../20-Investigacion/Compresion-Telemetria-Neural|Compresion-Telemetria-Neural]].

## Definiciones Iniciales (abreviado)

- **Tipo**: Trabajo de Investigación · **Línea**: Transformación Digital
- **Título tentativo**: Caracterización de la frontera de compresión sin pérdida para telemetría neural de alto ancho de banda
- **Justificación de línea (3 renglones)**: sin telemetría eficiente, los implantes neurales no escalan: el N1 genera 200 veces más datos de los que puede transmitir. La compresión es la condición técnica de la adopción.
- **Explicación (resumen)**: banco de pruebas reproducible sobre el dataset público del Neuralink Compression Challenge (1 h de señal del implante N1, archivos WAV); baselines (zip/zstd/FLAC ≈ 2-3x) y técnicas por capas (deltas, predicción lineal, correlación inter-canal, codificación entrópica) midiendo ratio, velocidad y verificación bit a bit; estimación de la entropía de la señal como límite teórico.
- **Pregunta**: ¿qué combinación de técnicas maximiza el ratio lossless bajo restricciones de tiempo real, y dónde está el límite teórico que explica por qué la meta de 200x es inalcanzable sin pérdida?
- **Literatura (4)**: Neuralink Compression Challenge (content.neuralink.com/compression-challenge) · n1-codec (github.com/mikaelhaji/n1-codec) · cobertura técnica CBC/foros de compresión · ⚠️ literatura académica de compresión de biosignals, verificar.
- **Justificación (esbozo)**: el tema más barato en recursos de la lista (143 MB, sin GPU) con validación bit a bit trivial; CV único ("datos reales del N1").
