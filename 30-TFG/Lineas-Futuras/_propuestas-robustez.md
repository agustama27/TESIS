# Propuestas de manuscrito · Líneas 4 y 5 (EEGNet endurecida e híbrido con vigía)

> 2026-09-27 · Sesión autónoma. Texto **propuesto** para Módulo 3/4 si estas variantes entran a la tesis; no se editó nada en `30-TFG/Entregas/`. Registro imitado de `Entregas/Modulo-2/src/contenido.js` (impersonal, "se", oraciones largas, cita APA en línea). Números de [[Linea-4-Endurecer-EEGNet]] y [[Linea-5-Hibrido-Vigia]]; citas verificadas en [[_research-robustez]]. Los números de tabla/figura son provisionales (siguen a la Tabla 4 y la Figura 3 de E2).

## 1. Introducción (antecedentes)

Párrafo nuevo, después del que presenta EEGNet como segundo decodificador:

> Los decodificadores basados en redes neuronales requieren una entrada de tamaño fijo, de modo que un pipeline en línea que pierde muestras debe decidir qué valor ocupa su lugar. En aprendizaje profundo, la estrategia habitual para volver un modelo tolerante a porciones faltantes de la entrada es el aumento de datos por enmascarado: borrar durante el entrenamiento regiones contiguas de la entrada, como el *Cutout* en imágenes (DeVries y Taylor, 2017) o el enmascarado temporal de SpecAugment en reconocimiento del habla (Park et al., 2019). Para electroencefalografía, el aumento de datos cuenta con revisiones (Lashgari et al., 2020) y con comparaciones sistemáticas de transformaciones sobre conjuntos públicos (Rommel et al., 2022), orientadas a mejorar la generalización con pocos ensayos más que a tolerar fallas del transporte. Una alternativa es informar explícitamente a la red dónde falta la señal mediante un indicador de faltante que acompaña a la serie, como en los modelos recurrentes para series multivariadas con valores ausentes (Che et al., 2018). Ninguno de estos trabajos evalúa la estrategia frente a los huecos que produce un enlace de transporte en tiempo real, que es lo que permite el banco de este trabajo.

Referencias a agregar (APA 7, verificadas en Crossref/arXiv): Che et al. (2018); DeVries y Taylor (2017); Lashgari et al. (2020); Park et al. (2019); Rommel et al. (2022). Lawhern et al. (2018) ya está. Texto completo de las referencias en [[_research-robustez]] §3.

## 2. Métodos

### 2.1 Instrumentos (agregar al final del párrafo del segundo decodificador)

> Para indagar el origen de la sensibilidad de EEGNet a los huecos se evaluaron, sobre los mismos segmentos, variantes del segundo decodificador que difieren en un solo aspecto: dos formas alternativas de completar las muestras faltantes antes del filtrado (interpolación lineal por canal y retención de la última muestra); una red entrenada con aumento por huecos, en la que en cada época cada ensayo de entrenamiento pierde, con probabilidad 0,5, un tramo contiguo de entre 0,4 y 1,6 s en una posición al azar de la ventana, borrado sobre la señal cruda antes del filtro para reproducir exactamente lo que ocurre en línea; una versión con tramos de hasta 2,6 s; y una red con un canal adicional que indica, muestra a muestra, si la señal falta. Todas se entrenaron con la misma sesión, el mismo número de épocas, la misma semilla y la misma arquitectura que la red original. Se evaluó además un decodificador híbrido que, en el momento de la decisión, examina las marcas de tiempo de las muestras recibidas en la ventana del ensayo y usa EEGNet si ningún intervalo entre muestras supera 40 ms (un bloque de transporte) y CSP con LDA en caso contrario.

### 2.2 Análisis de datos (agregar después del párrafo de pruebas)

> Cada variante se analizó con el mismo procedimiento que los decodificadores principales, contra su propia condición de referencia. Las variantes se compararon además entre sí, sujeto por sujeto, mediante la diferencia apareada con el decodificador original y la prueba de Wilcoxon, que se informa sin corrección por tratarse de un análisis exploratorio. Para separar el efecto del largo del hueco del de su posición, se borró un tramo de 1,52 s al inicio, al medio o al final de la ventana en los ensayos limpios de la sesión de evaluación. Antes de comparar, se verificó que la cadena de evaluación reprodujera ensayo por ensayo las decisiones originales de EEGNet.

## 3. Resultados

**Tabla 5 (nueva).** *Balanced accuracy de las variantes del segundo decodificador y del decodificador híbrido en las condiciones con hueco dentro de la ventana del ensayo.* Filas: referencia, pérdida contigua 10/25/40 %, desconexión en el ensayo 0,5/1/2 s. Columnas: CSP+LDA en línea, EEGNet, EEGNet con relleno por interpolación, EEGNet con aumento por huecos, EEGNet con canal de máscara, híbrido. Celda: mediana entre sujetos (p corregido). Fuente: `results/robustez/tabla_variantes.md` (recortar a esas columnas).

**Figura 4 (nueva, opcional).** *Balanced accuracy según la posición de un hueco de 1,52 s en la ventana del ensayo.* Cuatro posiciones (sin hueco, inicio, medio, final) × CSP+LDA, EEGNet, EEGNet con aumento. Fuente: `results/robustez/sonda_posicion.csv`.

Oraciones propuestas:

> Completar las muestras faltantes por interpolación o por retención del último valor no modificó el desempeño de EEGNet: después del filtro de 8 a 30 Hz, la señal dentro del hueco resultó prácticamente nula con los tres rellenos (su valor cuadrático medio fue el 0,1 % del de la señal presente). El entrenamiento con aumento por huecos eliminó la caída ante la pérdida contigua del 40 % (0,708 frente a una referencia de 0,833, p corregido = 0,328; mejoró en ocho de los nueve sujetos respecto de la red original) sin reducir el desempeño sin fallo, pero no la caída ante la desconexión dentro del ensayo, que se mantuvo en 0,583, 0,583 y 0,542 para cortes de 0,5, 1 y 2 s (p corregido = 0,012 en los tres casos), aun con tramos de entrenamiento de hasta 2,6 s. La red con canal de máscara llevó los cortes de 0,5 y 1 s a 0,667 (p corregido = 0,094), pero no el de 2 s (0,583, p corregido = 0,023) (Tabla 5).

> La posición del hueco explicó la diferencia entre ambas familias de fallas: con los ensayos limpios de la sesión de evaluación, borrar 1,52 s en el medio de la ventana no cambió el desempeño de EEGNet (0,750), mientras que borrarlos al inicio lo redujo a 0,604; CSP con LDA pasó de 0,722 a 0,715 con el hueco al inicio (Figura 4). En la campaña, la desconexión dentro del ensayo cae siempre al inicio de la ventana y la pérdida contigua en una posición al azar.

> El decodificador híbrido no envió ningún ensayo a CSP con LDA en la referencia, el *jitter*, el retraso ni la pérdida aleatoria de muestras, envió entre el 6 y el 8 % de los ensayos en la desconexión uniforme (los que el corte alcanzó dentro de la ventana) y todos los ensayos de las dos familias estructuradas. Conservó así la *balanced accuracy* de EEGNet en la referencia (0,750) y obtuvo 0,667 en los tres cortes dentro del ensayo, frente a 0,583, 0,583 y 0,500 de EEGNet; con el corte de 2 s mejoró respecto de EEGNet en ocho de los nueve sujetos (p = 0,008, sin corregir).

## 4. Discusión · Recomendaciones y líneas futuras (un párrafo)

> Los resultados de las variantes indican que la fragilidad de EEGNet ante la desconexión dentro del ensayo no se debe principalmente a que la red recibe ceros que no vio al entrenar, sino a que el corte elimina el tramo inicial de la ventana, en el que la red concentra la información que usa para decidir, mientras que CSP con LDA la reparte en toda la ventana. Enseñarle a la red a tolerar huecos resolvió la pérdida contigua en posición aleatoria y no la desconexión, y rellenar de otra forma no tuvo efecto porque el filtro anula cualquier relleno suave. Para un pipeline en línea, la mitigación que sí funcionó fue de arquitectura y no de modelo: un vigía que, con las marcas de tiempo que el pipeline ya tiene, decide en cada ensayo qué decodificador usar, lo que traslada a la acción el resultado de que el estado del flujo no alcanza por sí solo para saber si una decisión es confiable. Quedan como líneas futuras un aumento por huecos anclado al inicio de la ventana, la evaluación del híbrido en línea con la cadena de CSP con LDA sobre la señal compactada y la extensión del vigía como un detector de salud por ensayo dentro del objetivo de detección de la tesis.

## 5. Qué NO proponer

- No afirmar que el aumento **mejora** el desempeño sin fallo: la mediana sube (0,742 → 0,808) pero apareado por sujeto es neutro (3 mejoran, 3 empeoran).
- No presentar las comparaciones entre variantes como confirmatorias: n = 9, una semilla, sin corrección.
- No mencionar `gap200`/`complete` en el manuscrito salvo en una nota: `complete` es un antiejemplo (manda toda la pérdida aleatoria a CSP) y `gap200` no se distingue de `gap40` con estos datos.
