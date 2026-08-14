# Tema 19 — Fidelidad en la decodificación brain-to-text

> Estado: 🎯 **EN FOCO** · Investigación de implementación completa: [[../../20-Investigacion/Fidelidad-Brain-to-Text|Fidelidad-Brain-to-Text]]

## Definiciones Iniciales (formato oficial)

- **Tipo de TFG**: ☑ Trabajo de Investigación
- **Línea Temática**: ☑ Transformación Digital

### Título tentativo (~12 palabras)

Fidelidad en la decodificación brain-to-text: cuantificación del aporte del modelo de lenguaje frente a la señal neural

### Justificación de la Línea Temática elegida (3 renglones)

Las interfaces cerebro-computadora devuelven la comunicación digital a personas que la perdieron por completo — el caso más profundo de adopción de herramientas digitales para la vida. Garantizar que lo que el sistema "dice" provenga realmente del usuario es condición de confianza para que esa transformación sea adoptable y segura.

### Explicación del tema (5-15 renglones)

Los sistemas brain-to-text convierten la actividad neuronal de personas con parálisis en texto. Funcionan con dos componentes en serie: un decodificador neural, que traduce la señal del cerebro a sonidos del habla, y un modelo de lenguaje, que — como el autocorrector de un teléfono — completa y corrige esa salida usando su conocimiento del idioma. Los mejores sistemas reportan hasta 97,5% de precisión (Card et al., 2024, NEJM).

**Este trabajo NO busca mejorar ese número: busca auditarlo.** La distinción es la de un alumno que saca 97,5 en un examen múltiple choice: ¿sabía las respuestas o dedujo por contexto la opción esperable? La nota es la misma; el significado es distinto. Aplicado a estos sistemas: de cada 100 palabras correctas, ¿cuántas provienen realmente de la señal cerebral del paciente y cuántas las completó el modelo de lenguaje por ser lo estadísticamente probable?

La pregunta no es teórica: en el subcampo no invasivo se demostró que modelos alimentados con ruido puro (sin señal cerebral alguna) seguían generando oraciones fluidas — el rendimiento aparente era, en gran parte, el modelo de lenguaje adivinando. En los sistemas intracorticales de alto rendimiento — cuyos datos son públicos (repositorio Dryad, Stanford) — esa auditoría nunca se hizo: solo existe la afirmación de los autores de que la dependencia del modelo de lenguaje "no es excesiva". Este trabajo la somete a prueba con un protocolo medible y reproducible.

### Problema / pregunta de investigación (3-5 renglones)

¿Qué proporción de la salida de un sistema brain-to-text intracortical proviene de la señal neural del usuario y cuánta del prior lingüístico del modelo de lenguaje? ¿En qué condiciones (degradación de señal, contenido poco predecible) el sistema produce texto fluido que ya no refleja la intención del usuario — y cómo medirlo con un protocolo reproducible?

### Revisión de literatura principal (4 trabajos, APA)

1. Willett, F. R., Kunz, E. M., Fan, C., Avansino, D. T., Wilson, G. H., Choi, E. Y., Kamdar, F., Glasser, M. F., Hochberg, L. R., Druckmann, S., Shenoy, K. V., y Henderson, J. M. (2023). A high-performance speech neuroprosthesis. *Nature*, *620*(7976), 1031-1036. https://doi.org/10.1038/s41586-023-06377-x
2. Willett, F. R., et al. (2024). Brain-to-Text Benchmark '24: Lessons learned. *arXiv*. https://arxiv.org/abs/2412.17227
3. *Escaping the BLEU Trap: A Signal-Grounded Framework with Decoupled Semantic Guidance for EEG-to-Text Decoding*. (2026). *arXiv*. https://arxiv.org/abs/2603.03312
4. *Evaluating EEG-to-text models through noise-based performance analysis*. (2025). *Scientific Reports*. https://www.nature.com/articles/s41598-025-29587-x

### Justificación del TFG (15-20 renglones)

Las personas con parálisis total o esclerosis lateral amiotrófica avanzada conservan la mente intacta pero pierden todo canal de comunicación. Los sistemas brain-to-text ya demostraron devolverles el habla con precisión clínica, y sus datos y código son públicos, lo que permite investigarlos sin intervención sobre pacientes. Sin embargo, estos sistemas tienen una segunda cara: el usuario no puede corregir lo que el sistema dice en su nombre. Si el modelo de lenguaje completa palabras estadísticamente plausibles que no provienen de la señal cerebral, el sistema pone palabras en la boca de una persona sin voz — en contextos médicos, legales y familiares donde cada palabra importa. El subcampo no invasivo ya demostró que este riesgo es real; los sistemas intracorticales de alto rendimiento nunca fueron auditados con ese estándar. Este trabajo aporta esa auditoría: reproduce el sistema de referencia del benchmark público internacional, aísla el aporte de cada componente mediante ablación, construye curvas de degradación de señal que revelan cuándo la salida deja de ser fiel, y propone una métrica de tasa de alucinación aplicable a cualquier sistema de este tipo.

Cabe destacar que el objetivo no es superar la precisión publicada — donde el margen es mínimo — sino caracterizar su composición, y por eso el diseño es informativo en cualquier dirección: si la fidelidad resulta alta, se cuantifica por primera vez una afirmación publicada en Nature que carecía de verificación sistemática; si resulta menor de lo asumido, se revela un problema de confiabilidad con implicancias directas para los usuarios. El trabajo no depende de que un experimento "salga bien". El abordaje es íntegramente de ingeniería de software: pipelines de evaluación reproducibles, métricas estándar (PER/WER), análisis estadístico sobre el conjunto de evaluación oficial, y publicación del código. Los resultados benefician a la comunidad científica (verificación independiente), a la comunidad de software (protocolo de confiabilidad para sistemas de IA que hablan por sus usuarios) y a los usuarios finales, cuya agencia comunicativa es exactamente lo que está en juego.

## Ampliación

- Diseño experimental completo, métricas, plan de 4 meses y riesgos: [[../../20-Investigacion/Fidelidad-Brain-to-Text|Fidelidad-Brain-to-Text]]
- Contexto del campo e historia 2021→2024: [[../../20-Investigacion/Decodificacion-Brain-to-Text|Decodificacion-Brain-to-Text]]
- Preparación de la reunión con el tutor: [[../../20-Investigacion/Tu-Tesis-Explicada-Simple|Tu-Tesis-Explicada-Simple]] (actualizar analogías al enfoque de fidelidad)
