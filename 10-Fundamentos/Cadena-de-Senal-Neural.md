# La cadena de señal neural — de la neurona al cursor

> Nota de fundamentos · 2026-08-14 · el recorrido completo, etapa por etapa
> Complementa [[Como-Funciona-un-Implante-Intracortical]] (arquitectura y energía). Acá el foco es **qué le pasa a la señal** en cada paso.

## El mapa completo

```
DENTRO DE LA CABEZA                          │  AFUERA
                                             │
[1] Neurona dispara (spike)                  │
[2] Electrodo lo capta        ~10 µV-1 mV    │
[3] Amplificador              ×500-1000      │
[4] Filtro                    separa 2 señales│
[5] Digitalizador             20-30 kHz      │
[6] ⚠️ EXPLOSIÓN DE DATOS      ~200 Mbps      │
[7] Reducción a bordo         ÷ ~500         │
[8] Radio                     ~0,4 Mbps      │
                                             │  [9] Decodificador → intención
                                             │  [10] Acción (cursor, texto)
                                             │       ↓
                            ← ← ← ← ← ← ← ← ←│  el usuario VE el resultado
                              (lazo cerrado)
```

---

## Etapa 1 · La neurona y el spike

Una neurona "habla" disparando un **potencial de acción** (spike): un pulso eléctrico de aproximadamente **1-2 milisegundos** de duración. Es todo-o-nada: dispara o no dispara. La información no está en la intensidad de cada pulso, sino en **cuándo y con qué frecuencia** dispara.

Cuando pensás en mover la mano, miles de neuronas de tu corteza motora cambian su ritmo de disparo. **Ese patrón de ritmos es lo que se decodifica.**

## Etapa 2 · El electrodo: qué escucha realmente

Un electrodo clavado en la corteza no escucha *una* neurona: escucha **el murmullo eléctrico de su vecindario**.

- Las neuronas dentro de un radio de ~**100 micrómetros** producen spikes detectables, con amplitudes de **decenas a cientos de microvoltios**.
- Rango total del potencial de acción registrado extracelularmente: **10 µV a 1 mV**.

Para dimensionar: un microvoltio es **un millonésimo de voltio**. La pila de tu control remoto tiene 1,5 voltios — o sea, un millón y medio de veces más. **Estás midiendo susurros eléctricos.**

## Etapa 3 · Amplificación: hacer audible el susurro

Un amplificador de registro neural típico tiene **ganancia de 500 a 1000 veces**, y — el dato clave — un **piso de ruido de 2 a 7 microvoltios RMS**.

Pensá en lo que eso significa: si los spikes más chicos miden 10 µV y el ruido del propio amplificador es de 2 a 7 µV, **la calidad del amplificador determina qué neuronas podés escuchar y cuáles se pierden en el ruido**. Es como grabar un susurro en una habitación con ventilador: si el ventilador hace más ruido que el susurro, no hay software que lo recupere.

Costo: ~**10 microvatios por canal** y ~**0,04 mm² por canal** de área de silicio. Multiplicá por 1.024 canales y entendés por qué el chip es como es.

## Etapa 4 · Filtrado: hay DOS señales en el mismo cable

Este es un concepto que sorprende: el electrodo capta simultáneamente dos fuentes de información distintas, y se separan por frecuencia.

| Señal | Frecuencias | Amplitud | Qué es |
|---|---|---|---|
| **LFP** (potencial de campo local) | hasta **300 Hz** | hasta **3 mV** | El "rumor colectivo" de miles de neuronas — actividad de conjunto |
| **Spikes** (potenciales de acción) | **300 Hz a 10 kHz** | 10 µV a 1 mV | Los disparos individuales del vecindario |

Es como un estadio: el LFP es el murmullo general de la tribuna; los spikes son los gritos individuales de los que tenés cerca. **Los dos tienen información útil**, y muchos sistemas modernos usan ambos.

## Etapa 5 · Digitalización: por qué 20-30 kHz

Se muestrea a **20.000-30.000 muestras por segundo por canal**. ¿Por qué tan rápido?

Porque un spike dura 1-2 milisegundos, y si querés capturar su **forma** (no solo saber que ocurrió) necesitás varias muestras dentro de esos 2 ms. A 30 kHz tenés ~60 muestras por spike: suficiente para dibujar su perfil. A 1 kHz lo verías como un pico solitario sin forma.

## Etapa 6 · ⚠️ La explosión de datos

Acá está el problema central de todo el diseño. Hagamos la cuenta:

```
1.024 canales × 20.000 muestras/s × 10 bits = ~205.000.000 bits/s ≈ 200 Mbps
```

Doscientos megabits por segundo, generados **dentro de tu cabeza**, todo el tiempo. Y la radio de un implante a batería puede mandar del orden de **1 Mbps**.

**Sobran 200 veces los datos.** Todo lo que sigue existe para resolver eso.

## Etapa 7 · Reducción a bordo: el paso más inteligente

En vez de transmitir la forma completa de cada spike, el chip hace **detección por umbral** (*threshold crossing*): pone una línea, y cada vez que la señal la cruza hacia abajo, anota "acá hubo un spike".

Y después **agrupa por ventanas de tiempo**: cada 20 milisegundos cuenta cuántos spikes hubo en cada canal. Eso es todo lo que transmite.

Cuenta ilustrativa del ahorro:

```
1.024 canales × 50 ventanas/s × 8 bits = ~410.000 bits/s ≈ 0,4 Mbps
```

**De 200 Mbps a 0,4 Mbps: una reducción de ~500 veces.** Ahora sí entra en la radio.

> 💡 **El concepto clave**: se tira deliberadamente la forma del spike y se conserva solo el **ritmo de disparo**. ¿Por qué funciona? Porque la información motora está en el ritmo, no en la forma. Y notá algo importante: el sistema **no sabe qué neurona disparó** — solo que "en este electrodo hubo actividad". Eso se llama *actividad multi-unidad*, y alcanza. Separar cada neurona individual (*spike sorting*) es opcional y muchos sistemas modernos lo omiten.

## Etapa 8 · Transmisión

Los conteos por ventana salen hacia afuera. En sistemas académicos, por cable a través del pedestal. En sistemas inalámbricos, por radio de bajo consumo. ⚠️ *(El protocolo exacto del N1 no está verificado en fuente primaria — ver [[Como-Funciona-un-Implante-Intracortical]].)*

## Etapa 9 · El decodificador (AFUERA, hoy)

Acá corre el "traductor": recibe los conteos de spikes y produce la intención del usuario.

- **Clásico**: filtro de Kalman — matemática de los años 60, la misma familia que usa el GPS — que convierte la actividad en un vector de velocidad del cursor.
- **Moderno**: redes neuronales (RNN/GRU, Transformers) que mapean la actividad a fonemas, caracteres o movimientos.
- En BrainGate, las características neurales se computan **cada 20 ms** y se decodifican con un filtro de Kalman.

**Este es el eslabón donde vive el [[../30-TFG/Seleccion-Tema/Tema-25-Decodificadores-SNN-Neuromorficos|Tema 25]].**

## Etapa 10 · El lazo cerrado (lo que casi nadie explica)

Y acá está lo más lindo del sistema: **el usuario ve el resultado y corrige.**

El cursor se mueve → la persona lo ve → ajusta su intención → cambia su actividad neural → el decodificador responde. Es un **lazo de control cerrado**, como manejar un auto: no calculás el ángulo del volante, corregís continuamente mirando la ruta.

Consecuencia práctica enorme: **el usuario aprende a manejar el decodificador, y el decodificador se adapta al usuario.** Por eso un sistema mejora con las semanas de uso. Y por eso evaluar un decodificador *offline* (con datos grabados) no es lo mismo que evaluarlo *online* (con la persona en el lazo) — una limitación que hay que declarar en cualquier tesis que use datos públicos.

**El presupuesto de latencia**: para que se sienta natural, todo el recorrido — captar, procesar, transmitir, decodificar, dibujar — debe cerrarse en decenas de milisegundos. Si tarda mucho, el usuario "sobrecorrige" y el control se vuelve inestable, igual que un videojuego con lag.

---

## 🔑 El concepto que ordena todo: el embudo

```
205 Mbps  →  0,4 Mbps  →  2 números (velocidad x, y)
(crudo)      (conteos)     (la intención)
```

Cada etapa **tira información a propósito** y conserva solo lo que sirve para el objetivo. No es pérdida: es **compresión con criterio**. Toda la ingeniería de BCI consiste en decidir *qué tirar, dónde tirarlo y cuánto cuesta esa decisión* en energía, latencia y precisión.

Con ese marco, mirá dónde se paran los temas que evaluamos:

| Tema | Etapa de la cadena |
|---|---|
| 16 (descartado) — compresión de telemetría | Etapa 6-7: cómo achicar el caudal crudo |
| 19 — fidelidad brain-to-text | Etapa 9: qué tanto de la salida viene de la señal |
| 23 — compresión del decodificador | Etapa 9: achicar el traductor |
| **25 — redes de impulsos** | **Etapa 9: cambiar el paradigma del traductor para que quepa en la etapa 7** |

---

## Ejercicio para fijar el concepto

Respondé sin mirar (si podés, entendiste la cadena):

1. ¿Por qué se muestrea a 30 kHz y no a 1 kHz?
2. ¿Qué información se tira en la detección por umbral, y por qué no importa?
3. Si el amplificador tuviera un piso de ruido de 20 µV en vez de 5 µV, ¿qué pasaría?
4. ¿Por qué el sistema mejora después de semanas de uso?
5. ¿Por qué evaluar con datos grabados no es lo mismo que evaluar con el usuario en vivo?

## Fuentes

- Amplitudes y bandas: [Neural Signal Recording and Processing (Springer)](https://link.springer.com/chapter/10.1007/978-981-95-4145-4_4) · [Local Field Potential (ScienceDirect Topics)](https://www.sciencedirect.com/topics/medicine-and-dentistry/local-field-potential) · [Scholarpedia — LFP](http://www.scholarpedia.org/article/Local_field_potential)
- Muestreo y calidad de registro: [Improving data quality in neuronal population recordings (PMC5244825)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5244825/)
- Front-end y ruido: [Verification of a Rapidly Multiplexed Circuit for Scalable Action Potential Recording (PMC7454001)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7454001/)
- Decodificación cada 20 ms con filtro de Kalman: documentación de BrainGate (ver [[../20-Investigacion/Decodificacion-Brain-to-Text|nota de brain-to-text]])

⚠️ Las cuentas de las etapas 6 y 7 son **ilustrativas**, derivadas de los parámetros citados — no son especificaciones oficiales de ningún fabricante. Verificar contra fuente primaria antes de usarlas en el TFG.

## Enlaces

[[Como-Funciona-un-Implante-Intracortical]] · [[../20-Investigacion/Historia-Spiking-Neural-Networks|Historia de las SNN]] · [[../30-TFG/Seleccion-Tema/Tema-25-Decodificadores-SNN-Neuromorficos|Tema 25]]
