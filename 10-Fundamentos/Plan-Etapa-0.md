# Plan de Etapa 0 — Fundamentos de NeuroIngeniería y BCI

> Duración sugerida: 6-8 semanas, ~6-8 hs/semana. Cada módulo produce NOTAS en esta carpeta (una nota por concepto, enlazadas con wikilinks — así crece el grafo).

## Módulo 1 — Neurociencia básica para ingenieros (1-2 semanas)

Qué aprender: neurona, potencial de acción, corteza cerebral y sus áreas (motora, visual), ritmos cerebrales (alfa, beta, mu, gamma).

Recursos:
- Curso: *Fundamentals of Neuroscience* (HarvardX, gratis en edX) — módulos 1-2 alcanzan.
- Libro de referencia: Kandel, *Principles of Neural Science* (solo capítulos introductorios, es enciclopédico).

Notas a producir: [[Neurona-y-potencial-de-accion]], [[Ritmos-cerebrales]], [[Areas-corticales]].

## Módulo 2 — EEG y adquisición de señales (1-2 semanas)

Qué aprender: qué mide el EEG (y qué NO), sistema 10-20 de electrodos, artefactos (parpadeo, músculo), EEG vs. fMRI vs. ECoG vs. implantes (contexto Neuralink), muestreo y filtrado (Nyquist, pasabanda, notch 50 Hz).

Recursos:
- Mike X Cohen — *Analyzing Neural Time Series Data* (caps. iniciales) y sus videos de YouTube ("ANTS").
- Review de referencia: la que ya tenés guardada (PMC7875502) sobre neurotecnología.

Notas a producir: [[Que-mide-el-EEG]], [[Sistema-10-20]], [[Artefactos-EEG]], [[Filtrado-de-senales]].

## Módulo 3 — Paradigmas BCI (1-2 semanas)

Qué aprender: el pipeline BCI completo (adquisición → preprocesamiento → extracción de features → clasificación → feedback) y los paradigmas:
- **P300** (potencial evocado, spellers)
- **SSVEP** (estímulos visuales por frecuencia)
- **Imaginería motora** (ritmos mu/beta, control de cursores/prótesis)
- **Neurofeedback** (atención, relajación)

Recursos:
- Wolpaw & Wolpaw, *Brain-Computer Interfaces: Principles and Practice* (capítulos selectos).
- Review: "Brain-Computer Interfaces for Communication and Control" (Wolpaw et al., 2002) — el paper fundacional.

Notas a producir: [[Pipeline-BCI]], [[P300]], [[SSVEP]], [[Imagineria-motora]], [[Neurofeedback]].

## Módulo 4 — Herramientas y práctica (2 semanas)

Qué hacer (esto es PRÁCTICA, no lectura):
1. Setup Python: `uv` o `conda` + `mne`, `numpy`, `scikit-learn`, `matplotlib`.
2. Tutorial oficial de **MNE-Python**: cargar un dataset de ejemplo, plotear señal cruda, filtrar, épocas, ERP.
3. Descargar un dataset de **BCI Competition IV** o **PhysioNet (EEG Motor Movement/Imagery)** y reproducir una clasificación simple de imaginería motora.
4. Explorar **OpenBCI** (hardware) y **BrainFlow** (API) para evaluar factibilidad de hardware propio.

Salida: carpeta `40-Prototipo/etapa0-experimentos/` con notebooks funcionando.

## Módulo 5 — Panorama del campo y cierre (1 semana)

- Leer 3-5 papers recientes (2023+) de aplicaciones BCI accesibles con EEG de consumo.
- Escribir [[Ideas-candidatas-de-tesis]]: 3 ideas con: qué problema resuelve, paradigma BCI, datos necesarios, línea temática donde encaja, riesgo técnico.

## Checklist de salida de la etapa

- [ ] Módulos 1-5 completados con notas enlazadas.
- [ ] Al menos 1 notebook de clasificación EEG funcionando.
- [ ] [[Ideas-candidatas-de-tesis]] escrita → habilita la Etapa 1.
