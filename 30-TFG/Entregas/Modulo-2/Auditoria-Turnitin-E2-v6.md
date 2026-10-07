# Auditoría Turnitin — Entregable 2 v6 (diagnóstico, sin reescritura)

Fecha: 2026-10-03. Documento auditado: `v6/Tamagusuku_Agustin - Entregable 2 - Resultados.pdf` (35 págs.).
**Ningún número de este informe es un resultado de Turnitin.** Son estimaciones de un proxy heurístico y mediciones propias.

---

## 1. Executive summary

| Indicador | Valor | Tipo |
|---|---|---|
| Turnitin AI Proxy central | **16 %** | estimación heurística, no calibrada |
| Rango del proxy | **2 – 47 %** (cola hasta ~66 % si el clasificador marca toda la Introducción) | sensibilidad al umbral |
| Salida visual más probable | **`*%`**, con un porcentaje visible de 20–45 % casi igual de plausible | predicción |
| Confianza de la estimación | **baja** | — |
| Autocoincidencia con Entregable 1 | **49 %** del cuerpo (exacta ≥ 8 palabras); **56 %** del documento con bibliografía y portada | medido |
| Similitud externa estimada | **3–8 %** sin bibliografía; **15–22 %** con bibliografía | estimación (no se consultó ninguna base) |
| Riesgo de plagio externo | **bajo** | juicio |

Tres hallazgos pesan más que el número:

1. **El riesgo de IA está en la Introducción y casi en ningún otro lado.** Proxy medio 0,67 en Introducción, 0,41 en Métodos, 0,11 en Resultados. La Introducción es el 66 % del texto calificable.
2. **El número grande y seguro es la autocoincidencia, no la IA.** El 81 % de la Introducción es texto idéntico al Entregable 1. Si el Entregable 1 quedó en el repositorio de Turnitin y no se excluye, el Similarity va a verse alto (≈ 50–60 %) por una causa legítima.
3. **El proxy mide estilo; Turnitin no.** Turnitin declara que no programa señales como perplejidad o variabilidad: es un clasificador entrenado sobre texto humano y texto de modelos. Si la prosa de la Introducción fue redactada o pulida con un modelo de lenguaje, el resultado real puede quedar por encima del proxy aunque el estilo "parezca" humano; si fue escrita a mano, por debajo. Ese dato lo conocés vos, no el proxy.

Además, la auditoría contra el repositorio encontró **4 discrepancias de redacción/publicación** (ninguna numérica) que conviene corregir por razones académicas, independientes de Turnitin (sección 11).

---

## 2. Qué sabemos realmente de Turnitin

Categorías: **A** confirmado por Turnitin · **B** investigación independiente · **C** inferencia · **D** desconocido/propietario.

| Característica | Qué se sabe | Cat. | Fuente | Confianza |
|---|---|---|---|---|
| Qualifying text | Solo oraciones en prosa dentro de párrafos de un texto largo | A | [FAQ ES](https://guides.turnitin.com/hc/es/articles/28477544839821) | Alta |
| No se evalúa de forma fiable | Viñetas, tablas, bibliografías anotadas, código, poesía, guiones, texto fragmentario | A | [Using the AI Writing Report](https://guides.turnitin.com/hc/en-us/articles/22774058814093) | Alta |
| Captions, encabezados, notas de tabla | Sin documentación | D | — | — |
| Bibliografía | Excluida del reporte de IA desde 2023-08-09 | A | [Release notes](https://guides.turnitin.com/hc/en-us/articles/28294949544717) | Alta |
| Longitud | Mínimo 300 palabras de prosa; máximo 30.000 | A | [File requirements](https://guides.turnitin.com/hc/en-us/articles/28234943089933-File-requirements-for-an-AI-Writing-Report) | Alta |
| Segmentación (español) | Segmentos de "unos pocos cientos de palabras (alrededor de cinco a diez oraciones)", solapados | A | FAQ ES | Alta |
| Tamaño exacto y paso de la ventana | No publicado | D | — | — |
| Segmento → oración | Cada segmento recibe 0–1; la oración hereda el puntaje; si cae en varios segmentos, se "agrupan" en uno | A | [FAQ EN](https://guides.turnitin.com/hc/en-us/articles/28477544839821-Turnitin-s-AI-writing-detection-capabilities-FAQs) | Alta |
| Función de agrupación (¿promedio?) | No publicada; "promedio" es inferencia | C | FAQ ES/EN | Media |
| Umbral por oración | No publicado | D | — | — |
| Porcentaje del documento | Proporción del qualifying text predicha como IA, no del archivo | A | FAQ ES | Alta |
| Arquitectura | Clasificador basado en transformers, propio para español; no programa señales explícitas (perplejidad, burstiness) | A | FAQ ES/EN | Alta |
| Pesos, datasets, hiperparámetros | No publicados | D | — | — |
| Detector español | Modelo distinto del inglés, lanzado 2024-09-12; mejora 2026-05-05 | A | Release notes | Alta |
| Modelos cubiertos (español) | Familia GPT-3.5 a GPT-5.1 y Gemini 2.5; Claude no figura en la lista española (sí en la inglesa) | A | FAQ ES | Media (la FAQ ES puede estar desactualizada) |
| Parafraseo / bypasser en español | **No se detecta**; solo el detector inglés | A | Using the AI Writing Report | Alta |
| Scores 1–19 % | Se muestra `*%`, sin número ni resaltado (desde julio de 2024) | A | Release notes | Alta |
| Falsos positivos, documento | < 1 % declarado para documentos con > 20 %; cifra interna | A | FAQ ES | Alta como declaración |
| Falsos positivos, oración | ≈ 4 % (modelo inglés, 2023); sin cifra para español | A | [Blog Turnitin](https://www.turnitin.co.uk/blog/understanding-the-false-positive-rate-for-sentences-of-our-ai-writing-detection-capability) | Media |
| Sesgo en primeras y últimas oraciones | Reconocido en 2023; ajustado | A | Release notes | Alta |
| Limitación reconocida | Más falsos positivos en texto "sin mucha variación estructural" o repetitivo | A | FAQ ES | Alta |
| Evaluación independiente | Weber-Wulff et al. (2023), Perkins et al. (2024): solo modelo inglés | B | fuentes secundarias | Media-baja |
| Evaluación independiente del español | No se encontró ninguna | D | — | — |
| IA y Similarity | Completamente independientes | A | FAQ ES | Alta |
| Similarity: bibliografía y citas | Filtros opcionales de exclusión; coincidencia mínima por defecto 8 palabras | A | [Exclusion filters](https://guides.turnitin.com/hc/en-us/articles/23539146689549-How-exclusion-filters-refine-the-Similarity-Report) | Alta |
| Similarity: entregas propias previas | Exclusión automática solo dentro de la misma clase; entre clases no | A | [Help center](https://helpcenter.turnitin.com/hc/en-us/articles/27811963885069) | Alta |
| Similarity: plagio traducido | Existió "translated matching" (2012, 2022); vigencia actual sin confirmar | A / D | [Blog 2022](https://www.turnitin.com/blog/how-turnitin-supports-languages-to-ensure-integrity-in-a-global-marketplace-of-ideas) | Media-baja |

No se pudo leer el whitepaper técnico (acceso restringido). Nada de este informe se apoya en él.

---

## 3. Metodología del proxy

**Lo que imita de Turnitin (estructura externa, confirmada):** filtrar a prosa calificable → ventanas solapadas de 5–10 oraciones → puntaje 0–1 por ventana → cada oración combina los puntajes de sus ventanas → porcentaje = palabras calificables sobre umbral / palabras calificables → regla de presentación `*%` bajo 20 %.

**Lo que es heurística propia (no es de Turnitin):** el puntaje de cada ventana.

1. **Extracción.** Texto por página del PDF (PyMuPDF) y párrafos del `.docx` v6, para no perder los límites de párrafo.
2. **Clasificación.** Prosa calificable; listas (3 interrogantes, 6 objetivos); captions y notas; tablas; títulos; portada; referencias.
3. **Oraciones.** Corte por puntuación final seguida de mayúscula, protegiendo "et al." y "s. f.".
4. **Ventanas.** Deslizantes con paso de una oración, tamaños 5, 8 y 10; continuas a través de párrafos y secciones.
5. **Puntaje de ventana.** Un puntaje base por párrafo, asignado por lectura completa del párrafo (señales de las dos listas del pedido), más tres ajustes calculados: uniformidad de longitud de oraciones (±0,06), densidad de cifras propias (hasta −0,12), densidad de conectores (hasta +0,04).
6. **Oración.** Promedio de las ventanas que la contienen (inferencia C).
7. **Escenarios.** La escala del proxy no está calibrada contra Turnitin, así que los umbrales 0,80/0,85/0,90 no significan lo mismo aquí. Se usan tres cortes sobre la escala propia: sensible 0,65, central 0,72, conservador 0,78. Son un análisis de sensibilidad, no umbrales reales.

Script y salida: `proxy.py` y `proxy_out.json` (carpeta temporal de la sesión).

---

## 4. Estadísticas del qualifying text

| Categoría | Palabras | % del documento |
|---|---|---|
| Prosa calificable | 6.233 | 70,2 % |
| Referencias | 1.342 | 15,1 % |
| Captions y notas | 509 | 5,7 % |
| Tablas | 409 | 4,6 % |
| Listas (interrogantes y objetivos) | 270 | 3,0 % |
| Títulos | 65 | 0,7 % |
| Portada | 50 | 0,6 % |
| **Total** | **8.878** | 100 % |

Oraciones calificables: **140**. Si Turnitin tratara las listas como prosa (son oraciones completas), entraría el 73,2 %.

---

## 5. Resultado global

Porcentaje de palabras calificables sobre cada corte (escala del proxy):

| Ventana | 0,60 | 0,65 | 0,70 | 0,72 | 0,75 | 0,78 | 0,80 | 0,85 | 0,90 |
|---|---|---|---|---|---|---|---|---|---|
| 5 oraciones | 58,3 | 42,0 | 28,1 | 19,5 | 14,4 | 6,5 | 2,8 | 0 | 0 |
| 8 oraciones | 56,0 | 46,8 | 20,4 | 16,4 | 11,2 | 2,3 | 0 | 0 | 0 |
| 10 oraciones | 56,0 | 41,7 | 20,2 | 14,5 | 9,4 | 0 | 0 | 0 | 0 |

| Escenario | Corte | AI proxy % | Presentación simulada |
|---|---|---|---|
| Conservador | 0,78 | 2 % (0–7) | `*%` |
| **Central** | 0,72 | **16 %** (15–20) | `*%`, al borde del 20 % |
| Sensible | 0,65 | 47 % (42–47) | porcentaje visible |

**Lectura.** El resultado es muy sensible al corte porque casi toda la Introducción tiene un puntaje parecido (0,60–0,77): un clasificador que la marque, la marca casi entera. Por eso el desenlace real tiende a ser bimodal —`*%` o un número cercano al peso de la Introducción— más que un valor intermedio. La estimación central cae a 4 puntos del umbral de visibilidad: no hay margen para afirmar `*%` con seguridad.

---

## 6. Resultado por sección

| Sección | Palabras | Oraciones | Proxy medio | Rango | Riesgo |
|---|---|---|---|---|---|
| Intro: contexto y revisión bibliográfica | 3.130 | 61 | 0,66 | 0,55–0,79 | 🟠 |
| Intro: research gap | 276 | 6 | 0,67 | 0,66–0,68 | 🟠 |
| Intro: problema y preguntas | 273 | 8 | 0,74 | 0,70–0,77 | 🔴 |
| Intro: relevancia y alcance | 351 | 9 | 0,73 | 0,67–0,77 | 🔴 |
| Intro: objetivos (prosa) | 79 | 2 | 0,64 | 0,61–0,64 | 🟠 |
| **Introducción total** | 4.109 | 86 | **0,67** | 0,55–0,79 | 🟠 |
| **Métodos** | 1.334 | 32 | **0,41** | 0,31–0,59 | 🟢 |
| **Resultados** | 790 | 22 | **0,11** | 0,05–0,32 | 🟢 |

Escala: 🟢 < 0,45 · 🟡 0,45–0,62 · 🟠 0,62–0,72 · 🔴 ≥ 0,72.

Las preguntas y los objetivos en lista quedan fuera del cálculo (probablemente no calificables). Si entraran, sumarían 270 palabras de riesgo 🟠: son formulaciones muy canónicas.

---

## 7. Heatmap por páginas

| Pág. | Sección | Palabras calif. | Proxy | Riesgo |
|---|---|---|---|---|
| 2 | Intro: BCI, neuroprótesis | 348 | 0,65 | 🟠 |
| 3 | Intro: recorrido de la señal | 234 | 0,67 | 🟠 |
| 4 | Intro: bits por minuto, CSP/LDA | 292 | 0,68 | 🟠 |
| 5 | Intro: plataformas de software | 259 | 0,65 | 🟠 |
| 6 | Intro: LSL | 421 | 0,63 | 🟠 |
| 7 | Intro: arquitectura LSL, relevamiento GitHub | 242 | 0,57 | 🟡 |
| 8 | Intro: tiempo real, Gemborn Nilsson, Wilson | 359 | 0,56 | 🟡 |
| 9 | Intro: tres propiedades; fallas cotidianas | 279 | 0,69 | 🟠 |
| **10** | Intro: capas; inicio de dependabilidad | 229 | **0,78** | 🔴 |
| **11** | Intro: Avizienis, Natella, Basiri; stream processing | 311 | **0,74** | 🔴 |
| 12 | Intro: Vogel; molde metodológico; gap | 284 | 0,68 | 🟠 |
| 13 | Intro: gap; problema | 307 | 0,70 | 🟠 |
| **14** | Intro: pregunta central | 59 | **0,76** | 🔴 |
| **15** | Intro: resultado negativo; relevancia; planteo | 319 | **0,75** | 🔴 |
| 16 | Intro: alcance; objetivo general | 128 | 0,65 | 🟠 |
| 17 | Objetivos (lista) | 0 | — | no calificable |
| 18 | Métodos: diseño | 306 | 0,51 | 🟡 |
| 19 | Métodos: participantes, instrumentos | 266 | 0,34 | 🟢 |
| 20 | Métodos: pipeline | 123 | 0,32 | 🟢 |
| 21 | Métodos: verificación, EEGNet, entorno | 198 | 0,34 | 🟢 |
| 22 | Métodos: variables (Tabla 1) | 81 | 0,40 | 🟢 |
| 23 | Métodos: análisis (Tabla 2) | 168 | 0,45 | 🟡 |
| 24 | Métodos: análisis | 192 | 0,41 | 🟢 |
| 25 | Resultados: banco; flujo | 323 | 0,17 | 🟢 |
| 26–29 | Resultados | 467 | 0,06–0,09 | 🟢 |
| 30–35 | Referencias | 0 | — | no calificable |

---

## 8. Hotspots principales

| # | Pág. | Empieza con… | Termina con… | Proxy | Sube el puntaje | Lo baja |
|---|---|---|---|---|---|---|
| 1 | 15 | "La relevancia del problema proviene del lugar del software abierto…" | "…condición para que lo construido sobre ella sea reproducible." | 0,77 | Afirmación genérica de relevancia ("fronteras de la transformación digital en salud"); dos oraciones largas y simétricas; cierre sentencioso | Ninguna cifra ni decisión propia |
| 2 | 15 | "Las tres admiten un resultado negativo…" | "…hacia el resultado esperado." | 0,77 | Tríada perfecta "si…; si…; y si…"; cierre aforístico | Idea metodológica propia (admitir resultado nulo) |
| 3 | 14 | "La pregunta central es cómo se propagan fallos controlados…" | "…las tres comparaciones del diseño experimental:" | 0,76 | Fórmula canónica de pregunta de investigación; nominalizaciones | Términos específicos del estudio |
| 4 | 9–10 | "Estas fallas no son situaciones excepcionales, sino parte…" | "…no se presentan como fallas propias del protocolo LSL." | 0,76 | Molde "no X, sino Y" repetido; tres capas en paralelo estricto; nueve oraciones de longitud pareja | Razonamiento técnico específico (TCP retransmite; búfer descarta) |
| 5 | 10–11 | "Fuera del dominio BCI, la ingeniería de software tiene un cuerpo de conocimiento maduro…" | "…perturbaciones que reproducen eventos ordinarios de operación." | 0,76 | Síntesis de literatura muy homogénea: autor (año) + verbo + enumeración, tres veces; cierre que ata con el propio trabajo | Selección concreta de dos de los cuatro principios |
| 6 | 15 | "El planteo es conservador: somete al software…" | "…un modelo basado en telemetría." | 0,74 | Paralelismo "Toma de… de… y de…"; registro uniforme | Delimitación concreta (sin hardware, GPU ni pacientes) |
| 7 | 13 | "El problema que aborda esta investigación es el desconocimiento…" | "…solo se descubre por sus consecuencias." | 0,73 | "No se sabe… Tampoco se sabe…"; cierre antitético | Variables concretas del estudio |
| 8 | 11–12 | "Los sistemas de procesamiento de flujos (stream processing)…" | "…pero con mayor latencia." | 0,72 | Resumen de un solo paper en tres oraciones de 60 palabras; enumeración "que…, que…, y que…" | Detalle fiel de la fuente |
| 9 | 4 | "Para la persona que usa el sistema, el desempeño…" | "…y no solo en el estado técnico del sistema." | 0,69 | "No es X sino Y"; párrafo cerrado con "Por eso este trabajo…" | Cifras de Wolpaw |
| 10 | 12 | "Ese trabajo ofrece el molde metodológico…" | "…agrega al molde metodológico." | 0,69 | Párrafo de transición cerrado sobre sí mismo (empieza y termina con la misma expresión) | Aporte propio enunciado |

**Por qué un clasificador contextual puede ser sensible a estos bloques.** Comparten cuatro rasgos acumulados: (a) cada párrafo abre con una tesis, la desarrolla y cierra con una frase que la conecta con "este trabajo"; (b) las enumeraciones son casi siempre de tres elementos y en paralelo gramatical; (c) cada término técnico va seguido de su definición en aposición, con la misma construcción; (d) el registro no varía en dieciséis páginas. Ninguno demuestra nada por separado; juntos y sostenidos, describen texto "sin mucha variación estructural", que es la limitación que Turnitin reconoce.

**Bloques de la Introducción con menor puntaje** (0,55–0,60): el relevamiento de repositorios del 16 de agosto de 2026 (pág. 7), la búsqueda bibliográfica de septiembre de 2026 (págs. 12–13) y los párrafos con cifras de Gemborn Nilsson y Wilson (pág. 8). Los tres contienen acciones fechadas del autor o datos puntuales.

---

## 9. Análisis de Métodos

Proxy medio 0,41 (🟢), con un solo tramo 🟡: el primer párrafo de Diseño (pág. 18, 0,58), que es la clasificación metodológica estándar según Hernández Sampieri y por eso inevitablemente formularia.

Lo que baja el puntaje del resto: decisiones concretas y justificadas —bloques de diez muestras cada 40 ms, espera activa en los últimos 2 ms, 125 muestras como mínimo de validez, temporizador de Windows de 15 ms como motivo para usar una máquina virtual, el ejemplo de 10 y 4 ensayos para justificar la exactitud balanceada, la mediana por sujeto para evitar pseudorreplicación, el p mínimo alcanzable de 0,012 con nueve sujetos—. Todas son contrastables con el código (sección 11).

Señal estilística a notar: el 22 % de las oraciones de Métodos comparte arranque ("La investigación…", "Para el primer/segundo interrogante…"). Es esperable en una sección de procedimiento.

---

## 10. Análisis de Resultados

**Sí, el perfil es claramente distinto del de la revisión bibliográfica.**

| Indicador | Revisión bibliográfica | Resultados |
|---|---|---|
| Proxy medio | 0,66 | 0,11 |
| Densidad de cifras (% de palabras) | 1,8 % | 15,7 % |
| Longitud media de oración | 51,3 | 35,9 |
| Punto y coma por mil palabras | 8,6 | 2,5 |
| Conectores por cien palabras | 0,64 | 0,25 |
| Variación entre párrafos (CV de longitud media) | 0,25 | 0,39 |

Los ocho elementos pedidos están en el texto como datos, no como comentario: 855 ejecuciones en 8,1 h; exactitud de CSP+LDA (0,708) y EEGNet (0,750); cuatro pruebas de Friedman con su χ²; Wilcoxon con Holm (p ≤ 0,012, r = 0,96); prevalencia 0,0134 sobre 242.250 ventanas; cuatro detectores con precisión entre 0,000 y 0,036; resultados negativos explícitos (la familia uniforme no modificó ninguna métrica; divergencia silenciosa nula; gradient boosting sin detecciones); familia estructurada declarada exploratoria.

**Dos reservas honestas:**

1. Que la especificidad empírica baje el proxy es una decisión de diseño del proxy. No hay evidencia pública de que el clasificador de Turnitin trate distinto la prosa cargada de cifras; lo razonable es esperarlo (hay poco texto de entrenamiento así), pero es inferencia.
2. Resultados pesa poco: 790 palabras, el 13 % del texto calificable. Aunque saliera en cero, no compensa a la Introducción.

Observación de estilo: el 36 % de las oraciones de Resultados repite arranque ("La balanced accuracy…", "La proporción…", "La regresión…"). Es propio de un reporte de resultados y no pesa en el proxy.

---

## 11. Evidencia del repositorio GitHub

Repositorio público, tags `v1.0` y `v2.0`, licencia MIT. Se contrastaron unas 62 afirmaciones del PDF.

- **49 coinciden con el valor visto en el repo (79 %).** Sobre las cifras de Métodos y Resultados, la coincidencia es del 100 %: Tablas 3 y 4, los cuatro Friedman, los p de Holm, exactitudes, divergencias, 77 episodios, 242.250 ventanas, 20.511 decisiones, 99,0 %.
- Los detectores de la Tabla 4 se **reprodujeron de forma independiente** desde `windows.csv`, con coincidencia exacta.
- Parámetros de diseño verificados en código: `CHUNK=10`, espera activa bajo 2 ms, `N_CSP=6`, 125 muestras, `TRIAL_TIMEOUT_S=3.0`, ventana 8 con regla de mínimo, severidades de las dos familias.

Conclusión de trazabilidad: Métodos y Resultados reflejan decisiones y números específicos, existentes y reproducibles. Esto no cambia el proxy; es evidencia independiente de autoría del trabajo experimental.

**Discrepancias entre PDF y repositorio** (ninguna es numérica):

| # | PDF | Repositorio |
|---|---|---|
| D1 | Pág. 29: "los segmentos de señal de todas las ejecuciones se publicaron" | No hay ningún `segments.npz`; el README dice que se depositan aparte |
| D2 | Pág. 29: random forest tuvo "la menor tasa de falsos positivos entre los detectores que emitieron alarmas" | Gradient boosting sí emitió alarmas (unas 15, todas falsas; tasa 0,00006), menos que random forest |
| D3 | Tabla 1: el flujo se corta "cinco veces por corrida" | Una ejecución de 135 (`s07-r2-disconnect-1`) tuvo 4 cortes |
| D4 | Págs. 18 y 29: la semilla "hace repetible" la realización | Las 855 semillas están registradas, pero el plan no se regenera: `seed_for` usa `hash()` sobre cadenas, que cambia entre procesos |

Otros puntos menores: el PDF cita "versión 2.0", pero parte del cálculo de intervalos máximos está un commit después del tag; la etapa de 234 ejecuciones vive en `v1.0`, que el PDF no menciona; `requirements.txt` no fija las versiones que el PDF declara; la columna "Precisión promedio" de la Tabla 4 y dos columnas de CSV no tienen script publicado; el README público todavía describe la campaña de 234 ejecuciones; "8,1 horas" es consistente (8,02 h calculadas) pero no verificable de forma exacta.

---

## 12. Similarity y autocoincidencia (independiente de la IA)

### Autocoincidencia con el Entregable 1 (medida)

| Alcance | Exacta ≥ 8 palabras | Exacta ≥ 5 palabras |
|---|---|---|
| Cuerpo (prosa, tablas, captions) | **49,0 %** | 52,4 % |
| Referencias | 92,6 % | 94,3 % |
| Cuerpo + bibliografía + portada | **55,8 %** | 59,0 % |

| Sección (solo prosa) | Exacta ≥ 8 | Aproximada* |
|---|---|---|
| Introducción | 81,3 % | 82,2 % |
| Métodos | 4,6 % | 7,3 % |
| Resultados | 0,0 % | 0,0 % |
| Total prosa | 54,6 % | 55,8 % |

\* Oraciones con al menos la mitad de sus trigramas presentes en el Entregable 1.

Exacta y aproximada casi coinciden: lo reutilizado se copió literal y lo nuevo es nuevo. Métodos fue reescrito casi por completo. **Autocoincidencia no es plagio externo**: el Módulo 2 pide Introducción y Métodos corregidos más Resultados.

### Similitud externa (estimada, sin consultar bases)

- **Bibliografía:** 30 referencias con títulos y DOI reales; coinciden con cualquier base. Aportan hasta ~15 % del documento si no se excluyen.
- **Cuerpo:** prosa en español que resume fuentes en inglés; no hay citas textuales. Coincidencias esperables: nombres de herramientas y fabricantes (pág. 6), títulos, portada institucional, fórmulas metodológicas de Hernández Sampieri (pág. 18). Estimación: 3–8 %.
- **Repositorio público:** los `.md` del repo coinciden con el 0,5 % del cuerpo (≥ 8 palabras). Despreciable.
- **Coincidencias traducidas:** los resúmenes de Vogel, Wilson, Gemborn Nilsson y Kothe siguen de cerca el contenido de cada fuente, con cita. Si Turnitin aplicara comparación traducida podría marcar fragmentos; su vigencia no está confirmada.

### Cómo podría verse el Similarity Score

| Configuración | Estimación |
|---|---|
| Entregable 1 incluido, con bibliografía | 55–62 % |
| Entregable 1 incluido, sin bibliografía | 48–55 % |
| Entregable 1 excluido, con bibliografía | 15–22 % |
| Entregable 1 excluido, sin bibliografía | 3–8 % |

Turnitin excluye automáticamente las entregas propias solo dentro de la misma clase. Si los dos módulos son actividades de la misma clase, el caso probable es "excluido"; no lo sé y conviene confirmarlo con el tutor.

---

## 13. Limitaciones de esta simulación

1. **El puntaje de ventana es un juicio, no un clasificador.** Lo asigné leyendo cada párrafo; otro evaluador daría otros valores. Los ajustes automáticos pesan poco.
2. **La escala no está calibrada.** No existe un par (texto, resultado real de Turnitin en español) contra el cual ajustarla. Los tres cortes son sensibilidad, no umbrales.
3. **Turnitin no mide estilo de forma explícita.** Un proxy basado en estilo puede errar en ambos sentidos.
4. **El proxy lo ejecutó un modelo de lenguaje.** Mi lectura de "qué suena a IA" tiene sesgos propios y no equivale a la de un clasificador entrenado.
5. **Desconocidos que mueven el resultado:** tamaño y paso de ventana, función de agrupación, umbral, trato de captions y listas, cobertura real de modelos del detector español.
6. **No hay evaluación independiente del detector español.**
7. **La similitud externa no se midió** contra ninguna base; solo la autocoincidencia y el repo.
8. **Segmentación de oraciones aproximada:** una oración de la pág. 16 no pudo asignarse a página.

La única medición que resuelve la incertidumbre es un reporte real: si la universidad permite un envío de borrador, vale más que todo este proxy.

---

## 14. Veredicto final

El documento tiene dos mitades con perfiles opuestos. Métodos y Resultados (34 % del texto calificable) son específicos, numéricos, trazables al repositorio y de riesgo bajo. La Introducción (66 %) es una síntesis de literatura muy pulida y estructuralmente uniforme, y concentra todo el riesgo; dentro de ella, los puntos más altos son la justificación de relevancia, la formulación del problema y las preguntas (págs. 14–15) y la revisión de dependabilidad (págs. 10–11).

En Similarity, el número alto esperable proviene de la reutilización legítima del Entregable 1, no de fuentes externas.

Antes de cualquier decisión de redacción hay cuatro correcciones de contenido que se justifican solas (D1 a D4).

```
TURNITIN AI PROXY:                 16 %   (no es un resultado de Turnitin)
INTERVALO:                         2–47 % (cola hasta ~66 %)
SALIDA TURNITIN MÁS PROBABLE:      *%  (un porcentaje visible de 20–45 % es casi igual de plausible)
SIMILITUD EXTERNA ESTIMADA:        3–8 % sin bibliografía · 15–22 % con bibliografía
AUTOSIMILITUD CON ENTREGABLE 1:    49 % del cuerpo · 56 % del documento completo
CONFIANZA DE LA ESTIMACIÓN:        baja (IA) · alta (autocoincidencia) · media (similitud externa)
```
