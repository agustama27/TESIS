# Tema 23 — Del paper al dispositivo: compresión de decodificadores brain-to-text

> Estado: 🎯 **EN FOCO** (finalista junto al [[Tema-19-Fidelidad-Brain-to-Text|tema 19]]) · agregado 2026-08-14
> Origen: diseñado desde las búsquedas laborales reales de Neuralink — la intersección AI engineering × Software Engineering × neurotecnología.

## La idea en palabras simples

El programa que convierte señales del cerebro en texto (el de los papers de Nature) hoy solo funciona en computadoras potentes de laboratorio, sin apuro y enchufadas a la pared. Para que le sirva a una persona real, tiene que correr en el aparato que lleva puesto: chico, rápido y gastando casi nada de batería. **Tu tesis: achicar ese programa paso a paso — con las técnicas estándar que la industria ya usa para meter inteligencia artificial en los celulares — y medir cuánta calidad pierde en cada paso, hasta encontrar el punto justo.** El resultado es una tabla: cada fila es una versión del programa (original, mitad de tamaño, un cuarto…) con tres números: qué tan preciso quedó, qué tan rápido responde, cuánto pesa. Esa tabla, y el análisis de dónde está el equilibrio óptimo, es la tesis.

## Definiciones Iniciales (formato oficial)

- **Tipo de TFG**: ☑ Trabajo de Investigación
- **Línea Temática**: ☑ Transformación Digital

### Título tentativo (~12 palabras)

Compresión y optimización de decodificadores brain-to-text para inferencia en tiempo real

### Justificación de la Línea Temática elegida (3 renglones)

Los sistemas que devuelven la comunicación a personas paralizadas ya funcionan en laboratorio, pero solo llegarán a la vida real cuando corran en dispositivos portátiles de bajo consumo. Cerrar la brecha entre el prototipo científico y el producto usable es, literalmente, hacer adoptable la transformación digital más profunda que existe.

### Explicación del tema (5-15 renglones)

Los decodificadores brain-to-text del estado del arte (Willett 2023; Card 2024) convierten señal cerebral en texto con precisión clínica, pero se ejecutan sin restricciones: computadoras de laboratorio, GPU, sin límite de latencia ni de energía. Un dispositivo real impone lo contrario: respuesta en milisegundos y consumo mínimo — las búsquedas laborales de Neuralink piden exactamente ingenieros que dominen "quantization effects" y "constraints on power, latency and throughput". La industria del software ya resolvió este problema para otros dominios: las técnicas de compresión de modelos (cuantización: guardar los números del modelo con menos precisión; poda: eliminar conexiones que casi no aportan; destilación: entrenar un modelo chico para imitar al grande) son las que hoy meten modelos de lenguaje en celulares. Este trabajo las aplica sistemáticamente al decodificador público del Brain-to-Text Benchmark y construye el mapa precisión-latencia-tamaño: cuánta calidad de decodificación sobrevive a cada nivel de compresión y dónde está la frontera del tiempo real.

### Problema / pregunta de investigación (3-5 renglones)

¿Cuánta precisión de decodificación (WER) se pierde al comprimir un decodificador brain-to-text mediante cuantización, poda y destilación, y dónde está la frontera óptima entre precisión, latencia y tamaño del modelo bajo un presupuesto de inferencia en tiempo real?

### Revisión de literatura principal (4 trabajos, APA)

1. Willett, F. R., Kunz, E. M., Fan, C., Avansino, D. T., Wilson, G. H., Choi, E. Y., Kamdar, F., Glasser, M. F., Hochberg, L. R., Druckmann, S., Shenoy, K. V., y Henderson, J. M. (2023). A high-performance speech neuroprosthesis. *Nature*, *620*(7976), 1031-1036. https://doi.org/10.1038/s41586-023-06377-x
2. Willett, F. R., et al. (2024). Brain-to-Text Benchmark '24: Lessons learned. *arXiv*. https://arxiv.org/abs/2412.17227
3. *Low-latency neural inference framework for real-time handwriting recognition from EEG signals on an edge device*. (2025). *Scientific Reports*. https://www.nature.com/articles/s41598-025-24972-y
4. *Latency-Aware Pruning and Quantization of Self-Supervised Speech Transformers for Edge Devices*. *ACM Transactions on Embedded Computing Systems*. https://dl.acm.org/doi/10.1145/3746638

### Justificación del Trabajo Final de Graduación (15-20 renglones)

Las personas con parálisis total ya pueden comunicarse mediante decodificadores cerebrales con precisión clínica — en el laboratorio. El paso que falta para que esa tecnología llegue a la vida cotidiana no es científico sino de ingeniería: los modelos publicados son demasiado grandes, lentos y demandantes para ejecutarse en un dispositivo portátil. Es la misma brecha que la industria del software cruzó con los modelos de lenguaje — de los centros de datos a los teléfonos — mediante técnicas de compresión hoy maduras y bien documentadas. Sin embargo, nadie publicó su aplicación sistemática a los decodificadores brain-to-text de referencia, cuyos datos y código son públicos. Este trabajo produce ese estudio: reproduce el decodificador del benchmark internacional como línea base, aplica cuantización, poda y destilación en niveles crecientes, y mide en cada punto la precisión (WER contra el conjunto de evaluación oficial), la latencia de inferencia y el tamaño del modelo. El resultado — la frontera precisión-latencia-tamaño — es conocimiento accionable para toda la industria neurotecnológica: indica cuánta compresión tolera un decodificador clínico antes de degradarse, y con qué técnica conviene comprimirlo. El diseño es informativo en cualquier resultado: si los modelos toleran compresión agresiva, se demuestra la viabilidad del despliegue en dispositivo; si no la toleran, se identifica y localiza el cuello de botella — ambos hallazgos importan. El abordaje es íntegramente de Ingeniería de Software e ingeniería de IA: benchmarking riguroso, optimización de modelos, análisis de rendimiento y publicación reproducible del código. No requiere hardware especializado ni datos propios: datasets públicos (Dryad), modelos públicos, y mediciones ejecutables en equipamiento estándar.

## Cómo se ve el trabajo, mes a mes

| Mes | Qué hacés | En criollo |
|---|---|---|
| 1 · E1 | Marco teórico (historia brain-to-text + técnicas de compresión de modelos) y dominio del pipeline público. | Leer, bajar el código, hacerlo andar. |
| 2 · E2 | Reproducir el baseline y medirlo completo: WER, milisegundos por oración, megabytes, memoria. | La línea de largada: los números del modelo original. |
| 3 · E3 | Aplicar las técnicas en niveles crecientes (cuantización 16→8→4 bits, poda 25/50/75%, destilación a un modelo menor). Medir todo en cada paso. | Achicar y medir, achicar y medir. Cada corrida, una fila de la tabla. |
| 4 · E4 | Armar la frontera precisión-latencia-tamaño, análisis de dónde y por qué se rompe, redacción, código público. | Contar qué encontraste. |

**Stack**: Python · PyTorch (cuantización/poda/destilación nativas) · dataset Dryad + pipeline del benchmark · GPU moderada (Colab Pro) · mediciones de latencia en CPU/GPU estándar.

## Viabilidad de cómputo (objeción anticipada: "no tengo capacidad de cómputo")

**No hay simulaciones**: las mediciones son directas (correr el modelo, cronometrar, contar aciertos).

| Parte | ¿GPU potente? | Dónde |
|---|---|---|
| Latencia y tamaño | NO — medir en CPU de notebook ES el experimento (escenario de dispositivo) | Máquina propia |
| Cuantización post-entrenamiento | NO — minutos, sin reentrenar | Máquina propia / gratis |
| Entrenar el baseline (una vez) | Sí, horas acotadas | Kaggle (30 hs GPU gratis/semana) o Colab Pro (~USD 12/mes) |
| Poda + ajuste fino | GPU moderada | Kaggle / Colab Pro |
| Destilación | La más cara | Solo si el presupuesto alcanza |

**Escalera de alcance declarada en el diseño metodológico**:
- **Plan A (núcleo garantizado, recursos gratuitos)**: baseline + cuantización en niveles + todas las mediciones → la tesis ya existe.
- **Plan B**: + poda con ajuste fino.
- **Plan C**: + destilación; si no entra, trabajo futuro declarado.

Mitigaciones extra: empezar por el dataset de **handwriting** (más liviano que speech) y escalar; ⚠️ **verificar en el Mes 1 si el repo del benchmark publica los pesos pre-entrenados del baseline** — si están, cae el paso más caro.

**Respuesta modelo al tutor**: "El diseño está pensado para mis recursos: la latencia se mide en CPU estándar — que es el escenario de dispositivo que estudio, no una concesión. La técnica principal no requiere reentrenar. Lo único costoso es entrenar el baseline una vez, y entra en las horas gratuitas de Kaggle o en Colab Pro. El alcance está escalonado y declarado: el núcleo es ejecutable con recursos gratuitos."

## Ampliación

- Contexto del campo: [[../../20-Investigacion/Decodificacion-Brain-to-Text|Decodificacion-Brain-to-Text]]
- Evidencia de demanda laboral: búsquedas de Neuralink piden "quantization effects, numerical precision trade-offs, real-time ML products, constraints on power/latency/throughput" — y aclaran "no prior knowledge of neuroscience required".
- Pariente: [[Tema-16-Compresion-N1|tema 16]] comprimía los DATOS crudos (descartado); este comprime el MODELO — mismo espíritu de eficiencia, pero dentro del stack de ML del autor.
