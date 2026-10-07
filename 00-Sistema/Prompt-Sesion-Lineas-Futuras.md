# Prompt de arranque: sesión autónoma de líneas futuras (Módulos 3 y 4)

> Copiar como primer mensaje de una sesión nueva en `C:\Users\agustin.tamagusuku\Desktop\TESIS`. Corre en paralelo con la sesión que cierra el Entregable 2 y **sin humano en el lazo**: el autor no va a estar disponible durante horas.

---

Hola. Soy Agustín, autor del TFG *Interfaces cerebro-computadora bajo condiciones adversas: del software a la decodificación* (Ingeniería en Software, Siglo 21). El Entregable 2 lo está cerrando **otra sesión** (se entrega el lunes 28/09). Esta sesión trabaja **de forma autónoma y continua**: no voy a estar para responder preguntas durante varias horas. Tomá las decisiones vos, registralas, y seguí. Cuando vuelva quiero encontrar todo preparado para **encender la VM y correr los experimentos siguientes**.

Antes de empezar, leé en este orden: `TESIS/00-Sistema/ESTADO-ACTUAL.md` (traspaso; incluye la sección "Versión 2"), `TESIS/30-TFG/Trabajo-Futuro.md`, `TESIS/30-TFG/Fundamentos-Diseno-Estadistico.md`, `TESIS/40-Prototipo/README.md` y el código en `TESIS/40-Prototipo/src/bcibench/`. Buscá en engram (proyecto `tesis`) los topic keys `tfg/entregable-2/*`.

## Reglas duras (no negociables)

1. **No modificar** nada en `TESIS/30-TFG/Entregas/`, `TESIS/40-Prototipo/` (código y resultados de la campaña actual), `00-Sistema/ESTADO-ACTUAL.md` ni `00-Sistema/Bitacora.md`. Esos los usa la otra sesión. Tu espacio de escritura en el vault: `TESIS/30-TFG/Lineas-Futuras/` (crealo) y `TESIS/20-Investigacion/`.
2. **Código**: trabajá en un clon aparte del repositorio público, `C:\Users\agustin.tamagusuku\Desktop\bci-fault-bench-futuro`, en ramas `feat/<linea>`. Nunca en `main`. Si una línea necesita un proyecto separado (por ejemplo, intracortical), creá un repositorio nuevo público con `gh repo create agustama27/<nombre> --public` y trabajá ahí. Commits con *conventional commits*, sin atribución de IA. Podés hacer push de tus ramas.
3. **No encender la instancia de AWS** ni contratar nada que cueste dinero. Todo corre en la notebook (12 CPU, sin GPU) o es lectura. Preparás los comandos; los ejecuto yo en la VM cuando vuelva.
4. **Ninguna cita ni afirmación de hecho sin fuente primaria verificada** (Crossref por DOI, o fetch de la página oficial). Lo dudoso se marca ⚠️ SIN VERIFICAR y no se usa como base de una decisión.
5. **La tesis es dinámica.** Lo único fijo es la pregunta de investigación y la línea temática. Todo lo demás (antecedentes de la Introducción, diseño y modelos de fallo en Métodos, Resultados) puede y debe evolucionar con lo que encuentres: el profesor confirmó que se pueden hacer todos los cambios que hagan falta modificando el diseño metodológico. Por eso, además de las notas técnicas, redactá **propuestas de modificación al manuscrito** para integrar después del 28/09: qué párrafos de la Introducción agregar o cambiar (con las citas verificadas), qué cambia en Métodos (Tabla 1, instrumentos, diseño), y qué resultados nuevos habría que reportar. Guardalas en `TESIS/30-TFG/Lineas-Futuras/Propuestas-Manuscrito.md`; no edites los archivos de la entrega.
6. Registrá cada decisión que tomes sin mí en `TESIS/30-TFG/Lineas-Futuras/Decisiones-Autonomas.md` (qué, por qué, alternativa descartada) y guardá lo importante en engram con `mem_save` (proyecto `tesis`, topic keys `tfg/lineas-futuras/*`).

## Las tres líneas, en orden de prioridad

1. **Segundo framework (BciPy o MEDUSA)**. Meta del Módulo 4: reemplazar nuestro consumidor por un framework BCI completo y medir si sus búferes amortiguan o amplifican el costo de reconexión de LSL (≈ 570 ms por corte, medido en la campaña). Hacé: comparación verificada de ambos (estado del repositorio, licencia, cómo reciben LSL, dónde se enchufa un decodificador propio, esfuerzo real); elegí uno y justificalo; instalalo en un venv aparte; construí un consumidor alternativo (`consumer_<framework>.py`) que reciba nuestros dos flujos LSL (`<exec>-eeg`, `<exec>-markers`) y produzca **los mismos** `trials.csv`, `telemetry.csv`, `segments.npz` que el nuestro, para que `runner.py` y `analyze.py` sirvan sin cambios; probalo en la notebook con `scripts/smoke_run.py` (o un equivalente) contra el reproductor existente. Dejá el comando exacto de campaña para la VM.
2. **Trazas reales**. Reemplazar las fallas sintéticas por comportamiento medido de enlaces reales. Hacé: búsqueda de trazas o mediciones publicadas de pérdida/latencia/cortes en Bluetooth de cascos EEG y en Wi-Fi congestionado (con fuente verificada); diseñá un modo `trace` del inyector que reproduzca una traza (formato de archivo, cómo se ancla a la escala del ensayo); si encontrás una traza usable, implementalo y probalo en la notebook; si no, dejá el diseño y la lista de lo que falta.
3. **Señal intracortical**. Hacé: relevar qué datasets públicos de implantes existen de verdad (disponibilidad, licencia, formato, tasa de muestreo, tarea), cuál es el decodificador de referencia para disparos neuronales, y qué cambia en el banco (cargador, decodificador, escala de severidades). Estimación honesta de esfuerzo y una recomendación: ¿Módulo 4 o tesis aparte? Si un dataset es accesible sin registro y chico, bajalo y hacé el PoC 1 (cargar + decodificar fuera de línea) en la notebook.

## Entregables al terminar

- Una nota por línea en `TESIS/30-TFG/Lineas-Futuras/` con hallazgos verificados, tradeoffs, esfuerzo estimado, y el **comando exacto** para correr lo que corresponda en la VM.
- `Propuestas-Manuscrito.md`: cambios propuestos a Introducción, Métodos y Resultados por cada línea, redactados en el registro del manuscrito y con citas verificadas, más un párrafo por línea para "Recomendaciones y líneas futuras" de la Discusión.
- `Decisiones-Autonomas.md` completo y `mem_session_summary` en engram.
- Un mensaje final en el chat con: qué quedó listo para la VM, qué quedó a medias, qué necesita una decisión mía.

Trabajá hasta terminar las tres líneas o hasta agotar lo que se puede hacer sin la VM y sin mí. No pares para preguntar salvo que algo pueda costar dinero o dañar lo existente.

---

## Agregado (27/09, 13:10): dos líneas nuevas, prioridad por encima de las tres anteriores

Se suma a lo que ya estás haciendo; no reemplaza nada. Leé primero la sección "B bis" de `TESIS/30-TFG/Trabajo-Futuro.md` (líneas 10a y 10b). Hallazgo que las motiva: en la campaña de 855 ejecuciones, EEGNet cayó al azar con cualquier corte dentro de la ventana del ensayo (0,583 / 0,583 / 0,500, p = 0,012) mientras CSP+LDA solo cayó en la severidad máxima. Causa probable: la red recibe ceros donde falta señal y nunca vio silencios al entrenar; CSP usa covarianzas de las muestras presentes.

Ventaja: **no hace falta la VM.** Todo se evalúa en la notebook sobre los segmentos ya guardados. Datos de solo lectura: `TESIS/40-Prototipo/results/vm/campana2/<exec>/segments.npz` (855 ejecuciones; formato en `TESIS/40-Prototipo/scripts/redecode_segments.py`), modelos en `TESIS/40-Prototipo/results/models/` (`decoder_sXX.pkl` CSP+LDA, `eegnet_sXX.pkl`), código de EEGNet en `TESIS/40-Prototipo/src/bcibench/eegnet.py`, entrenamiento en `scripts/train_eegnet.py`. Regla 1 sigue: no modifiques nada dentro de `40-Prototipo`; copiá lo que necesites a tu clon `bci-fault-bench-futuro` (rama `feat/robustez-modelo`) y escribí resultados en `TESIS/30-TFG/Lineas-Futuras/`.

**Línea 4 (nueva, prioridad máxima): endurecer la red.** Entrenar variantes de EEGNet por sujeto (misma sesión 1, mismos 300 épocas, misma semilla) con: (a) aumentación de huecos (borrar al azar tramos contiguos de 0,4 a 1,6 s en cada época de entrenamiento, rellenados igual que en inferencia); (b) relleno alternativo en inferencia (interpolación lineal y último valor, en lugar de ceros); (c) canal de máscara "falta señal" como entrada adicional. Evaluar cada variante sobre los segmentos de las 855 ejecuciones con la misma métrica del banco (balanced accuracy, mediana por sujeto sobre cinco corridas, Wilcoxon apareado contra referencia con Holm), reutilizando `analyze.py --trials-file` de tu clon. Entregable: tabla EEGNet original vs variantes por condición, y una recomendación concreta ("entrenar con huecos elimina/no elimina la fragilidad"). Si la CPU no da para todas las variantes en las nueve personas, hacé primero (a) en las nueve y (b)/(c) en tres sujetos (1, 5, 8) y decilo.

**Línea 5 (nueva): híbrido con vigía.** Diseñar y prototipar fuera de línea un decodificador que use la red cuando la ventana llegó entera y caiga a CSP+LDA cuando la telemetría del ensayo indique hueco (`n_samples < 1000` o intervalo entre llegadas mayor a un umbral). Evaluarlo sobre los mismos segmentos: ¿recupera el desempeño de CSP en las fallas estructuradas sin perder el de la red en la referencia? Entregable: tabla híbrido vs CSP vs EEGNet por condición, y el diseño de cómo se integraría en `consumer.py` en línea (sin implementarlo ahí).

Para ambas: registrá cada decisión en `Decisiones-Autonomas.md`, citá con fuente verificada cualquier técnica que nombres (aumentación, máscaras), y agregá a `Propuestas-Manuscrito.md` qué cambiaría en Métodos y Resultados si estas variantes entran al Módulo 3 o 4.
