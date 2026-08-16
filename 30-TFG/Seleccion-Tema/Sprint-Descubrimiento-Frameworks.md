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

## 4. Resultados del sprint — día 1: análisis riguroso de 6 ideas de expansión (2026-08-16)

El autor trajo 6 ideas de expansión para el tema 28. Se auditaron las afirmaciones de hecho ANTES de aceptarlas (regla vigente). Veredictos:

### ✅ 28.1 — Robustez: inyección de fallos (chaos engineering) → **PASA, la más fuerte**

- **Afirmación verificada**: la literatura de "robustez BCI" es sobre modelos frente a ruido/ataques en la señal; la **capa de software** (pérdida de muestras, desconexión, jitter, deriva de reloj) no aparece evaluada en ningún framework BCI. ✔ Confirmado con búsqueda dedicada.
- **Bonus metodológico encontrado**: existe una plantilla EXACTA a seguir — *A Comprehensive Benchmarking Analysis of Fault Recovery in Stream Processing Frameworks* ([arXiv 2404.06203](https://arxiv.org/pdf/2404.06203)) hace esto mismo para Flink/Spark. Metodología madura de otro dominio + ausencia en BCI = el molde tema-19/SpeakFaster que ya sabemos que funciona.
- **Es justo (no hombre de paja)**: LSL y los frameworks DECLARAN recuperación de conexión y manejo de interrupciones — se testea lo que prometen.
- **Tesis**: *"Evaluación de resiliencia de frameworks BCI mediante inyección de fallos"* — inyectores (drop, jitter, desconexión, clock skew) + replay de señal + curvas de degradación/recuperación por framework. ¿Pierde datos en silencio? ¿avisa? ¿se recupera? Testing puro, disciplina núcleo.

### ✅ 28.2 — Seguridad: el costo de cifrar señal neural → **PASA, CON CORRECCIÓN**

- **Verificado**: [Secure LSL existe](https://eeglab.org/secureLSL/) (cifrado autenticado libsodium sobre LSL, con protección de replay e integridad). ✔
- **CORRECCIÓN al texto del autor**: la afirmación "nadie midió el overhead" es **falsa** — los propios docs reportan *"overhead < 5%"* a 1000 Hz. Lo que NO existe: **verificación independiente** de ese número, y **caracterización bajo carga creciente** (canales × frecuencia) y bajo condiciones adversas (pérdida de paquetes + cifrado).
- **Tesis (reformulada honesta)**: *"Verificación independiente y caracterización del costo del cifrado en streaming de señales neurales"* — replicación del claim + curvas de costo bajo carga. Encuadre correcto: costo de escalamiento, no "mirá cómo falla". Conecta neuroderechos (tema 18) → justificación ética fuerte.

### ✅ 28.3 — Benchmark como producto vivo → **PASA como ENVOLTORIO, no como tesis autónoma**

- MOABB como precedente real (benchmark continuo para algoritmos; nadie para frameworks). ✔
- **Crítica**: no es una pregunta de investigación — es el mecanismo de entrega. Correcto uso: convierte el tema 28 (con 28.1 o 28.2 adentro) en **Prototipado Tecnológico**: contenedores + CI + reproducción con un comando. El aporte es la infraestructura; los resultados la validan.

### 🟡 4, 5 y 6 → componentes, NO tesis autónomas

- **Interoperabilidad/conformidad**: un eje más de la evaluación (matriz de estándares soportados). Se integra, no encabeza.
- **Minería de repositorios**: ya iniciada (tabla de salud de la sección 1); fortalece la evaluación estática. Componente.
- **Evaluar→extender (PR upstream)**: cierre elegante del modelo UNSAM, no tema.

### La configuración recomendada

**Tema 28 base (evaluación con ISO 25010 + benchmark justo) + UNA expansión de identidad:**
- **28.1 Robustez** si el autor se identifica con testing → Investigación.
- **28.2 Seguridad** si se identifica con el eje neuroderechos/implantes → Investigación.
- **+ 28.3** si prefiere que el producto sea software → lo vuelve Prototipado.

Los tres caminos usan: los frameworks vivos según la tabla de salud (BciPy, MEDUSA, LSL; Timeflux como caso "¿estancado?"), replay de señal pública, sin hardware, sin GPU.

## Enlaces

[[Tema-28-Evaluacion-Frameworks-BCI]] · [[../../20-Investigacion/Que-Es-BRAND|Qué es BRAND]] · [[../../20-Investigacion/Que-Es-Un-Framework-BCI|Qué es un framework BCI]] · [[../../20-Investigacion/Calibracion-Alcance-Tesis-BCI|Calibración]]
