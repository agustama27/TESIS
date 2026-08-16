# ESTADO ACTUAL DEL PROYECTO — documento de traspaso entre sesiones

> **Escrito: 2026-08-16, al cierre de la sesión de kickoff/selección de tema (sesión larga, ~2 semanas).**
> **Toda sesión nueva debe leer este documento PRIMERO**, después [[Bitacora]] y [[Roadmap]].

---

## 🎯 Dónde está parado el proyecto HOY

**Fase**: selección de tema **CERRADA (2026-08-16)** — tema confirmado por el autor, ver [[Decisiones|D-004]]. Próxima fase: formalización (Módulo 0 + Word oficial) y primer contacto técnico.

**Tema confirmado** (elegido por el mentor tras ~30 temas explorados, confirmado por el autor el 2026-08-16 con la alternativa LLM-agentes sobre la mesa):

> **"Evaluación de resiliencia de frameworks BCI open source mediante inyección de fallos, con medición del impacto en la precisión del decodificador."**
> Tema 28 + expansión 28.1 (robustez/chaos engineering) + capa IA (función de transferencia falla-de-software → error-del-modelo).
> Trabajo de Investigación · línea Transformación Digital · sin hardware, sin GPU, datos públicos.

**Estado de la decisión**: ✅ **CONFIRMADA por el autor (2026-08-16)** — regla de veto no ejercida. La decisión incluyó el giro de dominio (sección más abajo): las alternativas LLM-agentes fueron presentadas explícitamente y el autor eligió BCI por el puente de carrera hacia neurotecnología. Detalle y consecuencias (tipo=Investigación, línea=Transformación Digital, datos públicos) en [[Decisiones|D-004]]. La selección NO se reabre.

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

## 🔀 Giro de dominio evaluado y RESUELTO (2026-08-16): se mantiene BCI

Al cerrar la sesión se encontró en el vault un documento nuevo — [[../30-TFG/Seleccion-Tema/Alternativas-Fuera-de-BCI-2026-08-16|Alternativas fuera de BCI]] — que plantea **temas de Ingeniería de Software × sistemas LLM/agentes** (testing de regresión de agentes conversacionales, evaluación de agentes de voz en español, benchmarks): el dominio que el autor ejerce a diario en Evoltis. El documento sigue la calibración correcta y contiene una observación clave: *tras 30 temas BCI sin que ninguno encienda — incluido el de mayor motivación declarada — el candidato a problema puede ser el dominio, no la lista.*

**Resolución (2026-08-16)**: el dilema (a) BCI vs (b) LLM-agentes fue presentado al autor con ambas opciones completas. El mentor recomendó el tema B (evaluación de agentes de voz); **el autor eligió BCI** priorizando el puente de carrera hacia neurotecnología/maestría. Registrado en [[Decisiones|D-004]]. Los temas A/B/C quedan en el vault como material de referencia (posibles publicaciones laterales), NO como candidatos de TFG. Sus citas siguen ⚠️ SIN VERIFICAR.

## ⏭️ Próximos pasos (en orden)

**Corrección de proceso (2026-08-16, aportada por el autor)**: NO existe una fecha de Módulo 0. El proceso real es: presentar el/los temas en Word según el estándar oficial → el tutor aprueba o rechaza las ideas. Estrategia acordada: presentar la propuesta confirmada; si el autor luego quiere un seguro contra rechazo, el tema 19 ya tiene su Word listo como segunda idea (misma línea temática). Regla vigente: dos ideas EN EL DOCUMENTO es aceptable; trabajar dos temas en paralelo hasta etapas avanzadas, NO (es el patrón de búsqueda infinita).

1. **[BLOQUEANTE — en manos del autor] Enviar al tutor el Word del tema confirmado**: `30-TFG/Seleccion-Tema/Tamagusuku_Agustin - Trabajo de Investigacion - Tema 28 Resiliencia.docx` (generado 2026-08-16, formato verificado contra la plantilla oficial). Antes de enviar: completar Documento y Legajo (dice "Completar").
2. **Prueba de humo** (3 hs de sábado): `pip install bcipy` + hola mundo de BciPy y MEDUSA — primer contacto real con los frameworks que la tesis va a evaluar.
3. Regenerar presentación NotebookLM del tema confirmado (prompts listos).
4. Pendientes menores: repositorio PUCE caído (reintentar); texto completo tesis Uniandes (anti-bot); completar revista/DOI exactos de la cita de MEDUSA (quedó fuera del Word por estar incompleta).

## 🗂️ Estado del repo

- Rama de trabajo: `feat/temas-candidatos-tfg` (~25 commits de selección de tema) → **mergeada a `main` al cierre de esta sesión** para que toda sesión/herramienta nueva vea el estado completo.
- Remoto: https://github.com/agustama27/TESIS (privado, cuenta personal).
