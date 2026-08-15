# Mapa completo: ramas de la Ingeniería de Software × BCI

> 2026-08-15 · Respuesta sistemática a "¿qué otras ramas de la carrera, además de QA, dan tesis sobre BCI?"
> Bajo la vara correcta ([[../../20-Investigacion/Calibracion-Alcance-Tesis-BCI|calibración]]): todos los temas siguen el molde "diseñar/implementar/evaluar sobre algo existente", que es el de las tesis que se aprueban.

## El mapa

| Rama de la carrera | Ya explorado en el vault | Tema NUEVO posible (formato tesis) |
|---|---|---|
| **Requisitos** | — | 🆕 Elicitación y especificación de requisitos para sistemas BCI asistivos, con usuarios y terapeutas (⚠️ requiere acceso a personas — riesgo logístico) |
| **Arquitectura e interoperabilidad** | Tema 7 (SDK/framework) | 🆕 **Tema 28**: evaluación de arquitecturas middleware para streaming de señales neurales (LSL vs alternativas), o diseño de un adaptador/puente entre estándares |
| **Construcción** | Temas 7, 25 (implementación de decodificadores) | — (cubierto) |
| **Testing / QA** | **Tema 26** (embrión): framework de pruebas automatizadas para pipelines BCI OSS | Variantes: emulador de señal para tests de regresión (estilo DEEGMUX por software), suite de conformidad |
| **Seguridad** | Temas 18 (threat modeling + neuroderechos) y 21 (robustez adversarial) | — (cubiertos, reactivables bajo la vara nueva) |
| **Usabilidad / HCI / accesibilidad** | Opción C (descartada): diseño de interfaces para cursores BCI con ley de Fitts | ♻️ **Reactivable**: bajo la vara correcta es un "diseño y evaluación con usuarios sanos + simulación de cursor degradado" — ejecutable y con estudio humano barato |
| **Mantenimiento / MLOps** | Tema 20: drift y recalibración de decodificadores (benchmark FALCON) | ♻️ Reactivable igual que el 25 (fue descartado con la vara equivocada) |
| **Performance** | Temas 23 (compresión de modelos) y 16 (compresión de datos) | ♻️ Reactivables |
| **Ingeniería de datos** | — | 🆕 **Tema 27**: pipeline automatizado de datos EEG conforme al estándar BIDS — adquisición (LSL) → conversión (EEG-BIDS) → validación → versionado. Precedente a extender: LSLAutoBIDS |
| **Calidad de proceso / normativa** | Capítulo de normativa en la tesis UNSAM (precedente) | 🆕 **Tema 29**: aplicación del ciclo de vida de software de dispositivos médicos (norma IEC 62304 ⚠️ verificar alcance) a un sistema BCI open source — gap analysis + artefactos de conformidad |
| **Gestión de proyectos** | — | Débil como tesis técnica de la carrera; descartar |

## Los tres nuevos, en una línea cada uno

**27 · Ingeniería de datos (BIDS)**: los laboratorios pierden tiempo convirtiendo datos EEG a mano; existe el estándar (EEG-BIDS, *Nature Scientific Data* 2019) y un precedente parcial (LSLAutoBIDS). Tesis: *"diseño e implementación de un pipeline automatizado de gestión de datos EEG conforme a BIDS"*. Data engineering puro, sin hardware, sobre estándares publicados.

**28 · Arquitectura/interoperabilidad (LSL)**: el ecosistema BCI tiene estándares que no siempre se hablan entre sí (LSL/XDF, BCI2000, OpenViBE, NWB, BIDS) y un roadmap IEEE de estandarización en curso. Tesis: *"evaluación comparativa de middleware de streaming neural"* o *"diseño de un adaptador entre estándares"*. Arquitectura de software clásica: contratos, acoplamiento, latencia.

**29 · Proceso/normativa (IEC 62304)**: el software BCI clínico es software de dispositivo médico, con norma de ciclo de vida propia. Tesis: *"análisis de brecha y aplicación de IEC 62304 a un proyecto BCI open source"* — qué le falta al software libre del área para ser certificable. Ingeniería de procesos + calidad; hereda el espíritu del capítulo normativo de la tesis UNSAM. ⚠️ Verificar acceso al texto de la norma (las ISO/IEC son pagas; hay resúmenes académicos).

## Anclas verificadas (2026-08-15)

- EEG-BIDS: [Pernet et al., *Scientific Data* (2019)](https://www.nature.com/articles/s41597-019-0104-8)
- Lab Streaming Layer: [paper en *Imaging Neuroscience* (MIT Press)](https://direct.mit.edu/imag/article/doi/10.1162/IMAG.a.136/132678/) · [150+ dispositivos soportados](https://labstreaminglayer.readthedocs.io/info/supported_devices.html)
- LSLAutoBIDS (precedente a extender): [Aperture Neuro](https://apertureneuro.org/article/159415-automating-data-integration-and-publishing-for-neuroimaging-via-lslautobids)
- IEEE Standards Roadmap on Neurotechnologies for BMI: [IEEE Brain](https://brain.ieee.org/newsletter/2020-issue-1/overview-of-the-ieee-standards-roadmap-on-neurotechnologies-for-brain-machine-interfacing/)
- NWB, XDF, BCI2000, OpenViBE: referenciados en el paper de LSL.

## Lectura del mapa

**Todas las ramas de la carrera tienen tesis posible sobre BCI.** La pregunta ya no es "¿hay tema?" — hay más de veinte entre vivos, reactivables y nuevos. La pregunta es cuál vas a disfrutar ejecutar durante cuatro meses. Criterios que ya probamos: hueco tipo "ausencia verificable" o "extensión declarada de algo existente" (no predicciones), datos/código públicos, y motivación real del autor.

## Enlaces

[[Reevaluacion-2026-08-15]] · [[00-Indice]] · [[../../20-Investigacion/Calibracion-Alcance-Tesis-BCI|Calibración]]
