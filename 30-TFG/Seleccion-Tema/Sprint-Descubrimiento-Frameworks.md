# Sprint de descubrimiento — ecosistema de frameworks/middleware BCI

> 2026-08-16 · Sprint ACOTADO pactado con el autor: una semana, con fecha de fin y regla de decisión.
> Regla aprendida y vigente: **verificar antes de enamorarse** — cada dirección candidata lleva su tarea de verificación.

## 1. Señales de vida del ecosistema (datos GitHub reales, 2026-08-16)

| Repositorio | ⭐ | Forks | Último push | Desde | Lectura |
|---|---|---|---|---|---|
| **MOABB** (benchmark) | 1.036 | 258 | **hoy** | 2017 | El más vivo del ecosistema — pero es evaluación offline, no middleware |
| **LSL** (transporte) | 772 | 193 | 2026-05 | 2018 | El estándar de facto, activo |
| **Open Ephys** (adquisición ephys) | 241 | **710** | 2026-08 | 2015 | Fork/estrella altísimo = uso masivo de laboratorio |
| **SpikeGLX** (adquisición) | 109 | 37 | **ayer** | 2016 | Vivo, mantenido por Janelia |
| **BciPy** (framework EEG) | 155 | 42 | 2026-07 | 2018 | Activo |
| **Timeflux** (framework EEG) | 189 | 31 | **2024-12 ⚠️** | 2019 | **~20 meses sin push — posiblemente estancado** |
| **BRAND** (iBCI lazo cerrado) | 50 | 10 | 2026-03 | 2023 | Vivo pero chico: nicho de investigación, NO estándar |
| MEDUSA (framework EEG) | 22 | 4 | 2026-07 | 2022 | Chico, activo |
| NeuXus (framework EEG) | 21 | 5 | 2026-04 | 2020 | Marginal |
| RSNN Basilea (artefacto de paper) | 15 | 5 | 2025-01 | 2024 | Congelado post-publicación (normal) |

### Lo que los datos responden (preguntas del autor)

- **¿BRAND se usa de verdad?** Sí, pero en un nicho chico (50⭐, 10 forks). NO es un estándar — es infraestructura de un consorcio académico. Duda del autor: confirmada.
- **¿Hay un estándar de framework?** NO en la capa de aplicación. El único estándar real es LSL, y es solo transporte. La capa de aplicación está **fragmentada**: 4-5 frameworks chicos compitiendo, uno posiblemente muerto (Timeflux).
- **El hallazgo del día**: la fragmentación + el estancamiento de Timeflux muestran un ecosistema **sin señales claras de salud para quien tiene que elegir** — lo cual es en sí mismo el argumento de que hace falta evaluación sistemática.

## 2. Las tres direcciones candidatas del sprint

### S1 — Benchmark empírico justo de frameworks (Investigación)
Evaluar los frameworks activos **en lo que SÍ prometen** (tiempo real a escala EEG — sin el hombre de paja intracortical): latencia extremo a extremo, jitter, throughput, con protocolo común y replay de señal; + atributos de calidad ISO/IEC 25010 (mantenibilidad, documentación, actividad).
**Verificación pendiente**: buscar benchmarks empíricos publicados entre frameworks modernos (los antecedentes hallados son cualitativos/2012). ⏳

### S2 — Reconstrucción arquitectónica (Investigación/diseño)
"Architecture recovery": extraer y documentar las vistas de arquitectura de 4-5 frameworks desde su código (módulos, flujos, contratos), compararlas, y producir **la arquitectura de referencia documentada que el campo no tiene**. Método formal de la disciplina (reconstrucción de arquitectura + vistas tipo arc42/C4).
**Verificación pendiente**: ¿algún framework tiene documentación arquitectónica formal? ¿Existe una arquitectura de referencia BCI publicada? ⏳

### S3 — Estudio de experiencia de desarrollo (Investigación empírica con humanos accesibles)
La única evaluación con personas que NO requiere pacientes: **desarrolladores** (n≈8-12 — colegas, estudiantes) implementan la misma tarea BCI mínima en 2-3 frameworks; se mide tiempo, errores, obstáculos, percepción (cuestionarios estándar de usabilidad de APIs). DX research aplicado a BCI tooling.
**Verificación pendiente**: ¿existen estudios de DX sobre herramientas BCI? (El de 2023 era usabilidad de configuración de spellers, ángulo distinto). ⏳

### Variantes aplicadas (Prototipado) si alguna investigación no cierra
- Puente/adaptador entre capas (ej. exportador BIDS para un framework que no lo tenga — verificar cuál).
- Migración documentada de un paradigma legado (BCI2000) a un framework moderno, con método.

## 3. Plan del sprint (fecha de fin: 2026-08-23)

| Día | Tarea |
|---|---|
| 1-2 | Correr las 3 verificaciones pendientes (⏳) con búsqueda exhaustiva |
| 3 | Instalar los 2-3 frameworks vivos y correr su "hola mundo" — contacto real, no papel |
| 4-5 | Redactar la formulación de la dirección sobreviviente con más tracción para el autor |
| 6-7 | Página oficial (formato Definiciones Iniciales) + decisión |

**Regla de decisión pactada**: al 2026-08-23, de las direcciones que sobrevivan la verificación, el autor ELIGE UNA o acepta que esta rama no es la suya y se cierra. **No hay extensión del sprint.**

## Enlaces

[[Tema-28-Evaluacion-Frameworks-BCI]] · [[../../20-Investigacion/Que-Es-BRAND|Qué es BRAND]] · [[../../20-Investigacion/Que-Es-Un-Framework-BCI|Qué es un framework BCI]] · [[../../20-Investigacion/Calibracion-Alcance-Tesis-BCI|Calibración]]
