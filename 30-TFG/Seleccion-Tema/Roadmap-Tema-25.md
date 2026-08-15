# Roadmap del Tema 25 — de la decisión al TFG entregado

> 2026-08-14 · Plan operativo para el caso de elegir el [[Tema-25-Decodificadores-SNN-Neuromorficos|Tema 25]].
> **Doble uso**: (1) hoja de ruta de ejecución; (2) insumo directo del **diagrama de Gantt** que exige la Entrega 1 (Diseño Metodológico).

---

## Fase 0 — Antes de escribir una línea de código (esta semana)

Tres cosas, ninguna técnica:

1. **Conseguir la fecha del Módulo 0** de tu cursada (Profesor Director o calendario del SAM). Es tu deadline real.
2. **Reunión con el tutor**: llevar el Word de Definiciones Iniciales + la presentación de 8 láminas. Objetivo doble: aprobación del tema y **bloqueo de la línea temática** (Transformación Digital — irreversible, pero segura: los tres finalistas caen ahí).
3. **Registrar la decisión** en `00-Sistema/Decisiones.md` como D-00X, con fecha y alternativas descartadas.

> Nota: la línea temática se puede bloquear aunque el tema fino siga en ajuste. No esperes a tener todo cerrado para ese trámite.

---

## Fase 1 — La prueba de humo (semanas 1-2) ⚠️ EL GATE QUE DECIDE

**Objetivo**: NO es avanzar la tesis. Es responder una sola pregunta con evidencia y no con intuición: *¿me banco este paradigma?*

| Día | Tarea | Resultado esperado |
|---|---|---|
| 1 | `pip install snntorch` + Tutorial 1-3 de snnTorch (neurona de impulsos, cómo se simula el tiempo) | Entender qué es un "paso temporal" en una SNN |
| 2-3 | Tutorial 5 de snnTorch: entrenar una SNN con gradiente sustituto sobre un dataset de juguete (MNIST) | **Una SNN entrenada por vos, con su curva de accuracy** |
| 4-5 | Bajar el dataset más chico de FALCON desde DANDI; abrirlo en Python; graficar los spikes | Ver los datos reales con tus ojos |
| 6-8 | Clonar `fmi-basel/neural-decoding-RSNN`; leer README y paper asociado; intentar correr `tinyRSNN` | Que corra (aunque sea con dataset de ejemplo) |
| 9-10 | `pip install neurobench`; correr un ejemplo; entender el conteo de operaciones sinápticas | Saber medir "energía" |

**Gate de decisión al día 10** — sé brutalmente honesto:

- ✅ **Verde**: entrenaste una SNN, viste los datos, algo del repo de Basilea corrió. Aunque hayas peleado. → **El tema es tuyo, seguí.**
- 🟡 **Amarillo**: entrenaste la SNN de juguete pero el repo no corre y los datos te confunden. → Normal. Una semana más de margen; si a la 3ª semana seguís igual, pasá a rojo.
- 🔴 **Rojo**: no lograste entrenar ni la SNN de MNIST, o el paradigma te resulta hostil y te aburre. → **Cambiá al Tema 24 o al 19 sin culpa.** Perdiste 2 semanas y te ahorraste 4 meses de sufrimiento. Eso es una decisión inteligente, no un fracaso.

> Este gate vale más que cualquier deliberación adicional. Dos semanas de contacto real deciden mejor que dos meses de pensarlo.

---

## Fase 2 — Entrega 1 (Mes 1): marco teórico y diseño

- **Mapeo de huecos** (tarea obligatoria): leer qué comparaciones ya cubrieron NeuroBench y el repo de Basilea, y escribir en una página dónde queda TU hueco (p. ej. comparación sobre FALCON multi-sesión, o condiciones no barridas). Esto blinda la originalidad ante la CAE.
- Marco teórico: qué es una SNN, gradiente sustituto, decodificación intracortical, energía como atributo de calidad (green software engineering).
- Diseño experimental formal: datasets, modelos a comparar, métricas (precisión / operaciones sinápticas / latencia), protocolo de splits, semillas, test estadístico.
- **Diagrama de Gantt**: este roadmap, formateado.

**Entregable**: Entrega 1 del Seminario + notas del vault en `20-Investigacion/`.

## Fase 3 — Entrega 2 (Mes 2): baseline y reproducción

- Baseline convencional (GRU o Kalman) entrenado sobre el dataset elegido → precisión medida.
- `tinyRSNN` reproducido → verificar que tus números se parecen a los publicados.
- Harness de medición con NeuroBench funcionando: toda corrida escupe los 3 números automáticamente.

**Hito crítico**: si a fin del Mes 2 tenés baseline + una SNN corriendo + medición automática, **el 80% del riesgo del TFG ya pasó**.

## Fase 4 — Entrega 3 (Mes 3): el experimento propio

- Barrido de condiciones: arquitecturas SNN (tiny vs big), tamaños, ventanas temporales.
- Cada configuración × varias semillas → promedio y desvío.
- Test estadístico pareado entre paradigmas.
- Construcción de la tabla y las curvas del trade-off precisión-vs-operaciones.

## Fase 5 — Entrega 4 (Mes 4): cierre

- Análisis final, discusión de implicancias para implantes, limitaciones declaradas.
- Redacción completa, abstract, referencias APA.
- Código publicado en GitHub con README reproducible.

---

## Plan B (declarado desde el inicio)

Si las SNN no convergen bien sobre los datos:
- La comparación **entre las SNN publicadas** (tinyRSNN vs bigRSNN) contra el baseline convencional, con medición estandarizada, **ya es una tesis completa**.
- Si el dataset elegido da problemas: cambiar a otro de FALCON (hay cinco).
- Si el cómputo aprieta: reducir a una sola tarea y declararlo en alcance.

**Regla de oro**: cada fase deja un resultado defendible por sí solo. Nunca dependés de que la última corrida "salga bien".

---

## Cómo trabajamos juntos (el loop)

Por sesión: yo aporto búsqueda de literatura verificada, diseño experimental, revisión de código y redacción académica; vos aportás las decisiones, la ejecución y la autoría. Al cierre de cada sesión: `obsidian-scribe` vuelca hallazgos al vault, actualiza bitácora y commitea.

Agentes disponibles: `bci-explorer` (literatura), `bci-tutor` (conceptos que no entiendas), `obsidian-scribe` (notas y commits), `tfg-editor` (verificación de entregas contra el formato de la universidad).

---

## Tu primer sábado (3 horas, si querés empezar YA)

```bash
pip install snntorch torch matplotlib
```

1. Abrir el Tutorial 5 de snnTorch (https://snntorch.readthedocs.io/en/latest/tutorials/tutorial_5.html)
2. Copiar el notebook a Colab y correrlo entero sin modificar nada.
3. Cambiar UN parámetro (el umbral de disparo, o el número de pasos temporales) y ver qué pasa con la accuracy.
4. Escribir 5 líneas en `00-Sistema/Bitacora.md`: qué entendiste, qué no.

Si al final de esas 3 horas tenés curiosidad por seguir → tenés tu tesis.
