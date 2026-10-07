# Decisiones metodológicas tomadas al redactar el Entregable 1

> 2026-09-07 · Registro de lo que se decidió mientras se escribían Introducción y Métodos, con su porqué. Todo esto ya está en el texto entregado; acá queda la trazabilidad para el Módulo 2 y para la defensa.
> Versión entregada: 25 páginas (Introducción 12, Métodos 6, Referencias 5), 29 referencias verificadas contra Crossref y fuentes primarias.

## Hueco de investigación (formulación vigente)

Tres grupos de fuentes y qué midió cada uno: (1) plataformas de software BCI — describen arquitectura y capacidades, algunas latencias nominales, ninguna el decodificador bajo falla; (2) robustez de la decodificación — perturban la señal, no el software; (3) inyección de fallos / *stream processing* — perturban el software, sin decodificador al final. La combinación **no se encontró en las fuentes de referencia relevadas para este trabajo**. Nunca "nadie evaluó".

**Precisión sobre LSL** (verificada en Kothe et al. 2025 y en la FAQ oficial): transporte por TCP (datos) y UDP (descubrimiento), sincronización tipo NTP cada 5 s, búferes configurables, reconexión automática aun con otra IP, pruebas de estrés con cientos de flujos y desconexiones aleatorias, *jitter* de campo ~0,5 ms. **No reportan** tasas de pérdida, tiempos de recuperación ni efecto sobre la decodificación.

## Modelos de fallo = perturbaciones en la interfaz de transporte

Corrección importante (feedback externo, verificado): una pérdida de paquetes de red **no** borra muestras porque TCP retransmite; produce latencia y *jitter*. La pérdida real de muestras ocurre antes de LSL (dispositivo) o por saturación del búfer del consumidor, que descarta las más antiguas (FAQ de LSL).

| Modelo | Dónde se aplica | Qué mide | Origen real que representa |
|---|---|---|---|
| Pérdida de muestras (1/5/10 %, aleatoria o en ráfagas) | Contenido del flujo (el inyector omite muestras) | Tolerancia del pipeline a datos faltantes | Dispositivo que pierde muestras antes de LSL; búfer saturado |
| *Jitter* (10/50/100 ms) y retraso (50/100/250 ms) | Instante de entrega de cada bloque | Tolerancia a la temporalidad | Congestión de red, retransmisiones TCP, consumidor demorado |
| Desconexión (0,5/1/3 s) | Transporte real: el flujo de origen se cierra y se recrea | Reconexión y búferes de LSL (**único modelo que los ejercita directamente**) | Corte de enlace, caída del proceso productor |

Rangos anclados al ensayo de 4 s a 250 Hz (1000 muestras). Valores definitivos tras el piloto; no se cambian después de ver resultados.

## Diseño experimental

- **Objeto de estudio**: un pipeline BCI único (MNE-LSL + código propio + CSP/LDA sobre MNE-Python y scikit-learn). No se usa BciPy/MEDUSA de entrada porque traen sus propios búferes y manejo de errores y no permitirían atribuir el efecto al transporte. Segunda implementación = validez externa, después.
- **Unidades experimentales**: los 9 sujetos de BCI IV 2a. Sesión 1 entrena el decodificador (sin fallo, offline); sesión 2 se reproduce por el pipeline.
- **Bloques**: corridas 1-5 de la sesión 2 en la campaña principal; **corrida 6 reservada al piloto** (calibra severidades, umbral y tamaño de ventana; no entra en las comparaciones). Cada corrida se reproduce sin fallo y bajo cada condición, con semilla fija. Toda comparación es *misma corrida con vs. sin fallo*.
- **Clases**: se reproduce la corrida completa (48 ensayos + pausas) para conservar carga y temporalidad; se clasifican solo los 24 ensayos izquierda/derecha. Dos clases porque CSP es binario por formulación.
- **Campaña**: 585 ejecuciones (5 referencia + 60 con fallo por sujeto) ≈ 68 h de replay en tiempo real, automatizadas. Piloto aparte sobre la corrida 6 de un subconjunto de sujetos.

## Variables y umbral

- *Balanced accuracy* como métrica funcional principal (las fallas descartan ventanas de forma no uniforme y desbalancean el conjunto evaluado).
- **Misma escala**: la *balanced accuracy* se calcula siempre sobre ventana móvil de ensayos; la distribución de referencia usa la misma ventana sobre las 5 corridas sin fallo del sujeto; el umbral sale de su dispersión. Tamaño de ventana fijado en el piloto, constante después.
- Estado operativo = proceso activo + flujo conectado + sin excepciones + llegada continua de muestras y predicciones. Degradación funcional = caída de *balanced accuracy* que supera el umbral. Inicio = primera ventana que lo cruza; de ahí se mide el retardo de detección.

## Análisis

- **Unidad estadística = sujeto**. Las 5 corridas de cada sujeto y condición se resumen en su mediana antes de las pruebas (evita pseudorreplicación); la variabilidad entre corridas se reporta descriptivamente. Alternativa para más adelante: modelo jerárquico que preserve las 5 observaciones.
- RQ1: Friedman (referencia + 3 severidades por tipo) → Wilcoxon vs. referencia con Holm → tamaños de efecto.
- RQ2: cruce ventana a ventana de estado operativo vs. degradación; proporción de ventanas divergentes por condición.
- RQ3: detector por umbrales vs. modelo (regresión logística como referencia lineal; *random forest* y *gradient boosting* para interacciones entre variables de telemetría; sin *deep learning* por volumen de datos). Validación cruzada dejando un sujeto fuera. **Pendiente Módulo 2**: selección de hiperparámetros dentro del entrenamiento (LOSO externo + validación interna).

## Convenciones de redacción fijadas

- Términos técnicos: nombres de algoritmos/métricas/técnicas en inglés con traducción entre paréntesis (*deep learning*, *jitter*, *balanced accuracy*, *data leakage*, *chaos engineering*, *random forest*, *gradient boosting*); conceptos descriptivos en español con el inglés al lado (pérdida de muestras, computación confiable, *silent failures*, procesamiento de flujos, retardo de detección, ventana móvil, imaginería motora).
- Todo término que un lector externo no conozca lleva explicación breve en la primera aparición.
- No comparar bits/min (Wolpaw) con palabras/min (Willett). Relación exactitud → esfuerzo no es lineal.
- Relevamiento de repositorios: declarar indicador (estrellas de GitHub + fecha del último cambio) y fecha (16-08-2026); inferencia acotada.
- Lo que el estudio no pretende (SiL no reproduce electrodos, amplificadores, interferencia ni adaptación del usuario) va explícito en la Introducción.

## Hecho después de la entrega (2026-09-07, misma sesión)

- **Tabla 1 (modelos de fallo)** en Métodos: reemplaza el párrafo de 400 palabras por una tabla APA (número, título en cursiva, solo líneas horizontales, nota) + un párrafo corto con la distinción TCP/interfaz. `build.js` ahora soporta `{ table: {num, title, headers, rows, note} }`. Esta versión NO es la entregada: es la base para el Módulo 2.

## Pendiente si el tutor lo pide

- Tabla 2 de variables dependientes por familia (mismo mecanismo).
- Pasada de legibilidad: partir los párrafos largos de LSL, Gemborn Nilsson/Wilson y Vogel; oraciones de menos de 40 palabras; menos jerga de infraestructura en Vogel.
- Párrafo de síntesis al inicio de Métodos, antes de Diseño.
- Versión larga (25 págs previa, v4) y versión de 19 págs (v5) guardadas en `src/`.
