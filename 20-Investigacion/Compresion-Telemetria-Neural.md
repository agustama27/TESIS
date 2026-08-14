# Compresión de telemetría neural (tema 16) — bajado a tierra

> Nota de investigación · 2026-08-14 · profundización del tema 16 de [[Temas-Candidatos-TFG]]
> Estilo llano, como [[Tu-Tesis-Explicada-Simple]]. Para la historia del problema ver la ficha 16 del deck.

---

## El problema en tres frases

1. El implante de Neuralink tiene 1.024 sensores que generan **muchísimos datos** (~200 megabits por segundo) pero la radio que tiene para mandarlos afuera del cráneo solo transmite ~1 megabit por segundo. **Generan 200 veces más de lo que pueden enviar.**
2. Neuralink publicó **una hora de datos reales de su implante** y le pidió al mundo: comprímanlos 200 veces **sin perder ni un bit**, en menos de 1 milisegundo y gastando casi nada de batería. Nadie lo logró — el compresor común (zip) apenas logra 2,2 veces.
3. Tu tesis: **estudiar sistemáticamente hasta dónde se puede llegar y por qué** — probando técnicas de compresión de menor a mayor sofisticación y midiendo cada una.

## La analogía

Comprimir sin pérdida es lo que hace **ZIP**: achicás el archivo y al descomprimirlo recuperás EXACTAMENTE el original, bit por bit. Funciona encontrando repeticiones y patrones.

El problema: la señal del cerebro se parece mucho al **ruido** — y el ruido casi no tiene patrones que explotar. Es como intentar comprimir el video de una TV sin señal: no hay redundancia de la que agarrarse. La pregunta científica de tu tesis es: **¿cuánta redundancia REAL hay en la señal neural, y qué técnica la aprovecha mejor?**

## Cómo se ve el trabajo en tu pantalla, semana a semana

**Semana 1-2 — Conocer los datos.**
Bajás un zip de 143 MB del sitio de Neuralink. Adentro hay... **archivos WAV — archivos de audio comunes**. Los abrís con Python (`scipy.io.wavfile`) y tenés un array de números enteros: 20.000 muestras por segundo por canal. Los podés graficar. Los podés literalmente **ESCUCHAR** (son audio: el crepitar de las neuronas). No hay formato exótico: es el tipo de dato más estándar que existe.

**Semana 3-4 — El banco de pruebas.**
Escribís UN script que es el corazón de toda la tesis: recibe un compresor, lo corre sobre los archivos, y devuelve tres números — **ratio de compresión** (tamaño antes / tamaño después), **velocidad** (muestras por segundo), y **verificación lossless** (descomprimir == original, un simple assert de igualdad). Después corrés los métodos existentes: zip, zstd, FLAC (el compresor de audio sin pérdida). Eso te da la **tabla baseline** — y de paso verificás el 2,2x que reporta Neuralink. Ya estás reproduciendo resultados.

**Mes 2-3 — Tu experimento: construir por capas.**
Cada técnica es un escalón de sofisticación, y cada una te da una fila más en la tabla:

| Corrida | Técnica (en criollo) | Ratio esperado |
|---|---|---|
| A | zip / zstd tal cual | ~2,2x |
| B | FLAC (compresor de audio) | ¿? |
| C | **Deltas**: guardar la DIFERENCIA entre muestras consecutivas (los cambios son más chicos que los valores) | ¿? |
| D | **Predicción lineal**: predecir la próxima muestra a partir de las anteriores y guardar solo el ERROR de predicción | ¿? |
| E | **Entre canales**: ¿los sensores vecinos ven señales parecidas? Explotar esa correlación | ¿? |
| F | **Codificación entrópica** (Huffman/rANS): darle códigos cortos a los valores frecuentes — hay librerías, no lo inventás vos | ¿? |
| G | Combinaciones de las anteriores | ¿? |

Y el análisis estrella, que es pura teoría de la información aplicada: **estimar la entropía de la señal** — o sea, calcular el LÍMITE TEÓRICO de compresión sin pérdida. Si ese límite da (por ejemplo) 5x, acabás de demostrar rigurosamente **por qué el 200x lossless es imposible** y que la industria necesita otro camino (compresión con pérdida controlada, extracción de eventos). Un resultado "negativo" así, bien argumentado, es un aporte científico real.

**Mes 4 — Contarlo.**
La tabla final ratio-vs-velocidad, el análisis del límite teórico, la discusión, el documento con formato de la universidad, el código en GitHub.

## Validación y población estadística (la pregunta del tutor)

Acá este tema BRILLA — es el más fácil de validar de los 18:

- **¿Mejoró?** El ratio de compresión es un número objetivo: tamaño antes dividido tamaño después. No hay interpretación posible.
- **¿Es sin pérdida?** Descomprimís y comparás bit a bit contra el original. Un assert. Verde o rojo.
- **¿Población estadística?** Los archivos/canales del dataset (1 hora de señal, múltiples canales): cada canal-segmento es una observación. Reportás promedio y variación del ratio entre canales, y comparás técnicas con test pareado sobre los mismos segmentos. Mismo esquema que ya entendés del tema 17.
- **¿Velocidad?** Muestras procesadas por segundo, medida en tu máquina, con la salvedad declarada de que el hardware del implante es distinto (analizás complejidad, no watts).

## Viabilidad honesta

**A favor — y es mucho:**
- **Dataset chiquito**: 143 MB. Entra en cualquier laptop.
- **CERO GPU, cero hardware, cero aduana.** El tema más barato de los 18 en recursos.
- **Feedback en segundos**: corrés y ves el ratio al instante. Nada de esperar horas de entrenamiento. Para un constructor, el loop más satisfactorio.
- **Verificación trivial y objetiva** (el assert bit a bit).
- Podés prototipar TODO en Python con NumPy; la velocidad se analiza por complejidad y, si querés lucirte, implementás la mejor técnica en C/Rust al final — opcional, no requisito.
- Hay comunidad y soluciones publicadas (el repo n1-codec y foros de compresión) para contrastar tus números.

**En contra — que lo sepas antes de elegir:**
- Es investigación **algorítmica**: tu día es matemática ligera + código + medir. No hay interfaz, no hay demo visual, no hay "app que se ve andando". Si eso te apaga, no es tu tema.
- Hay que estudiar **teoría de la información básica** (entropía, predicción, codificación) — es aprendible en semanas y yo te la enseño, pero es un mundo nuevo si nunca la tocaste.
- La trampa retórica: NO prometas "voy a lograr el 200x". La tesis es **caracterizar la frontera** — hasta dónde se llega y por qué no más. Eso hay que dejarlo clarísimo con el tutor desde el día uno.

## El guion para el tutor (dos minutos)

> "Profe, Neuralink tiene un problema de ingeniería sin resolver y lo hizo público: su implante genera 200 veces más datos de los que su radio puede transmitir. Publicaron una hora de datos reales del implante y desafiaron al mundo a comprimirlos sin pérdida 200 veces. Nadie pudo — el compresor estándar logra 2,2.
>
> Mi tesis toma ese dataset público y estudia sistemáticamente hasta dónde se puede llegar: armo un banco de pruebas, corro los compresores existentes como línea base, y construyo técnicas por capas — deltas, predicción lineal, correlación entre canales, codificación entrópica — midiendo ratio y velocidad de cada una. Además estimo el límite teórico de la señal, que probablemente demuestre por qué la meta de 200x sin pérdida es inalcanzable y qué camino le queda a la industria.
>
> La validación es la más objetiva posible: el ratio es tamaño antes sobre tamaño después, y 'sin pérdida' se verifica comparando bit a bit. No necesito GPU, ni hardware, ni datos propios: el dataset pesa 143 megas y corre en mi notebook. Es un Trabajo de Investigación en Transformación Digital, y es ingeniería de software en estado puro: algoritmos, optimización y medición rigurosa — sobre los datos del implante más famoso del mundo."

## Comparación rápida con el 17 (para tu decisión)

| | Tema 16 (compresión) | Tema 17 (brain-to-text) |
|---|---|---|
| Tu día típico | Escribir algoritmos, medir en segundos | Entrenar modelos, esperar horas, medir |
| Requiere GPU | No | Sí (Colab Pro) |
| Mundo nuevo a estudiar | Teoría de la información | Datos intracorticales + secuencias |
| Encaje con tu stack actual (AI/ML) | Menor | Mayor |
| Distintivo del CV | "Datos reales del implante N1" | "El problema exacto del equipo de decodificación" |
| Demo para la defensa | Tabla + "escuchen neuronas" 🔊 | Tabla + texto decodificado de un paciente real |
| Riesgo principal | Que la teoría de la información no te guste | Que el cómputo/curva de datos te coma tiempo |

## Referencias y recursos (verificados 2026-08-12/14)

- Neuralink Compression Challenge — datos y especificaciones: https://content.neuralink.com/compression-challenge/data.zip (143 MB, WAVs de 1 h, corteza motora)
- Especificaciones del reto: 1.024 electrodos @ 20 kHz, 10 bits → ~200 Mbps; radio ~1 Mbps; requisitos <1 ms y <10 mW; zip ≈ 2,2x.
- n1-codec — solución comunitaria de referencia: https://github.com/mikaelhaji/n1-codec
- Cobertura técnica: CBC News (2024) y discusión en foros de compresión (encode.su, Hacker News).
- ⚠️ SIN VERIFICAR: papers académicos de compresión de señal neural (buscar "neural signal lossless compression" antes de la presentación formal — trabajo para bci-explorer).

## Enlaces

[[Temas-Candidatos-TFG]] · [[Tu-Tesis-Explicada-Simple]] · [[Decodificacion-Brain-to-Text]] · conceptos: [[Entropia]], [[Codificacion-entropica]], [[Prediccion-lineal]]
