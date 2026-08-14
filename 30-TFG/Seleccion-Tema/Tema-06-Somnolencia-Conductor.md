# Tema 6 — Detección de somnolencia del conductor

> Estado: ❌ **Descartado** — dominado por opciones de mayor retorno; sin interés del autor. Borrador abreviado.

## Definiciones Iniciales (abreviado)

- **Tipo**: Prototipado Tecnológico · **Línea**: Transformación Digital
- **Título tentativo**: Sistema de detección temprana de somnolencia en conductores mediante señales EEG
- **Justificación de línea (3 renglones)**: digitalización de la seguridad laboral en el transporte: monitoreo fisiológico de flotas donde hoy solo hay telemetría vehicular.
- **Explicación (resumen)**: clasificador vigilia/somnolencia sobre SEED-VIG (dataset público SJTU, 23 sujetos, etiquetas PERCLOS) con replay en tiempo real, módulo de alertas y dashboard de supervisor de flota.
- **Pregunta**: ¿cómo detectar la deriva de vigilancia ANTES del microsueño (ventaja del EEG sobre las cámaras, que ven síntomas tardíos) con confiabilidad utilizable?
- **Literatura (4)**: SEED-VIG (bcmi.sjtu.edu.cn/~seed/seed-vig) · EEG-Fest (arXiv 2211.03878) · fatiga EEG automotive (arXiv 2408.13929) · ⚠️ completar cuarta referencia.
- **Justificación (esbozo)**: 17,6% de choques fatales con conductor somnoliento (AAA 2017-2021); USD 109 mil millones/año de costo social (NHTSA). Software safety-critical de libro.
