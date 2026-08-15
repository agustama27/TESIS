# El software de Neuralink en pacientes + verificación del hueco del Tema 28

> Nota de investigación · 2026-08-15 · dos preguntas del autor respondidas con verificación
> (1) ¿Cómo funciona el software que usan los pacientes de Neuralink hoy? (2) ¿Ya se hizo la evaluación de frameworks a escala de implante?

---

## Parte 1 — Cómo funciona el software de Neuralink para sus pacientes

⚠️ **Nivel de evidencia**: reconstrucción a partir de fuentes secundarias consistentes (prensa técnica, reportes del estudio PRIME, patentes). Neuralink no publica documentación de arquitectura. Ninguna afirmación de esta sección debe citarse en el TFG sin esa aclaración.

### La cadena completa, según lo reportado

```
[Implante N1]                    [Computadora del paciente]        [Sistema operativo]
1024 electrodos                       "Neuralink App"                  Apps comunes
      ↓                                     ↓                              ↓
Detección de spikes  ──BLE──▶   Decodificador ML (tipo RNN,   ──▶   Mouse/teclado
EN EL CHIP                      calibrado por usuario)                VIRTUAL
(reduce el caudal                     +                          (ajedrez, navegador,
antes de transmitir)            flujos de calibración             lo que sea)
```

1. **En el implante**: detección de spikes en el propio chip — el caudal se reduce drásticamente ANTES de transmitir (coherente con todo lo estudiado en [[../10-Fundamentos/Cadena-de-Senal-Neural|la cadena de señal]]).
2. **Transmisión inalámbrica** (reportada como Bluetooth Low Energy con cifrado — ver advertencia de verificación en [[../10-Fundamentos/Como-Funciona-un-Implante-Intracortical|nota del implante]]).
3. **La "Neuralink App"** corre en la computadora del propio paciente (Noland Arbaugh usaba una MacBook): ahí vive el **decodificador de ML** (reportado como redes recurrentes calibradas por usuario) y los flujos de calibración (mapeo de intenciones de movimiento → acciones).
4. **La salida es un mouse/teclado virtual a nivel de sistema operativo**: el paciente controla las aplicaciones NORMALES (ajedrez online, navegador, juegos) — no apps especiales. El clic se hace, por ejemplo, deteniendo el cursor 0,3 s (dwell).

### Las tres observaciones que importan para la tesis

1. **Stack vertical y cerrado**: Neuralink construye TODO (implante, radio, app, decodificador, integración con el SO) como una sola pieza propietaria. **No hay SDK público, no hay middleware, no hay capa reutilizable por terceros.**
2. **La decisión arquitectónica clave es la misma que estudiamos**: procesamiento repartido — detección en el chip, decodificación en la computadora. El compromiso adentro/afuera de [[Donde-Decodificar-Adentro-o-Afuera]] en su versión comercial.
3. **La genialidad de producto está en la última milla**: traducir a mouse/teclado virtual del SO significa compatibilidad instantánea con todo el software del mundo. Cero apps especiales.

### Por qué esto FORTALECE el Tema 28

El contraste queda nítido:

| | Mundo Neuralink (pacientes hoy) | Mundo abierto (todos los demás) |
|---|---|---|
| Stack | Vertical, cerrado, integrado | Modular: frameworks + middleware (LSL, Timeflux…) |
| Acceso | Solo pacientes del ensayo | Cualquier laboratorio del planeta |
| Escala de datos que maneja | Intracortical (con reducción en chip) | Diseñado para EEG |

**La narrativa de la tesis**: los pacientes de hoy usan stacks cerrados que ya operan a escala intracortical. El resto del mundo — laboratorios, universidades, empresas emergentes — depende del ecosistema abierto, que nació para EEG. **¿Puede ese ecosistema abierto acompañar la era que los stacks cerrados inauguraron?** Nadie lo midió. Esa es la tesis.

---

## Parte 2 — Verificación del hueco: ¿ya se hizo esta evaluación?

**Búsquedas realizadas (2026-08-15)**: benchmarks de escalabilidad de LSL · surveys de comparación de plataformas BCI · evaluaciones de rendimiento entre frameworks.

### Lo que EXISTE (los antecedentes a citar — esto es bueno, no malo)

| Antecedente | Qué es | Limitación que deja el hueco abierto |
|---|---|---|
| **Brunner et al., "BCI Software Platforms"** (capítulo, ~2012) | Comparación de 7 plataformas de la época (BCI2000, OpenViBE, TOBI CIP, BCILAB, BCI++, xBCI, BF++) | **Cualitativa** (tabla de features: SO, licencias, dispositivos) y **pre-era Python** — no incluye Timeflux, BciPy, MEDUSA, PyNoetic |
| Estudio de usabilidad de 3 plataformas para spellers P300 (2023, ScienceDirect) | Comparación de usabilidad para UNA tarea de configuración | Ángulo estrecho (usabilidad de layout), sin rendimiento |
| Paper de LSL (2024/2025, Imaging Neuroscience) | Evalúa el desempeño de LSL "en contextos experimentales comunes" | Auto-evaluación, escala EEG, un solo componente |
| MetaBCI (2023) | Otra plataforma más (china) que se presenta a sí misma | Auto-descriptiva, como todos los papers de frameworks |

### Lo que NO existe (el hueco, verificado)

1. ❌ Comparación de la **generación moderna** de frameworks Python (Timeflux, BciPy, MEDUSA, NeuXus, PyNoetic) — los surveys son de la generación anterior.
2. ❌ **Benchmark empírico de rendimiento** entre frameworks (latencia extremo a extremo, throughput, jitter medidos con protocolo común) — las comparaciones existentes son tablas de características, no mediciones.
3. ❌ **Stress-test de escalabilidad a cargas intracorticales** (canales × frecuencia de muestreo hasta el punto de quiebre) — no aparece en ninguna búsqueda.

### Veredicto

**El hueco sobrevive la verificación — y con la estructura ideal**: antecedentes citables que legitiman la pregunta (los surveys viejos demuestran que comparar plataformas es un género académico aceptado) + tres dimensiones concretas sin cubrir (generación moderna, medición empírica, escala de implante). La tesis se posiciona como **la actualización empírica del survey de Brunner para la era Python e intracortical**.

⚠️ Mantener la disciplina: en el Mes 1 se repite esta verificación con búsqueda exhaustiva (Scholar, arXiv, IEEE) antes de la Entrega 1.

## Fuentes

- Brunner et al., BCI Software Platforms: [PDF (SCCN/UCSD)](https://sccn.ucsd.edu/~scott/pdf/Brunner_BCI11.pdf) · [Springer](https://link.springer.com/chapter/10.1007/978-3-642-29746-5_16)
- Usabilidad de 3 plataformas P300 (2023): [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1746809423007590)
- LSL performance: [Imaging Neuroscience (MIT Press)](https://direct.mit.edu/imag/article/doi/10.1162/IMAG.a.136/132678/)
- MetaBCI: [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0010482523012714)
- Neuralink en pacientes (fuentes secundarias): reportes del estudio PRIME y prensa técnica — ver [[../10-Fundamentos/Como-Funciona-un-Implante-Intracortical|advertencias de verificación]].

## Enlaces

[[../30-TFG/Seleccion-Tema/Tema-28-Evaluacion-Frameworks-BCI|Tema 28]] · [[../10-Fundamentos/Que-Es-Un-Framework-BCI|Qué es un framework BCI]] · [[Donde-Decodificar-Adentro-o-Afuera]]
