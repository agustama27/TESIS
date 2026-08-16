# Propuesta de actualización del Tema 28
## Handoff para revisión por agente con acceso de escritura al Vault

> **AUDITORÍA DEL VAULT (2026-08-16, mentor)**: revisada contra [[../../00-Sistema/ESTADO-ACTUAL|ESTADO-ACTUAL]], [[../../00-Sistema/Decisiones|Decisiones]] (D-004 preliminar), Bitácora y reglas de la universidad. **Veredicto: ACEPTADA como formulación de trabajo de la familia 28, condicionada a PoC** — según el criterio del propio documento (§35). Consistente con el recorte de alcance y el hueco refinado ya registrados en [[Tema-28-Evaluacion-Frameworks-BCI]]. Aportes nuevos aceptados: 3 RQs con resultados negativos válidos, capa IA como hipótesis con baseline de reglas obligatorio, sección de supuestos/validez, fault models acotados, dataset BNCI2014_001 + CSP/LDA, escalera de 4 PoCs. Verificado previamente: LSL (PMC12434378) y arXiv 2404.06203. ⚠️ Pendiente de verificar (día del PoC): MNE-LSL PlayerLSL, BNCI2014_001 vía MOABB. El [[Tema-28-Evaluacion-Frameworks-BCI|Tema-28]] NO se reescribe hasta que el PoC pase (§35, pasos 8-9). El Word ya generado sigue siendo válido para la presentación de idea.

> **Estado de este documento:** propuesta de revisión, **no actualización definitiva**.  
> **Objetivo:** documentar con rigor los cambios conceptuales, metodológicos y de alcance discutidos para que otro agente pueda contrastarlos contra el Vault completo, verificar consistencia con las reglas del TFG y decidir si corresponde modificar `30-TFG/Seleccion-Tema/Tema-28-Evaluacion-Frameworks-BCI.md`.  
> **Fecha de elaboración:** 2026-08-16.  
> **Principio rector:** no actualizar el Tema 28 por inercia. Primero auditar si la nueva formulación resuelve las debilidades detectadas y si mantiene una contribución clara de Ingeniería de Software.

---

# 1. Resumen ejecutivo

La formulación original del Tema 28 evolucionó desde una **comparación arquitectónica de frameworks BCI open source** hacia una propuesta más acotada y defendible centrada en **reliability engineering de pipelines BCI en tiempo real**.

La revisión propuesta parte de una corrección importante:

> **La tesis no debería tener como pregunta principal “qué framework BCI es mejor”.**

Tampoco debería basarse en el supuesto de que un determinado fallo de infraestructura necesariamente reduce la accuracy del decoder, ni en el supuesto de que una capa de IA es automáticamente útil por detectar fallos que el propio sistema ya conoce de manera explícita.

La nueva formulación sugerida es:

> **Estudiar empíricamente cómo fallos controlados en la capa de streaming de señales EEG se propagan hacia propiedades técnicas y funcionales de un pipeline BCI, identificar posibles discrepancias entre el estado observable de la infraestructura y el desempeño del decoder, y evaluar si una capa de detección basada en telemetría multivariable aporta valor frente a mecanismos convencionales de alerta.**

En esta formulación:

- el **objeto de estudio** es el pipeline BCI como sistema de software;
- el **testbed** es un instrumento experimental;
- la **finalidad del trabajo** es responder preguntas de investigación;
- la **capa de IA** es una hipótesis a evaluar, no un requisito decorativo;
- los **frameworks** pasan a ser implementaciones o contextos de validación, no el centro de la tesis;
- el estudio debe poder producir resultados válidos incluso si:
  - ciertos fallos no afectan la clasificación;
  - no aparecen `silent failures`;
  - un detector basado en reglas rinde igual o mejor que la capa de IA.

Esto favorece clasificar el TFG como **Trabajo de Investigación**, aunque la investigación requiera construir un artefacto de software considerable para ejecutar el experimento.

---

# 2. Problema detectado en la versión actual del Tema 28

El archivo actual contiene dos formulaciones parcialmente incompatibles.

La parte inicial todavía describe un trabajo orientado a:

- evaluar muchos frameworks;
- aplicar ISO/IEC 25010;
- medir developer experience;
- comparar latencia, throughput y jitter;
- implementar una misma BCI en varios frameworks;
- producir una guía de decisión;
- eventualmente realizar stress-test a escala intracortical.

Más adelante, el propio documento ya reconoce que ese alcance es demasiado grande y propone un recorte hacia:

- un banco de experimentación;
- uno o pocos pipelines;
- fault injection;
- observabilidad;
- medición del impacto sobre el decoder.

La actualización debería eliminar esa ambigüedad. No conviene que el archivo siga comunicando simultáneamente:

1. “esta tesis compara frameworks y produce un ranking”; y
2. “la unidad de análisis es el pipeline y el objetivo es estudiar resiliencia”.

La recomendación de este documento es adoptar explícitamente la segunda dirección.

---

# 3. Cambio de identidad conceptual

## 3.1 Formulación anterior

> Evaluación arquitectónica comparativa de frameworks BCI open source.

Esta formulación favorece preguntas del tipo:

- ¿qué framework tiene mejor calidad?;
- ¿cuál tiene menor latencia?;
- ¿cuál es más mantenible?;
- ¿cuál ofrece mejor developer experience?;
- ¿qué framework conviene elegir?

El principal riesgo es que el trabajo termine siendo una **comparativa de herramientas** extensa, difícil de controlar en cuatro meses y con una contribución de investigación poco nítida.

## 3.2 Formulación propuesta

Nombre conceptual interno:

> **BCI Reliability Engineering**

Título de trabajo recomendado:

> **Evaluación de resiliencia de pipelines BCI en tiempo real mediante inyección de fallos y observabilidad inteligente**

Alternativa más conservadora, si se quiere evitar “inteligente” hasta demostrar la necesidad de IA:

> **Evaluación de resiliencia de pipelines BCI en tiempo real mediante inyección de fallos y análisis de propagación hacia la decodificación**

La segunda es metodológicamente más segura para una aprobación inicial. La capa de IA puede mantenerse como tercera RQ o subestudio.

---

# 4. Tipo de TFG recomendado

La discusión actual sugiere que **Trabajo de Investigación** representa mejor la intención del proyecto.

Razón:

- el objetivo final no es construir una plataforma como producto;
- el testbed es el instrumento para ejecutar un experimento;
- el valor del trabajo está en producir evidencia que responda preguntas;
- la investigación sigue siendo válida aunque el artefacto nunca se convierta en una herramienta de uso general.

La existencia de arquitectura, componentes, código, automatización y un banco de pruebas **no convierte automáticamente el TFG en Prototipado Tecnológico**.

El testbed puede ser un artefacto metodológico importante dentro de un Trabajo de Investigación.

**Recomendación:** no modificar la clasificación definitiva sin contrastarla con las normas exactas de la universidad y con el tutor, pero internamente considerar “Trabajo de Investigación” como la opción preferente.

---

# 5. Pregunta de investigación central propuesta

Una formulación integradora podría ser:

> **¿Cómo se propagan fallos controlados en el streaming de señales EEG hacia las propiedades operativas y el desempeño funcional de un pipeline BCI, y en qué medida la telemetría del sistema permite detectar o anticipar esa degradación?**

Ventajas:

- no presupone que todo fallo afecta el decoder;
- no presupone que existen `silent failures`;
- no presupone que una capa de IA supera a una solución tradicional;
- permite resultados negativos o nulos;
- conecta software de tiempo real, observabilidad, dependability y BCI;
- mantiene la tesis en Ingeniería de Software.

---

# 6. Preguntas de investigación recomendadas

## RQ1 — Propagación del fallo

> **¿Cómo afectan distintos tipos y severidades de fallos controlados del streaming a la integridad de los datos, disponibilidad, latencia y desempeño de decodificación de un pipeline BCI?**

### Por qué es válida

No pregunta simplemente “¿baja la accuracy?”.

Distingue múltiples dimensiones:

- integridad;
- temporalidad;
- disponibilidad;
- desempeño funcional.

Esto es importante porque una falla puede:

- aumentar la latencia sin reducir accuracy;
- causar pérdida de datos sin detener el proceso;
- producir una desconexión recuperable;
- afectar la clasificación solo después de determinado nivel;
- ser completamente absorbida por mecanismos de buffering o corrección.

La ausencia de degradación funcional bajo ciertas condiciones también sería un resultado válido.

---

## RQ2 — Discrepancia entre infraestructura y función

> **¿Existe una discrepancia entre el estado observable de la infraestructura y el desempeño funcional del decoder bajo determinadas condiciones de fallo?**

Esta pregunta reemplaza una formulación demasiado afirmativa como:

> “¿Qué fallos silenciosos existen?”

La nueva RQ no presupone que los `silent failures` existan.

### Posibles resultados válidos

Resultado A:

> Se identifican zonas donde el pipeline se mantiene conectado y operativo, pero la calidad funcional cae significativamente.

Resultado B:

> Los mecanismos de infraestructura detectan o compensan adecuadamente las condiciones antes de observar degradación funcional relevante.

Ambos resultados responden la RQ.

### Definiciones que deben fijarse antes del experimento

**Operacionalidad**, por ejemplo:

- proceso activo;
- stream conectado;
- no se produce excepción;
- continúan llegando muestras;
- se siguen emitiendo predicciones.

**Degradación funcional**, por ejemplo:

- caída estadísticamente significativa respecto del baseline;
- o caída superior a un umbral predefinido y justificado.

No fijar el umbral arbitrariamente después de ver resultados.

---

## RQ3 — Valor de una capa de detección inteligente

> **¿Puede un modelo basado en telemetría multivariable detectar o anticipar degradación funcional con mejor desempeño que un detector convencional basado en umbrales?**

Esta RQ es preferible a:

> “¿Puede una IA detectar jitter, sample loss o desconexiones?”

porque esa formulación puede resultar trivial.

Si el Fault Injector sabe que introdujo 10% de pérdida y la telemetría calcula directamente `sample_loss_rate`, un `if` puede identificar la condición sin necesidad de ML.

La IA solo está justificada si resuelve un problema más complejo:

> inferir el **estado funcional o riesgo de degradación** a partir de múltiples señales de telemetría.

### Baseline obligatorio

El modelo de IA debe compararse contra una solución convencional.

Ejemplo:

```python
if sample_loss > X:
    alert()

if jitter > Y:
    alert()

if latency > Z:
    alert()
```

Sin baseline, la afirmación de que IA aporta valor sería metodológicamente débil.

### Resultado negativo permitido

Si:

> IA ≈ reglas

o:

> reglas > IA

la conclusión sigue siendo científicamente válida:

> no se justifica introducir complejidad de ML para este problema bajo las condiciones experimentales estudiadas.

Este punto es importante para evitar sesgo de confirmación.

---

# 7. Supuestos que NO deben darse por ciertos

La nueva versión del Tema 28 debería contener una sección explícita de supuestos y amenazas a la validez.

## Supuesto A — “Más jitter/delay implica menor accuracy”

**No asumir.**

Una infraestructura de streaming puede:

- compensar jitter;
- bufferizar;
- corregir timestamps;
- recuperarse de desconexiones;
- mantener intacto el input final del decoder a costa de mayor latencia.

Por lo tanto:

> una degradación temporal puede no convertirse en degradación de clasificación.

La tesis debe medirlo, no asumirlo.

---

## Supuesto B — “Si el stream está conectado, la BCI funciona correctamente”

**No asumir.**

Esta es precisamente una hipótesis interesante a investigar.

El pipeline puede:

- seguir recibiendo datos;
- seguir ejecutando inferencias;
- no lanzar errores;

y aun así:

- operar con ventanas incompletas;
- recibir muestras temporalmente degradadas;
- producir decisiones poco confiables.

Pero la existencia real de esta discrepancia debe demostrarse experimentalmente.

---

## Supuesto C — “Los fallos inyectados representan exactamente fallos reales de hardware”

**Incorrecto si se formula de forma absoluta.**

El estudio será **Software-in-the-Loop**.

La tesis reproduce condiciones controladas del subsistema software. No reproduce necesariamente:

- electrodos;
- amplificadores;
- USB/Bluetooth físico;
- interferencia electromagnética;
- movimiento de electrodos;
- comportamiento humano en closed-loop;
- cambios fisiológicos.

La formulación correcta debe hablar de:

> **fault models experimentales del pipeline de streaming**

y no de “simulación completa de fallos de una BCI clínica”.

---

## Supuesto D — “El replay equivale a una BCI online real”

**Solo parcialmente.**

El replay permite evaluar comportamiento temporal reproducible del software.

No reproduce:

- adaptación usuario-decoder;
- feedback cerrado;
- comportamiento humano;
- adquisición física.

Conclusión permitida:

> comportamiento del pipeline de software bajo condiciones Software-in-the-Loop.

Conclusión no permitida:

> resiliencia total de una BCI clínica real.

---

## Supuesto E — “Accuracy representa por sí sola el correcto funcionamiento”

**Incorrecto.**

Una BCI interactiva depende también de:

- latencia;
- disponibilidad;
- estabilidad temporal;
- frecuencia de decisión;
- falsas activaciones;
- recuperación.

Por lo tanto la variable funcional no debe ser solo accuracy.

---

## Supuesto F — “LSL no fue probado frente a fallos”

**Incorrecto.**

La literatura actual de LSL documenta mecanismos de:

- reconexión;
- corrección temporal;
- buffers;
- compensación de jitter;
- stress testing con desconexiones/reconexiones.

El hueco no debe formularse como:

> “nadie probó resiliencia en LSL”.

La contribución potencial debe buscarse en:

> **propagación cuantitativa end-to-end desde una perturbación del streaming hasta el comportamiento funcional del pipeline BCI**, especialmente bajo un protocolo externo y reproducible.

---

## Supuesto G — “Una capa de IA es necesariamente útil”

**No asumir.**

La IA debe competir contra:

- thresholds;
- reglas;
- detectores estadísticos simples.

Si no aporta:

- mejor precisión;
- menos falsas alarmas;
- mayor anticipación;
- robustez frente a combinaciones de señales;

no hay justificación para conservarla.

---

# 8. Datos recomendados

## Dataset base

**BNCI2014_001 / BCI Competition IV Dataset 2a**

Características relevantes:

- 9 sujetos;
- 2 sesiones por sujeto;
- 22 canales EEG;
- 3 canales EOG;
- 250 Hz;
- motor imagery;
- cuatro clases: mano izquierda, mano derecha, pies, lengua;
- integración disponible mediante MOABB.

Para el PoC:

> limitar inicialmente a **mano izquierda vs. mano derecha**.

### Razones de selección

- dataset público;
- benchmark clásico;
- ground truth disponible;
- tamaño manejable;
- carga estandarizada con MOABB;
- permite concentrarse en software en lugar de construir un pipeline de ingestión propio.

### Advertencia

La selección definitiva del dataset debe registrarse como decisión metodológica y verificarse formalmente antes de redactar la versión final de la propuesta.

---

# 9. Decoder de referencia

Se recomienda un baseline convencional.

Ejemplo:

```text
EEG
 ↓
preprocesamiento
 ↓
CSP
 ↓
LDA
 ↓
izquierda / derecha
```

El modelo no es la contribución.

Su función es servir como **sensor funcional** del sistema:

> medir si una perturbación de infraestructura termina afectando una decisión BCI.

### Métrica recomendada

- balanced accuracy como principal;
- accuracy como complemento;
- probabilidades/confidence si el modelo las ofrece y son útiles para RQ3.

### Riesgo metodológico

No cambiar el decoder entre condiciones.

La comparación debe controlar:

- mismos sujetos;
- misma señal;
- mismo modelo;
- mismo preprocesamiento;
- misma configuración;

y variar únicamente la condición de fallo.

---

# 10. Arquitectura experimental propuesta

```text
┌─────────────────────┐
│ Dataset EEG público │
└─────────┬───────────┘
          ↓
┌─────────────────────┐
│ Replay Service      │
│ MNE / MNE-LSL       │
└─────────┬───────────┘
          ↓
┌─────────────────────┐
│ Fault Injector      │
└─────────┬───────────┘
          ↓
┌─────────────────────┐
│ BCI Pipeline        │
│ preprocess + model  │
└─────────┬───────────┘
          ↓
┌─────────────────────┐
│ Telemetry Collector │
└─────────┬───────────┘
          ↓
┌─────────────────────┐
│ Health Detector     │
│ rules / ML          │
└─────────┬───────────┘
          ↓
┌─────────────────────┐
│ Experiment Runner   │
│ + results           │
└─────────────────────┘
```

La arquitectura debe mantenerse modular para permitir:

- condiciones normales;
- condiciones con fallo;
- detector tradicional;
- detector ML;
- eventualmente una segunda implementación BCI.

---

# 11. Fault models recomendados

El experimento debería trabajar con pocas familias de fallos bien definidas.

## Núcleo sugerido

### 1. Sample loss

Variantes:

- pérdida aleatoria;
- pérdida en ráfagas.

No asumir que ambos tienen el mismo impacto.

---

### 2. Jitter

Perturbación del tiempo de llegada.

Debe distinguirse de:

- error de timestamp;
- delay constante.

---

### 3. Delay / latency

Añadir retraso controlado.

Puede afectar timeliness sin alterar el contenido recibido.

---

### 4. Disconnect / reconnect

Interrumpir temporalmente el flujo y observar:

- pérdida;
- recuperación;
- reanudación;
- comportamiento del decoder.

---

## Extensiones no obligatorias

- clock skew;
- consumer slowdown;
- buffer pressure;
- reorder;
- corruption.

No incluirlas inicialmente si ponen en riesgo el alcance.

---

# 12. Severidad de los fallos

No fijar arbitrariamente desde ahora una matriz definitiva.

Se pueden usar valores preliminares para el PoC, por ejemplo:

| Falla | Valores exploratorios |
|---|---|
| sample loss | 1%, 5%, 10% |
| jitter | 10, 50, 100 ms |
| delay | 50, 100, 250 ms |
| disconnect | 0,5 s; 1 s; 3 s |

Los valores finales deben surgir de:

1. literatura;
2. comportamiento observado en el piloto;
3. límites prácticos del pipeline;
4. necesidad de evitar escenarios absurdos o no informativos.

---

# 13. Variables dependientes

No reducir el análisis a accuracy.

## Integridad

- muestras esperadas;
- muestras recibidas;
- gaps;
- pérdida total;
- pérdida en ráfagas.

## Temporalidad

- latencia;
- jitter;
- inter-arrival time;
- desviación temporal;
- tiempo de recuperación.

## Disponibilidad

- continuidad del stream;
- reconexiones;
- período sin datos;
- ventanas descartadas.

## Funcional

- balanced accuracy;
- accuracy;
- confidence;
- tasa de decisiones válidas;
- comportamiento inmediatamente posterior a una falla.

## Observabilidad

- alerta generada;
- falsos positivos;
- falsos negativos;
- detection delay.

---

# 14. Capa de IA reformulada

## Formulación que debe evitarse

> “Entrenar IA para reconocer qué fallo inyecté.”

Problema:

el sistema ya conoce el fallo y la telemetría puede revelar directamente ciertas anomalías.

Eso corre el riesgo de ser una demostración artificial.

## Formulación recomendada

La capa de IA debe estimar:

> **estado de salud o riesgo de degradación funcional del pipeline**

a partir de telemetría multivariable.

Ejemplo:

```text
Entrada:
- sample rate observado
- inter-arrival mean/std
- gaps
- latencia
- jitter
- buffer state
- prediction confidence
- otras variables justificadas

Salida:
HEALTHY
AT_RISK
DEGRADED
```

Alternativamente:

> probabilidad de que el desempeño funcional caiga por debajo de un umbral durante una ventana futura.

Esta formulación sería más ambiciosa; no adoptarla sin PoC.

---

# 15. Baselines de detección

La capa ML debe compararse como mínimo contra:

## Baseline 1 — reglas

```text
if sample_loss > X → alert
if jitter > Y → alert
if latency > Z → alert
```

## Baseline 2 — estadístico simple

Opcional:

- z-score;
- moving average;
- EWMA;
- control chart.

## Modelo ML

Comenzar con opciones simples:

- Logistic Regression;
- Random Forest;
- Gradient Boosting.

No usar deep learning o LLM sin evidencia de necesidad.

---

# 16. Diseño de labels para la capa de detección

Evitar usar como target:

```text
fault_type
```

si el objetivo real es estimar salud funcional.

Mejor target:

```text
functional_state
```

Ejemplo:

```text
HEALTHY:
decoder dentro del rango basal

AT_RISK:
telemetría alterada pero función todavía estable

DEGRADED:
desempeño funcional cruza umbral
```

### Problema metodológico crítico

El target no debe construirse usando exactamente las mismas variables que luego el modelo recibe de forma trivial.

Ejemplo a evitar:

```text
label = DEGRADED if sample_loss > 5%
```

y después usar `sample_loss` como feature.

Eso crea una tarea artificial.

La etiqueta debe estar anclada principalmente en:

> consecuencia funcional medida.

---

# 17. Prevención de data leakage

La capa de IA puede quedar metodológicamente invalidada si se mezclan ventanas casi idénticas entre train y test.

Debe decidirse un split robusto.

Opciones:

- leave-one-subject-out;
- train en ciertos sujetos y test en sujetos nunca vistos;
- separar ejecuciones completas;
- separar severidades;
- separar escenarios.

Una opción especialmente interesante:

> entrenar con ciertas severidades y comprobar generalización a intensidades no vistas.

Esto debe diseñarse antes de entrenar el modelo.

---

# 18. Diseño experimental conceptual

Para cada sujeto:

1. generar condición normal;
2. ejecutar baseline;
3. guardar telemetría y output funcional;
4. introducir una única familia de fallo;
5. variar severidad;
6. repetir con seeds controladas;
7. almacenar resultados;
8. analizar curvas de degradación;
9. identificar si aparece discrepancia infraestructura/función;
10. entrenar y evaluar detectores en datos separados.

Ejemplo conceptual:

```text
9 sujetos
× 4 fallos
× 3 severidades
× N repeticiones
```

El N definitivo requiere:

- estimación de varianza;
- piloto;
- diseño estadístico.

---

# 19. Comparaciones que realmente importan

La tesis debería priorizar:

## Comparación A

```text
Normal
vs.
Fault
```

Responde RQ1.

## Comparación B

```text
Infrastructure health metrics
vs.
Functional decoder performance
```

Responde RQ2.

## Comparación C

```text
Rule-based detector
vs.
ML-based detector
```

Responde RQ3.

Estas tres comparaciones forman una narrativa mucho más coherente que:

```text
Framework A
vs.
Framework B
vs.
Framework C
...
```

---

# 20. Rol de los frameworks

Los frameworks no desaparecen.

Cambian de rol.

## Antes

> objeto principal de comparación.

## Ahora

> implementaciones o ambientes donde validar el protocolo.

### Recomendación

Comenzar con:

- MNE;
- MOABB;
- MNE-LSL / LSL;
- scikit-learn;
- código propio.

Después del PoC puede incorporarse:

- BciPy;
- MEDUSA;
- otro framework suficientemente activo.

Pero solo si aporta **validez externa**.

No comprometer dos o más frameworks hasta comprobar que:

- instalan;
- permiten reproducir el mismo caso;
- soportan el protocolo;
- no consumen desproporcionadamente el tiempo del TFG.

---

# 21. Qué pasa si solo se usa un pipeline

La tesis sigue siendo viable.

Debe evitarse una afirmación universal como:

> “los pipelines BCI se comportan así”.

La conclusión sería:

> “en el pipeline y condiciones estudiadas...”.

Una segunda implementación fortalece la generalización, pero no es necesariamente imprescindible.

La contribución primaria puede ser:

> caracterización empírica profunda de propagación de fallos en una arquitectura reproducible.

---

# 22. PoC recomendado antes del cierre definitivo del tema

## PoC 1 — clasificación offline

```text
BNCI2014_001
→ sujeto
→ izquierda/derecha
→ CSP + LDA
→ balanced accuracy
```

Objetivo:

- validar carga de datos;
- etiquetas;
- decoder.

---

## PoC 2 — replay

```text
EEG
→ MNE-LSL PlayerLSL
→ receptor
→ pipeline
→ output
```

Objetivo:

- validar la cadena Software-in-the-Loop.

---

## PoC 3 — primer fallo

```text
mismo replay
→ sample loss o jitter
→ mismo decoder
→ telemetría
→ comparación funcional
```

Objetivo:

demostrar:

```text
datos reales
→ streaming reproducible
→ perturbación controlada
→ consecuencia medible
```

---

## PoC 4 — observabilidad

Implementar dos detectores simples:

- reglas;
- modelo básico.

No para producir resultados finales, sino para comprobar que RQ3 es técnicamente operacionalizable.

---

# 23. Criterio de cierre del tema

No seguir agregando tópicos.

El Tema 28 debería considerarse técnicamente viable si:

- el dataset se carga;
- el decoder funciona;
- el replay funciona;
- se puede introducir al menos una perturbación;
- existe telemetría suficiente para cuantificarla;
- puede medirse una consecuencia técnica o funcional.

No se requiere demostrar en el PoC que:

- existe silent failure;
- IA supera reglas;
- accuracy necesariamente cae.

Esas son preguntas de la tesis.

---

# 24. Por qué esto sí es una tesis y no “un ETL”

El testbed requiere software, pero el argumento académico no debe basarse en “tiene muchos componentes”.

El valor está en:

1. definición de un problema de dependability;
2. construcción de fault models;
3. diseño experimental;
4. instrumentación;
5. observación de propagación end-to-end;
6. operacionalización de métricas;
7. comparación entre métodos de detección;
8. análisis estadístico;
9. evaluación de amenazas a la validez;
10. producción de conocimiento empírico reproducible.

El software es el instrumento para obtener evidencia.

---

# 25. Contribuciones esperadas

La tesis podría declarar tres tipos de contribución.

## Contribución metodológica

Un protocolo reproducible para introducir y medir fallos en un pipeline BCI Software-in-the-Loop.

## Contribución empírica

Curvas y resultados que caractericen la relación:

```text
fault condition
→ infrastructure impact
→ functional impact
```

## Contribución de detección

Evaluación comparativa de:

```text
reglas
vs.
modelo basado en telemetría
```

para detectar o anticipar degradación funcional.

---

# 26. Qué NO debe prometer la tesis

Evitar afirmaciones como:

- “voy a demostrar que LSL no es confiable”;
- “voy a demostrar que la IA mejora la resiliencia”;
- “voy a descubrir silent failures”;
- “voy a demostrar que estos frameworks no sirven para implantes”;
- “voy a determinar cuál framework BCI es el mejor”;
- “voy a modelar fallos reales de dispositivos clínicos”;
- “voy a validar seguridad clínica”.

La investigación debe estar diseñada para aceptar resultados contrarios.

---

# 27. Qué hacer con el contenido Neuralink / intracortical

Recomendación:

**demoverlo de núcleo a motivación o trabajo futuro.**

Puede mantenerse como conexión de carrera:

- neurotech;
- sistemas de tiempo real;
- reliability;
- neural data infrastructure.

Pero no debe condicionar el experimento.

Razones:

- cambia la escala de datos;
- introduce otra modalidad;
- puede crear un benchmark injusto;
- amenaza el alcance;
- no es necesario para justificar la contribución.

---

# 28. Qué hacer con ISO/IEC 25010

Recomendación:

**no usar el modelo completo como eje experimental.**

Puede utilizarse para:

- vocabulario;
- justificar atributos;
- conectar con Ingeniería de Software.

Pero no evaluar:

- mantenibilidad;
- portabilidad;
- usability;
- security;
- compatibility;
- etc.

de múltiples frameworks salvo que el tutor lo exija.

El núcleo experimental está más cerca de:

- reliability;
- performance efficiency;
- fault tolerance;
- recoverability;
- observability.

---

# 29. Qué hacer con Developer Experience

Mover a:

> fuera de alcance / trabajo futuro.

No medir:

- líneas de código;
- tiempo de instalación;
- experiencia subjetiva;

como dimensión principal.

No aporta a las RQ nuevas y abre otro estudio distinto.

---

# 30. Qué hacer con “comparar frameworks”

Reemplazar el objetivo:

> “determinar cuál es mejor”

por:

> “evaluar si el comportamiento observado se reproduce en más de una implementación”.

Eso convierte al segundo framework en:

> mecanismo de validez externa,

no en:

> competidor de ranking.

---

# 31. Marco de validez

La nueva versión debería mencionar al menos:

## Validez interna

¿La degradación observada fue realmente causada por el fault injection?

Controles:

- misma señal;
- mismo modelo;
- misma máquina;
- seeds;
- configuración fija;
- orden aleatorizado si corresponde.

## Validez externa

¿Se generaliza a:

- otros sujetos?;
- otros pipelines?;
- otros paradigmas BCI?;
- hardware real?

Reconocer límites.

## Validez de constructo

¿Las métricas realmente representan:

- resiliencia?;
- degradación?;
- salud?;
- fallos silenciosos?

Definir operacionalmente.

## Validez de conclusión

¿La cantidad de ejecuciones permite distinguir ruido de efecto real?

Requiere estadística adecuada.

---

# 32. Posibles resultados y valor científico

## Escenario 1

Los fallos degradan rápidamente el decoder.

Valor:

- caracteriza sensibilidad funcional.

## Escenario 2

La infraestructura absorbe fallos sin afectar accuracy.

Valor:

- evidencia robustez.

## Escenario 3

El sistema se mantiene operativo pero el decoder se degrada.

Valor:

- evidencia `silent failure`.

## Escenario 4

Todas las degradaciones visibles son detectadas por thresholds.

Valor:

- IA innecesaria.

## Escenario 5

ML anticipa combinaciones que thresholds no detectan.

Valor:

- evidencia a favor de observabilidad multivariable.

La tesis debe ser publicable conceptualmente en cualquiera de estos escenarios.

---

# 33. Formulación breve para el tutor

> “El trabajo propone estudiar cómo fallos de la capa de streaming de una BCI se propagan hacia el comportamiento funcional del decoder. Para hacerlo se utilizará un dataset EEG público y etiquetado, que se reproducirá como stream en tiempo real mediante un entorno Software-in-the-Loop. Se implementará un banco experimental capaz de introducir fallos controlados, registrar telemetría y medir tanto propiedades técnicas como desempeño de clasificación. El estudio buscará determinar si existen condiciones donde la infraestructura parece operar normalmente pero la calidad funcional se degrada y, como tercera pregunta, evaluará si un detector basado en telemetría multivariable aporta ventajas frente a mecanismos convencionales por umbrales. El software construido es el instrumento experimental; la finalidad es responder esas preguntas de investigación.”

---

# 34. Cambios concretos sugeridos en `Tema-28-Evaluacion-Frameworks-BCI.md`

El agente que revise este documento debería considerar:

### Reemplazar

- título actual;
- “la idea en palabras simples”;
- pregunta principal;
- justificación;
- explicación del tema;
- plan experimental;
- lista de riesgos.

### Reescribir

- rol de los frameworks;
- rol de ISO 25010;
- rol de la capa IA;
- definición de gap;
- contribución esperada.

### Mover a antecedentes / futuro

- Neuralink / escala intracortical;
- SNN;
- cifrado;
- neurorights;
- developer experience;
- ranking de muchos frameworks.

### Conservar

- motivación de Ingeniería de Software aplicada a BCI;
- uso de software open source;
- replay sin hardware;
- reproducibilidad;
- fault injection;
- observabilidad;
- medición de decoder;
- reconocimiento ya presente de que el gap no puede formularse como “nadie probó LSL”.

---

# 35. Recomendación final al agente del Vault

No actualizar el archivo basándose únicamente en que esta formulación “suena mejor”.

Antes de hacer cambios definitivos:

1. contrastar con `ESTADO-ACTUAL.md`;
2. revisar `Decisiones.md`;
3. revisar `Bitacora.md`;
4. contrastar con restricciones universitarias;
5. verificar que Trabajo de Investigación sea consistente;
6. revisar literatura primaria sobre:
   - LSL reliability;
   - fault injection / stream processing;
   - BCI real-time software;
   - missing EEG data;
   - MNE-LSL replay;
7. verificar dataset y pipeline;
8. ejecutar PoC mínimo;
9. decidir recién entonces si se reemplaza la identidad anterior del Tema 28.

La actualización correcta no debería afirmar:

> “el Tema 28 definitivo es este”.

Debería reflejar:

> “esta es actualmente la formulación metodológicamente más sólida de la familia 28, condicionada a PoC y verificación formal”.

---

# 36. Síntesis para decisión

La familia Tema 28 sigue siendo viable, pero su versión más defendible no es una comparación de frameworks.

La formulación recomendada es un estudio de:

> **propagación de fallos + observabilidad + impacto funcional + comparación de mecanismos de detección**

aplicado a un pipeline BCI Software-in-the-Loop.

La tesis sería fuerte si puede demostrar que:

- las RQ no presuponen el resultado;
- el experimento controla variables;
- los fault models están justificados;
- el replay se trata como una aproximación Software-in-the-Loop, no como un sustituto completo de hardware;
- la IA compite contra un baseline trivial;
- un resultado negativo sigue siendo una conclusión válida;
- el alcance se mantiene suficientemente acotado para cuatro meses.

Ese es el criterio recomendado para decidir si el `Tema-28-Evaluacion-Frameworks-BCI.md` debe ser actualizado.
