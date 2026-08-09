# Roadmap del TFG — NeuroIngeniería / BCI

> Etapa actual: **Etapa 0 — Fundamentos** (iniciada 2026-08-09)
> Las fechas de las Etapas 3-4 dependen del cuatrimestre en que se curse Seminario Final.

## Visión general

```
Etapa 0          Etapa 1         Etapa 2          Etapa 3           Etapa 4        Etapa 5
Fundamentos  →   Definición  →   Pre-Seminario →  Seminario Final → CAE +       →  Difusión
(aprender)       del tema        (estado del      (4 entregas)      Defensa Oral   (opcional)
                                  arte + PoC)
```

---

## Etapa 0 — Fundamentos (6-8 semanas)

**Objetivo**: pasar de "sé poco de neuro" a poder leer un paper de BCI y entenderlo, y conocer el panorama del campo lo suficiente para elegir tema con criterio.

- Ver plan detallado en [[Plan-Etapa-0]].
- Ejes: neurociencia básica → señales (EEG) → paradigmas BCI → herramientas (Python, MNE, datasets públicos).

**Criterio de salida** (no avanzar sin esto):
- [ ] Puedo explicar qué mide el EEG y sus limitaciones.
- [ ] Conozco los 3-4 paradigmas BCI principales (P300, SSVEP, imaginería motora, neurofeedback).
- [ ] Ejecuté al menos 1 tutorial de MNE-Python con un dataset público.
- [ ] Tengo una lista de 3 ideas candidatas de tesis con pros/contras.

## Etapa 1 — Definición del tema (2-3 semanas)

**Objetivo**: decidir QUÉ tesis hacer, con qué encuadre institucional.

Decisiones a tomar (registrar en [[Decisiones]]):
1. **Tipo de TFG**: Prototipado tecnológico vs. Trabajo de investigación.
2. **Línea temática** (¡irreversible!): Transformación digital / Educación digital / Plataformas de desarrollo.
   - BCI de accesibilidad o salud → Transformación digital.
   - Neurofeedback / atención en aprendizaje → Educación digital.
3. **Factibilidad de datos**: ¿hardware EEG propio (ej. OpenBCI, Muse) o datasets públicos (PhysioNet, BCI Competition, OpenNeuro)? Costo, tiempos de importación a Argentina, plan B.

**Criterio de salida**:
- [ ] Tema elegido, título borrador, objetivo general borrador.
- [ ] Verificado que encaja en una línea temática y en un tipo de TFG.
- [ ] Fuente de datos asegurada (comprada o descargada).

## Etapa 2 — Pre-Seminario: estado del arte + PoC (mientras espero/curso materias previas)

**Objetivo**: llegar al Seminario Final con ventaja — el marco teórico ya avanzado y la parte técnica desriesgada.

- Relevar 15-25 papers → resúmenes en `20-Investigacion/` con cita APA lista.
- Prueba de concepto técnica (PoC) del pipeline: adquisición/dataset → filtrado → features → clasificación → salida.
- Definir stack definitivo y arquitectura del prototipo.

**Criterio de salida**:
- [ ] Marco teórico borrador (~70%).
- [ ] PoC que demuestra que el core técnico es realizable.

## Etapa 3 — Seminario Final (4 meses, fechas de la universidad)

Mapeo directo a las 4 entregas oficiales:

| Entrega | Contenido | Base ya preparada |
|---|---|---|
| 1 | Título, introducción, antecedentes, justificación, objetivos, marco teórico, diseño metodológico, relevamiento, proceso de negocio | Etapa 2 (estado del arte) |
| 2 | Diagnóstico, objetivos/límites/alcance del prototipo, análisis y diseño (UML/Scrum), demo de interfaces SIN código | Etapa 2 (arquitectura) |
| 3 | Seguridad, costos, riesgos, conclusión, resumen/abstract, anexos | — |
| 4 | Codificación del prototipo, portada, índices, referencias | Etapa 2 (PoC) |

Regla: aprobar entregas 1-3 con ≥50% y la 4 (obligatoria) con ≥50%.

## Etapa 4 — CAE + Defensa Oral

- Incorporar correcciones de la Comisión Académica Evaluadora.
- Preparar presentación y demo en vivo del prototipo. Ensayar la defensa ≥3 veces.

## Etapa 5 — Difusión (opcional pero clave para tu objetivo de posgrado)

Estas opciones las ofrece la propia universidad y son EXACTAMENTE lo que suma para un CV de maestría/doctorado:
- [ ] Publicar en el Repositorio Institucional.
- [ ] Postular a la revista **Ciencia y Técnica**.
- [ ] Presentar póster en **Open Lab** (octubre).
- [ ] Aspirar al anuario de mejores trabajos (CIENCIA 21).
- [ ] Subir el prototipo a GitHub público con README en inglés (portfolio internacional).
