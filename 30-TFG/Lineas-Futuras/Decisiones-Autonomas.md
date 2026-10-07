# Decisiones autónomas — sesión de líneas futuras (2026-09-27)

> Registro de cada decisión tomada sin el autor durante la sesión autónoma del 27/09 (líneas futuras del Módulo 3/4: segundo framework, trazas reales, señal intracortical). Formato: qué se decidió, por qué, alternativa descartada. Las decisiones importantes también están en engram (`tfg/lineas-futuras/*`).

## DA-01 · Rama base con instantánea del código v2 del prototipo local

- **Qué**: en el clon aparte (`C:\Users\agustin.tamagusuku\Desktop\bci-fault-bench-futuro`) se creó la rama `feat/base-v2-snapshot` con una copia exacta de `40-Prototipo/src/bcibench/` y `scripts/` (estado v2: fallos estructurados, `segments.npz`, EEGNet). Todas las ramas `feat/<linea>` nacen de ahí.
- **Por qué**: `main` del repositorio público está en v1.0 (234 ejecuciones) y la otra sesión va a publicar v2.0 el lunes. El consumidor alternativo debe producir `segments.npz` (formato v2) y el ejecutor v2 tiene `--family`; construir sobre v1.0 habría dejado el trabajo incompatible con lo que se entrega.
- **Alternativa descartada**: trabajar sobre `main` v1.0 y portar después. Descartada porque duplica trabajo y porque la contraparte del consumidor (segmentos por ensayo) ya existe en v2.
- **Consecuencia para el autor**: cuando v2.0 esté en `main`, cada rama se reubica con `git rebase --onto main feat/base-v2-snapshot feat/<linea>`. Si el snapshot coincide con lo publicado, el rebase es limpio (git omite el commit ya aplicado).

## DA-02 · Entornos virtuales

- **Qué**: `.venv` en el clon con los mismos `requirements.txt` del prototipo (para reproductor, ejecutor y análisis); el framework elegido se instala en un venv separado (`.venv-<framework>`) para no contaminar las dependencias del banco.
- **Por qué**: regla del autor (venv aparte para el framework) y para aislar conflictos de versiones (frameworks BCI suelen fijar numpy/scipy viejos).
- **Alternativa descartada**: reutilizar `40-Prototipo/.venv`. Descartada por la regla de no tocar `40-Prototipo/` y porque instalar ahí un framework la modificaría.

## DA-03 · Los decodificadores se copian, no se reentrenan

- **Qué**: `results/models/decoder_s0X.pkl` (CSP+LDA congelados de la campaña) copiados desde `40-Prototipo/results/models/` al clon (carpeta ignorada por git).
- **Por qué**: el consumidor alternativo debe reproducir las MISMAS decisiones que el nuestro; reentrenar introduciría una fuente de diferencia ajena a la pregunta (el framework).
- **Alternativa descartada**: reentrenar con `poc1_offline.py` (mismo resultado en teoría, pero cualquier diferencia de versión de MNE cambiaría los filtros CSP).

## DA-04 · Formato y anclaje del modo `trace` (línea 2)

- **Qué**: una traza es una línea de tiempo del estado del enlace en intervalos (`t_s, up, delay_ms, loss[, jitter_ms]`, CSV con cabecera de procedencia y licencia). Se reproduce 1:1 en el tiempo, cíclica si es más corta que la corrida, con punto de entrada al azar desde la semilla (o fijo con `@offset`). La "severidad" es un factor de escala sobre retraso y pérdida (1 = tal como se midió); los cortes no se escalan. Cada traza se analiza como un tipo de fallo propio (`trace:<nombre>`) comparado contra la referencia del mismo sujeto y corrida.
- **Por qué**: (a) un formato único permite convertir fuentes heterogéneas (huecos de marcas de tiempo de una grabación Bluetooth, registros de ping sobre Wi-Fi); (b) no estirar el tiempo respeta la física del enlace, que es justamente lo que se quiere reproducir; (c) el punto de entrada aleatorio evita que todas las corridas vean el mismo tramo, y queda registrado en `producer.json` para repetirlo.
- **Alternativa descartada**: reescalar la traza a la duración de la corrida (cambia la duración de cortes y ráfagas: inventa una realidad), o parametrizar la traza en severidades discretas (pierde la estructura temporal, que es el punto de la línea).
- **Alternativa descartada**: reproducir trazas a nivel de paquete de red (netem/tc en Linux). Es más fiel, pero saca el fallo de la interfaz de transporte del banco (donde actúan las otras dos familias) y no corre en Windows; queda anotado como extensión.

## DA-06 · La traza del Muse S se convierte a retraso y jitter por intervalo, no a calendario de paquetes

- **Qué**: la grabación real (Mind Monitor, CC BY 4.0) trae solo el instante de llegada de cada muestra. Se ajusta un reloj nominal lineal (256,04 Hz), el residuo llegada − nominal referido a su percentil 1 es el retraso, y por intervalo de 0,1 s se guardan media y desvío. Pérdida = 0 y sin cortes porque no son observables en esa fuente (declarado en la cabecera).
- **Por qué**: reutiliza el mecanismo existente del inyector (retraso + jitter por bloque) y reproduce la distribución temporal medida; el resultado (40,6 ms de latencia media) coincide con la medición independiente de Krigolson et al. (2017) para el mismo casco, lo que valida la conversión.
- **Alternativa descartada (por ahora)**: modo "calendario" que libera bloques según los instantes de llegada de la traza (reproduce el agrupamiento en paquetes de 12). Más fiel, pero requiere un mecanismo nuevo en el reproductor; queda listado como pendiente de 0,5 día.

## DA-07 · Modelo de Gilbert-Elliott parametrizado como sustituto declarado, no como traza

- **Qué**: se generó `ge-wifi-ble.csv` con un modelo de dos estados cuyos parámetros salen de fuentes verificadas (PER 2-9 %, correlación ≈ 1 s, latencia p50/p99 = 5/250 ms). La cabecera dice en mayúsculas que NO es una medición.
- **Por qué**: no existe una traza de pérdida descargable con licencia (CRAWDAD exige cuenta; ningún artículo publica *dropouts* en ms) y la campaña necesita al menos una condición con pérdida correlacionada para contrastar con la pérdida i.i.d. de E2. El modelo es la práctica estándar en simulación de enlaces cuando no hay traza.
- **Alternativa descartada**: no ofrecer nada para pérdida (deja la línea sin condición de pérdida) o inventar una traza sin fuente. **Requiere decisión del autor**: usarla en la campaña o reemplazarla por una medición propia (ver "Lo que falta" en [[Linea-2-Trazas-Reales]]).

## DA-08 · La señal intracortical va en un repositorio público aparte

- **Qué**: `agustama27/bci-fault-bench-intracortical` (nuevo), no una rama del banco EEG.
- **Por qué**: cambia el contenido del flujo (conteos de disparos a 50 Hz, 96 canales, sesión continua sin ensayos), el decodificador (regresión de velocidad con Kalman/Wiener en lugar de clasificación CSP+LDA) y las métricas (R², correlación); compartir el repositorio obligaría a ramificar `data.py`, `decoder.py`, `metrics.py` y `analyze.py` a la vez. El transporte (reproductor LSL + inyector) sí se reutiliza y se importará como dependencia cuando se llegue a la PoC 2.
- **Alternativa descartada**: subpaquete `bcibench.intracortical` en el mismo repositorio. Menos duplicación, pero mezcla en `main` una línea que el autor todavía tiene que decidir si entra en el Módulo 4 o es otra tesis.

## DA-10 · Líneas 4 y 5 (agregadas por el autor a mitad de sesión): matriz de variantes y presupuesto de CPU

- **Qué**: rama `feat/robustez-modelo` en un *worktree* propio (`bci-fault-bench-futuro-robustez`) para no chocar con la rama de BciPy que se construye en paralelo. Variantes: `eegnet` (control, debe reproducir la tabla de la campaña 2), `eegnet_gapaug` (aumentación de huecos U(0,4; 1,6) s, nueve sujetos), `eegnet_fill_interp` y `eegnet_fill_hold` (relleno en inferencia sobre los modelos originales, nueve sujetos, sin reentrenar), `eegnet_gapaug_fill_interp`, `eegnet_mask` (canal 23 de máscara, entrenado con huecos; sujetos 1, 5 y 8 primero, los nueve si el tiempo alcanza). Híbrido con reglas `complete` (1000 muestras), `gap40` y `gap200` sobre la red original y la endurecida. Evaluación en un espejo `results/campana2-eval/` (copias de los archivos chicos + `trials_<variante>.csv`), leyendo `segments.npz` del original sin escribir ahí.
- **Por qué**: el autor fijó el orden (a en nueve; b y c en tres si la CPU no da); el relleno en inferencia no requiere entrenamiento, así que va en nueve; el canal máscara sin huecos en el entrenamiento no tiene sentido, por eso hereda la aumentación. La memoria libre de la notebook era de ≈ 2,5 GB con otros trabajos corriendo: entrenamientos secuenciales o de a dos.
- **Alternativa descartada**: evaluar las variantes con un script propio fuera de `analyze.py`. Descartada porque la consigna pide la MISMA métrica y prueba del banco (mediana por sujeto sobre cinco corridas, Wilcoxon apareado con Holm); reutilizar `analyze.py --trials-file` garantiza que las tablas sean comparables con las de Resultados.

## DA-11 · Framework elegido: BciPy, solo su capa de adquisición, instalado sin dependencias en Python 3.12

- **Qué**: se construye el consumidor alternativo sobre `bcipy.acquisition` (BciPy 2.0.1, BSD-3) instalado con `--no-deps --ignore-requires-python` más las dependencias que esa capa importa (`requirements-bcipy.txt`). MEDUSA queda descartado para la implementación y se usa como contrapunto analítico en la Discusión.
- **Por qué**: BciPy es biblioteca, su capa de adquisición no arrastra la GUI, tiene búfer acotado consultable por marcas de tiempo y licencia compatible con el repo público. MEDUSA recibe LSL solo en su aplicación de escritorio (PySide6 + cuenta en línea, no corre sin pantalla en la VM) y su licencia CC BY-NC-ND impide publicar un consumidor derivado. Instalar Python 3.10 en la notebook era posible pero agrega un intérprete al sistema del autor sin necesidad: la capa de adquisición importa en 3.12 (verificado).
- **Alternativa descartada**: copiar los ~8 archivos de la capa de adquisición al repo (BSD-3 lo permite). Funciona igual, pero debilita el argumento "se usa el framework" y complica la trazabilidad de versión.
- **Amenaza a la validez que hay que declarar**: BciPy 2.0.1 se usa fuera de su rango de Python soportado (< 3.11) y sin sus versiones fijadas de numpy/pandas.

## DA-09 · El vault no se commitea en esta sesión

- **Qué**: los archivos nuevos en `30-TFG/Lineas-Futuras/` quedan sin commitear en el repo privado del vault.
- **Por qué**: ESTADO-ACTUAL indica "vault sin commitear desde el 07/09: commit cuando el autor lo pida", y la otra sesión tiene cambios pendientes en el mismo repo; un commit desde acá podría arrastrar archivos ajenos.
- **Alternativa descartada**: commit selectivo solo de `Lineas-Futuras/`. Seguro en principio, pero el autor definió la política y no hay urgencia.

---

# Decisiones de las líneas 4 y 5 (tomadas por el agente de implementación; revisadas por el orquestador)
> 2026-09-27 · Sesión autónoma. Para fusionar en [[Decisiones-Autonomas]] (este archivo no la edita). Código: worktree `bci-fault-bench-futuro-robustez`, rama `feat/robustez-modelo`. Notas: [[Linea-4-Endurecer-EEGNet]], [[Linea-5-Hibrido-Vigia]].

**DA-R1 · Intérprete de Python.**
- Qué: se usó `TESIS/40-Prototipo/.venv` (torch 2.14 CPU, mne 1.13, moabb 1.7, sklearn 1.9) y no `bci-fault-bench-futuro/.venv`.
- Por qué: el venv indicado **no tiene torch instalado** (verificado con `pip list`); el de 40-Prototipo tiene las mismas versiones de mne/moabb/sklearn/pandas más torch. Solo se ejecutó el intérprete; no se escribió nada dentro de 40-Prototipo.
- Descartado: instalar torch en el venv indicado (≈ 200 MB de descarga, cambio de entorno no pedido).

**DA-R2 · Espejo de evaluación en lugar de escribir en la campaña.**
- Qué: `results/campana2-eval/<exec>/` con copias de `producer.json`, `consumer.json`, `telemetry.csv`, `trials.csv`, `trials_csp_offline.csv` y el `trials_eegnet.csv` original renombrado `trials_eegnet_orig.csv`; los `segments.npz` se leen de la carpeta original.
- Por qué: la campaña es de solo lectura y `analyze.py` necesita todo junto en una carpeta por ejecución.
- Descartado: symlinks (Windows sin privilegios) o parametrizar `load_campaign` con dos raíces (más cambios en código ya publicado).

**DA-R3 · Control exacto antes de cualquier variante.**
- Qué: la variante `eegnet` se recalculó con el pipeline nuevo y se comparó ensayo por ensayo con el `trials_eegnet.csv` original: **0 diferencias** de predicción o validez en 20.520 ensayos (855 ejecuciones) y `t_desempeno.md` **idéntico byte a byte** al de `40-Prototipo/results/analysis-eegnet`. Lo mismo para CSP en línea (`trials.csv`) contra `analysis/t_desempeno.md`.
- Por qué: si el control no reproduce, cualquier diferencia entre variantes podría ser del pipeline.

**DA-R4 · Dónde se aplica el hueco del aumento: espacio crudo, antes del filtro.**
- Qué: el aumento borra el tramo en la época **cruda** con 1 s de relleno a cada lado (0 V), filtra 8-30 Hz y recorta [2, 6] s, exactamente la cadena de inferencia.
- Por qué: en inferencia la muestra faltante vale 0 V **antes** del filtro. Se verificó el temor de "-mu/sd ≠ 0": como la señal de entrenamiento está filtrada 8-30 Hz, mu es del orden de 1e-10 V y sd de 4e-6 V, así que **max |mu/sd| = 7·10⁻⁴** (sujetos 1 y 5): el silencio estandarizado es ≈ 0. Lo que sí difiere entre "cero crudo" y "cero estandarizado" es el **transitorio del filtro** en los bordes del hueco; borrar en crudo lo reproduce, borrar en espacio estandarizado no.
- Descartado: poner ceros después de la estandarización (entrenaría con bordes abruptos que la red nunca ve en inferencia).

**DA-R5 · Consecuencia de DA-R4: las variantes aumentadas se entrenan con ventanas filtradas por ensayo.**
- Qué: `eegnet_gapaug`/`_mask`/`_wide` ven ventanas filtradas sobre [1, 7) s (como en inferencia), mientras que el EEGNet original se entrenó con épocas recortadas de la corrida continua ya filtrada (`data.epochs_of`). Mismos ensayos (144 por sujeto, sin artefactos), mismas épocas (300), semilla 0, Adam 1e-3, lote 32, misma arquitectura.
- Por qué: es la única forma de que el hueco del entrenamiento tenga el mismo transitorio que en inferencia.
- Costo: confusión declarada. La variante endurecida difiere del original en dos cosas (aumento + filtrado por ventana). La sonda sin hueco y la tabla limpia permiten separarlo solo en parte (ver límites en la Línea 4).

**DA-R6 · Probabilidad del aumento p = 0,5.**
- Qué: en cada época, cada ensayo recibe un hueco con probabilidad 0,5 (nuevo sorteo por época: posición y largo).
- Por qué: la mayor parte del uso real (y 16 de las 19 condiciones de la campaña) es sin hueco en la ventana; con p = 1 la red nunca vería una ventana completa en el entrenamiento y se arriesga desempeño limpio, que es justamente lo que se pide no pagar. Con p = 0,5 el desempeño limpio no bajó (ver tabla limpia).
- Descartado: p = 1 (sin evidencia de que haga falta y con costo probable en limpio); barrer p (no entraba en el presupuesto).

**DA-R7 · Largo y posición del hueco: U(0,4; 1,6) s en posición uniforme dentro de la ventana.**
- Qué: se siguió la consigna. Se midió después que los huecos reales de la campaña son: pérdida contigua 0,40 / 1,00 / 1,60 s en posición aleatoria; desconexión en el ensayo **1,52 / 1,52 / 2,52 s y siempre al inicio de la ventana** (arranca a los 2,00-2,04 s).
- Consecuencia: el corte de 2 s (2,52 s) queda fuera del rango de entrenamiento; por eso se entrenó también `eegnet_gapaug_wide` con U(0,4; 2,6) s.
- Descartado (quedó como propuesta): un aumento **anclado al inicio** de la ventana, que es lo que la sonda de posición señala como causa.

**DA-R8 · Relleno alternativo aplicado en la grilla cruda, antes del filtro.**
- Qué: `interp` (np.interp por canal; bordes = valor más cercano) y `hold` (última muestra; hueco inicial = primer valor presente), en toda la grilla con relleno de 1500 muestras.
- Hallazgo: tras el filtro 8-30 Hz, **cualquier relleno suave se vuelve ≈ 0 dentro del hueco**: RMS en el interior del hueco (a más de 0,4 s de una muestra presente) / RMS de la señal presente = 0,001 para cero, interpolación y retención (medido en 30 ejecuciones de pérdida contigua 0,4 y corte en el ensayo 2 s). Solo cambia el borde (0,13 / 0,13 / 0,15 en los 0,4 s cercanos). Una recta o una constante no tienen energía en 8-30 Hz. Rellenar antes del filtro es, para la red, casi lo mismo que poner ceros.
- Descartado: rellenar después del filtro (no es lo que haría un pipeline real que filtra el flujo, y un relleno lineal del filtrado igual carece de contenido en banda).

**DA-R9 · Canal máscara: n_ch = 23, mu = 0 y sd = 1, sin filtrar.**
- Qué: canal 23 = 1 donde falta la muestra de la grilla nominal dentro de la ventana; la convolución espacial en profundidad abarca las 23 filas. Se entrena con el mismo aumento que `gapaug` (una máscara sin huecos en el entrenamiento sería constante e inútil).
- Por qué: es la forma más simple de "indicador de faltante" (Che et al., 2018) que no cambia la arquitectura salvo en el número de filas.
- Descartado: una rama separada para la máscara o multiplicarla dentro de la red (cambia la arquitectura de referencia).

**DA-R10 · Cobertura de sujetos.**
- Qué: `gapaug` 9/9, rellenos 9/9 (solo inferencia), `mask` en 1, 5 y 8 primero y luego extendida a 9/9 porque el tiempo medido lo permitió (≈ 5-6 min por sujeto con dos entrenamientos en paralelo de 5 hilos), `gapaug_wide` 9/9.
- Presupuesto usado: ver Línea 4 (tiempos por sujeto en `results/train_<variante>.csv`).

**DA-R11 · `analyze.py --perf-only`.**
- Qué: bandera nueva que corta el análisis después de desempeño e infraestructura (sección 1).
- Por qué: el análisis completo tardó 8,5 min por variante (la mayor parte en ventana móvil, divergencia y detectores LOSO, que no dependen de la variante en lo que aquí interesa); con ≈ 15 variantes eran más de 2 h. `t_desempeno.*` sale idéntico con y sin la bandera.
- Descartado: paralelizar el análisis (más memoria de la disponible).

**DA-R12 · Vigía: señales y reglas.**
- Qué: por ensayo, n.º de muestras en [2, 6) s y máximo intervalo entre muestras presentes **contando los bordes de la ventana** (un hueco que empieza en el borde también cuenta). Reglas `complete` (1000 muestras), `gap40` (≤ 40 ms = un bloque de transporte) y `gap200` (≤ 200 ms).
- Por qué los bordes: la desconexión en el ensayo empieza exactamente en el borde; sin contarlo, el vigía no la vería.
- Descartado: usar la telemetría por segundo (`telemetry.csv`): tiene resolución de 1 s y no se alinea con la ventana del ensayo.

**DA-R13 · Rama de respaldo del híbrido: CSP+LDA fuera de línea.**
- Qué: cuando el vigía detecta hueco se usa la decisión de `trials_csp_offline.csv` (misma grilla con ceros, filtrada, y CSP sobre las muestras presentes).
- Por qué: es la decisión que se obtiene del mismo segmento y con la misma cadena que la red; la de `trials.csv` filtra la señal compactada y es otra cadena. En la campaña ambas coinciden en las medianas de las condiciones estructuradas salvo desconexión en el ensayo 0,5 y 1 s (0,750 en línea vs 0,667 fuera de línea).
- Descartado: CSP en línea como respaldo (mezclaría dos cadenas de preprocesamiento en un mismo decodificador).

**DA-R14 · Sonda de posición del hueco.**
- Qué: `scripts/gap_position_probe.py` borra 1,52 s (el largo de la desconexión en el ensayo de 0,5 y 1 s) al inicio, al medio o al final de la ventana sobre la sesión 2 limpia y decodifica con cada modelo.
- Por qué: los números de la campaña mostraron que `gapaug` recupera la pérdida contigua de 1,6 s (posición aleatoria) pero no la desconexión de 1,52 s (siempre al inicio), aunque el largo está dentro del rango de entrenamiento. La sonda aísla la posición como variable.

**DA-R15 · Qué no se commitea.**
- `results/` está en `.gitignore` (modelos, espejo, análisis, tablas). Las tablas finales se copiaron como markdown a las notas del vault.

**DA-R16 · Comparación entre variantes apareada por sujeto, sin corrección.**
- Qué: además de cada variante contra su propia referencia (Holm, como en E2), `compare_variants.py` informa la diferencia apareada por sujeto contra EEGNet original (mediana, sujetos que mejoran/empeoran, Wilcoxon sin corregir).
- Por qué: la mediana de medianas engaña. La referencia de `gapaug` figura 0,833 contra 0,750, pero apareado por sujeto la diferencia es 0 (3 mejoran, 3 empeoran, p = 1). Sin esta tabla se habría reportado una mejora inexistente.
- Descartado: corregir por Holm sobre todas las variantes × condiciones (≈ 70 pruebas exploratorias; el objetivo es orientar, no confirmar).
