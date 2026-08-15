# Calibración de alcance — qué es realmente una tesis de grado sobre BCI

> Nota de investigación · 2026-08-15 · **documento correctivo**
> Origen: tras matar el Tema 25 aplicando estándar de paper de alto impacto, se relevaron tesis de grado reales sobre BCI en ingeniería. El estándar que se venía usando era incorrecto.

## El hallazgo en una frase

**La vara de un Trabajo Final de Graduación no es la originalidad mundial: es la ejecución rigurosa de un problema bien delimitado.** Las tesis de grado sobre BCI que efectivamente se aprueban **extienden sistemas existentes**, no descubren huecos inéditos.

---

## Caso de referencia: UNSAM (Argentina), 2021

**Helguera, A. (2021).** *Propuesta de optimización de un sistema de interfaz Cerebro-Computadora, utilizando potenciales evocados: adición por software de dos estímulos.* Universidad Nacional de San Martín, Escuela de Ciencia y Tecnología. **Trabajo Final Integrador**, Ingeniería Biomédica. 141 páginas. Acceso abierto: https://ri.unsam.edu.ar/handle/123456789/1889

### El objetivo, textual

> "El proyecto desarrollado en este informe se basó en la optimización del sistema de OTTAA Project para la selección en la toma de decisiones, mediante potenciales evocados en señales de EEG. **Se buscó aumentar la cantidad de posibles opciones para la toma de decisiones, de dos a tres**, entrenando una red neuronal para esta nueva configuración."

**Ese es el objetivo completo.** Pasar un sistema de 2 opciones a 3-4.

### Objetivos específicos (los cuatro)

1. Evaluar la implementación de un sistema con mayor cantidad de estímulos (modificar interfaz de usuario + procesamiento interno).
2. Definir las frecuencias de estimulación a utilizar.
3. Modificar la Red Neuronal Artificial de clasificación y entrenarla.
4. Realizar pruebas de aplicación para verificar el funcionamiento.

### Contexto y recursos

- **El sistema ya existía**: trabajó dentro del OTTAA Project (proyecto argentino de comunicación aumentativa). No partió de cero.
- **Hardware**: OpenBCI Ganglion, estimulador LED, tablet. Accesible.
- **Software**: Python, Anaconda, Jupyter Notebook.
- **Sujetos**: voluntarios sanos, con consentimiento informado y Mini-Mental State Examination como anexos.
- **NO probó con la población objetivo**: "pruebas con personas con discapacidad" quedó declarado como **trabajo futuro**.

### Estructura del informe (7 capítulos + anexos)

1. Introducción (contexto, antecedentes y justificación, objetivos, organización)
2. Marco teórico (sistemas aumentativos, BCI, EEG, potenciales evocados, redes neuronales)
3. Materiales y funcionamiento (herramientas, esquema de conexiones, modo de funcionamiento)
4. Protocolo experimental (sujetos, estimulación, adquisición)
5. Resultados (índices, desempeño de la red por arquitectura, matriz de confusión)
6. Discusión (procesamiento, RNA, robustez, verificación, **abordaje integral**, **normativa vigente**, trabajos futuros)
7. Conclusión
- Anexos: consentimiento informado · Mini-Mental State Examination
- Apéndice: terapia ocupacional

**Dato notable**: incluye capítulos **no técnicos** — normativa argentina para comercialización del dispositivo y abordaje interdisciplinario con terapeutas ocupacionales.

---

## Otras tesis relevadas (mismo patrón)

| Universidad | Nivel | Título | Patrón |
|---|---|---|---|
| PUCE (Ecuador) | Ing. en Sistemas | *Sistema para la integración de una interfaz cerebro-computador* | Integración de sistema |
| Uniandes (Colombia) | Pregrado | *Diseño e implementación de una interfaz cerebro-máquina para identificación de tareas cognitivas* | Diseño e implementación |
| UNAM (México) | Licenciatura | *Diseño y desarrollo de un sistema para control mental de prótesis utilizando BCI* | Diseño y desarrollo |
| UNAM | Maestría | *Interfaz cerebro computadora con imaginación musical* | Aplicación de paradigma |
| U. Málaga (España) | Doctorado | *Paradigmas de navegación basados en imaginación motora* | (nivel doctoral) |

**Verbos dominantes**: diseñar, implementar, desarrollar, integrar, optimizar. **Ninguno**: descubrir, superar el estado del arte, refutar.

---

## ⚠️ El error de calibración que se cometió (2026-08-14/15)

Durante la selección de tema se aplicó a los candidatos un estándar de **paper de alto impacto**:

- Se exigió que el hueco fuera inédito a nivel mundial.
- Se descartó el Tema 25 porque NeuroBench (consorcio, *Nature Communications*) ya había hecho una comparación equivalente.
- Se descartó su plan B porque la crítica al proxy energético ya estaba publicada.

**Con ese criterio, la tesis de UNSAM tampoco habría existido**: los sistemas SSVEP con redes neuronales estaban resueltos hacía años; su aporte fue extender uno existente de 2 a 4 opciones.

### La vara correcta

| Estándar incorrecto (paper) | Estándar correcto (TFG) |
|---|---|
| ¿Es inédito en el mundo? | ¿Está el problema bien delimitado? |
| ¿Supera el estado del arte? | ¿Se aplicó método con rigor? |
| ¿El hueco resiste una revisión sistemática? | ¿Los resultados están documentados y son verificables? |
| ¿Nadie lo hizo antes? | ¿Se declararon alcance y limitaciones con honestidad? |

> **Regla operativa**: para un TFG, que un trabajo similar exista **no invalida** el tema — lo convierte en referente de contraste. Replicar, extender o adaptar con método propio es aporte válido a nivel de grado, **siempre que se declare explícitamente qué es replicación y qué es contribución propia**.

---

## Consecuencias para la selección de tema

1. **El Tema 25 vuelve a ser viable**, reformulado como *"implementación y evaluación comparativa de decodificadores convencionales y de impulsos sobre datos públicos"*, usando NeuroBench como **referente de contraste** y no como competidor. Declarando explícitamente qué se replica y qué se aporta.
2. Lo mismo aplica al resto de los candidatos descartados por "falta de originalidad mundial".
3. **El criterio de decisión ahora es otro**: no "¿es inédito?" sino **"¿puedo ejecutarlo con rigor en 4 meses y defenderlo con honestidad?"**.
4. Un modelo replicable del caso UNSAM: **trabajar dentro de un proyecto existente y de código abierto**, agregándole una capacidad concreta. Reduce riesgo y acota alcance naturalmente.

## Pendiente

- [ ] Releer los temas finalistas (19, 24, 25) con la vara correcta.
- [ ] Considerar el ángulo de **QA/testing de sistemas BCI** (surgido de literatura de testing), no explorado aún.
- [ ] Descargar y revisar la tesis de PUCE (Ing. en Sistemas) como segundo referente de la disciplina exacta.

## Enlaces

[[../30-TFG/Seleccion-Tema/00-Indice|Índice de temas]] · [[../30-TFG/Seleccion-Tema/Tema-25-ESTADO-CONSOLIDADO|Tema 25]] · [[Decodificadores-Estado-del-Arte]] · [[Donde-Decodificar-Adentro-o-Afuera]]
