# Fidelidad en la decodificación brain-to-text — investigación de implementación

> Nota profunda · 2026-08-14 · TEMA EN FOCO para el TFG
> Presentación formato universidad: [[../30-TFG/Seleccion-Tema/Tema-19-Fidelidad-Brain-to-Text|Tema 19 — Definiciones Iniciales]]
> Contexto del campo: [[Decodificacion-Brain-to-Text]] · Lista maestra: [[Temas-Candidatos-TFG]]

## La pregunta

> **¿Cuánto de la salida de un sistema brain-to-text proviene de la señal neural del paciente y cuánto del prior lingüístico del modelo de lenguaje — y en qué condiciones el sistema deja de decodificar y empieza a "adivinar"?**

Por qué importa: el usuario de estos sistemas no puede corregir lo que el sistema dice en su nombre. Si el modelo de lenguaje completa palabras plausibles que no vinieron del cerebro, le está poniendo palabras en la boca a una persona sin voz.

## Validación adversarial de la pregunta (2026-08-14) — VEREDICTO: ABIERTA en el nicho correcto

**Lo que YA existe (y juega A FAVOR — te da metodología y urgencia):**

1. **El problema es real y está documentado en EEG no invasivo (2025-2026):**
   - *Escaping the BLEU Trap* (arXiv 2603.03312): modelos EEG-to-text alimentados con **ruido gaussiano puro siguen generando oraciones fluidas** — la "decodificación" era en gran parte el LLM alucinando. Proponen controles con perturbación de ruido.
   - *Evaluating EEG-to-text models through noise-based performance analysis* (Scientific Reports, 2025): análisis de degradación por ruido como protocolo de evaluación.
   - *What Are We Actually Decoding?* (arXiv 2605.24524): los priors del decodificador y las elecciones de protocolo (teacher-forcing) **inflan el rendimiento aparente**; con controles, la señal real aporta mucho menos de lo reportado.
   - *Do LLM Decoders Listen Fairly?* (arXiv 2604.21276): benchmark de cómo los priors del LM sesgan el reconocimiento.
2. **La dimensión ética está planteada** (le da peso al marco teórico):
   - *Control and Ownership of Neuroprosthetic Speech* (PMC8550345): ¿de quién son las palabras que produce el sistema?
   - *Recommendations for promoting user agency in speech neuroprostheses* (Frontiers, 2023): el LM introduce una contribución "fuera del control del usuario".

**El GAP (tu tesis):**

- Toda esa artillería de fidelidad se desarrolló para **EEG no invasivo**, donde los sistemas eran débiles y la alucinación, escandalosa.
- En los sistemas **intracorticales de alto rendimiento** (Willett 2023, Card 2024 — los de Nature/NEJM, con datos públicos), la fidelidad NO fue cuantificada sistemáticamente. Willett 2023 **afirma** que "el buen rendimiento no depende excesivamente del modelo de lenguaje" (la RNN decodifica fonemas sensatos antes del LM) — pero es una observación lateral, no un estudio de fidelidad con controles.
- **Nadie aplicó el protocolo de fidelidad (ruido, ablación de LM, atribución de fuente) a los sistemas intracorticales del benchmark público.**

**La tesis, formulada como prueba de una afirmación**: *"Willett et al. sostienen que sus sistemas no dependen excesivamente del LM. Esta tesis somete esa afirmación a prueba sistemática con el protocolo de fidelidad desarrollado para sistemas no invasivos."* — Probar (o refutar, o matizar) una afirmación de un paper de Nature con método riguroso: eso ES una tesis con dientes.

## Diseño experimental (implementación concreta)

Sobre el pipeline público del Brain-to-Text Benchmark (dataset speech de Willett en Dryad, código de referencia en GitHub):

**E1 — Ablación de la etapa de lenguaje (la base).**
Correr el sistema con: (a) RNN sola (salida cruda de fonemas → palabras por diccionario directo), (b) + LM n-gram chico, (c) + LM trigram 125k (el del paper), (d) + LLM rescoring (lo que usaron los ganadores del benchmark). Medir **PER** (error de fonemas, pre-LM) y **WER** (error de palabras, post-LM) en cada configuración. El "salto" PER→WER por configuración = **cuánto aporta el prior lingüístico**.

**E2 — Curvas de degradación (el experimento estrella).**
Mezclar la señal neural con ruido en proporciones crecientes (0%, 25%, 50%, 75%, 100%) y medir, para cada nivel: WER, fluidez de la salida (perplejidad según un LM externo) y una métrica nueva: **tasa de alucinación** = % de palabras fluidas-pero-incorrectas. La predicción interesante: con señal pura el sistema decodifica; con ruido creciente, ¿colapsa honestamente (salida rota) o **sigue produciendo frases fluidas que ya no vienen del cerebro**? El punto donde fluidez y fidelidad divergen es el resultado central de la tesis. (Metodología adaptada de *Escaping the BLEU Trap* — protocolo validado, aplicación nueva.)

**E3 — Sensibilidad al contenido.**
¿La fidelidad depende de qué se dice? Comparar oraciones predecibles (alta probabilidad según el LM) vs. raras (baja probabilidad). Hipótesis: el sistema "acierta" oraciones predecibles incluso con señal pobre (el LM las adivina) y falla las raras — un sesgo grave para un usuario real, que necesita decir cosas NO predecibles (nombres, síntomas, decisiones).

**E4 (si el tiempo alcanza) — Atribución.**
Medir cuánta información de la señal sobrevive hasta la salida (mutual information proxy / análisis del margen de decisión), siguiendo *What Are We Actually Decoding?*.

## Métricas

| Métrica | Qué mide | Estándar |
|---|---|---|
| PER | Error de fonemas ANTES del LM — la decodificación neural "pura" | Sí (Willett) |
| WER | Error de palabras después del LM | Sí (benchmark) |
| Δ(PER→WER) | El aporte del prior lingüístico | Derivada — tu contribución |
| Perplejidad de salida | Fluidez (independiente de corrección) | Sí (NLP) |
| Tasa de alucinación | Fluido pero ≠ ground truth | Definida en la tesis (basada en 2603.03312) |

## Plan de 4 meses

| Mes | Trabajo | Entregable |
|---|---|---|
| 1 | Marco teórico (historia BCI + los papers de fidelidad EEG + ética/agencia). Dominio del dataset y el pipeline. Diseño experimental formal. | Entrega 1 |
| 2 | Reproducir baseline (PER y WER del paper). Implementar E1 (ablación de LM por niveles). | Entrega 2 |
| 3 | E2 (degradación por ruido + tasa de alucinación) y E3 (sensibilidad al contenido). Análisis estadístico. | Entrega 3 |
| 4 | E4 opcional, análisis integral, discusión (técnica + implicancias de agencia del usuario), redacción final, código público. | Entrega 4 |

**Stack**: Python · PyTorch · dataset Dryad (speech) · código del benchmark · KenLM/n-gram + LLM ligero · GPU Colab Pro.

**Población y validación**: oraciones del conjunto de evaluación oficial (cientos), test pareado entre configuraciones sobre las mismas oraciones, varias semillas. Ver [[Tu-Tesis-Explicada-Simple]] §validación.

## Por qué esta tesis no es "de nicho"

- **La pregunta de fondo es universal**: ¿cuánto podemos confiar en lo que un sistema de IA dice en nombre de una persona? Es LA pregunta de AI reliability de esta década, instanciada en su caso más sensible.
- **Puentea dos subcampos**: trae la metodología de fidelidad (EEG no invasivo) a los sistemas de alto rendimiento (intracortical) donde nadie la aplicó.
- **Pone a prueba una afirmación de Nature** — no una curiosidad marginal.
- **Implicancias regulatorias**: conecta con agencia del usuario y neuroderechos ([[Temas-Candidatos-TFG|tema 18]]) sin dejar de ser un trabajo técnico medible.

## Objeciones anticipadas (simulacro para el tutor)

**"El sistema ya tiene 97,5% de precisión — ¿qué margen de mejora te queda?"**
> No busco mejorar la precisión: busco auditar qué significa. Es la diferencia entre un alumno que saca 97,5 sabiendo las respuestas y uno que dedujo por contexto: misma nota, distinto significado. Mido cuánto de ese número proviene de la señal neural y cuánto del modelo de lenguaje completando texto probable. Cuanto más alto el número publicado, más relevante la auditoría — nadie pregunta qué compone un número mediocre; los números espectaculares son los que hay que abrir.

**"¿Y si el resultado da que el sistema es fiel — no te quedás sin tesis?"**
> Al revés: el diseño es informativo en ambas direcciones. Fidelidad alta = primera cuantificación de una afirmación de Nature que estaba sin verificar. Fidelidad baja = hallazgo de un problema de confiabilidad con implicancias clínicas. No dependo de que el experimento "salga bien" — esa independencia del resultado es la marca de una buena pregunta.

**"¿Esto no es neurociencia?"**
> Los datos ya existen, públicos, grabados por Stanford. Mi trabajo es evaluación de sistemas de ML: ablaciones, métricas, protocolos reproducibles — ingeniería de software de confiabilidad aplicada al caso más sensible que existe.

**"¿Por qué nadie lo hizo antes?"**
> Porque el protocolo de fidelidad nació en 2025-2026 en el subcampo no invasivo (donde la alucinación era escandalosa) y los grupos intracorticales están enfocados en rendimiento, no en auditoría. La ventana entre ambos subcampos es exactamente donde se para esta tesis.

## Riesgos honestos

1. Willett podría tener razón (los sistemas intracorticales son fieles) → el resultado sigue siendo publicable: "verificamos cuantitativamente la afirmación" + las curvas de degradación son aporte igual.
2. Cómputo del dataset de speech → mitigación: subconjuntos + handwriting dataset como segundo escenario más liviano.
3. El campo EEG-fidelity avanza rápido → tu nicho intracortical + benchmark público te aísla (esos grupos trabajan sobre EEG y datasets propios).

## Referencias nuevas (verificadas hoy — sumar a las de [[Decodificacion-Brain-to-Text]])

- *Escaping the BLEU Trap: A Signal-Grounded Framework... EEG-to-Text Decoding*. arXiv:2603.03312.
- *What Are We Actually Decoding? Source Attribution for Non-Invasive Brain-to-Language Retrieval*. arXiv:2605.24524.
- *Do LLM Decoders Listen Fairly? Benchmarking How Language Model Priors Shape Bias in Speech Recognition*. arXiv:2604.21276.
- *Evaluating EEG-to-text models through noise-based performance analysis*. Scientific Reports (2025). https://www.nature.com/articles/s41598-025-29587-x
- *Control and Ownership of Neuroprosthetic Speech*. (PMC8550345) — ⚠️ completar metadatos APA exactos.
- *Recommendations for promoting user agency in the design of speech neuroprostheses*. Frontiers in Human Neuroscience (2023). https://doi.org/10.3389/fnhum.2023.1298129 — ⚠️ verificar DOI exacto.
