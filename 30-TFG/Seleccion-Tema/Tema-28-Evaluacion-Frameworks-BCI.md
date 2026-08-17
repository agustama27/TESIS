# Tema 28 — Resiliencia de pipelines BCI mediante inyección de fallos ("BCI Reliability Engineering")

> Estado: 🎯 **CANDIDATO PRINCIPAL** · decisión de tema preliminar, ver [[../../00-Sistema/Decisiones|D-004]] · reorganizado 2026-08-17 para eliminar la ambigüedad entre formulaciones (la original quedó abajo, en Historia).
> **Formulación vigente**: [[Propuesta-Reformulacion-Tema-28]] (3 RQs, supuestos, fault models, dataset, escalera de PoCs) — auditada y aceptada como versión de trabajo, **condicionada al PoC**. La identidad definitiva se consolida cuando la escalera de PoCs pase (§35 de la propuesta).

## La idea en palabras simples

Los laboratorios que investigan interfaces cerebro-computadora dependen de software open source (LSL, BciPy, MEDUSA…) que transporta y procesa señal neural en tiempo real, y que **declara** tolerar desconexiones, retrasos y pérdida de datos. Nadie verificó esas promesas de forma independiente y cuantitativa, ni midió qué pasa con la **decisión final de la BCI** cuando algo falla en el camino. Esta tesis hace el crash test: reproduce señal EEG pública como stream en tiempo real, **inyecta fallos controlados** (pérdida de muestras, jitter, retraso, desconexión) y mide cómo se propagan por el pipeline hasta el decodificador — ¿el sistema avisa, se recupera, o falla en silencio?

Es la analogía del crash test: los autos declaran ser seguros; alguien tiene que chocarlos contra la pared con método y publicar los resultados.

## Formulación vigente (resumen — el detalle completo está en la propuesta)

- **Título de trabajo**: *Evaluación de resiliencia de pipelines BCI en tiempo real mediante inyección de fallos y análisis de propagación hacia la decodificación*.
- **Unidad de análisis**: el pipeline BCI como sistema de software (NO un ranking de frameworks).
- **Pregunta central**: ¿cómo se propagan fallos controlados del streaming de señales EEG hacia las propiedades operativas y el desempeño funcional de un pipeline BCI, y en qué medida la telemetría permite detectar o anticipar esa degradación?
- **3 RQs falsables**: propagación del fallo · discrepancia infraestructura-función (sin presuponer silent failures) · valor de un detector ML de telemetría multivariable contra baseline de reglas (resultado negativo válido).
- **Núcleo ejecutable en 4 meses**: 1 banco Software-in-the-Loop (replay MNE-LSL + inyectores + telemetría) · 1 pipeline de referencia (BNCI2014_001 vía MOABB, CSP+LDA) · 3-4 familias de fallos · métricas de sistema Y de decodificador. Un segundo framework solo como validez externa, después del PoC.
- **Tipo/línea**: Trabajo de Investigación · Transformación Digital (el testbed es instrumento experimental, no producto).

## Definiciones Iniciales (formato oficial — según el Word generado el 2026-08-16)

El Word entregable es `Tamagusuku_Agustin - Trabajo de Investigacion - Tema 28 Resiliencia.docx`. Su contenido:

- **Tipo**: ☑ Trabajo de Investigación · **Línea**: ☑ Transformación Digital

### Título tentativo

Evaluación de resiliencia de frameworks de código abierto para interfaces cerebro-computadora mediante inyección de fallos

### Pregunta de investigación

¿Cómo se comportan los frameworks BCI de código abierto ante fallas realistas de la capa de software (pérdida de muestras, desconexiones, jitter, deriva de reloj): las detectan, las informan y se recuperan según lo que declaran? ¿Cómo se propagan esas fallas a la precisión del decodificador que consume la señal?

### Revisión de literatura (4 citas verificadas)

1. *A comprehensive benchmarking analysis of fault recovery in stream processing frameworks*. (2024). arXiv. https://arxiv.org/abs/2404.06203
2. *An open-source human-in-the-loop BCI research framework: method and design*. (2023). *Frontiers in Human Neuroscience*. https://doi.org/10.3389/fnhum.2023.1129362
3. *PyNoetic: A modular python framework for no-code development of EEG brain-computer interfaces*. (2025). *PLOS One*. https://doi.org/10.1371/journal.pone.0327791
4. *The lab streaming layer for synchronized multimodal recording*. (2024). *Imaging Neuroscience*. https://doi.org/10.1162/IMAG.a.136

> Nota: el título del Word usa "frameworks" (nivel presentación-de-idea); el título de trabajo interno usa "pipelines" (formulación refinada). Son compatibles: el pipeline se construye sobre esos frameworks. El refinamiento fino va en la Entrega 1 si el tutor aprueba.

## Evidencia de adopción del ecosistema open source (verificada 2026-08-17)

La afirmación "los laboratorios BCI dependen de software open source" fue cuestionada por el autor y verificada contra fuentes:

- **LSL — fidelidad ALTA (estándar de facto)**: el paper de LSL (PMC12434378) reporta **>2.300 menciones en artículos científicos** (a mediados de 2025), **>150 clases de dispositivos compatibles**, **>100 aplicaciones cliente**, integración en BCI2000, OpenViBE, NeuroPype, Open Ephys, MNE-Python, Timeflux, MEDUSA y Dareplane, adopción comercial (iMotions, BrainProducts) y bindings en 8+ lenguajes. ⚠️ Cifras autoreportadas por los autores de LSL — citarlas como "según el paper de LSL".
- **BciPy/MEDUSA — fidelidad MEDIA (frameworks académicos de nicho)**: son frameworks publicados (BciPy: arXiv 2002.06642; MEDUSA: ScienceDirect S016926072300024X) y activos, pero de comunidades chicas (tabla de salud GitHub: 155⭐ y 22⭐). NO afirmar que "los laboratorios dependen de BciPy/MEDUSA".
- **Formulación correcta para la tesis y las presentaciones**: *"la investigación BCI se apoya en un ecosistema open source cuyo estándar de facto de transporte es LSL (>2.300 menciones científicas según sus autores); la capa de aplicación la cubren frameworks académicos más chicos y fragmentados (BciPy, MEDUSA, Timeflux…)"*. La fragmentación de esa capa es en sí misma parte de la motivación del estudio.

## El hueco, formulado con precisión (verificado)

La literatura de "robustez BCI" evalúa modelos frente a ruido en la señal. Sobre la capa de software: el paper de LSL (PMC12434378, verificado por fetch 2026-08-16) declara mecanismos de reconexión y stress-tests con desconexiones, **pero sin métricas cuantitativas** (sin tasas de pérdida ni tiempos de recuperación; pruebas formales solo en condiciones ideales) y **sin medir jamás el impacto sobre el decodificador**. → El hueco es: **verificación independiente y cuantitativa de lo autodeclarado + propagación de la falla a la decodificación**. La frase absoluta "nadie evaluó la capa de software" NO debe usarse. Es el mismo molde que Secure LSL (<5% de overhead autoreportado → la verificación independiente es el aporte).

## Auditoría externa (2026-08-16) — resumen

Un segundo agente de IA auditó el repo; sus aportes se verificaron antes de aceptarse:

- ✔ **Corrección del hueco** (verificada contra PMC12434378) — incorporada arriba.
- ✔ **Recorte de alcance** — incorporado en la formulación vigente. Fuera del núcleo: ISO 25010 integral, 7 frameworks, DX study, escala intracortical, SNN, cifrado, neuroderechos → antecedentes o trabajo futuro.
- ✔ **Prueba de humo v3**: escalera de 4 PoCs ([[Propuesta-Reformulacion-Tema-28]] §22-23) — reemplaza al "hola mundo". Si dataset+decoder+replay+una perturbación+telemetría+consecuencia medible funcionan → tema técnicamente viable, decisión prácticamente cerrada.
- ✗ **Rechazado**: reabrir la comparación 28 vs 20 vs 19 — tres señales independientes convergen en la familia 28; el mecanismo de cierre es el PoC + el tutor.

## Refuerzos desde la investigación de carrera (2026-08-16)

Del [[../../20-Investigacion/Oportunidades-Neurotech-Para-Ingenieros-Software|mapa de oportunidades neurotech]]:

1. **Antecedente para la RQ3 (capa IA)**: ENFOR-SA — fault injection para evaluar confiabilidad de DNNs (https://arxiv.org/pdf/2602.00909) ⚠️ SIN VERIFICAR (leer en Mes 1 antes de citar).
2. **Munición regulatoria para la justificación**: la FDA clasifica el software de BCI implantadas como "major level of concern" (guidance 2021) e IEC 62304 exige V&V en todo el ciclo de vida. ⚠️ Verificar textos antes de citar.
3. **Trabajo futuro declarado**: closed-loop con el modelo en el lazo (candidato a tema de maestría) · neuroseguridad (fallos maliciosos) · extensión hardware-in-the-loop.

**Nota de motivación (2026-08-16)**: al leer "confiabilidad de pipelines ML mediante fault injection" como área futura, el autor lo marcó como lo que más le interesó — sin registrar que es su propia tesis con otras palabras. El tema elegido y el interés espontáneo coinciden.

---

# Historia — formulación original (SUPERADA, conservada por contexto)

> Todo lo que sigue es la versión previa del tema (comparación arquitectónica). Se conserva porque documenta el razonamiento y contiene material reutilizable en antecedentes/motivación, pero **ya no describe la tesis**.

## Formulación original: evaluación arquitectónica comparativa

Existen al menos siete frameworks open source para construir sistemas BCI (Timeflux, BciPy, MEDUSA, OpenViBE, BCI2000, NeuXus, PyNoetic…). Cada uno promete cosas distintas, cada paper elogia el suyo, y nadie los comparó sistemáticamente. La idea original: evaluarlos con método de ingeniería de software — atributos de calidad ISO/IEC 25010, benchmarks de rendimiento, developer experience medible y un caso de estudio implementado en los finalistas — y producir la guía de decisión que el campo no tiene.

**Por qué se superó**: intentaba demasiadas cosas a la vez (ISO 25010 + 7 frameworks + DX + benchmark + stress intracortical), la pregunta "¿cuál es mejor?" empuja a un ranking arbitrario, y la contribución de investigación quedaba difusa. La energía correcta de esa idea sobrevive en la formulación vigente con el pipeline como unidad de análisis.

## El gancho Neuralink / era intracortical (demovido a motivación y trabajo futuro)

La era que Neuralink inauguró es de datos intracorticales: 1.024 canales a ~30.000 Hz — tres órdenes de magnitud más caudal que el EEG para el que nació el ecosistema abierto. Los datos de esa escala ya son públicos (Stanford/Willett, FALCON). La pregunta "¿está el software abierto preparado para la era de los implantes?" es potente como **motivación y trabajo futuro**, pero NO condiciona el experimento del TFG: cambia la escala, introduce otra modalidad y amenaza el alcance. La respuesta a la objeción "la industria hará su propio software" se conserva: el usuario del ecosistema abierto es la ciencia (validación, replicación, formación), los datos de implante ya son públicos, y cada era de cómputo maduró sobre infraestructura abierta (Unix→Linux, PyTorch bajo toda la IA actual).

## Sinergia SNN (opcional, conservada)

El caso de estudio puede incluir un decodificador convencional Y uno de impulsos como cargas de trabajo — el interés del autor por las SNN sobrevive sin cargar con su justificación. Hoy: fuera del núcleo; posible extensión.

## Relación con los temas vecinos (respuestas del 2026-08-15)

**¿El tema 7 (construir un SDK nuevo) es buena tesis? → NO en su forma original.** El espacio está lleno: siete frameworks activos, incluido uno no-code publicado en 2025 (PyNoetic). Construir el octavo sin demostrar que los existentes fallan sería scope creep puro. La forma correcta de esa energía es este tema: primero se evalúa lo que hay.

**¿Qué aporte queda para el 25 (SNN)?** → Ver [[Tema-25-ESTADO-CONSOLIDADO]]: extensión FALCON multi-sesión, reformulación como Prototipado del banco de evaluación, o fusión aquí como carga de trabajo del caso de estudio.

## Tabla de salud del ecosistema (2026-08-16, dato del estudio)

BciPy y MEDUSA activos · LSL activo · Timeflux posiblemente estancado (~20 meses sin push) — la fragmentación y ese estancamiento son en sí mismos el argumento de que hace falta evaluación sistemática. Detalle en [[Sprint-Descubrimiento-Frameworks]] sección 1.

## Enlaces

[[Propuesta-Reformulacion-Tema-28]] · [[Sprint-Descubrimiento-Frameworks]] · [[../../20-Investigacion/Calibracion-Alcance-Tesis-BCI|Calibración]] · [[../../20-Investigacion/Que-Es-Un-Framework-BCI|Qué es un framework BCI]] · [[00-Indice]]
