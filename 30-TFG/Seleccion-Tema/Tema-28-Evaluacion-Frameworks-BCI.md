# Tema 28 — Resiliencia de pipelines BCI mediante inyección de fallos ("BCI Reliability Engineering")

> Estado: 🎯 **CANDIDATO PRINCIPAL** · decisión de tema preliminar, ver [[../../00-Sistema/Decisiones|D-004]] · reorganizado 2026-08-17 para eliminar la ambigüedad entre formulaciones (la original quedó abajo, en Historia).
> **Formulación vigente**: [[Propuesta-Reformulacion-Tema-28]] (3 RQs, supuestos, fault models, dataset, escalera de PoCs) — auditada y aceptada como versión de trabajo, **condicionada al PoC**. La identidad definitiva se consolida cuando la escalera de PoCs pase (§35 de la propuesta).

## La idea en palabras simples

Los laboratorios que investigan interfaces cerebro-computadora dependen de software open source (LSL, BciPy, MEDUSA…) que transporta y procesa señal neural en tiempo real, y que **declara** tolerar desconexiones, retrasos y pérdida de datos. Nadie verificó esas promesas de forma independiente y cuantitativa, ni midió qué pasa con la **decisión final de la BCI** cuando algo falla en el camino. Esta tesis hace el crash test: reproduce señal EEG pública como stream en tiempo real, **inyecta fallos controlados** (pérdida de muestras, jitter, retraso, desconexión) y mide cómo se propagan por el pipeline hasta el decodificador — ¿el sistema avisa, se recupera, o falla en silencio?

Es la analogía del crash test: los autos declaran ser seguros; alguien tiene que chocarlos contra la pared con método y publicar los resultados.

## Formulación vigente (resumen — el detalle completo está en la propuesta)

- **Título oficial (elegido 2026-08-17, el que va al tutor)**: *Interfaces cerebro-computadora bajo condiciones adversas: del software a la decodificación*. Molde: [objeto] bajo [condición]: [recorrido medido]. El "del software a la decodificación" declara la cadena completa sin gastar palabras en "evaluación" ni "impacto".
- **Unidad de análisis**: el pipeline BCI como sistema de software (NO un ranking de frameworks).
- **Pregunta central**: ¿cómo se propagan fallos controlados del streaming de señales EEG hacia las propiedades operativas y el desempeño funcional de un pipeline BCI, y en qué medida la telemetría permite detectar o anticipar esa degradación?
- **3 RQs falsables**: propagación del fallo · discrepancia infraestructura-función (sin presuponer silent failures) · valor de un detector ML de telemetría multivariable contra baseline de reglas (resultado negativo válido).
- **Núcleo ejecutable en 4 meses**: 1 banco Software-in-the-Loop (replay MNE-LSL + inyectores + telemetría) · 1 pipeline de referencia (BNCI2014_001 vía MOABB, CSP+LDA) · 3-4 familias de fallos · métricas de sistema Y de decodificador. Un segundo framework solo como validez externa, después del PoC.
- **Tipo/línea**: Trabajo de Investigación · Transformación Digital (el testbed es instrumento experimental, no producto).

## Definiciones Iniciales — ENTREGABLE OFICIAL (regenerado 2026-08-17)

**Archivo**: `Tamagusuku_Agustin - Trabajo de Investigacion.docx` — nombre según exige la plantilla oficial (`<<Apellido_Nombre - Tipo TFG>>.docx`). Adaptado al PDF *"Selección Tema TFG - Seminario Final - ING SOFT"*: Arial 12, A4, interlineado 1,5, todas las secciones con sus conteos de renglones respetados (3 / 5-15 / 3-5 / 15-20) y el campo "Nombre del archivo" que faltaba. Contenido alineado con la formulación vigente (pipelines, no ranking de frameworks). Antes de enviar: completar **Documento** y **Legajo**.

- **Tipo**: ☒ Trabajo de Investigación · **Línea**: ☒ Transformación Digital

### Título tentativo (10 palabras, elegido por el autor el 2026-08-17)

Interfaces cerebro-computadora bajo condiciones adversas: del software a la decodificación

### Pregunta de investigación

¿Cómo se propagan fallos controlados de la capa de transporte de señal —pérdida de muestras, jitter, retraso y desconexión— hacia las propiedades operativas y el desempeño funcional de un pipeline BCI en tiempo real? ¿Existen condiciones en las que la infraestructura permanece operativa mientras la decodificación se degrada, y en qué medida la telemetría del sistema permite detectar o anticipar esa degradación?

### Revisión de literatura (4 citas — autores verificados 2026-08-17)

1. Kothe, C., Shirazi, S. Y., Stenner, T., Medine, D., Boulay, C., Grivich, M. I., Artoni, F., Mullen, T., Delorme, A., y Makeig, S. (**2025**). The lab streaming layer for synchronized multimodal recording. *Imaging Neuroscience, 3*. https://doi.org/10.1162/IMAG.a.136
2. Vogel, A., Henning, S., Perez-Wohlfeil, E., Ertl, O., y Rabiser, R. (2024). A comprehensive benchmarking analysis of fault recovery in stream processing frameworks. *arXiv*. https://arxiv.org/abs/2404.06203
3. Natella, R., Cotroneo, D., y Madeira, H. (2016). Assessing dependability with software fault injection: A survey. *ACM Computing Surveys, 48*(3), artículo 44. https://doi.org/10.1145/2841425
4. Gemborn Nilsson, M., Tufvesson, P., Heskebeck, F., y Johansson, M. (2023). An open-source human-in-the-loop BCI research framework: Method and design. *Frontiers in Human Neuroscience, 17*. https://doi.org/10.3389/fnhum.2023.1129362

> **Correcciones respecto de la versión anterior del Word**: el paper de LSL es de **2025** (vol. 3), no 2024 · las 4 citas ahora llevan autores (antes empezaban por el título) · entró el survey de fault injection de Natella et al. (fundamento metodológico de la disciplina) en lugar de PyNoetic, que era redundante con la cita de BCI-HIL.

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
