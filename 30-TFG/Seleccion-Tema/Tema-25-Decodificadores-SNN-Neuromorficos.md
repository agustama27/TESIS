# Tema 25 — Redes de impulsos para decodificar señales del cerebro

> Estado: 🎯 **EN FOCO** (finalista junto a [[Tema-24-LLM-Comunicacion-Asistida-Espanol|24]] y [[Tema-19-Fidelidad-Brain-to-Text|19]])
> **Cómo leer esta página**: las secciones 1 a 5 son para entender el tema (cualquier persona las entiende). De la 6 en adelante es el material formal para el formulario de la universidad y la ejecución.

---

# PARTE A — El tema, en criollo

## 1. La tesis en una frase

**Poner a competir dos tipos de programas que traducen señales del cerebro — el que se usa hoy y uno nuevo que gasta mucha menos energía — y medir cuál traduce mejor y a qué costo.**

Eso es todo. El resto de la página explica por qué eso importa y cómo se hace.

## 2. El problema, contado como historia

**Paso 1.** Hay personas paralizadas que tienen un chip implantado en la cabeza. Ese chip escucha sus neuronas.

**Paso 2.** Un **programa** traduce esa actividad cerebral en algo útil: mover un cursor, escribir, controlar una prótesis. Ese programa se llama *decodificador*. Ya existe y funciona.

**Paso 3.** Hoy ese programa corre en **una computadora grande al lado del paciente**, enchufada a la pared. El objetivo de la industria es que corra **adentro del propio chip**, en la cabeza — sin cables, sin computadora externa.

**Paso 4. Y acá está el problema**: un chip dentro del cráneo **no puede calentarse**, porque está tocando tejido cerebral. Su presupuesto de energía es minúsculo — menos que una lamparita de navidad. Los programas de inteligencia artificial normales **gastan demasiado** para entrar ahí.

> **El problema en una línea**: el traductor funciona, pero consume demasiado para vivir dentro del implante.

⚠️ **Precisión importante — no apostamos a una predicción**: no se afirma que "el futuro sea decodificar todo adentro". La literatura documenta **dos caminos vigentes** (cómputo en el implante vs. en un dispositivo externo) y trata el reparto como un **compromiso de diseño abierto**; la práctica actual es híbrida. Lo que sí está establecido es que la transmisión es el mayor consumidor de energía y que el reparto depende de **cuánto cuesta computar adentro** — que es justamente la variable que esta tesis mide. Evidencia de ambos lados: [[../../20-Investigacion/Donde-Decodificar-Adentro-o-Afuera|¿Dónde decodificar?]].

## 3. La solución que se está explorando

Comparemos dos formas de computar:

| | Cómo trabaja | Consumo |
|---|---|---|
| **Red neuronal normal** (la de hoy) | Como una **oficina donde todos los empleados hacen cuentas todo el tiempo**, haya trabajo o no | Alto |
| **Red de impulsos / SNN** (la candidata) | Como un **sereno con silbato**: en silencio, y solo hace *¡pip!* cuando pasa algo | Muy bajo |

Las redes de impulsos copian el truco del cerebro real: por eso tu cerebro entero, más potente que cualquier computadora en muchas cosas, funciona con **20 watts — lo que gasta una lamparita**.

**Y hay una coincidencia hermosa**: ¿qué graban los electrodos dentro de la cabeza? Los "pips" de las neuronas reales. O sea que la red de impulsos y el cerebro **hablan el mismo idioma**. Hoy el sistema convierte esos pips a números para dárselos a la red normal; con una red de impulsos, esa traducción intermedia sobra.

## 4. Entonces, ¿qué hago YO en la tesis?

Acá está la clave que hay que tener clarísima — **qué ya existe y qué aporto yo**:

| Ya existe (lo uso) | Lo hago yo (es mi tesis) |
|---|---|
| Las grabaciones de cerebros reales (públicas, en internet) | El **experimento comparativo** |
| Los dos tipos de programas traductores | Ponerlos a competir **en igualdad de condiciones** |
| Las herramientas para medir | La **tabla de resultados** y su análisis |

**Cómo lo hago**: agarro las mismas grabaciones, entreno los dos traductores, y a cada uno le mido tres números:

1. **¿Qué tan bien traduce?** (¿acierta lo que la persona quiso hacer?)
2. **¿Cuántas cuentas hizo?** (el termómetro de cuánta energía gastaría)
3. **¿Qué tan rápido responde?**

**El resultado es una tabla**, y esa tabla responde la pregunta que la industria necesita: *¿el traductor eficiente ya está a la altura, o todavía le falta — y cuánto?*

## 5. ¿Y dónde está la originalidad? (la analogía de las zapatillas)

Ya hay otros trabajos que probaron redes de impulsos para esto. **Pero fijate el problema:**

Imaginate cinco marcas de zapatillas de running. Cada una publicó "las nuestras son las más rápidas" — pero **la A midió en su pista, la B en otra pista, la C en cinta bajo techo**, cada una con su corredor y su cronómetro. Las cinco tienen razón en sus datos… **y ninguna es comparable con las otras**. Nadie sabe cuál es realmente mejor.

Eso pasa hoy con las redes de impulsos en decodificación neural: hay como ocho trabajos, cada uno con **su** dataset, **su** métrica y **su** forma de medir energía. Todos válidos, ninguno comparable.

> **Mi aporte: yo organizo la carrera.** Traigo a los competidores a la misma pista (un benchmark público), les pongo el mismo cronómetro a todos (una herramienta de medición estandarizada), mismas reglas — y publico la tabla de posiciones.
>
> La originalidad no es inventar una zapatilla nueva. Es ser **el juez de la carrera que nadie organizó todavía**. En ciencia eso se llama estudio comparativo, y es lo que un campo joven necesita para saber dónde está parado.

**Bonus**: que existan antecedentes juega a favor — hay código para reutilizar y papers que legitiman la línea. Un campo vacío sería mucho más riesgoso para 4 meses.

## 6. Por qué NO hay resultado malo

- Si las redes de impulsos **igualan** la precisión gastando mucho menos → evidencia de que los implantes del futuro pueden usarlas. Gran noticia.
- Si **pierden** precisión → sos el primero en medir limpio cuánto cuesta el ahorro. También es conocimiento nuevo y útil.

La tesis no depende de que un experimento "salga bien". Depende de medir bien.

## 7. El guion de 60 segundos (para contárselo a cualquiera)

> "Hay gente paralizada con chips en la cabeza que traducen sus neuronas en movimientos o palabras. El programa traductor hoy corre en una computadora grande, pero el objetivo es que corra adentro del chip — y ahí no puede gastar energía, porque un chip que se calienta daña el cerebro. Existe un tipo de inteligencia artificial que computa como el cerebro mismo: en silencio, activándose solo cuando hace falta, como un sereno con silbato en vez de una oficina calculando sin parar — y por eso gasta muchísimo menos. Ya hay trabajos que la probaron, pero cada uno midió a su manera y no se pueden comparar entre sí. Mi tesis los pone a competir en la misma pista, con el mismo cronómetro, y publica la tabla de posiciones. Eso le dice a la industria de los implantes si el futuro eficiente ya llegó o cuánto le falta."

---

# PARTE B — Material formal

> A partir de acá es el contenido para el formulario de la universidad y la ejecución del trabajo.

## 8. Definiciones Iniciales (formato oficial)

- **Tipo de TFG**: ☑ Trabajo de Investigación
- **Línea Temática**: ☑ Transformación Digital

### Título tentativo (~12 palabras)

Evaluación de redes neuronales de impulsos como decodificadores neuronales eficientes en energía

### Justificación de la Línea Temática elegida (3 renglones)

Los implantes neurales solo escalarán a productos cotidianos cuando su software de decodificación pueda ejecutarse con consumo mínimo dentro del dispositivo. Evaluar el paradigma de cómputo que promete esa eficiencia es evaluar la viabilidad energética de la transformación digital neurotecnológica.

### Explicación del tema (5-15 renglones)

Los decodificadores neuronales actuales usan redes convencionales que computan con valores continuos y consumo elevado — aceptable en una computadora de laboratorio, inviable dentro de un implante cuyo presupuesto energético es de milivatios, porque el calor disipado dañaría el tejido cerebral. Las redes neuronales de impulsos (SNN) computan como las neuronas biológicas: unidades que permanecen en silencio y disparan impulsos discretos solo ante actividad relevante, con un costo por operación muy inferior. La literatura 2024-2025 muestra trabajo activo en SNN para decodificación intracortical, pero cada estudio emplea datasets, métricas y protocolos propios, por lo que sus resultados no son comparables entre sí. Este trabajo produce la comparación unificada que falta: entrena decodificadores convencionales (referencia) y SNN — mediante frameworks abiertos sobre PyTorch — sobre los mismos datasets públicos de movimiento, y mide en cada caso la precisión de decodificación, el número de operaciones de cómputo (el proxy de energía estándar en la literatura) y la latencia. La señal intracortical ya está compuesta de impulsos, por lo que las SNN la procesan en formato nativo. El resultado es el mapa del compromiso entre precisión y energía de ambos paradigmas.

### Problema / pregunta de investigación (3-5 renglones)

¿Pueden los decodificadores basados en redes de impulsos igualar la precisión de los decodificadores convencionales sobre señal intracortical pública, y con qué reducción de operaciones de cómputo lo logran? ¿En qué condiciones (tarea, cantidad de datos, arquitectura) el paradigma neuromórfico resulta preferible como software de decodificación?

### Revisión de literatura principal (4 trabajos, APA)

1. *Few-shot Algorithms for Consistent Neural Decoding (FALCON) Benchmark*. (2024). *NeurIPS Datasets and Benchmarks Track*. https://proceedings.neurips.cc/paper_files/paper/2024/file/8c2e6bb15be1894b8fb4e0f9bcad1739-Paper-Datasets_and_Benchmarks_Track.pdf
2. *Adaptively Pruned Spiking Neural Networks for Energy-Efficient Intracortical Neural Decoding*. (2025). *arXiv*. https://arxiv.org/abs/2504.11568
3. *A Scalable, Causal, and Energy Efficient Framework for Neural Decoding with Spiking Neural Networks*. (2025). *arXiv*. https://arxiv.org/abs/2510.20683
4. *Multiscale fusion enhanced spiking neural network for invasive BCI neural signal decoding*. (2025). *Frontiers in Neuroscience*. https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2025.1551656/full

### Justificación del Trabajo Final de Graduación (borrador — expandir a 15-20 renglones al confirmar)

El consumo energético del software es hoy un atributo de calidad de primera clase (green software engineering), y en ningún dominio es tan crítico como dentro de un implante cerebral, donde el calor disipado tiene un límite fisiológico estricto. Las redes de impulsos prometen resolver exactamente ese problema, pero la evidencia comparativa contra los decodificadores convencionales está fragmentada: cada trabajo publicado usa su propio dataset, sus propias métricas y su propio protocolo de medición, de modo que la comunidad no puede establecer con rigor en qué punto se encuentra el paradigma. Este trabajo aporta la comparación unificada que falta, con protocolo reproducible sobre benchmarks públicos y métricas declaradas de antemano (precisión, operaciones de cómputo y latencia). El diseño es informativo en cualquier dirección: si las redes de impulsos igualan la precisión con una fracción del cómputo, se aporta evidencia de viabilidad para el despliegue dentro del implante; si pierden precisión, se cuantifica por primera vez el costo real del paradigma en este dominio. El abordaje es íntegramente de ingeniería de software: evaluación empírica de dos paradigmas de software para el mismo problema, con la energía como requisito no funcional cuantificado, y publicación reproducible del código. No requiere hardware especializado: el entrenamiento se realiza en GPU estándar mediante frameworks abiertos y la energía se estima por conteo de operaciones, el método aceptado por la literatura del área.

## 9. Alcance — qué SÍ y qué NO

**Incluye**: datasets públicos de movimiento (FALCON / Neural Latents Benchmark); un decodificador convencional de referencia frente a 1-2 arquitecturas de red de impulsos; métricas de precisión, operaciones de cómputo y latencia; análisis del compromiso entre ambas.

**Excluye** (declarado desde el inicio): chips neuromórficos físicos — la energía se **estima**, no se mide con instrumentos; implantes reales; tiempo real estricto; una segunda tarea solo si sobra tiempo.

## 10. Plan de 4 meses

| Mes | Trabajo |
|---|---|
| 1 · Entrega 1 | Curva de aprendizaje del paradigma (tutoriales, 2-3 semanas) + marco teórico + diseño experimental + mapeo de huecos. **El mes de mayor riesgo — declarado.** |
| 2 · Entrega 2 | Decodificador convencional de referencia reproducido y medido; primera red de impulsos funcionando; medición automatizada. |
| 3 · Entrega 3 | Barrido de configuraciones, varias semillas por condición, análisis estadístico, construcción de la tabla y las curvas. |
| 4 · Entrega 4 | Análisis final, discusión de implicancias para implantes, redacción, código público. |

**Herramientas**: Python · PyTorch · snnTorch o SpikingJelly · datasets FALCON/NLB · Google Colab (GPU moderada).

Detalle operativo semana a semana, con el gate de decisión de las primeras dos semanas: [[Roadmap-Tema-25]].

## 11. Materia prima verificada (existe y está disponible)

| Recurso | Qué es | URL |
|---|---|---|
| FALCON datasets | 5 datasets de movimiento, descarga directa desde DANDI | https://snel-repo.github.io/falcon/datasets.html |
| snnTorch / SpikingJelly | Frameworks de redes de impulsos sobre PyTorch, con tutoriales | https://snntorch.readthedocs.io · https://github.com/fangwei123456/spikingjelly |
| **fmi-basel/neural-decoding-RSNN** | **Código público del problema exacto**: decodificación de velocidad de dedos con redes de impulsos (modelos `bigRSNN` y `tinyRSNN`) | https://github.com/fmi-basel/neural-decoding-RSNN |
| **NeuroBench** | Herramienta de benchmarking neuromórfico (*Nature Communications*, 2025) con conteo estandarizado de operaciones | https://github.com/NeuroBench/neurobench |

**Tarea obligatoria del Mes 1**: mapear qué comparaciones ya cubrieron esos trabajos, para posicionar con precisión el aporte propio.

## 12. Riesgo principal (honesto)

Es el finalista con mayor curva de aprendizaje: alrededor de un mes para volverse productivo en un paradigma nuevo (los otros dos usan el stack actual del autor desde el día uno). A cambio, es el perfil más orientado a investigación de frontera: las redes de impulsos para implantes son una apuesta a 5-10 años y tema natural de posgrado.

## 13. Comparación con los otros finalistas

| | 24 · LLM comunicación asistida | 19 · Fidelidad | 25 · Redes de impulsos |
|---|---|---|---|
| Distancia del stack actual | Cero | Corta | Un mes de curva |
| Riesgo técnico | Bajo | Medio | Medio-alto |
| Impacto social inmediato | Máximo | Alto | Indirecto (habilita implantes futuros) |
| Señal para posgrado | Alta | Alta | Máxima |

## Enlaces

[[Roadmap-Tema-25]] · [[../../20-Investigacion/Historia-Spiking-Neural-Networks|Historia de las redes de impulsos]] · [[00-Indice]]
