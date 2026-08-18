# ESTADO ACTUAL DEL PROYECTO — documento de traspaso entre sesiones

> **Escrito: 2026-08-16, al cierre de la sesión de kickoff/selección de tema (sesión larga, ~2 semanas).**
> **Toda sesión nueva debe leer este documento PRIMERO**, después [[Bitacora]] y [[Roadmap]].

---

## 🎯 Dónde está parado el proyecto HOY

**Fase**: selección de tema — **decisión definitiva PENDIENTE**. El 2026-08-16 el autor eligió preliminarmente BCI (propuesta 28+28.1+capa IA) en sesión, pero horas después aclaró que **aún no tiene la decisión tomada de forma definitiva**. Ver [[Decisiones|D-004]] (estado: preliminar).

**Tema candidato principal** (elegido por el mentor tras ~30 temas explorados; preferencia preliminar del autor el 2026-08-16 con la alternativa LLM-agentes sobre la mesa):

> **"Evaluación de resiliencia de frameworks BCI open source mediante inyección de fallos, con medición del impacto en la precisión del decodificador."**
> Tema 28 + expansión 28.1 (robustez/chaos engineering) + capa IA (función de transferencia falla-de-software → error-del-modelo).
> Trabajo de Investigación · línea Transformación Digital · sin hardware, sin GPU, datos públicos.

**Estado de la decisión**: 🟡 **PRELIMINAR, NO definitiva** (corrección del autor, 2026-08-16). En sesión el autor eligió BCI frente a la alternativa LLM-agentes (por el puente de carrera hacia neurotecnología), pero luego aclaró que la decisión definitiva sigue abierta. El proceso real de la universidad es el que decide: se presentan idea(s) en Word al tutor y él aprueba. El Word del tema 28 ya está generado y listo. Consecuencias condicionales al tema (tipo=Investigación, línea=Transformación Digital, datos públicos) en [[Decisiones|D-004]]. **Regla que sigue vigente**: NO se generan temas nuevos — la decisión es entre los candidatos ya documentados.

**Esquema visual de la propuesta** (para mostrar al tutor): https://claude.ai/code/artifact/2b87500e-b857-4f89-b859-f614e57479ae

## ✅ Qué respalda la propuesta

- Hueco verificado DOS veces y **REFINADO el 2026-08-16 tras auditoría externa**: el paper de LSL (PMC12434378, verificado por fetch) SÍ declara mecanismos de recuperación y dice hacer stress-tests con desconexiones — pero **sin métricas cuantitativas** (ni tasas de pérdida, ni tiempos de recuperación), con pruebas formales solo en condiciones ideales, y **sin medir jamás el impacto sobre el decodificador aguas abajo**. Formulación correcta del hueco: *no existe evaluación independiente y cuantitativa del comportamiento bajo fallas, ni medición de su propagación a la decodificación* — el mismo patrón que Secure LSL (<5% autoreportado → la verificación independiente es el aporte). La frase absoluta "nadie evaluó la capa de software" NO debe usarse.
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

## 🔀 Giro de dominio evaluado (2026-08-16): preferencia preliminar por BCI

Al cerrar la sesión se encontró en el vault un documento nuevo — [[../30-TFG/Seleccion-Tema/Alternativas-Fuera-de-BCI-2026-08-16|Alternativas fuera de BCI]] — que plantea **temas de Ingeniería de Software × sistemas LLM/agentes** (testing de regresión de agentes conversacionales, evaluación de agentes de voz en español, benchmarks): el dominio que el autor ejerce a diario en Evoltis. El documento sigue la calibración correcta y contiene una observación clave: *tras 30 temas BCI sin que ninguno encienda — incluido el de mayor motivación declarada — el candidato a problema puede ser el dominio, no la lista.*

**Estado (2026-08-16)**: el dilema (a) BCI vs (b) LLM-agentes fue presentado al autor con ambas opciones completas. El mentor recomendó el tema B (evaluación de agentes de voz); el autor eligió **preliminarmente** BCI priorizando el puente de carrera hacia neurotecnología/maestría — pero luego aclaró que la decisión definitiva sigue pendiente. Registrado en [[Decisiones|D-004]] (preliminar). Las citas de los temas A/B/C siguen ⚠️ SIN VERIFICAR — si vuelven a considerarse, la verificación completa es prerequisito.

## ⏭️ Próximos pasos (en orden)

**Corrección de proceso (2026-08-16, aportada por el autor)**: NO existe una fecha de Módulo 0. El proceso real es: presentar el/los temas en Word según el estándar oficial → el tutor aprueba o rechaza las ideas. Estrategia acordada: presentar la propuesta confirmada; si el autor luego quiere un seguro contra rechazo, el tema 19 ya tiene su Word listo como segunda idea (misma línea temática). Regla vigente: dos ideas EN EL DOCUMENTO es aceptable; trabajar dos temas en paralelo hasta etapas avanzadas, NO (es el patrón de búsqueda infinita).

1. **[BLOQUEANTE — en manos del autor] Tomar la decisión definitiva de tema** (entre candidatos ya documentados: propuesta BCI 28+28.1+IA, finalistas BCI 19/24/28.2, alternativas LLM A/B/C) **y/o enviar al tutor el Word de idea(s)** para que el proceso de aprobación decida. **Entregable listo**: `30-TFG/Seleccion-Tema/Tamagusuku_Agustin - Trabajo de Investigacion.docx` (regenerado 2026-08-17 contra el PDF oficial "Selección Tema TFG - Seminario Final - ING SOFT": Arial 12, conteos de renglones respetados, 4 citas APA con autores verificados, contenido en la formulación vigente de pipelines). Antes de enviar: **completar Documento y Legajo**.
2. **Prueba de humo v3 — escalera de 4 PoCs** (sábado; reemplaza a la v2): según [[../30-TFG/Seleccion-Tema/Propuesta-Reformulacion-Tema-28|Propuesta-Reformulacion-Tema-28]] §22 — (1) BNCI2014_001 + CSP/LDA offline; (2) replay con MNE-LSL PlayerLSL; (3) primer fallo inyectado + comparación funcional; (4) detector de reglas vs modelo básico. Criterio de cierre en §23: si dataset+decoder+replay+una perturbación+telemetría+consecuencia medible funcionan → **el tema queda técnicamente viable y la decisión prácticamente cerrada**. ⚠️ Verificar ese día: docs de MNE-LSL PlayerLSL y carga de BNCI2014_001 vía MOABB.
3. Regenerar presentación NotebookLM del tema confirmado (prompts listos).
4. Pendientes menores: repositorio PUCE caído (reintentar); texto completo tesis Uniandes (anti-bot); completar revista/DOI exactos de la cita de MEDUSA (quedó fuera del Word por estar incompleta).

## 🗂️ Estado del repo

- Rama de trabajo: `feat/temas-candidatos-tfg` (~25 commits de selección de tema) → **mergeada a `main` al cierre de esta sesión** para que toda sesión/herramienta nueva vea el estado completo.
- Remoto: https://github.com/agustama27/TESIS (privado, cuenta personal).
