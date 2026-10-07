# Trabajo futuro — perspectivas para los Módulos 3 y 4 y después

> 2026-09-26 · Ideas conversadas durante la campaña del Entregable 2, ordenadas por dónde encajan según la guía oficial: el Módulo 3 pide Intro/Métodos/Resultados corregidos + **Discusión** (interpretación, limitaciones, aportes, conclusiones y **recomendaciones**); el Módulo 4 es el manuscrito completo (portada, índice, resumen/abstract, palabras clave). Nada nuevo se experimenta formalmente después del Módulo 2.

## Principio de diseño que habilita todo esto

El banco es agnóstico a la carga y al decodificador: el inyector actúa sobre bloques en la interfaz de transporte y el consumidor no sabe qué modelo tiene enchufado. Cambiar señal o decodificador es reemplazar una pieza, no rehacer el laboratorio (objetivo específico 6).

## A. Ejecutable y admisible en "Resultados corregidos" del Módulo 3

> **Actualización 27/09**: los puntos 1 y 2 y la sección A bis (fallas estructuradas) **se ejecutaron en la versión 2 del Entregable 2** (campaña de 855 ejecuciones con dos familias y dos decodificadores; segmentos guardados por ensayo). Quedan como hechos, no como futuro. El DOI Zenodo (punto 8) se tramita el lunes 28.

Solo lo que Métodos ya prometió; agregar experimentos nuevos obligaría a reescribir Métodos.

1. **Completar las cinco corridas por sujeto** (585 ejecuciones). Deuda declarada en Métodos corregido (D-008). Una noche de VM. Antes de lanzarla, correr el control de paralelismo con **12 ejecuciones simultáneas** (la VM de 8 vCPU estuvo al 3-6 % de carga con 6): si el control sale limpio como con 6 (diferencias < 0,1 ms), la campaña entera va a 12 y tarda la mitad. No se cambió a mitad de la campaña de E2 para no mezclar condiciones de máquina.
2. **Segundo decodificador: EEGNet** (Lawhern et al., 2018 ⚠️ SIN VERIFICAR). Métodos ya contempla "una segunda implementación como validez externa". Hipótesis: CSP tolera la pérdida aleatoria porque trabaja con covarianzas; un modelo que mira la forma de onda podría degradarse antes. Convierte "el decodificador aguanta" en "depende de la familia de modelo". Una tarde.

## A bis. Criterio para la segunda campaña: estructura, no magnitud (2026-09-27)

Las severidades de E2 se anclaron a la escala del ensayo (nota de la Tabla 1). Las fuentes ya citadas acotan lo realista: casco inalámbrico 20-40 ms de retraso con 5 ms de jitter (Gemborn Nilsson), procesamiento hasta 50-141 ms (Wilson), LSL en campo 0,5 ms de jitter (Kothe). Jitter y retraso de E2 ya cubren ese rango: **subir magnitudes sería inventar una realidad**. Lo que E2 no probó es la **forma** de las fallas reales:

1. **Pérdida contigua y localizada**: ráfagas de 100-500 ms (duración típica de un *dropout* Bluetooth ⚠️ buscar fuente) colocadas dentro de la ventana [2, 6] s del ensayo; misma pérdida total que E2, distinta estructura. CSP promedia; "medio mes sin mediciones" sí mueve la media.
2. **Desconexiones que caen en el ensayo** (controlar el instante, no alargar el corte).
3. **Plazo del consumidor como variable** (250/500/1.000 ms tras el fin del ensayo): hoy espera hasta 3 s, por eso el retraso nunca produjo decisiones inválidas.
4. **Decodificador que no promedie** (EEGNet): ¿la robustez es del transporte o del modelo?

Cómo declararlo: los objetivos no cambian; Métodos corregido agrega una segunda familia de modelos de fallo ("estructurados") y la variable plazo, con la frase "a la luz de los resultados de la primera campaña…". Con esa frase es ciencia; sin ella, ajuste post hoc. Toda severidad nueva se ancla a una fuente verificada antes de escribirla.

## B. Discusión del Módulo 3: recomendaciones y líneas futuras (argumentadas con los datos)

3. **Detector en vivo.** Hoy los detectores se evalúan fuera de línea sobre la telemetría. Convertirlos en una alarma que corre durante la ejecución y medir su retardo real. Paso de "medí un problema" a "construí una mitigación".
4. **Segundo marco de aplicación (BciPy o MEDUSA).** ¿Las capas de búfer y manejo de errores del framework amortiguan o amplifican el costo de reconexión de LSL? Una o dos semanas.
5. **Fallas realistas.** Reproducir en el inyector una traza real de un enlace Wi-Fi congestionado o de un casco Bluetooth, en lugar de jitter gaussiano. Cierra la objeción "fallas de laboratorio".
6. **Señal intracortical.** Datasets públicos de implantes (Willett et al.; Neural Latents Benchmark ⚠️ verificar disponibilidad y licencia). Pregunta nueva: ¿la vulnerabilidad al transporte depende del tipo de señal? Tasas mucho más altas y decodificadores distintos (CSP no aplica a disparos). Es casi una tesis de maestría; es la extensión que más acerca a la meta de carrera.
7. **Devolver el hallazgo a LSL.** Si la campaña confirma que cada reconexión cuesta ~1 s de señal, abrir un *issue* documentado en el proyecto LSL con método y números. Contribución al ecosistema.

## B bis. Robustez por familia de modelo (sale del hallazgo central de la v2, 27/09)

Hallazgo: EEGNet cae al azar con cualquier corte dentro del ensayo (0,583/0,583/0,500, p = 0,012) mientras CSP+LDA solo cae en la severidad máxima. Causa probable: la red recibe ceros donde falta señal (tensor de tamaño fijo) y nunca vio silencios al entrenar; CSP usa covarianzas de las muestras presentes. Tres caminos, todos evaluables sobre los segmentos guardados sin nueva campaña:

10a. **Endurecer la red** (días): entrenar con aumentación de huecos (borrar tramos al azar), comparar rellenos (ceros vs interpolación vs último valor), agregar un canal máscara "acá falta señal". Comparación EEGNet original vs endurecida sobre las 855 ejecuciones. Candidato a Resultados del Módulo 3/4.
10b. **Híbrido con vigía** (una semana): red cuando la señal está entera, caída a CSP cuando la caja negra detecta hueco en la ventana; le da función al detector (objetivo 5). Módulo 4.
10c. **Ampliar la familia** (semanas): riemannianos (covarianza: deberían aguantar como CSP), redes más profundas (ShallowConvNet, Deep4 ⚠️ verificar citas), modelos clínicos. De "la red se rompe" a "la fragilidad crece con X propiedad del modelo". Publicación / maestría.

## C. Módulo 4 (manuscrito final)

8. **Publicar el banco** con licencia abierta y DOI (Zenodo). Responde el objetivo 6 con una URL citable.
9. **Open Lab (octubre)**: demo en vivo del banco (saboteador cortando el cable, caja negra mostrándolo). Ver Guía-SeminarioFinal.

## Hallazgos del piloto que motivan lo anterior (2026-09-26, VM, sujetos 1, 5 y 8)

- Infraestructura responde exacta a cada modelo de fallo; desconexión de 3 s × 5 → 13 s sin datos y 4,6 % de señal perdida (nominal 3,9 %): **costo de reconexión** confirmado.
- Desempeño funcional casi invariante (s8 = 1,000 en las 13 condiciones; s1 solo baja con pérdida; s5 en efecto piso, 0,50). → La divergencia infraestructura/decodificación (objetivo 4) es el resultado central; motiva 2, 3 y 5.
- Regla de umbral: percentil/MAD marcan 4-7 % de ventanas sanas por construcción; `min` (peor que cualquier ventana sin fallo) discrimina con W = 8.
