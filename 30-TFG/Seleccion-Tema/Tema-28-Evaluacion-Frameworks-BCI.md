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

## 🚀 El gancho Neuralink (agregado 2026-08-15, a pedido del autor)

**Lo honesto primero**: Neuralink no usa estos frameworks — construye su stack propietario. La conexión NO es "evalúo lo que usa Neuralink". La conexión legítima es mejor:

### El stress-test de la era de los implantes

Todo el ecosistema de frameworks abiertos nació para **EEG**: 8-64 canales a 250-1000 Hz. Pero la era que Neuralink inauguró es de **datos intracorticales**: 1.024 canales a ~30.000 Hz — **tres órdenes de magnitud más caudal**. Y los datos de esa escala ya son públicos (datasets de Stanford/Willett, FALCON).

**La pregunta que hace única a la tesis**: *¿está el ecosistema de software abierto preparado para la era de los implantes?* El benchmark deja de ser "comparar frameworks con cargas de juguete" y pasa a ser un **stress-test de escalabilidad**: reproducir señal a escala creciente (canales × frecuencia de muestreo) a través de cada framework y medir **dónde se rompe cada uno** — latencia, jitter, pérdida de muestras, CPU. Curvas de quiebre por arquitectura.

- Es medible, reproducible y visual (las curvas de degradación de cada framework son la demo).
- Es una ausencia verificable: los frameworks se evalúan a sí mismos con EEG; nadie publicó su comportamiento a escala intracortical. ⚠️ Verificar en el Mes 1 con búsqueda dedicada.
- No afirma nada sobre Neuralink — usa la escala de datos que esa industria volvió realidad, con datasets públicos.

### Título tentativo alternativo (con el gancho)

*"Evaluación arquitectónica de frameworks BCI de código abierto frente a cargas de datos de próxima generación"*

### La línea de CV que produce

> "Evalué sistemáticamente la infraestructura de software abierta del campo BCI y medí si puede escalar a los caudales de datos de los implantes de nueva generación."

Arquitectura de software + benchmarking + neurotecnología de frontera — el perfil que las empresas del área (que construyen exactamente esta infraestructura, pero cerrada) contratan. Y para una maestría: metodología de evaluación + resultados reproducibles + un hueco real.

### Sinergia con el interés en SNN (opcional)

El caso de estudio puede incluir un decodificador convencional Y uno de impulsos como cargas de trabajo — el interés del autor por las SNN sobrevive dentro de esta tesis sin cargar con su justificación.

## Objeción anticipada clave (planteada por el autor, 2026-08-15)

**"La industria va a construir su propio software cuando llegue la era de los implantes — no va a usar los frameworks gratuitos. ¿Para qué evaluarlos?"**

Respuesta en tres capas:

1. **El usuario de la tesis no es la industria: es la ciencia.** Las empresas hacen stacks propietarios para sus productos; pero la validación científica, la replicación y la formación de los ingenieros ocurren en universidades y laboratorios que dependen del ecosistema abierto. Si las herramientas abiertas no aguantan datos de implante, la ciencia queda afuera de esa era.
2. **Para los DATOS, la era de los implantes ya llegó**: los datasets intracorticales (Stanford/Willett, FALCON) son públicos HOY, y los laboratorios ya necesitan procesarlos con las herramientas que tienen. La pregunta es de presente, no de futuro.
3. **Precedente histórico**: cada era arrancó con stacks cerrados y maduró sobre infraestructura abierta (Unix propietario → Linux en toda la nube; móviles cerrados → Android; y PyTorch, open source, debajo de toda la IA actual — incluida la de las empresas que compiten entre sí). Las empresas compiten en el producto y convergen en la infraestructura.

**Formulación blindada de la pregunta**: "Los datos de implante ya son públicos y la comunidad científica ya los necesita procesar, pero sus herramientas se diseñaron para un caudal mil veces menor. Esta tesis mide si las herramientas que la ciencia realmente usa pueden con los datos que ya existen." — Sin futurología: presente medible.

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

## Auditoría externa (2026-08-16) — corrección verificada + recorte de alcance

Un segundo agente de IA leyó el repo completo y produjo tres aportes; se auditaron antes de aceptarlos (regla vigente):

### ✔ Corrección del hueco (VERIFICADA por fetch de PMC12434378)

La afirmación absoluta "nadie evaluó la capa de software BCI frente a fallas" **no debe usarse**. El paper de LSL: (a) describe mecanismos de reconexión, corrección de timestamps y compensación de jitter (secc. 2.2.5, 2.4); (b) declara stress-tests periódicos con cientos de streams y desconexiones aleatorias (secc. 2.6) — **pero sin ninguna métrica cuantitativa** (sin tasas de pérdida, tiempos de recuperación ni latencia bajo fallo; las pruebas formales de la secc. 3 son en condiciones ideales); (c) admite pérdida de datos ante desconexiones largas (secc. 5); (d) **no mide impacto sobre decodificador o pipeline alguno**. → **Hueco refinado y MÁS fuerte**: verificación independiente y cuantitativa de lo autodeclarado + propagación de la falla a la decodificación. Es el mismo molde que ya validamos con Secure LSL.

### ✔ Recorte de alcance (ACEPTADO — coincide con nuestro riesgo declarado)

El tema 28 "base" acumula demasiado (ISO 25010 completo + 7 frameworks + DX study + stress intracortical + cifrado). **Núcleo ejecutable en 4 meses**: 1 banco de experimentación (replay + inyectores + observabilidad) · 1 pipeline BCI de referencia · 2 frameworks/implementaciones · 3-4 tipos de falla (drop, jitter, desconexión, clock skew) · métricas de sistema Y de decodificador. Todo lo demás (ISO 25010 integral, era intracortical, SNN, cifrado, neuroderechos, DX) → antecedentes o trabajo futuro. La unidad de análisis es **el pipeline BCI como sistema de software**, no un ranking de frameworks.

### ✔ Prueba de humo v2 (MEJOR que "hola mundo")

En vez de solo instalar BciPy/MEDUSA: dataset EEG público → MNE → **MNE-LSL PlayerLSL** (replay como stream LSL simulado — ⚠️ verificar docs el día del PoC) → receptor → clasificador baseline → accuracy normal; luego el mismo replay + jitter/pérdida inyectados → medir la degradación. Si sale aunque sea rudimentario, demuestra de un golpe la cadena completa de la tesis: datos → streaming reproducible → falla controlable → efecto cuantificable.

### ✗ Rechazado de esa auditoría

Su sugerencia de "comparar seriamente 28 vs 20 vs 19" — reabriría el carrusel de rankings. Tres señales independientes ya convergen en la familia 28 (elección del mentor, interés espontáneo del autor por la capa IA, y el propio ranking del agente externo que la pone 🥇). El mecanismo de cierre es el PoC + el tutor, no otra comparación.

## Refuerzos desde la investigación de carrera (2026-08-16)

Del [[../../20-Investigacion/Oportunidades-Neurotech-Para-Ingenieros-Software|mapa de oportunidades neurotech]], tres insumos que FORTALECEN esta tesis (no la cambian):

1. **Antecedente para la capa IA**: ENFOR-SA — fault injection para evaluar confiabilidad de DNNs (https://arxiv.org/pdf/2602.00909) ⚠️ SIN VERIFICAR (leer en Mes 1 antes de citar). Ancla la medición falla-de-software → error-del-decodificador en literatura de dependability de ML.
2. **Munición para la justificación** (entregas posteriores): la FDA clasifica el software de BCI implantadas como "major level of concern" (guidance 2021) e IEC 62304 exige V&V en todo el ciclo de vida — la tesis produce exactamente el tipo de evidencia que ese marco pide. ⚠️ Verificar textos antes de citar.
3. **Trabajo futuro declarado** (sección final de la tesis, NO alcance del TFG): (a) versión closed-loop con el modelo en el lazo y fallas dentro de la DNN — candidato natural a tema de maestría; (b) neuroseguridad: de fallos accidentales a maliciosos; (c) extensión hardware-in-the-loop.

**Nota del autor (2026-08-16)**: al leer el tema "confiabilidad de pipelines ML de decodificación mediante fault injection" como área futura, el autor lo marcó como lo que más le interesó — sin registrar que es la capa IA de su propia tesis con otras palabras. Señal de motivación correcta: el tema elegido y el interés espontáneo coinciden.

## Relación con los temas vecinos (las respuestas del 2026-08-15)

**¿El tema 7 (construir un SDK nuevo) es buena tesis? → NO en su forma original.** El espacio está lleno: siete frameworks activos, incluido uno *no-code* publicado en 2025 (PyNoetic). Construir el octavo framework sería entrar a un mercado saturado sin haber demostrado que los existentes fallan — y con riesgo brutal de scope creep. **La forma correcta de esa energía es este tema 28**: primero se evalúa lo que hay; si la evaluación revela un hueco real, construirlo será la continuación natural (o el trabajo futuro declarado).

**¿Qué aporte queda para el 25 (SNN)? → Tres opciones concretas**, ver [[Tema-25-ESTADO-CONSOLIDADO]]:
1. La extensión FALCON multi-sesión/few-shot (robustez temporal — NeuroBench no la cubrió).
2. Reformularlo como **Prototipado**: el banco de evaluación reproducible + la demo de trayectorias como producto de software — el aporte es LA HERRAMIENTA, los resultados la validan.
3. Fusionarlo aquí: los decodificadores (convencional y SNN) como cargas de trabajo del caso de estudio del tema 28.
