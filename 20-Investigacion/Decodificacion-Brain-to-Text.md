# Decodificación Brain-to-Text (intracortical)

> Nota de investigación · exploración profunda 2026-08-14 · candidato 🥇 del [[Temas-Candidatos-TFG|ranking de temas]]

## Síntesis

La decodificación *brain-to-text* convierte actividad neuronal de la corteza motora en texto, devolviéndole comunicación a personas con parálisis total o anartria. Es el problema insignia de la BCI invasiva moderna — el mismo que atacan Neuralink y los laboratorios académicos del consorcio BrainGate — y en cinco años pasó de demo de laboratorio a resultados clínicos espectaculares: 90 caracteres/minuto escribiendo "a mano" con la mente (2021), habla decodificada a 62 palabras/minuto (2023) y 97,5% de precisión sostenida con calibración de minutos (2024).

Lo extraordinario para una tesis de Ingeniería en Software: **los datos de estos papers de Nature/NEJM son públicos** (repositorio Dryad), el código de referencia está en GitHub, y existe un benchmark internacional activo (Brain-to-Text Benchmark) con leaderboard y lecciones documentadas. El cuello de botella del campo ya no es el implante — es el **software de decodificación**: mejor modelo = más palabras por minuto para el mismo hardware. Trabajarlo no requiere quirófano: requiere exactamente el stack de un AI engineer.

## La historia en tres saltos (todo verificado)

### 2021 — Handwriting BCI ([[Willett-2021]])

Participante con parálisis **imagina escribir a mano**; dos arrays de Utah (96 electrodos c/u) en el área de la mano de la corteza motora registran la actividad; una RNN decodifica trazos → caracteres.

- **90 caracteres/minuto con 94,1% de precisión cruda** (99%+ con autocorrección offline) — récord de la época.
- Pipeline: etiquetado con HMMs → RNN → language model.
- **Dataset público**: 1.000 oraciones, 43.501 caracteres, 10,7 horas de señal (Dryad, doi:10.5061/dryad.wh70rxwmv).
- **Código público**: github.com/fwillett/handwritingBCI (notebooks completos del pipeline).

### 2023 — Speech neuroprosthesis ([[Willett-2023]])

Participante T12 (ELA) **intenta hablar**; la RNN decodifica fonemas desde threshold crossings, y un language model (Kaldi) arma las palabras.

- **62 palabras/minuto** — 3,4× el récord anterior.
- **9,1% WER** en vocabulario de 50 palabras; **23,8% WER en vocabulario de 125.000 palabras** — la primera demostración de vocabulario abierto.
- ~41 min de datos de entrenamiento por sesión (260-480 oraciones).
- **Dataset público** en Dryad (doi:10.5061/dryad.x69p8czpq).

### 2024 — Precisión clínica ([[Card-2024]]) y el benchmark

**UC Davis (Card et al., NEJM 2024)**: participante con ELA, **99,6% de precisión con 50 palabras tras solo 30 minutos de calibración**; 90,2% con 125.000 palabras tras 1,4 h adicionales; **97,5% sostenida** en uso continuado. La calibración rápida — el mismo problema del [[Temas-Candidatos-TFG|tema 4]] — es ahora el diferenciador clínico.

**Brain-to-Text Benchmark '24** (arXiv 2412.17227) — las lecciones que definen el estado del arte y que son LA guía metodológica de la tesis:

1. **Baseline RNN: 9,7% WER.** Mejorar el ENTRENAMIENTO (schedule de learning rate, objetivo de difonos) lo bajó a **8,0%** — sin tocar la arquitectura.
2. **Los 3 mejores equipos usaron ensembles de decodificadores + merge con un LLM fine-tuneado.** El salto grande vino de ahí, no de arquitecturas nuevas.
3. **Transformers y state-space models NO superaron a la RNN** — un hallazgo contraintuitivo y abierto: ¿por qué la receta que domina el NLP no domina la decodificación neural? (Hipótesis del campo: pocos datos, señal no estacionaria, regularización distinta).
4. Código del 2° puesto público: github.com/CIBR-Okubo-Lab/speechBCI_2024.

## Qué haría la tesis, concretamente

**Pregunta**: ¿qué aporta más a la precisión de decodificación brain-to-text: la arquitectura del decodificador neural o el modelo de lenguaje que lo corrige? (ablación sistemática sobre el benchmark público)

| Mes | Trabajo |
|---|---|
| 1 | Marco teórico (BCIs intracorticales, spike features, seq2seq, el pipeline RNN+LM). Exploración de los datasets Dryad. Diseño: métricas CER/WER, splits oficiales del benchmark. |
| 2 | **Reproducir el baseline RNN** del benchmark (código público como referencia) y validar contra el 9,7%/8,0% publicado. Reproducir un resultado de Nature ya es defendible. |
| 3 | Experimento propio: ablación del language model (RNN sola vs +n-gram vs +LLM rescoring) y comparación GRU vs Transformer ligero con presupuesto de datos idéntico — atacando directamente la pregunta abierta del benchmark. |
| 4 | Análisis de errores cualitativo (qué fonemas confunde y por qué), corridas finales, redacción, código y configs publicados. |

**Stack**: Python · PyTorch · datasets Dryad · KenLM/n-gram + LLM ligero para rescoring · GPU (Colab Pro alcanza para el baseline; el dataset de speech es el más pesado).

**Encuadre institucional**: Trabajo de Investigación · Transformación Digital (tecnología que devuelve comunicación digital a quien la perdió — el caso de uso más fuerte imaginable de la línea).

## Por qué es defendible ante el tutor

- **Problema real con números**: la ELA y el síndrome de enclaustramiento dejan a personas cognitivamente intactas sin canal de salida; esta tecnología ya demostró 97,5% de precisión clínica. El software es el cuello de botella declarado del campo.
- **Datos públicos de papers de Nature/NEJM** — cero riesgo logístico, máxima legitimidad académica.
- **Benchmark internacional activo** — los resultados son comparables contra equipos de Stanford, no contra la nada.
- **Es Ingeniería en Software**: ML de secuencias, integración con language models, pipelines de evaluación reproducibles, análisis de latencia para tiempo real. Los cirujanos implantan; los ingenieros de software decodifican.
- **Pregunta abierta genuina**: por qué los Transformers no ganan acá es un misterio activo del campo — cualquier evidencia nueva es aporte.

## Riesgos honestos

- Los datos intracorticales tienen curva de aprendizaje (spike band power, bins de 20 ms, drift entre sesiones) — presupuestar el Mes 1 para domarla.
- El dataset de speech es grande; entrenar ensembles completos excede Colab gratuito → alcance: baseline + ablación, no ganar el leaderboard.
- La CAE probablemente no conozca el área → la presentación debe educar primero (la historia 2021→2024 en 3 láminas hace ese trabajo).

## Gaps identificados (candidatos a pregunta de investigación)

- ~~¿Por qué RNN > Transformers en decodificación neural?~~ → **ACTUALIZADO 2026-08-14, ver sección siguiente: la pregunta mutó.**
- ¿Cuánto del rendimiento es el LM "adivinando" vs la señal neural? (la ablación propuesta — sigue abierta)
- Transferencia entre participantes (cross-brain) — emergente en 2026, conecta con [[Temas-Candidatos-TFG|tema 4]].

## Estado de la pregunta de investigación (verificación 2026-08-14)

**Validación adversarial pedida por el usuario**: ¿sigue abierta la pregunta "por qué los Transformers no superan a la RNN"? **Respuesta honesta: en su forma 2024, NO — está mutando. Y eso la mejoró.**

**La contradicción documentada en la literatura** (esto es lo valioso):

- **2024**: El Benchmark '24 (arXiv 2412.17227, Willett et al.) reporta que Transformers y state-space models "no parecen ofrecer beneficio" sobre la RNN. Todos los ganadores usaron RNN + ensembles + LLM rescoring.
- **2025-2026**: la marea cambió:
  - *A generalizable speech neuroprosthesis* (bioRxiv 2026, ⚠️ preprint sin revisión de pares): un decodificador de fonemas **basado en Transformer escala con el tamaño del dataset y supera a la RNN en TODOS los tamaños**, con modelos multi-usuario logrando >50% menos WER relativo que modelos individuales.
  - *Cross-species neural foundation model* (arXiv 2511.21740): un encoder **pre-entrenado** supera tanto a RNNs como a Transformers entrenados desde cero.
  - Brain-to-Text '25 (competencia Kaggle, 466 participantes): los primeros puestos bajaron a ~1,5-1,8% WER con sistemas basados en Transformers (⚠️ fuente parcial: nota patrocinada de Tether en TechCrunch — verificar con el reporte oficial del benchmark '25 cuando se publique).
  - *Time-Masked Transformers with Lightweight Test-Time Adaptation* (arXiv 2507.02800) — más evidencia de Transformers competitivos.
  - NeurIPS 2025: *A Generalist Intracortical Motor Decoder* (Ye et al.) — escalar Transformers autorregresivos tiene límites propios por variabilidad entre datasets.

**La pregunta REFINADA (esta sí está abierta y es mejor):**

> **¿Bajo qué condiciones una arquitectura Transformer supera a la RNN como decodificador intracortical — cantidad de datos, pre-entrenamiento, uno vs. varios usuarios — y cuánto aporta cada etapa (decodificador neural vs. modelo de lenguaje) al rendimiento final?**

**Por qué esta versión aporta de verdad:**

1. **Adjudica una contradicción publicada**: 2024 dice "los Transformers no ayudan"; 2026 dice "ganan en todos los tamaños". Ambas no pueden ser ciertas sin condiciones de borde — mapearlas con protocolo controlado y reproducible sobre los datasets públicos ES el aporte. Las contradicciones documentadas son el mejor lugar donde puede pararse una tesis: garantizan que la respuesta le importa a alguien.
2. **Produce conocimiento de ingeniería accionable**: "usá RNN si tenés X datos y un solo usuario; Transformer si Y" — una guía de decisión de arquitectura, el tipo de resultado que la comunidad de software consume.
3. **Es robusta al avance del campo**: aunque salgan papers nuevos durante los 4 meses de tesis, una caracterización controlada en régimen de datos reproducible (un participante, presupuesto acotado — el caso real de un implante nuevo) no pierde validez: los preprints 2026 usan datos multi-usuario masivos privados; tu nicho es el régimen de datos del benchmark público.
4. La **ablación decodificador-vs-LM sigue intacta** como segunda pata: nadie publicó esa cuantificación sistemática.

**Riesgo declarado**: el campo se mueve rápido (competencias anuales, preprints). Mitigación: anclar la tesis al protocolo del benchmark público (comparabilidad garantizada) y encuadrarla como caracterización de condiciones, no como carrera de novedad.

## Referencias (APA)

- Willett, F. R., Avansino, D. T., Hochberg, L. R., Henderson, J. M., y Shenoy, K. V. (2021). High-performance brain-to-text communication via handwriting. *Nature*, *593*, 249-254. https://doi.org/10.1038/s41586-021-03506-2
- Willett, F. R., Kunz, E. M., Fan, C., Avansino, D. T., Wilson, G. H., Choi, E. Y., Kamdar, F., Glasser, M. F., Hochberg, L. R., Druckmann, S., Shenoy, K. V., y Henderson, J. M. (2023). A high-performance speech neuroprosthesis. *Nature*, *620*(7976), 1031-1036. https://doi.org/10.1038/s41586-023-06377-x
- Willett, F. R., et al. (2024). Brain-to-Text Benchmark '24: Lessons Learned. *arXiv*. https://arxiv.org/abs/2412.17227
- Card, N. S., et al. (2024). An accurate and rapidly calibrating speech neuroprosthesis. *New England Journal of Medicine*. ⚠️ Completar volumen/páginas/DOI exactos antes de citar en el TFG (verificado el estudio y la revista vía UC Davis Health y PMC11030484).

## Datasets y código

| Recurso | URL | Verificado |
|---|---|---|
| Dataset handwriting (2021) | https://doi.org/10.5061/dryad.wh70rxwmv | ✅ |
| Dataset speech (2023) | https://datadryad.org/dataset/doi:10.5061/dryad.x69p8czpq | ✅ |
| Código handwriting oficial | https://github.com/fwillett/handwritingBCI | ✅ |
| Código 2° puesto benchmark '24 | https://github.com/CIBR-Okubo-Lab/speechBCI_2024 | ✅ |

## Enlaces

Relacionadas: [[Temas-Candidatos-TFG]] · conceptos a desarrollar: [[Spike-band-power]], [[Pipeline-RNN-LM]], [[Word-Error-Rate]]
