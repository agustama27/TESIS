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

Los sistemas brain-to-text convierten actividad neuronal de personas con parálisis en texto, combinando dos componentes: un decodificador neural (una red recurrente que traduce la señal a fonemas) y un modelo de lenguaje que corrige y completa la salida. Los mejores sistemas reportan hasta 97,5% de precisión (Card et al., 2024, NEJM). Sin embargo, investigaciones recientes en el subcampo no invasivo demostraron que parte del rendimiento aparente proviene del modelo de lenguaje "adivinando" texto plausible y no de la señal cerebral: modelos alimentados con ruido puro siguieron generando oraciones fluidas. En los sistemas intracorticales de alto rendimiento — cuyos datos son públicos (repositorio Dryad, Stanford) — esa fidelidad nunca fue cuantificada sistemáticamente: solo existe la afirmación de los autores de que la dependencia del modelo de lenguaje no es excesiva. Este trabajo somete esa afirmación a prueba, midiendo cuánto aporta cada componente y en qué condiciones el sistema deja de decodificar y empieza a completar.

### Problema / pregunta de investigación (3-5 renglones)

¿Qué proporción de la salida de un sistema brain-to-text intracortical proviene de la señal neural del usuario y cuánta del prior lingüístico del modelo de lenguaje? ¿En qué condiciones (degradación de señal, contenido poco predecible) el sistema produce texto fluido que ya no refleja la intención del usuario — y cómo medirlo con un protocolo reproducible?

### Revisión de literatura principal (4 trabajos, APA)

1. Willett, F. R., Kunz, E. M., Fan, C., Avansino, D. T., Wilson, G. H., Choi, E. Y., Kamdar, F., Glasser, M. F., Hochberg, L. R., Druckmann, S., Shenoy, K. V., y Henderson, J. M. (2023). A high-performance speech neuroprosthesis. *Nature*, *620*(7976), 1031-1036. https://doi.org/10.1038/s41586-023-06377-x
2. Willett, F. R., et al. (2024). Brain-to-Text Benchmark '24: Lessons learned. *arXiv*. https://arxiv.org/abs/2412.17227
3. *Escaping the BLEU Trap: A Signal-Grounded Framework with Decoupled Semantic Guidance for EEG-to-Text Decoding*. (2026). *arXiv*. https://arxiv.org/abs/2603.03312
4. *Evaluating EEG-to-text models through noise-based performance analysis*. (2025). *Scientific Reports*. https://www.nature.com/articles/s41598-025-29587-x

### Justificación del TFG (15-20 renglones)

Las personas con parálisis total o esclerosis lateral amiotrófica avanzada conservan la mente intacta pero pierden todo canal de comunicación. Los sistemas brain-to-text ya demostraron devolverles el habla con precisión clínica, y sus datos y código son públicos, lo que permite investigarlos sin intervención sobre pacientes. Sin embargo, estos sistemas tienen una segunda cara: el usuario no puede corregir lo que el sistema dice en su nombre. Si el modelo de lenguaje completa palabras estadísticamente plausibles que no provienen de la señal cerebral, el sistema pone palabras en la boca de una persona sin voz — en contextos médicos, legales y familiares donde cada palabra importa. El subcampo no invasivo ya demostró que este riesgo es real; los sistemas intracorticales de alto rendimiento nunca fueron auditados con ese estándar. Este trabajo aporta esa auditoría: reproduce el sistema de referencia del benchmark público internacional, aísla el aporte de cada componente mediante ablación, construye curvas de degradación de señal que revelan cuándo la salida deja de ser fiel, y propone una métrica de tasa de alucinación aplicable a cualquier sistema de este tipo. El abordaje es íntegramente de ingeniería de software: pipelines de evaluación reproducibles, métricas estándar (PER/WER), análisis estadístico sobre el conjunto de evaluación oficial, y publicación del código. Los resultados benefician a la comunidad científica (verificación independiente de una afirmación publicada en Nature), a la comunidad de software (protocolo de evaluación de confiabilidad para sistemas de IA que hablan por sus usuarios) y, en última instancia, a los usuarios finales de estas tecnologías, cuya agencia comunicativa es exactamente lo que está en juego.

## Ampliación

- Diseño experimental completo, métricas, plan de 4 meses y riesgos: [[../../20-Investigacion/Fidelidad-Brain-to-Text|Fidelidad-Brain-to-Text]]
- Contexto del campo e historia 2021→2024: [[../../20-Investigacion/Decodificacion-Brain-to-Text|Decodificacion-Brain-to-Text]]
- Preparación de la reunión con el tutor: [[../../20-Investigacion/Tu-Tesis-Explicada-Simple|Tu-Tesis-Explicada-Simple]] (actualizar analogías al enfoque de fidelidad)
