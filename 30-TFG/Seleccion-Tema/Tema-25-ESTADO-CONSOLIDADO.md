# Tema 25 — Estado consolidado

> **Esta es la única versión vigente.** Escrita el 2026-08-14 después de dos correcciones de rigor.
> Reemplaza cualquier formulación anterior. Si algo de otra nota la contradice, manda esta.
> Página con formato oficial: [[Tema-25-Decodificadores-SNN-Neuromorficos]] · Roadmap: [[Roadmap-Tema-25]]

---

## 1. Qué es, en una frase

**Comparar dos tipos de programas que traducen señales del cerebro — el convencional y uno que gasta mucha menos energía — sobre los mismos datos públicos, midiendo precisión y costo de cómputo, y producir la comparación que hoy no existe.**

## 2. La premisa (versión corregida y definitiva)

> Los decodificadores neuronales corren en dispositivos con **restricciones de energía**: el implante, un dispositivo vestible o un equipo portátil. Un usuario real no puede estar atado a una workstation. Las redes de impulsos prometen eficiencia sustancial. **Nadie hizo la comparación limpia entre paradigmas.** Esta tesis la hace.

**Lo que la premisa NO afirma** (y esto es deliberado):

- ❌ No afirma que la industria esté migrando los decodificadores hacia adentro del implante. **No hay evidencia pública de eso** — las empresas (Neuralink, Paradromics, Synchron, Precision) se diferencian en electrodos e invasividad, no en dónde corre el decodificador.
- ❌ No hace ninguna predicción sobre el futuro del campo.

**Lo que sí está establecido y sostiene el trabajo**:

- ✅ La transmisión de datos es el mayor consumidor de energía del implante (documentado).
- ✅ El reparto de cómputo adentro/afuera es un **compromiso de diseño abierto**, con dos caminos vigentes en la literatura.
- ✅ Dispositivos aprobados por FDA ya decodifican dentro del cuerpo (NeuroPace RNS, Medtronic Percept), pero **con algoritmos muy simples** por límite de recursos.
- ✅ Existe trabajo reciente (2024-2026) de redes de impulsos para decodificación, **pero cada uno con su dataset, su métrica y su protocolo** — resultados no comparables entre sí.

> **Por qué esta premisa es robusta**: el resultado sirve en los tres escenarios posibles — si el cómputo migra adentro (dice si el paradigma alcanza), si se mantiene el esquema híbrido actual (dice cuánto más se puede hacer adentro), o si el decodificador queda en un vestible externo (que también funciona a batería).

## 3. Pregunta de investigación

> ¿Pueden los decodificadores basados en redes de impulsos igualar la precisión de los decodificadores convencionales sobre señal intracortical pública, y con qué reducción de operaciones de cómputo lo logran? ¿En qué condiciones (tarea, cantidad de datos, arquitectura) resulta preferible cada paradigma?

## 4. La originalidad (analogía de las zapatillas)

Cinco marcas dicen "las nuestras son las más rápidas", pero cada una midió en su pista, con su corredor y su cronómetro. Todas tienen razón; ninguna es comparable.

**Mi aporte: organizo la carrera.** Misma pista (benchmark público), mismo cronómetro (herramienta de medición estandarizada), mismas reglas — y publico la tabla de posiciones. No invento una zapatilla: soy **el juez de la carrera que nadie organizó**. En ciencia eso se llama estudio comparativo o de consolidación, y es lo que un campo joven necesita.

## 5. Qué hago yo vs. qué ya existe

| Ya existe (lo uso) | Lo hago yo |
|---|---|
| Grabaciones públicas de actividad cerebral con el movimiento real sincronizado | El experimento comparativo |
| Los dos tipos de decodificadores (hay código público) | Ponerlos a competir en igualdad de condiciones |
| Herramientas de medición (NeuroBench) | La tabla, las curvas y su análisis |
| | La demostración visual |

## 6. Método

⚠️ **Definición crítica del baseline** (ver [[../../20-Investigacion/Decodificadores-Estado-del-Arte|Estado del arte de decodificadores]]): comparar solo contra un filtro de Kalman sería vencer a un decodificador de generación anterior — resultado sin valor. **El rival real es una red recurrente moderna (GRU/LSTM)**, que es el estado del arte vigente. Diseño correcto: **tres competidores** — lineal (Kalman/Wiener, como piso), recurrente moderna (el rival de verdad) y redes de impulsos.

1. Cargar sesiones de datasets públicos: matriz de spikes + trayectoria real del movimiento, sincronizadas.
2. Entrenar los tres decodificadores (lineal, recurrente moderno, redes de impulsos) con los mismos splits.
3. Medir en cada configuración: **precisión** de decodificación, **operaciones de cómputo** (proxy de energía), **latencia**.
4. Repetir con varias semillas; test estadístico pareado entre paradigmas.
5. Construir la frontera precisión-vs-cómputo.

**Herramientas**: Python · PyTorch · snnTorch/SpikingJelly · datasets FALCON / Neural Latents Benchmark · NeuroBench · Google Colab.

## 7. La demostración (para la defensa)

**Tres trayectorias animadas en una sola pantalla**, sobre la misma grabación cerebral:

1. El movimiento **real** que hizo el sujeto (la verdad).
2. El decodificado por la **red convencional**.
3. El decodificado por la **red de impulsos**.

Con **dos contadores de operaciones** sumando en vivo al costado. El tribunal ve la misma señal, dos traductores, cuál sigue mejor y a qué costo.

⚠️ **Limitación declarada desde el inicio**: es una **reconstrucción offline**, no control en lazo cerrado. El sujeto no está controlando nada en vivo; se reproduce una grabación. En control real el usuario ve y corrige, lo que puede compensar un decodificador mediocre. Declarar esta limitación es estándar en los trabajos que usan estos benchmarks.

## 8. Validación

- **¿Cómo se sabe si acertó?** Los datasets traen el movimiento real sincronizado — se compara lo decodificado contra la verdad.
- **Población**: ensayos/segmentos del conjunto de evaluación (MC_Maze: 2.869 ensayos; MC_RTT: 15 minutos continuos).
- **Protocolo**: splits oficiales del benchmark, varias semillas por condición, test estadístico pareado.
- **Energía**: estimada por conteo de operaciones — el método aceptado por la literatura, sin hardware especializado.

## 9. Encuadre institucional

- **Tipo**: Trabajo de Investigación
- **Línea temática**: Transformación Digital
- **Ingeniería de Software**: evaluación empírica de dos paradigmas de software para el mismo problema, con la energía como requisito no funcional cuantificado (green software engineering), benchmarking reproducible y publicación del código.

## 10. Por qué no hay resultado malo

- Si las redes de impulsos **igualan** precisión gastando mucho menos → evidencia de viabilidad para dispositivos con restricción energética.
- Si **pierden** precisión → primera cuantificación limpia del costo del paradigma en este dominio.

La tesis no depende de que un experimento "salga bien". Depende de medir bien.

## 11. Riesgos, sin maquillaje

| Riesgo | Mitigación |
|---|---|
| **Curva de aprendizaje** (~1 mes para ser productivo en el paradigma) | Prueba de humo de 2 semanas con gate de decisión antes de comprometerse |
| Justificación menos épica que la versión original | Es el costo de la honestidad; a cambio no tiene flanco atacable |
| Las redes de impulsos podrían no converger bien | Plan B: comparar las SNN ya publicadas contra el baseline con medición estandarizada — sigue siendo tesis |
| Cómputo limitado | Datasets de movimiento son livianos; Colab alcanza |
| Campo activo, podrían publicar algo similar | El mapeo de huecos del Mes 1 posiciona el aporte; una comparación unificada reproducible no caduca |

## 12. Historial de correcciones (para no repetirlas)

| Fecha | Qué se corrigió |
|---|---|
| 2026-08-14 | Specs del N1 (consumo, compresión, protocolo BLE) marcadas como **no verificadas en fuente primaria** — provienen de divulgación técnica |
| 2026-08-14 | **Premisa**: de "el futuro es decodificar todo adentro" a "el reparto es un compromiso abierto" — no hay evidencia de migración industrial |

**Regla operativa**: toda especificación de hardware o afirmación sobre tendencias de la industria se verifica contra fuente primaria antes de entrar al TFG.

## 13. Lo que falta decidir / verificar

- [ ] **Decisión del autor**: hacer la prueba de humo de 2 semanas ([[Roadmap-Tema-25]] Fase 1).
- [ ] Verificar cuáles datasets de FALCON son humanos y cuáles de primates.
- [ ] Elegir la tarea (cursor / dedos) — cambia cómo se ve la demo, no la factibilidad.
- [ ] Mapeo de huecos vs. NeuroBench y el repo de Basilea (Mes 1).
- [ ] Verificar en fuente primaria las specs de hardware que se vayan a citar.

---

## El guion de 60 segundos (versión definitiva)

> "Hay personas paralizadas con implantes que traducen su actividad cerebral en movimiento o texto. Ese programa traductor corre en dispositivos con muy poca energía disponible — un implante no puede calentarse porque daña el tejido, y un usuario real no quiere estar atado a una computadora de escritorio. Existe un tipo de inteligencia artificial que computa como el cerebro: en silencio, activándose solo cuando hace falta, y por eso gasta mucho menos. Ya hay trabajos que la probaron para esto, pero cada uno usó su dataset y su forma de medir, así que no se pueden comparar entre sí. Mi tesis los pone a competir en la misma pista con el mismo cronómetro, sobre grabaciones públicas de actividad cerebral real, y publica la comparación que falta: cuánta precisión se obtiene por unidad de cómputo con cada paradigma."
