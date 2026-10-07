# Fundamentos del diseño estadístico y del muestreo — argumentos para la defensa

> 2026-09-26 · Justificación crítica del diseño de la campaña del Entregable 2: por qué se decidió así, qué alternativas se descartaron y qué flancos débiles hay que declarar antes de que los pregunten. Insumo para la Discusión del Módulo 3 (limitaciones, fortalezas) y para la defensa oral. Ver también [[Trabajo-Futuro]] y [[../00-Sistema/Decisiones|D-008]].

## El diseño en una línea

> **Actualizado 2026-09-28 (Entregable 2 v3).** La campaña definitiva es de 855 ejecuciones y tiene dos familias de fallo; lo de abajo que dice "2 corridas" o "234" es la primera etapa.

9 sujetos × 5 corridas × 19 condiciones (1 referencia + 6 tipos de fallo × 3 severidades) = 855 ejecuciones, en diseño secuencial: la primera etapa (234 ejecuciones, familia uniforme, 2 corridas) fue preespecificada; la familia estructurada se agregó después de ver su resultado nulo y se reporta como **exploratoria**. Cada corrida se reproduce con señal idéntica, mismo decodificador congelado y misma máquina; lo único que cambia es el inyector. Unidad estadística: el sujeto (mediana de sus 5 corridas; las tablas muestran la mediana de esas 9 medianas). Pruebas: Friedman por tipo de fallo → Wilcoxon apareado por severidad vs. referencia → corrección de Holm **dentro de cada tipo de fallo (3 comparaciones)** → tamaño de efecto *r* = z(p) / √n.

**Piso y techo con n = 9** (verificado en `stats.py`): el menor *p* exacto de Wilcoxon es 2/2⁹ ≈ 0,0039 (los 9 sujetos cambian en la misma dirección); con Holm × 3 da ≈ 0,012, y el *r* correspondiente ≈ 0,96. Por eso se repiten esos valores: son el máximo resultado posible con 9 sujetos.

## Las cuatro decisiones y su fundamento

1. **Medidas repetidas con comparación apareada (misma corrida con y sin fallo).** La variabilidad entre sujetos en BCI es enorme (en este dataset, sujeto 5 = 0,50 y sujeto 8 = 1,00 de *balanced accuracy*). Un diseño entre sujetos la confundiría con el efecto de la falla. Comparar cada sujeto consigo mismo cancela esa variabilidad. Tradición de la experimentación controlada en ingeniería de software (Wohlin et al., 2012) cuando el sujeto es la mayor fuente de ruido.
2. **El sujeto como unidad estadística, no el ensayo.** Hay ~5.600 decisiones del decodificador, pero no son independientes (mismo cerebro, mismo día, mismo casco). Tratarlas como independientes es pseudorreplicación: infla artificialmente el *n* y produce "significancias" espurias. Nueve observaciones por condición, honestas.
3. **Pruebas no paramétricas.** Con *n* = 9 no se puede verificar normalidad (supuesto del ANOVA), y la *balanced accuracy* sobre 24 ensayos toma valores discretos. Friedman = ANOVA de medidas repetidas sin ese supuesto; Wilcoxon = comparación apareada sin ese supuesto. Tres comparaciones por tipo de fallo → Holm dentro de cada tipo, para que la probabilidad de al menos un falso positivo (≈ 14 % sin corrección con 3 comparaciones al 5 %) vuelva al 5 %.
   - **Mediana y no promedio**: con 5 corridas, una corrida anómala arrastra el promedio (0,75 · 0,79 · 0,71 · 0,50 · 0,75 → promedio 0,70, mediana 0,75).
4. **Muestreo no probabilístico, intencional.** Los 9 sujetos son los que existen en el dataset de referencia del área; el pipeline es uno. Las conclusiones se formulan para ese pipeline y esas condiciones (declarado en Métodos); el aporte generalizable es el protocolo.

## Alternativas descartadas

- **Modelo mixto / jerárquico** (todos los ensayos, sujeto como efecto aleatorio). Mejor en principio: preserva la información sin pseudorreplicar. Descartado por tiempo y porque con 9 sujetos la varianza entre sujetos se estima de forma inestable. Métodos lo deja como alternativa futura. Respuesta al jurado: "es la extensión natural con más sujetos".
- **Pruebas de permutación** en lugar de Wilcoxon: potencia equivalente para este *n*, menos conocidas por un tribunal.
- **Sumar sujetos de otros datasets**: mezcla equipos y protocolos, confunde. Mejor 9 homogéneos.
- **Una corrida por sujeto**: duplicaría lo que entra en una noche de máquina, pero sin réplica intrasujeto no se distingue efecto de casualidad.

## Flancos débiles y la respuesta preparada

| Objeción | Cuánto de cierto | Respuesta |
|---|---|---|
| "Nueve sujetos es poco" | Cierto: Wilcoxon con *n* = 9 solo detecta efectos grandes (*r* ≳ 0,6) | Es el dataset de referencia (Tangermann, Lotte); el diseño apareado maximiza la potencia disponible; los "no significativos" se reportan con tamaño de efecto, no solo con *p* |
| "Dos corridas en vez de cinco" | Resuelto en la campaña definitiva (5 corridas, 855 ejecuciones) | Solo aplica a la primera etapa, que se declara como tal |
| "La familia estructurada se diseñó después de ver los resultados" | Cierto | Declarada como fase exploratoria de un diseño secuencial; severidades fijadas antes de ejecutarla; sus *p* no se presentan como confirmatorios |
| "¿Por qué tantos *p* = 0,012?" | — | Es el piso de Wilcoxon exacto con 9 sujetos y Holm × 3: los 9 cambiaron en la misma dirección |
| "Las severidades son arbitrarias" | Parcialmente | Ancladas a la escala del ensayo (4 s a 250 Hz) y fijadas antes de ver resultados; reemplazarlas por trazas reales es línea futura ([[Trabajo-Futuro]] n.º 5) |
| "Cinco desconexiones por corrida es una decisión tuya" | Cierto: tasa alta vs. laboratorio normal | Elegida para tener eventos suficientes por corrida para medir tiempo de recuperación; parámetro documentado y cambiable |
| "Efecto piso (s5) y techo (s8)" | Cierto | Reduce la sensibilidad de la prueba de desempeño; declararlo en Resultados; en Discusión, el efecto funcional se concentra en sujetos de desempeño medio |
| "El umbral se define con los mismos datos" | El más fino | El umbral sale de la referencia de cada sujeto (sin fallos); la **regla** se eligió mirando el piloto, que usa la corrida 6, excluida de la campaña. Esa es la razón de existir del piloto |
| "El banco es artificial" | Cierto y declarado | Software-in-the-Loop: lista explícita en Introducción de lo que no reproduce (electrodos, amplificadores, interferencia, adaptación de la persona) |

## Resumen para la defensa

"Elegí el diseño que maximiza la validez interna con los datos que existen, declaré cada límite antes de que me lo pregunten, y publico el protocolo para que se pueda repetir con más."

## Hallazgos que ya condicionan la interpretación (piloto, 2026-09-26)

- Infraestructura responde exacta a cada modelo de fallo; **LSL tarda ≈ 560 ms en reconectar** además del corte (intervalo máximo sin datos 1.563 ms para cortes de 1 s, 3.563 ms para 3 s).
- Desempeño funcional casi invariante en los tres sujetos del piloto → el resultado central es la **divergencia** infraestructura/decodificación (objetivo 4), no una curva de degradación.
- **El retraso se traslada uno a uno al retardo de decisión** (+50/+100/+250 ms): efecto funcional temporal, no de exactitud.
- Regla de umbral: percentil/MAD marcan 4-7 % de ventanas sanas por construcción; `min` (peor que cualquier ventana sin fallo) discrimina con W = 8.
- Control de paralelismo: 6 ejecuciones simultáneas alteran latencia y dispersión en 0,05-0,1 ms, cien veces menos que la severidad mínima inyectada.
