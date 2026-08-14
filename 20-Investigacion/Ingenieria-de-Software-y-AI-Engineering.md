# Ingeniería de Software y AI Engineering — informe de estudio

> Nota de investigación · 2026-08-14 · material de preparación para la reunión con el tutor
> Complementa: [[Decodificacion-Brain-to-Text]] (el tema) y [[Temas-Candidatos-TFG]] (el ranking)
> **Cómo usar este documento**: Etapa 1 te da el marco teórico (estudialo), Etapa 2 lo mapea a tu tesis (memorizá la tabla), Etapa 3 es el simulacro de la reunión (practicalo en voz alta).

---

## La tesis central, en una frase

**AI Engineering es la especialización de la Ingeniería de Software que trata a los datos y a los modelos como artefactos de primera clase** — con su propio ciclo de vida, su propia deuda técnica y sus propias prácticas de calidad. No es una disciplina vecina: es Ingeniería de Software aplicada al tipo de sistema que domina esta década.

Esto no es una opinión mía: es la posición de la literatura académica top del área de Ingeniería de Software (ICSE, TOSEM, NeurIPS). Abajo está la evidencia.

---

## Etapa 1 — El marco: qué dice la literatura

### 1.1 Sculley et al. (2015) — "Hidden Technical Debt in Machine Learning Systems" (NeurIPS)

**El paper más citado sobre por qué los sistemas ML son un problema de INGENIERÍA.** Escrito por ingenieros de Google. Su figura más famosa muestra que en un sistema ML real, el código del modelo es una **caja diminuta** rodeada de infraestructura enorme: configuración, recolección de datos, features, gestión de recursos, serving, monitoreo.

Conceptos que tenés que dominar (van a salir en cualquier conversación seria):

- **Deuda técnica oculta**: los sistemas ML acumulan costos de mantenimiento masivos y silenciosos, peores que el software tradicional.
- **CACE — "Changing Anything Changes Everything"**: en ML nada es modular de verdad; cambiar un feature o un hiperparámetro cambia el comportamiento de todo el sistema. La modularidad — pilar de la Ing. de Software clásica — se erosiona.
- **Entanglement (entrelazamiento)**: los modelos mezclan señales de formas que impiden aislar componentes.
- **Data dependencies**: las dependencias de DATOS son más costosas que las de código, y no hay compilador que las detecte.
- **Hidden feedback loops**: el sistema influye sobre los datos que después consume.
- **Glue code y pipeline jungles**: el 95% del código de un sistema ML es plomería, no modelo.

**Por qué te sirve**: es la demostración canónica de que hacer ML en serio ES un problema de Ingeniería de Software. Publicada en la conferencia top de ML, escrita por Google.

### 1.2 Amershi et al. (2019) — "Software Engineering for Machine Learning: A Case Study" (ICSE)

**El estudio de Microsoft Research sobre cómo sus equipos integran ML en procesos de Ingeniería de Software.** Publicado en ICSE, LA conferencia de Ingeniería de Software. Casi 1.000 citas.

- Define el **workflow de 9 etapas** del ML en producción: requisitos del modelo → recolección de datos → limpieza → etiquetado → feature engineering → entrenamiento → **evaluación** → **despliegue** → **monitoreo**. (Fijate: tu tesis vive en las etapas 6-7, las más "de ingeniería" del workflow.)
- Documenta que los equipos de Microsoft integraron ese workflow **dentro de sus procesos ágiles existentes** — el ML no reemplazó a la Ing. de Software: se le subordinó.
- Identifica las **3 diferencias fundamentales** del dominio AI respecto del software tradicional:
  1. **Descubrir, gestionar y versionar DATOS** es mucho más complejo que versionar código.
  2. La construcción de modelos exige **habilidades distintas** que deben integrarse a los equipos de software.
  3. Los componentes de AI son **más difíciles de modularizar** que los componentes de software tradicionales (los modelos se "entrelazan" y su error no es monotónico).

**Por qué te sirve**: si tu tutor duda de que ML sea tema de Ingeniería en Software, este paper de ICSE — el techo académico de la disciplina — zanja la discusión.

### 1.3 Kreuzberger, Kühl y Hirschl (2023) — "MLOps: Overview, Definition, and Architecture" (IEEE Access)

**La formalización académica de MLOps** — la práctica que la industria inventó para operacionalizar ML. Con revisión de literatura, revisión de herramientas y entrevistas a expertos, define:

- **Principios**: CI/CD extendido a modelos (y **CT: continuous training**), versionado de datos y modelos, tracking de experimentos, reproducibilidad, monitoreo en producción.
- **Componentes de arquitectura**: feature stores, registros de modelos, pipelines de entrenamiento automatizados, serving.
- **Roles**: el **ML Engineer / AI Engineer** aparece formalmente definido como rol de ingeniería — el puente entre data science y operaciones.
- Dato clave que cita el paper: la mayoría de los proyectos ML **fallan en llegar a producción** — y la causa es de ingeniería (operacionalización), no de ciencia.

**Por qué te sirve**: le pone nombre, definición y arquitectura de referencia al trabajo que vos ya hacés como AI Engineer — y demuestra que es un campo de ingeniería con literatura propia.

### 1.4 Martínez-Fernández et al. (2022) — "Software Engineering for AI-Based Systems: A Survey" (ACM TOSEM)

**El mapeo sistemático del campo SE4AI**: 248 estudios entre 2010 y 2020, publicado en la revista top de Ingeniería de Software (TOSEM).

- Consolida "SE4AI" (Software Engineering **for** AI) como subcampo académico establecido, con líneas en: pipelines de datos, gestión del ciclo de vida de modelos, despliegue, monitoreo, robustez y gobernanza.
- Las propiedades más estudiadas de los sistemas basados en AI son **dependability y safety** — es decir, atributos de calidad CLÁSICOS de la Ingeniería de Software aplicados a sistemas con AI.

**Por qué te sirve**: prueba que existe un cuerpo académico completo (248 papers) dedicado exactamente a la intersección donde vive tu tesis. No estás inventando un encuadre: estás entrando a un campo con nombre.

### 1.5 Síntesis de la Etapa 1 (memorizable)

> La Ingeniería de Software clásica gestiona la complejidad del CÓDIGO. La AI Engineering gestiona además la complejidad de los DATOS y los MODELOS — artefactos que se degradan, se entrelazan y cambian con el mundo. Google lo demostró con la deuda técnica oculta (2015), Microsoft lo integró a sus procesos y lo publicó en ICSE (2019), la industria lo operacionalizó como MLOps (2023) y la academia lo consolidó como el subcampo SE4AI con 248 estudios (2022). Mi tesis se para exactamente ahí.

---

## Etapa 2 — El mapeo: tu tesis brain-to-text como sistema de software

Esta tabla es el corazón del argumento. Cada disciplina de la carrera tiene su instancia CONCRETA en la tesis:

| Disciplina de Ing. de Software | Instancia en la tesis brain-to-text |
|---|---|
| **Ingeniería de requisitos** | Requisitos no funcionales cuantificados: WER objetivo (<10% en 50 palabras), latencia de inferencia compatible con tiempo real, presupuesto de cómputo (Colab Pro) |
| **Arquitectura de software** | El pipeline RNN → fonemas → language model es una arquitectura de componentes con contratos: la ablación de la tesis es literalmente un ANÁLISIS DE ARQUITECTURA (¿qué componente aporta qué?) |
| **Testing y V&V** | Splits oficiales del benchmark, validación contra resultados publicados (reproducción del baseline = test de regresión científico), métricas CER/WER |
| **Gestión de configuración** | Versionado de experimentos, seeds, configs — el "experiment tracking" de MLOps es gestión de configuración aplicada a ML |
| **Mantenimiento y evolución** | El **drift neural entre sesiones** es un caso de libro del "changing external world" de Sculley: el mismo problema de concept drift que enfrenta cualquier sistema ML en producción, con el cerebro como fuente de datos |
| **Calidad / atributos** | Dependability del decodificador (el usuario DEPENDE del sistema para comunicarse — falla = silencio), reproducibilidad como requisito de primera clase |
| **MLOps / CT** | La "calibración rápida" de Card 2024 (99,6% en 30 min) ES continuous training: reentrenar con mínimo dato nuevo — el problema central de MLOps en su versión más extrema |
| **Deuda técnica** | Los datos intracorticales exigen pipelines de preprocesamiento (spike band power, bins, sincronización) — el glue code de Sculley, que la tesis debe diseñar limpio |

**El párrafo puente para decírselo al tutor** (practicalo):

> "Mi tesis no estudia el cerebro — estudia el SOFTWARE que decodifica sus señales. El pipeline brain-to-text tiene requisitos no funcionales cuantificados, una arquitectura de componentes que voy a analizar por ablación, un protocolo de testing contra un benchmark internacional, y el mismo problema de concept drift que cualquier sistema ML en producción. Cada capítulo de mi trabajo mapea a una disciplina de la carrera. La neurociencia es el dominio de aplicación, igual que la banca lo es para una tesis de fintech."

---

## Etapa 3 — Guía de estudio para la reunión

### 3.1 Los 12 conceptos que tenés que poder explicar (una línea cada uno)

1. **BCI intracortical**: electrodos DENTRO de la corteza (vs EEG sobre el cuero cabelludo) — más señal, requiere cirugía; los datos ya existen públicos.
2. **Spike / threshold crossing**: el "evento" eléctrico de una neurona; la señal cruda de la que se decodifica.
3. **Corteza motora**: de ahí se graba — el paciente INTENTA hablar/escribir y la intención motora se decodifica.
4. **RNN (GRU)**: red recurrente que mapea ventanas de actividad neural a fonemas/caracteres; el caballo de batalla del campo.
5. **Language model / rescoring**: el corrector estadístico que convierte fonemas ruidosos en texto plausible — la mitad del sistema.
6. **WER / CER**: word/character error rate — LAS métricas del campo (como accuracy en clasificación).
7. **Ablación**: quitar/cambiar UN componente y medir el impacto — el método experimental de tu tesis.
8. **Drift neural**: la señal cambia entre sesiones/días — el concept drift de tu sistema.
9. **CACE (Sculley)**: en ML, cambiar cualquier cosa cambia todo — por qué el ML necesita ingeniería.
10. **Workflow de 9 etapas (Amershi)**: el proceso estándar de ML en producción; tu tesis vive en evaluación y despliegue.
11. **MLOps / continuous training**: operacionalizar ML; la calibración rápida de Card 2024 es su versión extrema.
12. **SE4AI**: el subcampo académico (248 estudios, TOSEM 2022) donde tu tesis se inscribe formalmente.

### 3.2 Los números memorizables

| Número | Qué es | Fuente |
|---|---|---|
| 90 char/min, 94,1% | Handwriting BCI, récord 2021 | Willett 2021, Nature |
| 62 palabras/min | Speech BCI 2023, 3,4× el récord anterior | Willett 2023, Nature |
| 23,8% WER en 125.000 palabras | Primera decodificación de vocabulario abierto | Willett 2023 |
| 99,6% con 30 min de calibración; 97,5% sostenida | Estado del arte clínico | Card 2024, NEJM |
| 9,7% → 8,0% WER | Mejora del baseline SOLO por mejor entrenamiento | Benchmark '24 |
| Transformers NO superan a la RNN | La pregunta abierta que tu tesis ataca | Benchmark '24 (arXiv 2412.17227) |
| USD 3,4 → 6,5 mil millones (2025→2030) | Mercado BCI, CAGR 18% | Grand View Research |
| 1.000 oraciones / 10,7 hs de señal | Tamaño del dataset handwriting público | Dryad wh70rxwmv |

### 3.3 Simulacro: preguntas del tutor y respuestas modelo

**P1. "¿Esto no es una tesis de neurociencia o de medicina?"**
> No. Los datos neuronales ya existen, son públicos y fueron recolectados por Stanford bajo sus protocolos clínicos. Mi trabajo empieza donde termina el quirófano: es el software de decodificación — modelos de secuencia, integración con language models, evaluación reproducible. Es la misma división de trabajo del campo real: los cirujanos implantan, los ingenieros de software decodifican. Y la literatura de Ingeniería de Software (ICSE, TOSEM) reconoce formalmente este tipo de sistema como objeto de estudio propio: se llama SE4AI.

**P2. "¿Qué vas a hacer exactamente, en concreto?"**
> Cuatro fases: (1) marco teórico y dominio de los datasets públicos; (2) reproducir el baseline RNN del Brain-to-Text Benchmark — un resultado publicado en Nature — y validar contra sus números; (3) mi experimento: ablación sistemática del language model (¿cuánto decodifica la red vs cuánto corrige el LM?) y comparación GRU vs Transformer con presupuesto idéntico; (4) análisis de errores, redacción y publicación del código. Cada fase tiene entregable verificable.

**P3. "¿Y si no lográs mejorar el estado del arte?"**
> No necesito mejorarlo: mi pregunta es de CARACTERIZACIÓN, no de récord. La ablación responde cuánto aporta cada componente — eso es conocimiento nuevo aunque ningún número récord caiga. Y reproducir el baseline ya es un resultado: la crisis de reproducibilidad hace que una reproducción independiente documentada tenga valor académico propio.

**P4. "¿Es viable en 4 meses con los recursos que tenés?"**
> Sí, por diseño: datasets públicos (cero logística), código de referencia público (el del paper y el del segundo puesto del benchmark), GPU de Colab Pro suficiente para el baseline, y un alcance explícitamente acotado — baseline + ablación, no ganar el leaderboard. El riesgo mayor es la curva de aprendizaje de los datos intracorticales, y está presupuestado en el Mes 1.

**P5. "¿Dónde está la originalidad si usás datos y código de otros?"**
> En el mismo lugar donde está en la mayoría de la ciencia computacional: en la PREGUNTA y el DISEÑO EXPERIMENTAL, no en los datos. El propio benchmark dejó documentada la pregunta abierta — por qué los Transformers no superan a la RNN acá — y nadie publicó la ablación sistemática arquitectura-vs-language-model. Además el análisis se hace con protocolo reproducible publicado, que es exactamente lo que el campo pide.

**P6. "¿Por qué esta línea temática (Transformación Digital)?"**
> Porque es tecnología que devuelve capacidad digital — la comunicación — a quienes la perdieron por completo. Si restituir el acceso a la comunicación digital a una persona con ELA no es transformación digital, nada lo es. Y el mercado lo confirma: la industria BCI crece al 18% anual hacia los USD 6,5 mil millones en 2030.

**P7. "¿Qué te deja esto a vos profesionalmente?"**
> Tres cosas: competencias de AI Engineering de frontera (secuencias, LLM rescoring, evaluación rigurosa) que son transferibles a cualquier industria; un antecedente concreto en neurotecnología para maestría o trabajo en el área — es el problema exacto que trabajan Neuralink y BrainGate; y un trabajo publicable en el repositorio institucional y potencialmente en Ciencia y Técnica.

**P8. "¿Qué es lo que MÁS puede salir mal?"** *(honestidad = credibilidad)*
> Dos riesgos reales: que la curva de aprendizaje de los datos intracorticales me consuma más del mes presupuestado — mitigación: el código de referencia público y la comunidad del benchmark; y que el entrenamiento del dataset de habla exceda mi GPU — mitigación: empezar por el dataset de handwriting (más chico) y escalar. Ninguno compromete la tesis completa porque el diseño es incremental: cada fase deja un resultado defendible.

### 3.4 Orden de lectura sugerido (≈ 6-7 horas de estudio total)

1. **[[Decodificacion-Brain-to-Text]]** (la nota del vault) — 30 min. El panorama completo.
2. **Sculley et al. 2015** — 1 h. Leé completo; es corto y cambia cómo ves los sistemas ML. Quedate con la figura del "modelo como caja chica" y CACE.
3. **Brain-to-Text Benchmark '24 Lessons** (arXiv 2412.17227) — 1 h. TU paper guía: de acá sale la pregunta de la tesis.
4. **Amershi et al. 2019** — 1 h (secciones 1-4 alcanzan). Quedate con el workflow de 9 etapas y las 3 diferencias.
5. **Willett et al. 2023** (Nature) — 1,5 h de lectura selectiva: abstract, figuras, métodos de decodificación. No te pierdas en la neurociencia.
6. **Kreuzberger 2023** — 45 min de lectura diagonal: definición de MLOps, principios, roles.
7. **Repasar 3.1, 3.2 y 3.3 de esta nota en voz alta** — 45 min. Si podés explicar los 12 conceptos sin leer, estás listo.

---

## Referencias (APA — todas verificadas)

- Amershi, S., Begel, A., Bird, C., DeLine, R., Gall, H., Kamar, E., Nagappan, N., Nushi, B., y Zimmermann, T. (2019). Software engineering for machine learning: A case study. En *2019 IEEE/ACM 41st International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP)* (pp. 291-300). IEEE. https://www.microsoft.com/en-us/research/wp-content/uploads/2019/03/amershi-icse-2019_Software_Engineering_for_Machine_Learning.pdf
- Card, N. S., et al. (2024). An accurate and rapidly calibrating speech neuroprosthesis. *New England Journal of Medicine*. ⚠️ Completar volumen/páginas/DOI antes de citar en el TFG (estudio verificado vía UC Davis Health y PMC11030484).
- Kreuzberger, D., Kühl, N., y Hirschl, S. (2023). Machine learning operations (MLOps): Overview, definition, and architecture. *IEEE Access*, *11*, 31866-31879. https://arxiv.org/abs/2205.02302
- Martínez-Fernández, S., Bogner, J., Franch, X., Oriol, M., Siebert, J., Trendowicz, A., Vollmer, A. M., y Wagner, S. (2022). Software engineering for AI-based systems: A survey. *ACM Transactions on Software Engineering and Methodology*, *31*(2). https://doi.org/10.1145/3487043
- Sculley, D., Holt, G., Golovin, D., Davydov, E., Phillips, T., Ebner, D., Chaudhary, V., Young, M., Crespo, J. F., y Dennison, D. (2015). Hidden technical debt in machine learning systems. En *Advances in Neural Information Processing Systems 28 (NeurIPS 2015)*. https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems
- Willett, F. R., Avansino, D. T., Hochberg, L. R., Henderson, J. M., y Shenoy, K. V. (2021). High-performance brain-to-text communication via handwriting. *Nature*, *593*, 249-254. https://doi.org/10.1038/s41586-021-03506-2
- Willett, F. R., et al. (2023). A high-performance speech neuroprosthesis. *Nature*, *620*(7976), 1031-1036. https://doi.org/10.1038/s41586-023-06377-x
- Willett, F. R., et al. (2024). Brain-to-Text Benchmark '24: Lessons learned. *arXiv*. https://arxiv.org/abs/2412.17227

## Enlaces

[[Decodificacion-Brain-to-Text]] · [[Temas-Candidatos-TFG]] · conceptos a desarrollar: [[CACE]], [[MLOps]], [[Drift-neural]], [[Ablacion]]
