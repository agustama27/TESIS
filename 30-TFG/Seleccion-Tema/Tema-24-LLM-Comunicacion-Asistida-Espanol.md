# Tema 24 — LLMs para comunicación asistida en español

> Estado: 🎯 **EN FOCO** (finalista junto al [[Tema-19-Fidelidad-Brain-to-Text|tema 19]] — ver fusión posible al final) · agregado 2026-08-14
> Elegido por el autor en el ejercicio de decisión, junto al 19.

## La idea en palabras simples

Una persona con ELA que escribe con la mirada (o con un implante cerebral) tarda muchísimo en cada letra — cada tecla le cuesta. Google demostró en *Nature Communications* (2024) que un modelo de lenguaje puede expandir texto ultra-abreviado usando el contexto de la conversación: la persona teclea solo las iniciales ("qhh") y el LLM completa ("¿qué hacemos hoy?"). Resultado con usuarios reales con ELA: **57% menos movimientos y 29-60% más velocidad**. El sistema existe **solo en inglés**. Tu tesis: construir y evaluar la expansión de texto abreviado con LLMs **en español** — donde no existe — midiendo cuánto acelera y cuánto se equivoca, con el mismo método de simulación offline del paper original.

## Definiciones Iniciales (formato oficial)

- **Tipo de TFG**: ☑ Trabajo de Investigación
- **Línea Temática**: ☑ Transformación Digital

### Título tentativo (~12 palabras)

Expansión de texto abreviado con modelos de lenguaje para comunicación asistida en español

### Justificación de la Línea Temática elegida (3 renglones)

Las personas con discapacidad motora severa escriben a un costo altísimo por tecla; los modelos de lenguaje pueden multiplicar su velocidad de comunicación. Llevar esa capacidad al español — donde no existe — es adopción de herramientas digitales para la vida en su forma más literal.

### Explicación del tema (5-15 renglones)

Los usuarios de comunicación aumentativa (por mirada, por switch, o por interfaz cerebro-computadora) producen texto a velocidades de 5-15 palabras por minuto: cada tecla cuesta esfuerzo físico real. Google y Team Gleason demostraron (SpeakFaster, *Nature Communications* 2024) que un modelo de lenguaje con contexto conversacional puede expandir abreviaciones extremas — solo las iniciales de cada palabra — a la frase completa, ahorrando 57% de los movimientos en simulación y acelerando 29-60% la escritura de usuarios reales con ELA. Todo el sistema es ingeniería de modelos de lenguaje: prompting, fine-tuning, evaluación con métricas de exactitud de expansión y ahorro de teclas. No existe versión ni evaluación en español — un idioma con morfología más rica (género, conjugaciones) donde la expansión es un problema abierto. Este trabajo construye el pipeline de expansión en español (LLMs abiertos y comerciales), lo evalúa con el protocolo de simulación offline del paper original sobre corpus conversacionales en español, y audita sus errores: cuándo la expansión dice lo que el usuario quiso — y cuándo inventa algo fluido pero ajeno.

### Problema / pregunta de investigación (3-5 renglones)

¿Qué exactitud de expansión y qué ahorro de pulsaciones logran los modelos de lenguaje al expandir texto ultra-abreviado en español para comunicación asistida, y con qué frecuencia producen expansiones fluidas pero infieles a la intención del usuario? ¿Qué estrategias (contexto conversacional, fine-tuning, tamaño de modelo) mejoran ese equilibrio?

### Revisión de literatura principal (4 trabajos, APA)

1. Cai, S., et al. (2024). Using large language models to accelerate communication for eye gaze typing users with ALS. *Nature Communications*. https://www.nature.com/articles/s41467-024-53873-3
2. *Using Large Language Models to Accelerate Communication for Users with Severe Motor Impairments*. (2023). *arXiv*. https://arxiv.org/abs/2312.01532
3. Willett, F. R., et al. (2023). A high-performance speech neuroprosthesis. *Nature*, *620*(7976), 1031-1036. https://doi.org/10.1038/s41586-023-06377-x (el usuario BCI como destinatario final del teclado asistido)
4. ⚠️ Corpus conversacional en español para evaluación (CallHome Spanish / corpus AAC) — verificar y elegir en el Mes 1.

### Justificación del Trabajo Final de Graduación (borrador — expandir al confirmar)

La comunicación aumentativa en español no tiene hoy ningún sistema de expansión por LLM evaluado, mientras que el método está publicado y validado en inglés en una de las revistas científicas más importantes del mundo. La brecha es de ingeniería y de idioma, no de ciencia básica: exactamente el tipo de vacancia que un Trabajo Final de Graduación puede cerrar con rigor. El trabajo es 100% software (prompting, integración de modelos, pipeline de evaluación reproducible, métricas de ahorro de pulsaciones y exactitud), no requiere hardware ni pacientes (la validación principal del propio paper de Nature Communications fue simulación offline sobre corpus), y produce un resultado doblemente útil: la medición de viabilidad del método en español y la auditoría de fidelidad de las expansiones — crítica en un dominio donde el usuario no puede corregir fácilmente lo que el sistema dice por él. *(Expandir a 15-20 renglones al confirmar el tema.)*

## Por qué encaja con el autor

- Es su **stack diario** (ingeniería de LLMs en Evoltis) apuntado al caso de uso más noble.
- Sin hardware, sin GPU pesada (los LLMs se consumen por API o en tamaños chicos locales), simulación offline como método principal.
- Impacto directo en hispanohablantes con discapacidad — y conexión natural con BCI: este es el teclado que un usuario de implante usaría.
- CV: "repliqué y extendí en español un método de Nature Communications de Google" + LLM engineering demostrable.

## 🧬 Fusión posible con el Tema 19

Ambos temas comparten el corazón: **el rol del modelo de lenguaje en la comunicación de personas que no pueden hablar.** El 19 lo audita en brain-to-text; el 24 lo usa para acelerar y lo audita en la expansión. La tesis fusionada — "expansión LLM en español + auditoría de fidelidad de las expansiones" — construye el sistema Y responde la pregunta profunda: ¿cuándo el LLM dice lo que la persona quiso, y cuándo pone palabras en su boca? Un solo pipeline, las dos preguntas que el autor eligió.
