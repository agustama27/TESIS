# Alternativas fuera de BCI — Ingeniería de Software × Sistemas LLM

> 2026-08-16 · Generado tras el rechazo de los 29 temas BCI del vault.
> **La lectura del patrón**: el [[Mapa-Ramas-SE-x-BCI]] cubrió TODAS las ramas de la carrera dentro de BCI y ninguno convenció al autor — incluido el 25, que era el de mayor motivación declarada. Cuando el mapa completo de un dominio no enciende nada, el candidato a problema es el dominio, no la lista.
> **La hipótesis de este documento**: el dominio con motivación real es el que el autor ya ejerce a diario como AI Engineer — agentes LLM, agentes de voz, evaluación y testing de sistemas de IA. Todos los temas siguen la vara correcta de [[../../20-Investigacion/Calibracion-Alcance-Tesis-BCI|Calibración]]: "diseñar/implementar/evaluar sobre algo existente", datos/código públicos, sin hardware, ejecutable en 4 meses.

## Por qué este espacio es legítimo académicamente (verificado hoy)

La ingeniería de software para sistemas basados en LLM es un área de investigación activa y en formación — exactamente el momento en que los TFG de "diseño e implementación" tienen más valor:

- [LLM-Based Agentic Systems for Software Engineering: Challenges and Opportunities (arXiv 2601.09822)](https://arxiv.org/abs/2601.09822)
- [A Survey on Evaluation of LLM-based Agents (arXiv 2503.16416)](https://arxiv.org/html/2503.16416v2)
- [Evaluation and Benchmarking of LLM Agents: A Survey (KDD 2025)](https://dl.acm.org/doi/10.1145/3711896.3736570)
- [Evaluation of LLM-Based Software Engineering Tools: Practices, Challenges, and Future Directions (arXiv 2604.24621)](https://arxiv.org/html/2604.24621v1)
- FSE 2026 tiene track con papers de testing de regresión basado en LLM: [Evaluating LLM-based Regression Test Generation](https://conf.researchr.org/details/fse-2026/fse-2026-research-papers/54/Evaluating-LLM-based-Regression-Test-Generation)

El problema central del área es 100% Ingeniería de Software: **los sistemas LLM son no deterministas, y todo el arsenal clásico de testing (asserts exactos, regresión por diff) se rompe**. Reconstruir QA para esta clase de sistemas es disciplina núcleo de la carrera.

---

## Tema A — Framework de pruebas de regresión para agentes conversacionales LLM

**Formato tesis**: *"Diseño e implementación de un framework de pruebas de regresión automatizadas para agentes conversacionales basados en LLM"*.

- **El problema**: cambiar un prompt, un modelo o un flujo puede degradar silenciosamente al agente. El testing clásico no aplica (salidas abiertas, no determinismo). Se necesita: simulación de usuario, gold sets, LLM-as-judge, métricas semánticas, integración CI/CD.
- **Sobre qué construir**: [IntellAgent — framework multi-agente open source para evaluar IA conversacional (arXiv 2501.11067)](https://arxiv.org/pdf/2501.11067); precedentes industriales [promptfoo](https://medium.com/@alexrodriguesj/testing-llm-prompts-like-code-regression-evals-in-ci-cd-with-promptfoo-5242b4dcb9be) y [DeepEval](https://deepeval.com/blog/top-5-llm-evaluation-frameworks) (pytest-style, CI/CD).
- **Hueco tipo "extensión declarada"**: los frameworks existentes evalúan en inglés y de forma genérica; diseñar y evaluar un framework con simulación de usuario **en español** y validación por estado de la conversación (estilo tau-bench: verificar el resultado, no el texto) es extensión concreta.
- **Ventaja brutal**: es literalmente lo que el autor hace en Evoltis con Cekura y batch testing de Retell. La curva de aprendizaje es CERO — toda la energía va a la ejecución rigurosa.
- **Tipo TFG**: Prototipado Tecnológico. Motivación presunta: **alta**. Riesgo: bajo.
- ⚠️ **A verificar**: que no haya conflicto de propiedad intelectual con el empleador si el prototipo se parece demasiado a herramientas internas del trabajo. Construirlo open source, sobre casos públicos, y en tiempo propio.

## Tema B — Evaluación de agentes de voz: suite de fallos específicos de voz

**Formato tesis**: *"Diseño y evaluación de una suite de pruebas para modos de fallo específicos de voz en agentes conversacionales telefónicos"*.

- **El problema verificado**: ~42% de los problemas de producción en agentes de voz son específicos de voz (turnos, interrupciones, latencia, telefonía) e **invisibles para evaluaciones basadas solo en transcript** ([Cekura, métricas 2026](https://www.cekura.ai/blogs/voice-ai-evaluation-metrics)). La capa de telefonía (pérdida de paquetes, codecs, jitter) casi no se testea ([Speechmatics 2026](https://www.speechmatics.com/company/articles-and-news/de-risk-your-voice-agent-11-best-voice-agent-testing-platforms)).
- **Sobre qué construir**: [EVA-Bench (arXiv 2605.13841)](https://arxiv.org/abs/2605.13841) — framework end-to-end con métricas EVA-A (exactitud) y EVA-X (experiencia); [VoiceAgentEval (arXiv 2510.21244)](https://arxiv.org/pdf/2510.21244); [VISTA — simulación interactiva de usuarios (arXiv 2606.11079)](https://arxiv.org/pdf/2606.11079). Solo existe UNA evaluación cruzada independiente de plataformas (arXiv 2511.04133, cubre 3 plataformas) — el área está casi virgen.
- **Hueco tipo "ausencia verificable"**: nada de esto existe evaluado **en español** (menos aún rioplatense: turnos, muletillas, interrupciones culturalmente distintas).
- **Tipo TFG**: Prototipado Tecnológico o Investigación Aplicada. Motivación presunta: **máxima** — es el día a día del autor elevado a rigor académico.

## Tema C — Benchmark de evaluación de agentes LLM en español

**Formato tesis**: *"Construcción y validación de un benchmark de evaluación para agentes conversacionales con uso de herramientas en español"*.

- **El hueco**: los benchmarks serios (tau-bench, SWE-Bench, [MANTRA — compliance validada por SMT (arXiv 2605.06334)](https://arxiv.org/pdf/2605.06334)) son en inglés. Un benchmark en español con verificación por ejecución (estado de base de datos, no juicio de texto) es ausencia verificable — el mismo patrón que hacía sólido al tema 24, pero en un dominio que sí entusiasma.
- **Tipo TFG**: Investigación Aplicada. Más "dataset paper" que "sistema" — elegirlo solo si construir datos motiva más que construir software.

## Tema D (reserva) — Observabilidad de sistemas multi-agente

*"Diseño e implementación de una capa de observabilidad/tracing para sistemas multi-agente LLM"* — OpenTelemetry aplicado a agentes, con [Langfuse/Phoenix](https://www.confident-ai.com/knowledge-base/compare/best-ci-cd-tools-ai-applications-2026) como precedentes. Menos anclas académicas verificadas hoy; desarrollar solo si A/B/C no convencen.

---

## Cómo se compara con los finalistas BCI

| Tema | Hueco | Ejecutabilidad 4 meses | Motivación presunta | Curva de aprendizaje | Riesgo |
|---|---|---|---|---|---|
| A · Regresión agentes LLM | Extensión declarada (español + verificación por estado) | **Máxima** | **Alta** (es su oficio) | **Nula** | Bajo |
| B · Evaluación voz | **Ausencia verificable** (español, capa voz/telefonía) | Alta | **Máxima** | Baja | Bajo-medio |
| C · Benchmark español | Ausencia verificable | Alta | Media (¿datos > código?) | Baja | Bajo |
| 25 · SNN (mejor BCI) | Extensión FALCON | Media-alta | Alta declarada… pero no eligió | ~1 mes | Medio |
| 24 · LLM español (mejor en papel) | Ausencia verificable | Máxima | Baja | Baja | Bajo |

**Nota honesta**: el tema 24 ya era "LLM en español" y no entusiasmó. La diferencia de A y B no es el stack — es que el *problema* (testear agentes) es el que el autor resuelve todos los días y conoce visceralmente. Si A y B tampoco encienden nada, el problema no es el tema ni el dominio, y conviene otra conversación.

## Pendientes

- [ ] Decisión del autor: ¿se descarta BCI como dominio del TFG o convive con estas alternativas?
- [ ] Si A o B interesa: verificar con la universidad que la línea temática admite sistemas LLM (las líneas suelen ser amplias: calidad de software, IA aplicada).
- [ ] Si A: aclarar el límite de propiedad intelectual con Evoltis.
- [ ] Prueba de humo equivalente al [[Roadmap-Tema-25]]: un sábado, 3 horas — levantar IntellAgent o promptfoo contra un agente propio y ver si el problema engancha.

## Enlaces

[[00-Indice]] · [[Reevaluacion-2026-08-15]] · [[Mapa-Ramas-SE-x-BCI]]
