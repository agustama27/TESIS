# Tema 28 — Evaluación arquitectónica comparativa de frameworks BCI open source

> Estado: 🎯 **CANDIDATO ACTIVO** · formalizado 2026-08-15 a pedido del autor
> Nace de responder tres preguntas juntas: ¿el tema 7 (construir un SDK) es buena tesis?, ¿qué aporte queda para el 25?, y ¿qué hay en arquitectura/interoperabilidad?

## La idea en palabras simples

Existen **al menos siete frameworks open source** para construir sistemas BCI (Timeflux, BciPy, MEDUSA, OpenViBE, BCI2000, NeuXus, PyNoetic…). Cada uno promete cosas distintas, cada paper elogia el suyo, **y nadie los comparó sistemáticamente**: un desarrollador o laboratorio que arranca hoy no tiene forma objetiva de elegir. Tu tesis: **evaluarlos con método de ingeniería de software** — atributos de calidad, benchmarks de rendimiento y un caso de estudio implementado en los mejores — y producir la guía de decisión que el campo no tiene.

Es la analogía de las zapatillas otra vez, pero esta vez **el corredor es el software**: cada framework corrió en su propia pista (su paper); vos organizás la carrera.

## Por qué esta ES la tesis de tu carrera

- **Evaluación de arquitecturas de software con método documentado**: atributos de calidad según **ISO/IEC 25010** (mantenibilidad, portabilidad, eficiencia, usabilidad del API), análisis de trade-offs arquitectónicos — material central de la carrera, aplicado a un dominio de frontera.
- **Benchmarks reproducibles**: latencia extremo a extremo, throughput, jitter — medidos con señal reproducida (replay), sin hardware.
- **Developer experience medible**: el "hola mundo" en cada framework — líneas de código, tiempo, obstáculos documentados.
- **Caso de estudio**: implementar LA MISMA aplicación BCI mínima (ej. clasificador sobre dataset público en replay) en los 2-3 frameworks finalistas. Ahí la evaluación deja de ser opinión y pasa a ser evidencia.

## Definiciones Iniciales (formato oficial)

- **Tipo de TFG**: ☑ Trabajo de Investigación *(alternativa defendible: Prototipado, si el énfasis se pone en el banco de evaluación como producto)*
- **Línea Temática**: ☑ Transformación Digital *(alternativa natural: **Plataformas de Desarrollo** — herramientas para producir software; decidir con el tutor)*

### Título tentativo (~12 palabras)

Evaluación arquitectónica comparativa de frameworks de código abierto para interfaces cerebro-computadora

### Justificación de la línea (3 renglones)

El desarrollo de aplicaciones BCI depende de frameworks open source que ningún estudio comparó sistemáticamente: cada equipo elige a ciegas. Producir la evaluación arquitectónica y la guía de decisión que faltan acelera la construcción de las herramientas digitales que la transformación necesita.

### Explicación del tema (5-15 renglones)

El ecosistema de software para interfaces cerebro-computadora creció en frameworks de código abierto — Timeflux, BciPy, MEDUSA, OpenViBE, BCI2000, NeuXus, PyNoetic — cada uno con arquitecturas, paradigmas soportados y filosofías distintas. La literatura que los presenta es autodescriptiva: cada paper documenta las virtudes del propio framework, sin comparaciones sistemáticas entre ellos. Este trabajo produce esa comparación con método de ingeniería de software: (1) revisión y selección de frameworks activos; (2) evaluación de atributos de calidad según ISO/IEC 25010 sobre criterios verificables (documentación, cobertura de pruebas, actividad de mantenimiento, extensibilidad, portabilidad); (3) benchmark reproducible de rendimiento en tiempo real (latencia extremo a extremo, throughput, jitter) usando señal EEG pública reproducida; y (4) caso de estudio: la misma aplicación BCI mínima implementada en los frameworks finalistas, midiendo esfuerzo de desarrollo y calidad del resultado. El producto es una guía de decisión fundada en evidencia para desarrolladores y laboratorios.

### Problema / pregunta de investigación (3-5 renglones)

¿Qué framework open source de BCI ofrece el mejor equilibrio entre atributos de calidad de software, rendimiento en tiempo real y experiencia de desarrollo, según una evaluación arquitectónica sistemática y reproducible? ¿Qué trade-offs definen la elección según el caso de uso?

### Revisión de literatura (4 trabajos, APA)

1. *An open-source human-in-the-loop BCI research framework: method and design* (BCI-HIL, sobre Timeflux). (2023). *Frontiers in Human Neuroscience*. https://doi.org/10.3389/fnhum.2023.1129362
2. *PyNoetic: A modular python framework for no-code development of EEG brain-computer interfaces*. (2025). *PLOS One*. https://doi.org/10.1371/journal.pone.0327791
3. *MEDUSA©: A novel Python-based software ecosystem to accelerate brain-computer interface and cognitive neuroscience research*. (2023). ⚠️ completar revista/DOI exactos.
4. *The lab streaming layer for synchronized multimodal recording*. (2024/2025). *Imaging Neuroscience* (MIT Press). https://direct.mit.edu/imag/article/doi/10.1162/IMAG.a.136/132678/

### Justificación (borrador — expandir al confirmar)

La elección de framework es la primera decisión de arquitectura de cualquier proyecto BCI y hoy se toma sin evidencia comparativa. El trabajo aplica las herramientas centrales de la Ingeniería de Software — modelos de calidad, benchmarking, análisis de trade-offs — a un ecosistema que nunca fue evaluado así, con protocolo reproducible y datos públicos. El diseño es informativo en cualquier resultado: la guía de decisión tiene valor sea cual sea el framework que gane, y los benchmarks quedan publicados para la comunidad. Sin hardware, sin GPU, ejecutable con recursos mínimos. *(Expandir a 15-20 renglones.)*

## Plan de 4 meses

| Mes | Trabajo |
|---|---|
| 1 · E1 | Relevamiento del ecosistema, criterios de inclusión, marco teórico (ISO 25010, evaluación de arquitecturas, BCI), diseño del protocolo de evaluación |
| 2 · E2 | Evaluación estática de atributos de calidad (todos los frameworks incluidos) + instalación y "hola mundo" documentado en cada uno |
| 3 · E3 | Benchmark de rendimiento con replay de señal + caso de estudio en los 2-3 finalistas |
| 4 · E4 | Tabla final de trade-offs, guía de decisión, redacción, publicación del protocolo y el código |

**Herramientas**: Python · los frameworks bajo evaluación · dataset EEG público (replay) · scripts de medición propios. **Sin hardware, sin GPU.**

## Riesgos honestos

| Riesgo | Mitigación |
|---|---|
| Frameworks que no instalan/compilan (legado C++ como BCI2000) | Criterios de inclusión explícitos; documentar el fallo de instalación ES un dato de la evaluación |
| Acusación de subjetividad | Método documentado (ISO 25010), criterios definidos ANTES de evaluar, todo verificable |
| Alcance: 7 frameworks × profundidad | Dos niveles: evaluación estática para todos, benchmark+caso de estudio solo para finalistas |

## Relación con los temas vecinos (las respuestas del 2026-08-15)

**¿El tema 7 (construir un SDK nuevo) es buena tesis? → NO en su forma original.** El espacio está lleno: siete frameworks activos, incluido uno *no-code* publicado en 2025 (PyNoetic). Construir el octavo framework sería entrar a un mercado saturado sin haber demostrado que los existentes fallan — y con riesgo brutal de scope creep. **La forma correcta de esa energía es este tema 28**: primero se evalúa lo que hay; si la evaluación revela un hueco real, construirlo será la continuación natural (o el trabajo futuro declarado).

**¿Qué aporte queda para el 25 (SNN)? → Tres opciones concretas**, ver [[Tema-25-ESTADO-CONSOLIDADO]]:
1. La extensión FALCON multi-sesión/few-shot (robustez temporal — NeuroBench no la cubrió).
2. Reformularlo como **Prototipado**: el banco de evaluación reproducible + la demo de trayectorias como producto de software — el aporte es LA HERRAMIENTA, los resultados la validan.
3. Fusionarlo aquí: los decodificadores (convencional y SNN) como cargas de trabajo del caso de estudio del tema 28.
