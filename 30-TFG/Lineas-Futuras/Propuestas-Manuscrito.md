# Propuestas de modificación al manuscrito (para integrar después del 28/09)

> 2026-09-27 · Sesión autónoma. Cada línea futura trae: qué agregar o cambiar en la **Introducción** (con citas verificadas en Crossref o página oficial; lo demás lleva ⚠️), qué cambia en **Métodos** (Tabla 1, instrumentos, diseño, análisis), qué **Resultados** nuevos habría que reportar, y un párrafo para **"Recomendaciones y líneas futuras"** de la Discusión. Redactado en el registro del manuscrito (`Modulo-2/src/contenido.js`), sin editar la entrega. Las referencias nuevas van al final en APA 7. Notas de respaldo: [[Linea-1-Segundo-Framework]], [[Linea-2-Trazas-Reales]], [[Linea-3-Intracortical]], [[Linea-4-Endurecer-EEGNet]], [[Linea-5-Hibrido-Vigia]].

Convención: la pregunta de investigación y la línea temática no cambian. Todo lo que sigue se declara como modificación del diseño metodológico "a la luz de los resultados de la campaña anterior", que es la frase que lo convierte en diseño secuencial y no en ajuste *post hoc*.

---

## 0. Cambio transversal que ya sale de los datos de E2: el costo de reconexión de LSL está cuantizado

Este punto no necesita campaña nueva: se verificó sobre `results/analysis/execs.csv` de la campaña definitiva.

**Resultados (párrafo nuevo, junto al hallazgo de los ≈ 570 ms).** "El exceso de tiempo sin datos por encima de la duración nominal del corte no fue proporcional al corte: las medianas del intervalo máximo entre llegadas fueron de 1.561, 1.560 y 3.598 ms para cortes de 0,5, 1 y 3 s, es decir, un exceso de 1.061, 560 y 598 ms respectivamente. El corte más breve pagó casi el doble que los otros dos."

**Discusión (interpretación, con la fuente del código).** "La lectura del código de liblsl (versión 1.18; Swartz Center for Computational Neuroscience, 2026) ofrece una explicación consistente con esas cifras, que el proyecto no documenta: al perderse la conexión TCP, el receptor con recuperación habilitada busca el flujo durante al menos un segundo en su primer intento, con una onda de descubrimiento cada 0,5 s (`MulticastMinRTT`), y luego espera 500 ms fijos antes de reconectar; el *watchdog* de 15 s no interviene en cortes breves. Un corte de 1 o 3 s termina alineado con la onda de búsqueda y paga solo la espera fija; uno de 0,5 s cae dentro del primer segundo de búsqueda y paga, además, lo que resta de él. El costo de reconexión, entonces, no es un tiempo proporcional al corte sino un valor cuantizado por el ciclo de búsqueda de LSL, con un piso cercano a un segundo para los cortes más breves. Ninguna *issue* del proyecto reporta una medición de ese tiempo; la cifra es, hasta donde se relevó, un aporte de este trabajo y la base de la contribución al ecosistema propuesta en las líneas futuras."

---

## 1. Línea 1 · Segundo marco de aplicación (BciPy)

### Introducción

Reemplazar, en el párrafo que enumera BciPy, MEDUSA, Timeflux, etc., la frase "Estos ocho artículos describen la arquitectura y las capacidades…" por una versión que anticipe la diferencia de política entre marcos, y agregar el párrafo siguiente después del relevamiento de repositorios:

"Los marcos difieren, además, en cómo administran la recepción de la señal. BciPy (Memmott et al., 2021) mantiene, en su capa de adquisición, un búfer circular acotado que se consulta por rango de marcas de tiempo y delega la recuperación de un flujo perdido en el propio LSL; MEDUSA (Santamaría-Vázquez et al., 2023) asigna un hilo de recepción por flujo con un plazo de espera explícito, del orden de 1,5 s para EEG a 250 Hz, y declara un error cuando ese plazo se supera repetidamente. Esas capas intermedias son parte del sistema que recibe una persona usuaria y podrían amortiguar o amplificar el efecto de un fallo del transporte; en el diseño de este trabajo se las excluye deliberadamente para atribuir el efecto al transporte, y su evaluación se contempla como validez externa."

(Nota sobre §0: verificado en el código de liblsl v1.18.0.b5 el 2026-09-27: `src/inlet_connection.cpp` línea 204, `resolve_oneshot(..., attempt == 0 ? 1.0 : 5.0)`; `src/data_receiver.cpp` línea 381, `connected_upd_.wait_for(lock, std::chrono::milliseconds(500), ...)`.)

(Nota: las afirmaciones sobre el búfer y los plazos provienen de la lectura del código publicado, `bcipy/acquisition/protocols/lsl/lsl_client.py` de BciPy 2.0.1 y `src/acquisition/lsl_utils.py` de medusa-platform, commit `23d4019a`; los artículos no las documentan con ese detalle. Citar el software además del artículo.)

### Métodos

- **Participantes / muestra.** Mantener la frase que justifica el pipeline propio y reescribir su cierre: "…una segunda implementación, que reemplaza el consumidor propio por la capa de adquisición y búfer de BciPy 2.0.1 (licencia BSD-3) sin modificar el reproductor, el inyector ni el decodificador, se evalúa como validez externa después de la campaña principal. MEDUSA se descartó para esa implementación porque su recepción de LSL reside en una aplicación de escritorio que requiere interfaz gráfica y cuenta en línea, y porque su licencia (CC BY-NC-ND) no permite publicar una versión derivada."
- **Instrumentos.** Agregar: "El consumidor alternativo resuelve los mismos dos flujos, crea los receptores como lo hace BciPy (búfer de 365 s en el receptor, recuperación habilitada), conserva la señal en el búfer circular del marco y obtiene cada ventana de decisión mediante la consulta por rango de marcas de tiempo del marco; produce las mismas salidas que el consumidor propio. Dos adaptaciones fueron necesarias y se documentan: la resolución del flujo por nombre en lugar de por tipo, porque el marco tomaría un flujo ajeno con ejecuciones simultáneas, y un sondeo periódico del búfer, porque el marco no tiene hilo de recepción propio."
- **Amenaza a la validez (declarar).** "BciPy 2.0.1 declara compatibilidad con Python 3.9 y 3.10; la capa de adquisición se instaló sobre Python 3.12 sin las versiones de dependencias que fija el paquete, verificando que importa y opera. Los resultados se refieren a esa capa, no al marco completo."
- **Diseño.** "La segunda campaña de validez externa reproduce el diseño completo (9 sujetos × 5 corridas × 19 condiciones) con el consumidor alternativo; la comparación es apareada entre consumidores por sujeto y condición."
- **Tabla 1.** Sin cambios.

### Resultados (qué reportar; cifras de la campaña en la VM, aún no corridas)

Tabla nueva "consumidor propio vs BciPy" por familia de desconexión y severidad: ensayos válidos, excepciones del marco (`AssertionError` de la consulta por rango), segundos sin datos e intervalo máximo entre llegadas, retardo de decisión, *balanced accuracy*; Wilcoxon apareado propio vs BciPy con Holm. Resultado esperable según la prueba en la notebook (una corrida, no inferencial): "en ausencia de fallo, ambos consumidores produjeron decisiones idénticas (11 de 11 ensayos, segmentos idénticos); con cortes de 1 s el marco toleró el corte sin error, y con cortes de 3 s la consulta por rango falló y el ensayo quedó inválido, donde el consumidor propio decodifica la porción recibida".

### Discusión · Recomendaciones y líneas futuras (párrafo)

"El reemplazo del consumidor propio por la capa de adquisición de BciPy mostró que el marco no altera el costo de reconexión, que pertenece a LSL, pero sí cambia la política ante la señal faltante: tolera en silencio los cortes que se recuperan dentro del plazo de decisión y convierte en inválidos los que no, allí donde el pipeline de referencia decodifica lo recibido. La política de MEDUSA, leída en su código, es la opuesta: un plazo de 1,5 s que absorbe sin aviso cortes como los medidos y un contador de plazos vencidos que no se reinicia y termina el hilo de recepción tras el sexto. Que dos marcos abiertos tomen decisiones tan distintas ante el mismo evento, y que ninguno las documente, sugiere que la política ante la señal faltante debería ser un parámetro explícito y medible de todo marco BCI."

---

## 2. Línea 2 · Trazas reales de enlaces

### Introducción

Agregar, tras el párrafo de Gemborn Nilsson et al. (2023) y Wilson et al. (2010), un párrafo que fundamente las severidades con mediciones de enlaces reales:

"Las mediciones publicadas de enlaces inalámbricos de EEG acotan qué es realista. Krigolson et al. (2017) midieron en el casco Muse, conectado por Bluetooth, un retraso medio de 40 ms con una dispersión de 20 ms; Dasenbrock et al. (2022) reportaron, para un equipo que transmite por Bluetooth a un teléfono y de allí a LSL, un *jitter* cercano a 3 ms, un retraso que varió hasta 52 ms entre sesiones y muestras aisladas con hasta 150 ms de demora; Arpaia et al. (2025) encontraron retrasos medios de entre 20 y 102 ms según el equipo, sin pérdida de paquetes en sus pruebas; y Epinat-Duclos et al. (2026), al comparar un casco Bluetooth con uno Wi-Fi y uno cableado, registraron dos sesiones con pérdida total de la conexión y una media de cuatro disparadores perdidos por sesión en el primero. Con interferencia de Wi-Fi, la tasa de paquetes perdidos de Bluetooth de baja energía fluctúa entre 2 y 9 % (Mahmud et al., 2023). Del lado de la red, Aguayo et al. (2004) mostraron que la pérdida en enlaces 802.11 es independiente solo por debajo de una décima de segundo y, en los enlaces malos, está correlacionada hasta un segundo o más; Jardosh et al. (2005) situaron la congestión por encima del 84 % de uso del canal; y Sui et al. (2016) caracterizaron la latencia de Wi-Fi como una distribución de cola larga, con un percentil 90 cercano a 20 ms y un percentil 99 cercano a 250 ms (⚠️ cifra tomada del resumen). Ninguna de esas fuentes publica la duración de las interrupciones ni una traza reutilizable de pérdida: los modelos de fallo de este trabajo se anclan a la escala del ensayo y no a un enlace concreto, y la reproducción de trazas medidas se plantea como extensión."

### Métodos

- **Tabla 1.** Agregar una tercera familia con una fila:

| Modelo | Dónde se aplica | Severidades | Qué mide | Situación real |
|---|---|---|---|---|
| Traza de enlace | Contenido, instante de entrega y transporte, según lo que la traza registre en cada intervalo de 0,1 s | La traza tal como se midió (factor 1); factores 2 y 4 como estrés declarado | Efecto de la forma temporal real de las fallas (ráfagas, cola de latencia, cortes con reconexión) | El enlace del que proviene la traza: Bluetooth de un casco Muse S; Wi-Fi congestionado (modelo parametrizado) |

Nota de la tabla, agregar: "La familia de trazas reproduce el estado medido de un enlace a razón de un segundo de traza por segundo de corrida, sin estirar el tiempo; si la traza es más breve que la corrida se repite de forma cíclica y el punto de entrada se elige con la semilla de la ejecución. El factor de escala multiplica retraso y pérdida; los cortes no se escalan."

- **Instrumentos.** Agregar: "El inyector admite un tercer modo, de traza, que lee un archivo con el estado de un enlace por intervalo (enlace operativo o caído, retraso adicional, fracción de muestras perdidas y dispersión del retraso) y lo aplica a cada bloque. Dos convertidores producen ese archivo: uno a partir del instante de llegada de cada muestra de una grabación real, ajustando un reloj nominal por mínimos cuadrados y tomando el residuo como retraso; otro a partir de un registro de `ping`. La traza de Bluetooth proviene de una grabación pública de un casco Muse S (Iwendi et al., 2026; 66,9 s; licencia CC BY 4.0); la traza de Wi-Fi congestionado es un modelo de dos estados de Gilbert-Elliott cuyos parámetros se tomaron de Mahmud et al. (2023), Aguayo et al. (2004) y Sui et al. (2016), y se declara como modelo y no como medición."
- **Diseño.** "Tercera campaña: 9 sujetos × 5 corridas × (referencia + trazas), comparación apareada contra la referencia de la misma corrida, como en las otras familias."

### Resultados (qué reportar)

Filas nuevas en las tablas de infraestructura y desempeño por traza: recibido, huecos, latencia media y máxima, segundos sin datos, *balanced accuracy* de ambos decodificadores. Validación del instrumento (ya medida en la notebook, una corrida): "la reproducción de la traza Bluetooth produjo una latencia media de 40,6 ms con una dispersión del intervalo entre llegadas de 12,6 ms, coincidente con los 40 ms medidos por Krigolson et al. (2017) para el mismo casco con otro método".

### Discusión · Recomendaciones y líneas futuras (párrafo)

"Las severidades de este trabajo se fijaron en la escala del ensayo y no en la de un enlace concreto. El modo de traza del inyector permite reemplazarlas por el comportamiento medido de un enlace real: la traza de un casco Muse por Bluetooth reprodujo en el banco la latencia que la literatura mide para ese casco, y el mismo mecanismo acepta una traza de Wi-Fi congestionado o de cualquier otro enlace del que se disponga de un registro de llegadas. Lo que falta no es el instrumento sino los datos: ninguna fuente relevada publica trazas de pérdida o de interrupciones de cascos EEG con licencia de reutilización, de modo que la medición propia de un enlace, con marcas de tiempo del dispositivo y de llegada, es el paso siguiente más barato y más valioso."

---

## 3. Línea 3 · Señal intracortical

### Introducción

Agregar, tras el párrafo que menciona BRAND y los datos intracorticales, una oración que deje planteada la pregunta de generalización:

"Las plataformas de lazo cerrado sobre implantes (Ali et al., 2024) transportan un contenido distinto: conteos de disparos neuronales por intervalos de 10 a 20 ms provenientes de 96 a 256 electrodos, decodificados por regresión de la cinemática con filtros lineales o de Kalman (Wu et al., 2006; Gilja et al., 2012). Existen conjuntos públicos de esas señales con licencia abierta y sin registro, como las sesiones de alcance continuo de O'Doherty et al. (2017) reempaquetadas en el Neural Latents Benchmark (Pei et al., 2021). Si la vulnerabilidad al transporte depende del tipo de señal y del decodificador es una pregunta que este trabajo no responde, pero cuyo instrumento deja preparado."

### Métodos

Solo si la PoC entra al Módulo 4 como extensión preliminar: agregar en **Instrumentos** un párrafo "Extensión preliminar a señal intracortical": "El banco es agnóstico al contenido del flujo (objetivo 6). Como evidencia de factibilidad, y sin pretensión inferencial, se cargó una sesión pública de alcance continuo en un macaco (O'Doherty et al., 2017; 96 electrodos en corteza motora primaria, 374 s), se binnearon los disparos en intervalos de 20 ms (50 Hz) y se entrenaron fuera de línea un filtro de Wiener y un filtro de Kalman (Wu et al., 2006) para decodificar la velocidad del cursor, evaluados con validación cruzada temporal de cinco pliegues y con R² y correlación de Pearson por eje. Las severidades de un eventual experimento se expresan en milisegundos, porque el enlace no sabe qué transporta, con su equivalencia en intervalos de 20 ms." Tabla 1: sin cambios (la extensión no se corre bajo fallos en el Módulo 4).

### Resultados (qué reportar)

Solo la tabla de la PoC, en un anexo o en Discusión como "extensión preliminar": "Sobre una sesión de 374 s, con validación cruzada temporal de cinco pliegues, el filtro de Wiener alcanzó R² de 0,449 y 0,585 (correlación 0,680 y 0,770) para las componentes x e y de la velocidad, y el filtro de Kalman 0,378 y 0,425 (0,636 y 0,672). Ante un 20 % de intervalos faltantes elegidos al azar, el R² medio del Wiener cayó 0,042 y el del Kalman, que ante una observación faltante solo predice, 0,027." (Ver [[Linea-3-Intracortical]] §5 por las salvedades.)

### Discusión · Recomendaciones y líneas futuras (párrafo)

"La extensión a señal intracortical es la que más cambia el banco y la que más lo pone a prueba: el flujo pasa de voltaje continuo a conteos de disparos, la tarea de clasificación a regresión continua y la métrica de exactitud a R², mientras el transporte y el inyector permanecen iguales. Un decodificador con estado, como el filtro de Kalman, puede predecir sin corregir ante una observación faltante, de modo que la comparación entre señales confunde el tipo de señal con la arquitectura del decodificador y exige un control sin estado. Esa confusión es la misma que apareció en este trabajo entre CSP, que promedia las muestras presentes, y una red convolucional que recibe ceros donde falta señal. El estudio completo (varias sesiones y sujetos, señal humana y de primate, lazo cerrado simulado) excede este trabajo; la prueba de concepto de carga y decodificación fuera de línea deja el cargador y el decodificador de referencia listos."

---

## 4 y 5. Líneas 4 y 5 · EEGNet endurecida e híbrido con vigía

Respaldo: [[Linea-4-Endurecer-EEGNet]], [[Linea-5-Hibrido-Vigia]], `_research-robustez.md` (seis referencias verificadas en Crossref/arXiv).
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

---

## Referencias nuevas (APA 7; verificadas en Crossref/DataCite salvo ⚠️)

Aguayo, D., Bicket, J., Biswas, S., Judd, G., y Morris, R. (2004). Link-level measurements from an 802.11b mesh network. *ACM SIGCOMM Computer Communication Review, 34*(4), 121-132. https://doi.org/10.1145/1030194.1015482

Arpaia, P., Esposito, A., Galdieri, F., y Natalizio, A. (2025). Acquisition delay of wireless EEG instruments in time-sensitive applications. *IEEE Transactions on Neural Systems and Rehabilitation Engineering, 33*, 2151-2159. https://doi.org/10.1109/TNSRE.2025.3575695

Dasenbrock, S., Blum, S., Maanen, P., Debener, S., Hohmann, V., y Kayser, H. (2022). Synchronization of ear-EEG and audio streams in a portable research hearing device. *Frontiers in Neuroscience, 16*, 904003. https://doi.org/10.3389/fnins.2022.904003

Epinat-Duclos, J., Rossignon, A., Prado, J., Van der Henst, J., Paulignan, Y., Beaudoin-Gobert, M., Lecaignard, F., y Bedoin, N. (2026). Evaluating portable EEG: A comparison between two wireless systems (EPOC Flex and LiveAmp) and the wired BrainAmp system. *PeerJ, 14*, e20416. https://doi.org/10.7717/peerj.20416

Gilja, V., Nuyujukian, P., Chestek, C. A., Cunningham, J. P., Yu, B. M., Fan, J. M., Churchland, M. M., Kaufman, M. T., Kao, J. C., Ryu, S. I., y Shenoy, K. V. (2012). A high-performance neural prosthesis enabled by control algorithm design. *Nature Neuroscience, 15*(12), 1752-1757. https://doi.org/10.1038/nn.3265

Iwendi, C., NWibo, E., y Uwah, S. E. (2026). *EEG and motion signals pilot dataset* [Conjunto de datos]. Zenodo. https://doi.org/10.5281/zenodo.22093536

Jardosh, A., Ramachandran, K., Almeroth, K., y Belding-Royer, E. (2005). Understanding congestion in IEEE 802.11b wireless networks. En *Proceedings of the 5th ACM SIGCOMM Conference on Internet Measurement (IMC '05)*. ACM. https://doi.org/10.1145/1330107.1330140

Krigolson, O. E., Williams, C. C., Norton, A., Hassall, C. D., y Colino, F. L. (2017). Choosing MUSE: Validation of a low-cost, portable EEG system for ERP research. *Frontiers in Neuroscience, 11*, 109. https://doi.org/10.3389/fnins.2017.00109

Mahmud, S. A., Kasera, S., Ji, M., y Agarwal, V. (2023). *Experimental evaluation of interference in 2.4 GHz wireless network* (Informe INL/RPT-23-74719). Idaho National Laboratory; Office of Scientific and Technical Information. https://doi.org/10.2172/2242485

O'Doherty, J. E., Cardoso, M. M. B., Makin, J. G., y Sabes, P. N. (2017). *Nonhuman primate reaching with multichannel sensorimotor cortex electrophysiology* [Conjunto de datos]. Zenodo. https://doi.org/10.5281/zenodo.583331

Pei, F., Ye, J., Zoltowski, D., Wu, A., Chowdhury, R. H., Sohn, H., O'Doherty, J. E., Shenoy, K. V., Kaufman, M. T., Churchland, M., Jazayeri, M., Miller, L. E., Pillow, J., Park, I. M., Dyer, E. L., y Pandarinath, C. (2021). Neural Latents Benchmark '21: Evaluating latent variable models of neural population activity. En *Proceedings of the Neural Information Processing Systems Track on Datasets and Benchmarks*. https://doi.org/10.48550/arXiv.2109.04463 ⚠️ lista de autores completa SIN VERIFICAR contra la publicación (el informe verificó el arXiv).

Sui, K., Zhou, M., Liu, D., Ma, M., Pei, D., Zhao, Y., Li, Z., y Moscibroda, T. (2016). Characterizing and improving WiFi latency in large-scale operational networks. En *Proceedings of the 14th Annual International Conference on Mobile Systems, Applications, and Services (MobiSys '16)* (pp. 347-360). ACM. https://doi.org/10.1145/2906388.2906393 (⚠️ cifras tomadas del resumen; texto completo no accedido)

Swartz Center for Computational Neuroscience. (2026). *liblsl* (versión 1.18.0.b5) [Software]. GitHub. https://github.com/sccn/liblsl

Wu, W., Gao, Y., Bienenstock, E., Donoghue, J. P., y Black, M. J. (2006). Bayesian population decoding of motor cortical activity using a Kalman filter. *Neural Computation, 18*(1), 80-118. https://doi.org/10.1162/089976606774841585

Che, Z., Purushotham, S., Cho, K., Sontag, D., y Liu, Y. (2018). Recurrent neural networks for multivariate time series with missing values. *Scientific Reports, 8*(1), 6085. https://doi.org/10.1038/s41598-018-24271-9
DeVries, T., y Taylor, G. W. (2017). *Improved regularization of convolutional neural networks with Cutout* (arXiv:1708.04552). arXiv. https://arxiv.org/abs/1708.04552
Lashgari, E., Liang, D., y Maoz, U. (2020). Data augmentation for deep-learning-based electroencephalography. *Journal of Neuroscience Methods, 346*, 108885. https://doi.org/10.1016/j.jneumeth.2020.108885
Park, D. S., Chan, W., Zhang, Y., Chiu, C.-C., Zoph, B., Cubuk, E. D., y Le, Q. V. (2019). SpecAugment: A simple data augmentation method for automatic speech recognition. En *Proceedings of Interspeech 2019* (pp. 2613-2617). https://doi.org/10.21437/Interspeech.2019-2680
Rommel, C., Paillard, J., Moreau, T., y Gramfort, A. (2022). Data augmentation for learning predictive models on EEG: A systematic comparison. *Journal of Neural Engineering, 19*(6), 066020. https://doi.org/10.1088/1741-2552/aca220

Ya en Referencias del E2 (no repetir): Ali et al. (2024); Gemborn Nilsson et al. (2023); Lawhern et al. (2018); Memmott et al. (2021); Santamaría-Vázquez et al. (2023); Wilson et al. (2010).
