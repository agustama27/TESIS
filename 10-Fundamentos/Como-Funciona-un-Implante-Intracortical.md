# Cómo funciona un implante intracortical (y por qué la energía manda)

> Nota de fundamentos · 2026-08-14 · base técnica para el [[../30-TFG/Seleccion-Tema/Tema-25-Decodificadores-SNN-Neuromorficos|Tema 25]]
> Todos los números verificados; fuentes al final.

## Los dos mundos que conviven hoy

### Mundo A — académico (BrainGate, Stanford): **cableado**

- Sensor: *array de Utah* — grilla de silicio de ~4×4 mm con ~100 micro-agujas, implantada en la corteza.
- Conexión: un **pedestal** — un conector metálico que atraviesa el cuero cabelludo y asoma en la cabeza. Del pedestal sale un cable a los amplificadores.
- El participante está **literalmente enchufado** durante cada sesión.
- Ventaja: energía y ancho de banda casi ilimitados (todo el procesamiento pesado ocurre afuera).
- Desventaja: cable permanente atravesando la piel = riesgo de infección; imposible de usar en la vida cotidiana.

### Mundo B — comercial (Neuralink): **inalámbrico y sellado**

- Sensor: 1.024 electrodos en 64 hilos flexibles, insertados por un robot.
- Todo el sistema (chip + batería + radio) queda **sellado dentro del cráneo**, sin cables al exterior.
- Batería recargable **por inducción** (como el cargador inalámbrico del celular), ~12 horas de autonomía.
- Transmite de forma inalámbrica a una computadora o teléfono. ⚠️ **Protocolo NO verificado en fuente primaria**: múltiples fuentes secundarias afirman Bluetooth Low Energy (BLE) con cifrado AES-256, pero no se encontró confirmación en documentación oficial de Neuralink ni en papers. **Alerta de calidad de fuente**: una de esas fuentes afirma ">100 Mbps por BLE", lo cual es imposible (BLE 5 con PHY 2M llega a ~2 Mbps), lo que resta credibilidad al conjunto. El dato es *plausible* — el implante comprime antes de transmitir, así que un radio de bajo ancho de banda y bajo consumo es coherente con la arquitectura — pero **no citarlo en el TFG sin fuente primaria** (patente, paper o documentación oficial).

**Esta diferencia lo explica casi todo**: en el mundo A la energía no es problema porque hay cable; en el mundo B **la energía es EL problema**, porque todo tiene que vivir de una batería adentro de la cabeza sin calentar el tejido.

---

## La cadena física de un implante inalámbrico

```
[1] Electrodos          →  captan la actividad eléctrica de las neuronas
[2] Amplificación       →  la señal es de microvoltios: hay que agrandarla
[3] Digitalización      →  convertir la señal analógica en números
[4] Procesamiento       →  detectar los spikes (¿disparó una neurona?)
[5] Radio               →  transmitir hacia afuera
      ↓
[6] Decodificación      →  AFUERA hoy: traducir la actividad en intención
                           (mover el cursor, escribir una letra)
```

**Dónde ocurre cada cosa hoy**: los pasos 1 a 5 son hardware dentro de la cabeza. **El paso 6 — el decodificador, el "traductor" — corre AFUERA**, en el teléfono o la computadora.

---

## El límite térmico, con números

- Los organismos regulatorios limitan el aumento de temperatura de un implante a aproximadamente **1 °C** (AAMI recomienda el rango 1-2 °C).
- Un aumento de solo **1-2 °C** sobre la línea base puede causar **daño celular irreversible**.
- Traducido a densidad de potencia: los estudios asocian una operación segura con **~50 mW/cm²** para circuitos integrados de escala milimétrica con geometría plana (algunos reportes preliminares hablan de hasta ~80 mW/cm² para ese mismo 1 °C).
- Agravante: el cerebro **disipa calor mal**. La sangre y la convección ayudan poco a esa escala, y el implante está encendido todo el tiempo.

**Referencia de escala**: el sistema-en-chip del N1 mide 5×4 mm y su consumo total reportado es de **~24,7 mW**. Todo el presupuesto energético del implante — amplificar, digitalizar, procesar y transmitir — tiene que caber ahí adentro.

---

## 🔑 La lógica central: transmitir cuesta MÁS que calcular

Este es el concepto que hay que entender de verdad, porque es la puerta por donde entra la tesis.

Los 1.024 electrodos generan **muchísimos datos crudos** (del orden de 200 Mbps). Mandar todo eso por radio consumiría una cantidad de energía imposible para el presupuesto térmico. Entonces el diseño enfrenta un **compromiso**:

| Estrategia | Costo de cómputo adentro | Costo de radio | Estado real |
|---|---|---|---|
| **Mandar todo crudo afuera** | Cero | Altísimo ❌ | Inviable con batería |
| **Procesar un poco adentro, mandar lo esencial** | Bajo | Bajo ✅ | **Lo que se hace hoy** (esquema híbrido) |
| **Decodificar todo adentro, mandar solo la intención** | Alto ❓ | Mínimo | **Camino explorado, NO consenso** ⚠️ |

⚠️ **Corrección importante (2026-08-14)**: la tercera fila decía antes "el futuro" — es incorrecto presentarlo así. La literatura documenta **dos caminos vigentes** (cómputo en el implante vs. cómputo en el dispositivo vestible externo) y los trata como un **compromiso de diseño abierto**, no como una dirección única. Análisis completo con evidencia de ambos lados: [[../20-Investigacion/Donde-Decodificar-Adentro-o-Afuera|¿Dónde decodificar?]].

Por eso el N1 hace **detección de spikes en el propio chip** y comprime los datos hasta ~200 veces antes de transmitir: **es más barato calcular un poco adentro que transmitir mucho afuera.**

> **La regla de oro del diseño de implantes**: cada bit que evitás transmitir te ahorra más energía de la que gastás calculándolo. Por eso el procesamiento migra hacia adentro del chip.

---

## Y acá entra el Tema 25

Fijate la lógica encadenada — **sin apostar a ninguna predicción**:

1. Está establecido que **la transmisión es el mayor consumidor de energía** del implante, y que por eso el procesamiento migra hacia adentro cuando el cómputo lo permite (por eso el N1 detecta spikes en el chip).
2. **Cuánto más se puede mover hacia adentro es una pregunta abierta**, y depende de una sola variable: **cuánto cuesta computar ahí**.
3. Los programas de IA actuales gastan demasiado para el presupuesto de milivatios — por eso los dispositivos que ya decodifican dentro del cuerpo (NeuroPace RNS, Medtronic Percept) usan algoritmos muy simples.
4. **Las redes de impulsos atacan exactamente esa variable**: si computar sale mucho más barato, se puede hacer más adentro con el mismo presupuesto.

**La pregunta del Tema 25 mide esa variable.** Y el resultado sirve se resuelva el compromiso como se resuelva: si todo migra adentro, dice si el paradigma alcanza; si se mantiene el esquema híbrido actual, dice cuánto más se puede hacer adentro; y si el decodificador queda en un vestible externo, la eficiencia sigue importando porque también funciona a batería.

📄 Análisis completo de la premisa, con evidencia a favor y en contra: [[../20-Investigacion/Donde-Decodificar-Adentro-o-Afuera|¿Dónde decodificar?]]

---

## Para la reunión (30 segundos)

> "Un implante inalámbrico tiene que hacer todo con una batería adentro del cráneo y sin subir la temperatura más de un grado, porque más que eso daña el tejido. El cuello de botella es que transmitir datos por radio consume muchísimo más que calcular, así que el diseño empuja el procesamiento hacia adentro del chip: Neuralink ya detecta los spikes ahí mismo y comprime unas 200 veces antes de mandar nada. El paso siguiente sería meter también el decodificador adentro — pero los programas de IA actuales gastan demasiado. Mi tesis evalúa el paradigma de cómputo que promete resolver eso."

## Fuentes

- Límites térmicos: [Thermal Considerations for the Design of an Implanted Cortical BMI (NCBI Bookshelf)](https://www.ncbi.nlm.nih.gov/books/NBK3932/) · [Thermal safety considerations for implantable micro-coil design (PMC10467159)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10467159/) · [Thermal control of implantable optoelectronic devices (Springer, 2025)](https://link.springer.com/article/10.1007/s44291-025-00117-3)
- Arquitectura N1: [bionic-vision.org — Link N1](https://www.bionic-vision.org/implants/link-n1) · [Technical deep dive on Neuralink (Haji)](https://mikaelhaji.medium.com/a-technical-deep-dive-on-elon-musks-neuralink-in-40-mins-71e1100f54d4) · [All About Circuits — Neuralink](https://www.allaboutcircuits.com/news/behind-elon-musks-neuralink-company-developing-brain-machine-interfaces/)
- Energía en implantes neurales: [Comparative analysis of energy transfer mechanisms for neural implants (PMC10825050)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10825050/)

⚠️ Antes de citar cualquiera de estos números en el TFG, verificar la fuente primaria (paper original, no divulgación).

### Lección de rigor (2026-08-14)

Las especificaciones de hardware del N1 (consumo de 24,7 mW, compresión 200×, batería de 12 h, protocolo BLE) provienen de **divulgación técnica, no de fuentes primarias**. Al intentar verificarlas: el sitio de Neuralink es una SPA sin texto extraíble, y la ficha de bionic-vision.org solo confirma electrodos e hilos. Peor: una de las fuentes afirma ">100 Mbps por BLE", físicamente imposible.

**Regla para el TFG**: la divulgación técnica se copia entre sí sin verificar. Diez blogs coincidiendo no equivalen a un paper. Toda especificación de hardware citada debe venir de: el paper original (p. ej. Musk & Neuralink, JMIR 2019), una patente, o documentación oficial. Verificar antes de la Entrega 1.

## Enlaces

[[../30-TFG/Seleccion-Tema/Tema-25-Decodificadores-SNN-Neuromorficos|Tema 25]] · [[../20-Investigacion/Historia-Spiking-Neural-Networks|Historia de las SNN]] · [[../20-Investigacion/Decodificacion-Brain-to-Text|Decodificación brain-to-text]]
