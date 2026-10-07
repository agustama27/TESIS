# Patrones de las tesis aprobadas con Jorge Humberto Cassi como tutor y cómo adaptar el TFG

> 2026-09-28 (sesión nocturna autónoma). Insumos: 45 TFG descargados del repositorio institucional con Cassi como `dc.contributor.advisor` (27 con texto útil, 16 de modalidad Trabajo de Investigación 2020-2025), el material oficial del SAM guardado en `Trabajo Final de Graduación-Notas/`, el reglamento institucional y el Entregable 2 v4 (35 págs.). Ver también [[Mejoras-Redaccion-M3]] y [[Trabajo-Futuro]].
>
> Material de respaldo: perfiles crudos de cada tesis (una ficha por trabajo, con estructura, extensiones, verbos de los objetivos y frases fórmula) en `30-TFG/_perfiles-tesis-cassi/`; informe de normativa con URLs en `30-TFG/_normativa-siglo21-cae.md`. Nada commiteado.
>
> **Advertencia de lectura.** Las tesis publicadas muestran lo que la CAE *aprobó*, no las observaciones que hizo antes de aprobar (ninguna las menciona). Sirven para conocer el *piso* que la comisión tolera y la *forma* a la que está acostumbrada. Tu trabajo está muy por encima de ese piso en rigor; el riesgo no es de fondo, es de **forma y legibilidad** para una comisión que corrige, año tras año, estudios descriptivos por encuesta.

## 1. Corpus

Los 45 ítems se obtuvieron por la API DSpace del repositorio (`/server/api/discover/search/objects?query=Cassi`), filtrando los que tienen a Cassi en `dc.contributor.advisor`. Los de 2014-2018 (otras carreras, o Proyectos de Aplicación Profesional de 100-160 págs.) se descartaron: son de otra época y otra plantilla. Quedan 27 de 2020 en adelante. La "tesis de Jazmín Roca (2025)" que aparecía en un buscador es la de GEE (Google Earth Engine); su portada dice noviembre de 2024. **La fecha del repositorio es la de carga, no la de la portada** (difieren hasta 18 meses): si citás alguna, usá la fecha de portada.

### 1.1 Trabajos de Investigación (16), los comparables

| Carga | Carrera | Autor/a | Título (abreviado) | Págs. | Diseño y muestra | Handle |
|---|---|---|---|---|---|---|
| 2021-11 | Ing. Software | Flores | Plataformas de posicionamiento interno para hogares inteligentes | 17 | **Documental**, 5 plataformas, sin humanos | ues21/22292 |
| 2021-11 | Ing. Software | Acevedo Daud | Gamificación en alumnos universitarios | 41 | Encuesta, N=37 | ues21/23110 |
| 2021-11 | Ing. Software | Gutiérrez | Usabilidad e inclusión en bancas online (ISO/IEC 25010) | 54 | Encuesta, N=225 | ues21/22620 |
| 2022-04 | Ing. Software | Leguizamón Prado | Plataforma Discord en adolescentes | 33 | Mixto, N=40+3 entrevistas | ues21/24209 |
| 2022-12 | Ing. Software | Quevedo | Herramientas digitales y autismo | 25 | Encuesta, N=50 | ues21/26309 |
| 2023-05 | Ing. Software | Tamargo | Eficacia funcional de asistentes virtuales | 43 | Encuesta, N=106 | ues21/27725 |
| 2023-06 | Ing. Software | Sarsotti | Plataformas digitales para personas sordas | 33 | Encuesta, N=36 | ues21/27948 |
| 2023-11 | Ing. Software | Cáceres | ChatGPT-3 en el desarrollo de software | 25 | Encuesta, N=50 | ues21/28785 |
| 2024-09 | Ing. Software | Ordenavía | Metodologías tradicionales y ágiles en empresas | 41 | Mixto, N=25 | ues21/29293 |
| 2025-03 | Ing. Software | Alem | Billeteras electrónicas en Córdoba | 42 | Encuesta, N=44 | ues21/30772 |
| 2025-04 | Ing. Software | Roca | Plataforma GEE en análisis geoespacial | 36 | Cualitativo, 6 entrevistas | ues21/30807 |
| 2025-05 | Ing. Software | Maurino | **Investigación documental** sobre criptografía | 35 | **Documental**, 3 libros, sin humanos, sin anexos | ues21/30801 |
| 2025-07 | Ing. Software | Martinez Calizaya | Plataforma Moodle | 38 | Encuesta, N=40 | ues21/30799 |
| 2021-04 | Lic. Informática | Gutierrez Puertas | Moodle en pandemia | 45 | Encuesta, N=104 | ues21/21467 |
| 2021-04 | Lic. Informática | Muchevicz | Transformación digital del INTA | 46 | Mixto, N=23 | ues21/21275 |
| 2021-11 | Lic. Informática | Antonio | Transformación digital en la industria financiera | 33 | Encuesta, N=35 | ues21/22699 |
| 2022-03 | Lic. Informática | Nuñez Leal | Tokens inmobiliarios en CABA | 36 | Encuesta, N=28 | ues21/24219 |
| 2022-06 | Lic. Informática | Icardi | Niños y dispositivos móviles | 33 | Encuesta, N=104 | ues21/24902 |
| 2022-06 | Lic. Informática | Peralta Montero | Enseñanza virtual en pandemia (Tucumán) | 43 | Encuesta, N=50 | ues21/24801 |
| 2022-11 | Lic. Informática | Krojzl | Tecnología en las aulas en pandemia | 29 | Encuesta, N=88 | ues21/26102 |
| 2022-11 | Lic. Informática | Villagra | Herramientas digitales para niños sordos | 45 | Encuesta, N=45 | ues21/26093 |
| 2023-12 | Lic. Informática | Alfonso | Usabilidad de la Biblioteca Virtual de Maestros | 40 | Encuesta, N=26 | ues21/29193 |

(Son 22 filas porque incluí las de Informática, carrera hermana con el mismo tutor y la misma plantilla. Las 13 de Ingeniería en Software son las que más pesan.)

### 1.2 Prototipados tecnológicos (5), descartados para la forma pero útiles como control

Fratini 2020 (Museos), Romero 2023, Catanzaro 2023 (sidra + blockchain), Dejtiar 2025 y Yudicello 2025 (los dos últimos de Ingeniería en Software). Siguen otra plantilla (Marco teórico → Relevamiento → Diagnóstico → Product Backlog → Seguridad → Costos → Riesgos → Conclusiones). Confirman que la plantilla IMRyD de las de investigación no es una costumbre del tutor sino de la modalidad.

### 1.3 Los dos precedentes que más te sirven

- **Maurino (2025), investigación documental sobre criptografía.** Sin participantes humanos, sin consentimiento, sin anexos; "Participantes" redefinido como corpus de documentos; cita a Grasso (1999) en vez de Sampieri para el muestreo; Resultados de 10 págs. organizados por variable. Aprobada. Es la prueba de que la CAE acepta una tesis sin encuesta y sin personas si Diseño y Análisis de datos están fundamentados.
- **Flores (2021), plataformas de posicionamiento interno.** 17 páginas en total, análisis documental de 5 plataformas, 2 tablas comparativas, referencias académicas en inglés, subtítulos de Métodos exactos (Diseño / Participantes / Instrumentos / Análisis de datos). Aprobada. Es la prueba de que la CAE acepta bibliografía en inglés y un objeto de estudio que es software, no gente.

## 2. Patrones invariantes (se cumplen en todas o casi todas las 22)

### 2.1 Portada
`Universidad Siglo 21` → `Trabajo Final de Grado` → `Trabajo de Investigación en Tecnologías Informáticas` → carrera → título (17 de 22 agregan el título en inglés; 8 de 13 en Ingeniería en Software) → autor/a → legajo → `Tutor: Ing. Jorge Humberto Cassi` → ciudad, mes y año. Nunca DNI (una excepción). Para los entregables de módulo la portada es la de la consigna (tema, legajo, materia, módulo, tutor, fecha), que es la que ya usás.

### 2.2 Preliminares (solo en la versión final, Módulo 4)
Índice (a veces índice de figuras y de tablas aparte) → Resumen (130-230 palabras) con **3 a 7 palabras clave** → Abstract con las mismas *keywords* en espejo. Agradecimientos en 5 de 22. Nunca hay citas en el Resumen.

### 2.3 Macroestructura
`Introducción → Métodos → Resultados → Discusión → Referencias → Anexos`. **Ninguna de las 22 tiene una sección "Conclusiones"**: la conclusión son los últimos párrafos de la Discusión. Esto coincide con el material oficial (IMRyD, Day 2005) y es lo primero que la CAE mira.

### 2.4 Introducción (4 a 14 págs., consigna ≈15)
1. Abre con una definición o cita de autor sobre el concepto central (18 de 22), o con un dato.
2. Antecedentes en prosa narrativa, autor-año, sin subtítulos (ninguna usa "Antecedentes" como subtítulo en la modalidad investigación).
3. Planteo del problema.
4. **Preguntas de investigación explícitas, 2 a 6, en la mayoría de los casos en viñetas** ("En base a lo expuesto surgen los siguientes interrogantes:"); en 5 de 22 quedan como preguntas retóricas dentro del texto. **Ninguna declara hipótesis.**
5. Justificación o relevancia, breve.
6. **Cierra siempre con el objetivo general (un párrafo, un verbo en infinitivo: determinar, evaluar, indagar, analizar, conocer) seguido de los objetivos específicos en viñetas, 2 a 6, cada uno con verbo en infinitivo.** Es el patrón más rígido de todo el corpus: 22 de 22.

### 2.5 Métodos (2 a 6 págs., consigna ≈3)
- Subsecciones en este orden, con estos nombres o variantes mínimas: **Diseño → Participantes (o "Población y muestra") → Instrumentos (o "Instrumento") → Análisis de datos**. Nadie agrega una subsección "Variables": las variables se definen dentro de Instrumentos o de Análisis de datos, mapeadas a preguntas.
- Etiquetas de Hernández Sampieri, citadas textualmente y a veces con página: "enfoque cuantitativo (o mixto), alcance descriptivo (o exploratorio), diseño no experimental, transversal". Las 22 son no experimentales. Autor citado: Hernández Sampieri, Fernández Collado y Baptista Lucio (2010 o 2014); la edición varía y nadie lo objetó.
- Muestreo no probabilístico por conveniencia o intencional, N chico (6 a 225), sin justificación estadística del tamaño (una excepción con fórmula muestral).
- Instrumento: Google Forms con Likert de 5 puntos en 16 de 22. Consentimiento informado descrito en el cuerpo y adjunto en Anexos en la mayoría.
- Análisis: porcentajes con Excel o el propio Forms. **Ninguna de las 22 usa estadística inferencial.**

### 2.6 Resultados (2 a 19 págs., consigna ≈5)
- Organizados por variable o por objetivo específico, **en el orden de los objetivos** (también lo exige el material oficial), con o sin subtítulos.
- Figuras y tablas: `Figura N. Título.` y debajo `Fuente: Elaboración propia.` (variantes de mayúsculas y puntuación). 18 de 22 usan esa fórmula (APA 6.ª); las cuatro restantes no ponen fuente o no tienen figuras. Nadie usa "Nota." al estilo APA 7 salvo Alfonso (2023) para una figura tomada de otra fuente.
- Solo describen; sin citas bibliográficas; sin interpretación (la autoevaluación oficial del Módulo 2 lo marca como criterio).

### 2.7 Discusión (3 a 8 págs., consigna ≈10)
Fórmula idéntica en 21 de 22, sin subtítulos:
1. Primer párrafo: reitera el objetivo general ("La presente investigación tuvo como objetivo general…").
2. Un tramo por objetivo específico, en el orden de los Resultados, con contraste explícito contra los antecedentes citados en la Introducción ("Tal como señala…", "A diferencia de…", "en concordancia con…").
3. Limitaciones explícitas (muestra, alcance geográfico, sesgo del instrumento, contexto de pandemia). 20 de 22.
4. Fortalezas o aporte (solo 4 de 22 lo hacen como párrafo aparte; el material oficial lo exige).
5. Recomendaciones y líneas futuras.
6. Párrafo final "A modo de conclusión, se puede decir que…" o "En conclusión…".
7. **Cierre en primera persona con reflexión personal y profesional** ("a nivel personal…", "a nivel profesional…", "como futuro profesional…"). **Al menos 18 de 22**. No está en el material oficial; es la firma más reconocible de los alumnos de Cassi. La única de investigación que no lo hace (Alfonso 2023) también fue aprobada.

### 2.8 Referencias
Entre 5 y 34 (mediana ≈15). APA con "y" en lugar de "&" en la mayoría; DOI o "Recuperado de URL"; predominio de fuentes en español y de fuentes grises (prensa, organismos, sitios de producto). Una tesis aprobó con 7 referencias. Casi nunca hay referencias anteriores a 2005.

### 2.9 Anexos
Instrumento completo (capturas del formulario) y consentimiento informado, en 18 de 22. Las dos documentales no tienen anexos.

### 2.10 Estilo
Impersonal ("se realizó", "se obtuvo") y pretérito en Métodos y Resultados; "el presente trabajo de investigación" como fórmula; párrafos largos (8-15 líneas); siglas definidas la primera vez. La primera persona aparece solo en el cierre de la Discusión y en los agradecimientos.

## 3. Lo que la CAE toleró (y por lo tanto no va a ser tu problema)

Muestras de 6 personas, diseños "cuantitativos" sin una sola prueba estadística, muestreo llamado "probabilístico" cuando era por conveniencia, objetivos específicos con el mismo verbo seis veces, palabras clave de otra plantilla, 7 referencias, inconsistencias entre índice y cuerpo, "Ilustración" en vez de "Figura", una autora que declara no haber usado la plataforma que estudió. Todo eso está en tesis aprobadas. La comisión evalúa **que la estructura esté completa y en orden, que los objetivos se respondan uno a uno y que las limitaciones estén declaradas**. No evalúa potencia estadística ni originalidad frente a la literatura internacional.

## 4. Cruce con tu Entregable 2 (v4, 35 págs.)

### 4.1 Lo que ya está alineado
- Macroestructura IMRyD, sin "Conclusiones" aparte. ✔
- Introducción abre con definición + cita (Wolpaw et al., 2002), antecedentes en prosa sin subtítulos, planteo del problema, pregunta central e interrogantes, relevancia, y cierra con objetivo general y específicos. ✔
- Sin hipótesis (coincide con las 22; además tu texto explica por qué admite resultado negativo). ✔
- Métodos con Diseño / Participantes / Instrumentos / Análisis de datos y cita a Hernández Sampieri et al. (2014). ✔
- "La investigación no involucra participantes humanos" tiene precedente directo (Flores 2021, Maurino 2025). ✔
- Resultados en el orden de los objetivos específicos, con subtítulos por objetivo, 5 páginas. ✔
- Estilo impersonal y pretérito. ✔
- Referencias APA con "y" y DOI. ✔ (30 referencias, el doble de la mediana del corpus; no es problema.)
- Extensión proyectada del manuscrito final (≈50-55 págs. con Discusión y preliminares) dentro del rango del corpus (17-54). ✔

### 4.2 Desvíos respecto del patrón, ordenados por riesgo

| # | Riesgo | Dónde | Qué hacen las 22 | Qué hacer |
|---|---|---|---|---|
| 1 | **Alto** | Intro, objetivos específicos | Viñetas, un objetivo por línea, verbo en infinitivo al inicio | Los seis están en un solo párrafo de prosa (págs. 16-17). Pasarlos a viñetas: "Construir…", "Cuantificar…", "Medir…", "Identificar…", "Comparar…", "Documentar…". Es mecánico y es donde más se cae la corrección. |
| 2 | **Alto** | Intro, interrogantes | Viñetas numeradas después de "surgen los siguientes interrogantes" | Los tres interrogantes están dentro de un párrafo (pág. 14). Sacarlos a viñetas y numerarlos, dejando la pregunta central en prosa. Después, en la Discusión, respondés cada número. |
| 3 | **Alto** | Métodos, Diseño | "Enfoque cuantitativo, alcance descriptivo, diseño no experimental, transversal" con cita y página de Sampieri | Tu diseño es experimental, y está bien que lo sea, pero la CAE no lo ve nunca. Escribir la tríada completa con la terminología de Sampieri y página: enfoque cuantitativo; alcance explicativo; **diseño experimental** (manipulación deliberada de la variable independiente, condición de control, medidas repetidas), y aclarar en una frase que por eso no es "no experimental transversal" como los estudios por encuesta. Sampieri dedica el cap. 7 a diseños experimentales: citalo por página. |
| 4 | **Medio** | Métodos | Solo cuatro subsecciones; las variables van dentro de Instrumentos o de Análisis de datos | Tenés una quinta subsección "Variables". Opciones: (a) dejarla y aceptar que es la única del corpus; (b) fundirla en "Instrumentos" (lo que mide el banco) y "Análisis de datos" (cómo se resume). Recomiendo (b) para el Módulo 3 y de paso acortar Métodos, que hoy tiene 7 págs. contra ≈3 de la consigna y 2-6 del corpus. |
| 5 | **Medio** | Tablas y figuras | `Fuente: Elaboración propia.` debajo de cada una (APA 6.ª) | Usás APA 7 (`Tabla N` + título en cursiva arriba + `Nota.` debajo, y "Elaboración propia" dentro de la leyenda de las figuras). Es correcto y el material oficial dice "APA (2010)" pero acepta lo posterior. Unificá: que **todas** las tablas y figuras lleven una línea de fuente ("Nota. Elaboración propia." o "Elaboración propia a partir de…"), incluidas las Tablas 2 y 3, que hoy tienen "Nota." explicativa pero no la fuente. |
| 6 | **Medio** | Discusión (Módulo 3) | Fórmula de 2.7 | Ver §5: es lo que viene y donde más importa calcar el molde. |
| 7 | **Bajo** | Resultados | Sin pruebas estadísticas | Sos el único con Friedman, Wilcoxon, Holm, r y χ². No lo saques; asegurate de que cada estadístico esté explicado en Métodos en una frase llana (ya lo está) y de que en Resultados no haya interpretación. Revisá "el efecto de los fallos temporales apareció en el retardo de decisión": "apareció" roza interpretación; "se registró" es más seguro. |
| 8 | **Bajo** | Anexos (Módulo 4) | Instrumento y consentimiento | No tenés anexos. Las dos documentales tampoco y aprobaron, pero la consigna dice que son opcionales, no prohibidos. Un anexo corto ayuda a la comisión: (a) tabla completa de variables por condición (la que sacaste del manuscrito), (b) tabla por sujeto, (c) parámetros de los seis inyectores y comandos de reproducción, (d) enlace al repositorio y DOI de Zenodo. |
| 9 | **Bajo** | Portada final (Módulo 4) | Título en inglés en 12 de 16 | Agregar el título en inglés debajo del español. |
| 10 | **Bajo** | Título definitivo (Módulo 4) | "Estudio descriptivo sobre…", "Análisis de…": el título dice qué se hizo | El tema (irreversible, D-004) es "Interfaces cerebro-computadora bajo condiciones adversas: del software a la decodificación". El título definitivo se elabora al final y puede ser más técnico, p. ej. "Propagación de fallos de transporte de señal en un pipeline BCI de código abierto: un estudio experimental Software-in-the-Loop", conservando el tema como subtítulo o en la portada. Decisión tuya; la consigna del Módulo 1 pide título "corto, completo, en términos técnicos, que exprese el problema". |
| 11 | **Bajo** | Métodos, Participantes | Consentimiento o "sin participantes" | Agregar una frase de ética: el conjunto BCI Competition IV 2a es público, anonimizado y distribuido con fines de investigación (Tangermann et al., 2012), por lo que no requiere consentimiento adicional. Las 22 tienen una frase de este tipo. |
| 12 | **Bajo** | Preliminares (Módulo 4) | 3-7 palabras clave espejo | Preparar Resumen ≈200 palabras sin citas, Abstract, 5 palabras clave en ambos idiomas (p. ej. interfaz cerebro-computadora; inyección de fallos; Lab Streaming Layer; tolerancia a fallos; telemetría). |

### 4.3 Extensiones: consigna, corpus y tu E2

| Sección | Consigna oficial | Corpus (mín-máx) | Tu E2 v4 |
|---|---|---|---|
| Introducción | ≈15 | 3-14 | 16 |
| Métodos | ≈3 | 2-6 | 7 |
| Resultados | ≈5 | 2-19 | 5 |
| Discusión | ≈10 | 3-8 | pendiente |
| Referencias | — | 5-34 | 30 |

Métodos es la única sección fuera de rango por arriba. El Entregable 1 tuvo 6 páginas y sacó 8/10 sin comentarios, así que no es urgente; si fundís "Variables" y recortás el párrafo del banco (mejora A10 de [[Mejoras-Redaccion-M3]]) bajás a 5 sin perder nada.

## 5. Molde para la Discusión (Módulo 3), calcado del corpus y del material oficial

Extensión ≈10 págs., **sin subtítulos**, tiempo presente para las interpretaciones y pretérito para lo que se hizo. Orden:

1. **Párrafo de apertura.** Reiterá el objetivo general (sin transcribirlo) y enlazalo con la novedad: nadie había medido a la vez el estado del sistema y el desempeño del decodificador bajo fallos inyectados en el transporte (Zheng et al., 2025 midieron solo el decodificador; Kothe et al., 2025 solo el transporte). Cano et al. (2018) es el ejemplo que da el propio material oficial de este arranque.
2. **Un tramo por objetivo específico, en orden (seis).** Sin transcribir el objetivo; abrí con "Con respecto a…", "En cuanto a…". En cada uno: qué se encontró (una o dos cifras, no la tabla), qué significa, y contra qué antecedente se compara. Sugerencias de contraste, todas ya citadas en tu Introducción:
   - Banco: fidelidad temporal (p99 de 1,3 µs) frente a los 20-40 ms de periféricos que reportan Gemborn Nilsson et al. (2023) y los 8-141 ms de Wilson et al. (2010); concordancia 99 % en línea vs. fuera de línea.
   - Flujo: cada fallo altera solo la variable que define; el piso de reconexión de LSL de ≈1,56 s vs. la afirmación autorreportada de Kothe et al. (2025) sobre pruebas de estrés; TCP demora, no elimina (Lab Streaming Layer, s. f.-a).
   - Decodificador: nulo de la familia uniforme vs. la robustez de CSP+LDA que revisan Lotte et al. (2018) y la fragilidad de EEGNet ante huecos vs. Lawhern et al. (2018) y Roy et al. (2019); comparación con Zheng et al. (2025) sobre pérdida de paquetes; retardo de decisión = retraso inyectado, en línea con la definición de latencia de Wilson et al. (2010).
   - Divergencia: cero fallos silenciosos en el sentido de Avizienis et al. (2004) para este pipeline; qué habría hecho falta para que aparecieran.
   - Detectores: precisión por debajo de la prevalencia; el umbral no sirve y el modelo tampoco; relación con Vogel et al. (2024), que detectan recuperación con media móvil, y con el principio de "hipótesis de estado estable" de Basiri et al. (2016).
   - Documentación: repositorio, semillas, replicabilidad, en línea con Wohlin et al. (2012) y con los criterios de Natella et al. (2016).
3. **Resultados inesperados, explicados.** El nulo de la familia uniforme (por qué CSP con ventana de 4 s absorbe hasta 10 % de pérdida); EEGNet cae con cortes de 0,5 s (rellenado con ceros); gradient boosting sin alarmas. El material oficial exige "proponer explicaciones para los resultados inesperados" y "no ocultar los datos que no encajan".
4. **Limitaciones**, con su efecto sobre los resultados: Software-in-the-Loop sin electrodos ni persona en el lazo; un solo conjunto de datos y 9 sujetos (unidad estadística), CSP limitado a dos clases; familia estructurada exploratoria (diseño secuencial, B1); etiqueta de degradación con rezago de ocho ensayos, que impide medir anticipación (B2); telemetría de un consumidor propio y no de un marco completo; máquina virtual compartida; jitter de 100 ms como máximo; sin hardware. Cada limitación en una o dos oraciones, sin subtítulo.
5. **Fortalezas y aporte, articulados con las limitaciones** (Ejemplo 5 del material oficial): 855 ejecuciones sin fallas, protocolo preespecificado con semillas, banco abierto y reutilizable, primera medición conjunta transporte + decodificador, resultado negativo documentado con honestidad.
6. **Implicancias prácticas y recomendaciones** derivadas solo de tus resultados: monitorear huecos dentro de la ventana de decisión y no solo el estado del proceso; preferir CSP+LDA o un híbrido con vigía cuando el enlace es inestable (Línea 5 de [[Trabajo-Futuro]]); no confiar en detectores de telemetría sin etiqueta funcional; configurar el búfer de LSL con conocimiento del piso de reconexión.
7. **Líneas futuras**: las cinco ya prototipadas (BciPy, trazas reales, intracortical, EEGNet endurecida, híbrido) en un párrafo, sin describir los prototipos.
8. **Párrafo final de conclusiones y recomendaciones**, breve, un solo párrafo, que responda explícitamente a la pregunta central y a los tres interrogantes numerados de la Introducción (por eso conviene numerarlos, desvío 2).
9. **Cierre en primera persona, un párrafo, opcional pero habitual (al menos 18 de 22).** Sobrio: qué te dejó como profesional de software haber sometido a prueba una infraestructura que todos dan por confiable. Si te incomoda, Alfonso (2023) cerró sin él y aprobó; pero la comisión está acostumbrada a encontrarlo.

Errores que el material oficial nombra como los más frecuentes y que la CAE va a buscar: recapitular los resultados en vez de interpretarlos ("los resultados se exponen, no se recapitulan", Day 2005), conclusiones que no se derivan de los resultados, y falta de citas en la Discusión (a diferencia de Resultados, acá **sí** van).

## 6. Fuentes oficiales cruzadas

- Consignas y extensiones del Seminario Final (Trabajo de Investigación): Introducción ≈15, Métodos ≈3, Resultados ≈5, Discusión ≈10; Módulo 4 agrega Portada, Índice, Resumen/Abstract y Palabras clave; formato Times New Roman 12, márgenes 3 cm, interlineado doble, número de página arriba a la derecha, APA (2010). Fuente: `Trabajo Final de Graduación-Notas/TFG-Lineas_tematicas_y_material_de_investigacion.md`, líneas 940-980, 3821-3860, 4460-4630.
- Reglamento institucional (contenidos.21.edu.ar/microsites/reglamento, sección 12.2): la CAE evalúa en 60 días y puede aprobar, pedir modificaciones (30 días corridos, sin prórroga) o desaprobar; la nota final promedia Seminario, CAE y Defensa Oral; escala 4-10.
- Guía del Seminario Final (vault): "Tu Profesor Director te comunicará las sugerencias y requerimientos realizados por la CAE".

## 7. Plan de acción

**Antes del Módulo 3 (Introducción, Métodos y Resultados corregidos + Discusión):**
1. Objetivos específicos e interrogantes a viñetas (desvíos 1 y 2). 15 minutos.
2. Diseño con la tríada de Sampieri y cita de página; frase de ética sobre el conjunto de datos (desvíos 3 y 11). 30 minutos.
3. Fundir "Variables" en Instrumentos y Análisis de datos; Métodos a ≤5 págs. (desvío 4).
4. Línea de fuente en todas las tablas y figuras (desvío 5).
5. Escribir la Discusión con el molde de §5.

**Para el Módulo 4:** portada bilingüe, índice, Resumen/Abstract con 5 palabras clave, título definitivo, anexos (desvíos 8, 9, 10, 12), DOI de Zenodo.

**Lo que no hay que tocar:** el rigor estadístico, las 30 referencias en inglés, el diseño experimental, el resultado negativo. Nada de eso aparece en el corpus y nada de eso le va a sobrar a la comisión; lo que le va a faltar es el andamiaje formal al que está acostumbrada, y eso es lo que arreglan los doce puntos de arriba.

## 8. Perfil del tutor y normativa adicional (verificado por fetch, con URL)

**Dictámenes posibles de la CAE, y solo tres** (reglamento cap. 12.2 y portal oficial La Nube, `lanube.21.edu.ar/post/comision-academica-evaluadora`): (1) "cumple con lo esperado" y habilita la Defensa Oral; (2) "ajustes y modificaciones", con un **acta rúbrica** que detalla las recomendaciones y **30 días corridos** para reentregar, sin prórroga; si la reentrega no responde a lo indicado, Seminario Final queda desaprobado; (3) "no está en condiciones", con reunión de CAE, profesor y Dirección de Carrera. No existe "aprobado con observaciones" ni recuperatorio: desaprobar implica recursar con un TFG nuevo. Plazo máximo de 18 meses desde la regularización para aprobar el TFG (cap. 12.1). La CAE se activa automáticamente cuando el tutor marca el Seminario Final al 100 %. Defensa Oral presencial en Campus, unos 35 minutos de exposición y 10 de preguntas (dato de La Nube, no del texto reglamentario).

**Rúbrica de la CAE**: se confirma que existe y que acompaña cada devolución ("una rúbrica de evaluación que detalla los criterios utilizados", `lanube.21.edu.ar/seminariofinal`), pero **no es pública**: vive en el campus. La consigna y las autoevaluaciones del SAM que tenés en el vault son lo más cercano a esos criterios (§6).

**Jorge Humberto Cassi**: sin ficha docente pública, sin LinkedIn, CONICET ni publicaciones propias verificables. Toda su huella pública es como `dc.contributor.advisor` de unos 40 TFG (2014-2025) en Ingeniería en Software, Licenciatura en Informática, Contador Público y Educación, con temas recurrentes de transformación digital y TIC en educación. Un registro lo titula "Ing.". Un resumen de buscador lo presentaba como coautor de la tesis de Roca sobre Google Earth Engine; se verificó contra el ítem `ues21/30807` y es falso: figura solo como tutor. Ninguna de sus tesis publicadas menciona observaciones de la CAE; dos lo agradecen por "sus correcciones" y "buenas pautas y rúbricas" (Alem 2025, Villagra 2022).

**No encontrado**: testimonios de alumnos sobre el contenido de las correcciones de la CAE (solo una petición de Change.org sobre plazos de devolución, y grupos cerrados de WhatsApp y Discord); un instructivo oficial de Defensa Oral de 2016 (`contenidos.21.edu.ar/pdf/instructivo_defensa_oral_2016.pdf`) existe pero no pudo leerse ni confirmarse su vigencia.
