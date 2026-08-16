# ESTADO ACTUAL DEL PROYECTO — documento de traspaso entre sesiones

> **Escrito: 2026-08-16, al cierre de la sesión de kickoff/selección de tema (sesión larga, ~2 semanas).**
> **Toda sesión nueva debe leer este documento PRIMERO**, después [[Bitacora]] y [[Roadmap]].

---

## 🎯 Dónde está parado el proyecto HOY

**Fase**: selección de tema, en el momento de DECISIÓN FINAL (no de exploración — la exploración terminó).

**Propuesta sobre la mesa** (elegida por el mentor tras ~30 temas explorados, bajo regla de veto):

> **"Evaluación de resiliencia de frameworks BCI open source mediante inyección de fallos, con medición del impacto en la precisión del decodificador."**
> Tema 28 + expansión 28.1 (robustez/chaos engineering) + capa IA (función de transferencia falla-de-software → error-del-modelo).
> Trabajo de Investigación · línea Transformación Digital · sin hardware, sin GPU, datos públicos.

**Estado de la decisión**: PENDIENTE de confirmación del autor. **Regla de veto pactada**: puede vetar solo eligiendo otro tema de la lista final verificada (28.2 costo de cifrado, 24 LLM-español, 19 fidelidad) con razón escrita en bitácora. NO se generan más temas — regla firme acordada tras detectar el patrón de búsqueda infinita.

**Esquema visual de la propuesta** (para mostrar al tutor): https://claude.ai/code/artifact/2b87500e-b857-4f89-b859-f614e57479ae

## ✅ Qué respalda la propuesta

- Hueco verificado DOS veces: no existe evaluación de la capa de software de frameworks BCI frente a fallas (la literatura de "robustez BCI" es sobre modelos frente a ruido en la señal).
- Plantilla metodológica publicada: benchmark de fault recovery en stream processing (arXiv 2404.06203, hecho para Flink/Spark).
- Frameworks objetivo según tabla de salud GitHub (2026-08-16): BciPy y MEDUSA activos, LSL activo, Timeflux posiblemente estancado (~20 meses sin push) — eso también es un dato del estudio.
- Antecedente citable para la capa IA: literatura de degradación de señal sobre modelos EXISTE (se cita); lo nuevo verificado es la cadena con software real en el medio.
- Es justo (no hombre de paja): los frameworks DECLARAN recuperación de conexión — se testea lo que prometen.

## 📚 Las reglas aprendidas en esta sesión (NO repetir errores)

1. **Calibración UNSAM**: la vara de un TFG es ejecución rigurosa de un problema delimitado, NO originalidad mundial. Referencia: tesis UNSAM (Helguera 2021) extendió un sistema existente de 2 a 4 opciones y aprobó. Ver [[../20-Investigacion/Calibracion-Alcance-Tesis-BCI|Calibración]].
2. **Verificar antes de enamorarse**: toda afirmación de hueco/hecho se verifica con búsqueda propia ANTES de proponerla. Errores históricos que enseñaron esto: Bluetooth del N1 (sin fuente primaria), "el futuro es decodificar adentro" (sin evidencia), tema 25 vs NeuroBench (ya hecho), silos frameworks/ephys (BRAND ya existía), "nadie midió overhead de Secure LSL" (los autores sí, <5% autoreportado).
3. **Los temas de áreas calientes financiadas mueren**: SNN neuromórficas e infraestructura intracortical están cubiertas por consorcios (NeuroBench, BrainGate/BRAND). Los huecos viables para TFG son "ausencias verificables" o "extensiones declaradas de lo existente".
4. **El patrón del autor**: talento para objeciones agudas (corrigió al mentor 3+ veces) + tendencia a búsqueda infinita (30 temas, todos con grieta). La exploración fue declarada TERMINADA — no reabrirla.
5. **Ninguna cita sin fuente verificada** — regla dura de todo el harness.

## 📂 Mapa de documentos clave

| Qué | Dónde |
|---|---|
| Propuesta actual detallada + expansiones auditadas | [[../30-TFG/Seleccion-Tema/Sprint-Descubrimiento-Frameworks|Sprint-Descubrimiento-Frameworks]] (secciones 2 y 4) |
| Tema 28 base con gancho y objeciones respondidas | [[../30-TFG/Seleccion-Tema/Tema-28-Evaluacion-Frameworks-BCI|Tema-28]] |
| Índice de TODOS los temas (30) con estados | [[../30-TFG/Seleccion-Tema/00-Indice|00-Indice]] |
| La calibración de vara (documento correctivo central) | [[../20-Investigacion/Calibracion-Alcance-Tesis-BCI|Calibracion-Alcance-Tesis-BCI]] |
| Fundamentos aprendidos (implantes, señal, frameworks, BRAND) | `10-Fundamentos/` y `20-Investigacion/` |
| Word oficiales ya generados (temas 19 y 23, como plantilla) | `30-TFG/Seleccion-Tema/*.docx` |
| Prompts NotebookLM para presentaciones | [[../30-TFG/Seleccion-Tema/Prompts-NotebookLM|Prompts-NotebookLM]] |

**Artifacts publicados**: deck de 18 temas (HISTÓRICO, superado — https://claude.ai/code/artifact/9a29cb16-f79b-4d1d-9cbc-e2daac96f838) · esquema visual de la propuesta actual (VIGENTE — https://claude.ai/code/artifact/2b87500e-b857-4f89-b859-f614e57479ae).

**Memoria Engram**: proyecto `tesis`, topic keys `bci/*` (seleccion-tema/estado, seleccion-tema/calibracion, brain-to-text/*, se4ai/*).

## 🔀 NOVEDAD DE ÚLTIMO MOMENTO (2026-08-16, al cierre): posible giro de dominio

Al cerrar la sesión se encontró en el vault un documento nuevo — [[../30-TFG/Seleccion-Tema/Alternativas-Fuera-de-BCI-2026-08-16|Alternativas fuera de BCI]] — que plantea **temas de Ingeniería de Software × sistemas LLM/agentes** (testing de regresión de agentes conversacionales, evaluación de agentes de voz en español, benchmarks): el dominio que el autor ejerce a diario en Evoltis. El documento sigue la calibración correcta y contiene una observación clave: *tras 30 temas BCI sin que ninguno encienda — incluido el de mayor motivación declarada — el candidato a problema puede ser el dominio, no la lista.*

**Esto redefine la decisión pendiente**: ya no es solo "confirmar o vetar la propuesta BCI", sino **elegir dominio**: (a) la propuesta BCI (28+28.1+capa IA), o (b) las alternativas LLM-agentes (temas A/B del documento — motivación presunta máxima por ser su oficio).

⚠️ **Advertencia de rigor**: las citas y afirmaciones del documento de alternativas NO fueron verificadas por esta sesión (regla: verificar antes de enamorarse). Primera tarea si se toma ese camino: correr la verificación completa de sus fuentes y huecos. Segunda: confirmar con la universidad que la línea temática admite sistemas LLM. Tercera: límites de propiedad intelectual con el empleador (el tema A roza herramientas del trabajo).

## ⏭️ Próximos pasos (en orden)

1. **[BLOQUEANTE] Decisión de dominio del autor**: BCI (propuesta 28+28.1+IA) vs LLM-agentes (temas A/B de Alternativas). La prueba de humo aplica a ambos: 3 horas de sábado con el candidato elegido.
2. **[BLOQUEANTE] Conseguir la fecha del Módulo 0 / reunión con el tutor** (SAM o Profesor Director). Sin fecha no hay presión real y la decisión flota.
3. Generar el **Word oficial** del tema confirmado (plantillas .docx de los temas 19/23 como base; 5 minutos).
4. Día 3 del sprint: `pip install bcipy` + hola mundo de BciPy y MEDUSA — primer contacto real (3 hs).
5. Regenerar presentación NotebookLM del tema confirmado (prompts listos).
6. Pendientes menores: repositorio PUCE caído (reintentar); texto completo tesis Uniandes (anti-bot).

## 🗂️ Estado del repo

- Rama de trabajo: `feat/temas-candidatos-tfg` (~25 commits de selección de tema) → **mergeada a `main` al cierre de esta sesión** para que toda sesión/herramienta nueva vea el estado completo.
- Remoto: https://github.com/agustama27/TESIS (privado, cuenta personal).
