# Tema 9 — Control domótico por SSVEP

> Estado: ❌ **Descartado** (condicional) — la validación seria exige EEG occipital real, sin equipo en mano. Borrador abreviado.

## Definiciones Iniciales (abreviado)

- **Tipo**: Prototipado Tecnológico · **Línea**: Transformación Digital
- **Título tentativo**: Prototipo de control domótico mediante potenciales evocados visuales para movilidad reducida
- **Justificación de línea (3 renglones)**: vida independiente para personas con movilidad reducida cuya voz también está comprometida (la domótica por voz falla con disartria) — control del entorno sin manos ni voz.
- **Explicación (resumen)**: panel de estímulos parpadeando a frecuencias distintas; mirar uno dispara el comando (CCA/FBCCA sobre señal occipital) vía MQTT a actuadores (Home Assistant). Validación sobre datasets SSVEP públicos en reproducción.
- **Pregunta**: ¿cómo integrar detección SSVEP con una arquitectura IoT fail-safe para control confiable del entorno?
- **Literatura (4)**: SSVEP smart home (ResearchGate 317801658) · SSVEP wheelchair (arXiv 2307.08703) · drone SSVEP con EEG de consumo (IJEEEMI) · ⚠️ completar review de FBCCA.
- **Justificación (esbozo)**: precisiones >85% documentadas; IoT barato y estándar. Limitación excluyente: los headsets frontales de consumo no sirven para SSVEP.
