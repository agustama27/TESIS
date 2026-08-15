# Decodificadores neuronales — qué se usa hoy y cuál es el baseline correcto

> Nota de investigación · 2026-08-14 · define el punto de partida del [[../30-TFG/Seleccion-Tema/Tema-25-ESTADO-CONSOLIDADO|Tema 25]]
> Responde: ¿de qué tecnología parten los decodificadores actuales? ¿qué redes usan? ¿hay antecedentes con redes de impulsos?

## Resumen

Los decodificadores neuronales evolucionaron en tres generaciones: **filtros lineales** (años 90-2000), **filtro de Kalman** (el caballo de batalla clínico, todavía vigente), y **redes neuronales recurrentes** (LSTM/GRU, el estado del arte actual), con **Transformers** apareciendo en 2024-2025. Las redes de impulsos existen como línea de investigación desde 2023-2026, con al menos ocho trabajos y código público — **pero sin comparación unificada entre sí ni contra los convencionales**. Ahí está el hueco de la tesis.

---

## 1. La evolución de los decodificadores

### Generación 1 — Lineales (los cimientos)

- **Filtro de Wiener**: predice el movimiento actual como una **suma ponderada de los instantes anteriores**. Simple, rápido, interpretable.
- **Optimal Linear Estimation (OLE)**: estimación lineal óptima, usada como baseline clásico.

Siguen usándose como piso de comparación porque son transparentes y baratísimos.

### Generación 2 — Filtro de Kalman (el estándar clínico)

Matemática de los años 60 — la misma familia que usan los GPS. Modela el estado (posición y velocidad del cursor) y lo actualiza con cada nueva observación neural.

Variantes en uso: **velocity Kalman filter** (decodifica velocidad, no posición) y **ReFIT-KF** (recalibrado con la intención inferida del usuario).

**Es el decodificador más usado en sistemas clínicos reales.** BrainGate computa las características neurales cada 20 ms y las decodifica con Kalman. Es robusto, barato, estable en el tiempo — por eso sobrevive.

### Generación 3 — Redes recurrentes (el estado del arte)

- **LSTM / GRU / RNN**: superan claramente al Kalman. Un estudio con datos de BrainGate mostró que una LSTM **aumenta sustancialmente los bits por segundo** en tareas de selección de objetivos, tanto en velocidad como en precisión con objetivos chicos. Un modelo LSTM dual (decodificando movimiento y velocidad simultáneamente) superó tanto al Kalman de velocidad como a la LSTM de velocidad sola.
- Es lo que usan los sistemas brain-to-text de referencia (Willett 2021/2023 usan RNN).

### Generación 4 (emergente) — Transformers

Aparecen en 2024-2025 con arquitecturas específicas para el dominio, por ejemplo **SPINT** (*Spatial Permutation-Invariant Neural Transformer*, [arXiv 2507.08402](https://arxiv.org/html/2507.08402)), diseñadas para tolerar que los canales cambien entre sesiones.

---

## 2. Qué software se usa

| Capa | Herramientas dominantes |
|---|---|
| Entrenamiento de modelos | **PyTorch** (dominante en el trabajo reciente) |
| Análisis de señal | MNE-Python, NumPy/SciPy |
| Legado en laboratorios clínicos | MATLAB (todavía presente en pipelines históricos de BrainGate) |
| Redes de impulsos | **snnTorch**, **SpikingJelly** (ambos sobre PyTorch) |
| Benchmarking neuromórfico | **NeuroBench** (*Nature Communications*, 2025) |
| Datasets y evaluación | FALCON, Neural Latents Benchmark |

**Consecuencia práctica para vos**: todo el ecosistema moderno vive en PyTorch. No tenés que aprender un entorno exótico — las redes de impulsos se definen y entrenan en el mismo framework que ya conocés.

---

## 3. Antecedentes con redes de impulsos (verificados)

| Trabajo | Qué hace | Referencia |
|---|---|---|
| RSNN para velocidad de dedos | Decodifica cinemática desde spikes corticales; publica `bigRSNN` (rendimiento) y `tinyRSNN` (eficiencia). **Código público** | [github.com/fmi-basel/neural-decoding-RSNN](https://github.com/fmi-basel/neural-decoding-RSNN) |
| SNN + filtrado para BMI implantables | Decodificación eficiente combinando SNN con filtrado | [arXiv 2312.15889](https://arxiv.org/pdf/2312.15889) |
| SNN podadas adaptativamente | Poda para eficiencia energética en decodificación intracortical | [arXiv 2504.11568](https://arxiv.org/abs/2504.11568) |
| Framework causal y escalable | Decodificación neural con SNN, eficiente en energía | [arXiv 2510.20683](https://arxiv.org/abs/2510.20683) |
| SNN de fusión multiescala | Decodificación de señal neural invasiva | [Frontiers in Neuroscience, 2025](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2025.1551656/full) |
| Acumuladores Hebbianos | Decodificación SNN *online* en BMI intracorticales | [arXiv 2509.14447](https://arxiv.org/pdf/2509.14447) |
| Decodificadores híbridos neuromórficos | Exploración arquitectónica para BMI implantable | [arXiv 2505.05983](https://arxiv.org/pdf/2505.05983) |
| SNN sobre EEG en Loihi | Implementación PyTorch + hardware neuromórfico | [github.com/combra-lab/snn-eeg](https://github.com/combra-lab/snn-eeg) |

**Conclusión**: los antecedentes existen y son sólidos. **Pero cada uno usa su dataset, su métrica y su protocolo** — no hay comparación unificada entre ellos ni una comparación limpia contra los decodificadores convencionales sobre un benchmark común. Ese es el hueco.

---

## 4. ⚠️ La trampa metodológica que hay que evitar

**El resultado de la tesis depende enteramente de contra qué compares.**

| Si comparás contra… | Qué pasa |
|---|---|
| **Filtro de Wiener o Kalman solamente** | Las redes de impulsos probablemente ganan — pero el resultado **no dice nada**: estarías venciendo a un decodificador de generación anterior. Un evaluador informado lo desarma en un minuto. |
| **LSTM/GRU (estado del arte real)** | La comparación es **honesta y significativa**. Es difícil, pero es la única que vale. |
| **Ambos (lineal + moderno)** | ✅ **Lo correcto**: el lineal como piso de referencia, el recurrente como rival real. |

> **Regla**: en cualquier estudio comparativo, elegir un baseline débil es la forma más común — y más detectable — de inflar un resultado. Tu credibilidad depende de comparar contra lo mejor que existe, no contra lo más fácil de vencer.

**Recomendación para el diseño**: incluir **tres** competidores — un lineal (Kalman o Wiener, como piso), una recurrente moderna (GRU/LSTM, el rival de verdad) y las redes de impulsos. Así la tabla cuenta la historia completa: dónde está cada paradigma en precisión y en costo.

---

## 5. Qué significa para el Tema 25

1. **Tu baseline convencional debe ser una red recurrente moderna** (GRU/LSTM), no solo un Kalman. Está definido.
2. **Todo el ecosistema es PyTorch** — no hay salto de entorno.
3. **Los antecedentes SNN existen y tienen código público** — no arrancás de cero, y el repo de Basilea (`bigRSNN`/`tinyRSNN`) es tu punto de partida natural.
4. **El aporte es la comparación unificada**, y ahora está mejor definido: no solo "SNN vs convencional", sino **las tres familias sobre el mismo benchmark con el mismo medidor**.

## Fuentes

- LSTM vs Kalman en datos de BrainGate: [arXiv 1812.09835](https://arxiv.org/abs/1812.09835) · [IEEE Xplore](https://ieeexplore.ieee.org/abstract/document/8717140)
- Panorama de decodificación intracortical: [Neural Decoding for Intracortical Brain–Computer Interfaces (Cyborg and Bionic Systems)](https://spj.science.org/doi/10.34133/cbsystems.0044)
- Transformers para decodificación motora: [SPINT (arXiv 2507.08402)](https://arxiv.org/html/2507.08402)
- Antecedentes SNN: ver tabla de la sección 3.

⚠️ Verificar cada referencia contra su fuente primaria antes de citarla en el TFG.

## Enlaces

[[../30-TFG/Seleccion-Tema/Tema-25-ESTADO-CONSOLIDADO|Tema 25 — estado consolidado]] · [[Historia-Spiking-Neural-Networks]] · [[../10-Fundamentos/Cadena-de-Senal-Neural|Cadena de señal]] · [[Donde-Decodificar-Adentro-o-Afuera]]
