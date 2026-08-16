# Bitácora de trabajo

> Una entrada por sesión de trabajo. Formato: fecha, qué se hizo, próximo paso. La entrada más reciente arriba.

## 2026-08-16 — DECISIÓN DE DOMINIO: BCI confirmado como tema del TFG

**Qué se hizo**:
- Sesión corta y decisiva: el autor vino a resolver el bloqueante de dominio planteado en [[ESTADO-ACTUAL]].
- Se presentaron las dos opciones completas: (a) propuesta BCI 28+28.1+capa IA, (b) alternativas LLM-agentes (temas A/B/C de [[../30-TFG/Seleccion-Tema/Alternativas-Fuera-de-BCI-2026-08-16|Alternativas fuera de BCI]]). El mentor recomendó el tema B (evaluación de agentes de voz) por el patrón de los 30 temas sin encender.
- **El autor eligió BCI — propuesta 28+28.1+capa IA** — priorizando el puente de carrera hacia neurotecnología. Registrado como [[Decisiones|D-004]]. La selección de tema queda CERRADA.

- **Corrección de proceso del autor**: no hay fecha de Módulo 0; el gate real es presentar el Word de idea(s) para aprobación del tutor. Estrategia: una idea fuerte ahora (la confirmada); el 19 queda como backup listo si hiciera falta una segunda. Dos ideas en el documento sí; dos temas en paralelo hasta etapas avanzadas, no.
- **Generado el Word oficial del tema 28**: `Tamagusuku_Agustin - Trabajo de Investigacion - Tema 28 Resiliencia.docx`, clonando el formato de la plantilla del tema 19 (validado + render verificado). Contenido: título, justificación de línea, explicación (28+28.1+capa IA), pregunta, 4 citas APA verificadas del vault (fault recovery arXiv 2404.06203, BCI-HIL, PyNoetic, LSL; MEDUSA excluida por DOI incompleto), justificación completa.

**Próximo paso**: el autor completa Documento/Legajo y envía el Word al tutor → prueba de humo (`pip install bcipy`, 3 hs de sábado).

## 2026-08-16 — Cierre de la sesión de selección: propuesta final sobre la mesa

**Qué se hizo (últimos días de la sesión)**:
- Sprint de descubrimiento de frameworks: tabla de salud GitHub (Timeflux posiblemente estancado; BciPy/MEDUSA/LSL activos), 6 ideas de expansión auditadas → 28.1 (robustez/fault injection) y 28.2 (costo de cifrado, con corrección: Secure LSL autoreporta <5%) pasan; 28.3 como envoltorio.
- Ramas laterales investigadas y cerradas: video Shainline (neuromórfico = inspiración, no tesis), Science Corp/Max Hodak (biohíbrido + PRIMA; veta de visión protésica anotada sin desarrollar).
- **Intervención de mentor**: declarada terminada la exploración (30 temas, patrón de búsqueda infinita). Propuesta elegida por el mentor con regla de veto: **28 + 28.1 + capa IA (falla→error del modelo)**. Esquema visual publicado.
- Creado [[ESTADO-ACTUAL]] como documento de traspaso; rama mergeada a main.

**Pendiente BLOQUEANTE**: confirmación o veto-con-causa del autor + fecha del Módulo 0.

## 2026-08-15 — Corrección de calibración: la vara estaba mal

**Qué se hizo**:
- Auditoría rigurosa del Tema 25 → se encontró que NeuroBench (consorcio, *Nature Communications*) ya publicó la comparación SNN vs ANN en decodificación motora ("primate reaching task"), y que la crítica al proxy energético también está publicada. Se dio el tema por muerto.
- El usuario pidió relevar tesis reales de grado en ingeniería sobre BCI. **Hallazgo correctivo**: descargada y analizada la tesis de UNSAM (Helguera, 2021, Ing. Biomédica, 141 pp.) — su objetivo completo fue *extender un sistema BCI existente de 2 a 3-4 opciones*. No probó con la población objetivo (quedó como trabajo futuro).
- Escrita [[Calibracion-Alcance-Tesis-BCI]]: la vara de un TFG es **ejecución rigurosa de un problema delimitado**, no originalidad mundial.
- **Tema 25 reactivado** con reformulación: implementación y evaluación comparativa usando NeuroBench como referente de contraste.

**Lección**: se venían descartando temas buenos aplicando estándar de paper de alto impacto. Para un TFG, que exista trabajo similar no invalida — obliga a declarar qué es replicación y qué es aporte propio.

**Próximo paso**: reevaluar los tres finalistas con la vara correcta.

## 2026-08-14 — Convergencia al tema de fidelidad + reestructura del vault

**Qué se hizo**:
- Investigada en profundidad la implementación de la tesis de **fidelidad brain-to-text** → [[Fidelidad-Brain-to-Text]]. Hallazgo clave: el protocolo de fidelidad existe en EEG no invasivo (modelos alimentados con ruido puro siguen generando frases fluidas — arXiv 2603.03312, Sci Reports 2025) pero NADIE lo aplicó a los sistemas intracorticales de alto rendimiento; Willett 2023 solo AFIRMA baja dependencia del LM. La tesis pone esa afirmación a prueba.
- Actualizada la lista maestra: **tema 19 (fidelidad) EN FOCO**; 7 en reserva; 11 descartados con motivo registrado. Rankings anteriores marcados como superados.
- Creada `30-TFG/Seleccion-Tema/` con **una página por tema (19 + índice) en el formato oficial** "Definiciones Iniciales TFG" del PDF de la universidad; ampliaciones en páginas separadas de `20-Investigacion/`.

**Próximo paso**: decisión final del usuario sobre el tema 19 → redactar el documento Word oficial de presentación.

## 2026-08-12 — Investigación urgente: 15 temas candidatos para el TFG

**Contexto**: deadline de <10 hs para definir el tema. Se adelanta la selección de tema (Etapa 1) por delante de la Etapa 0, que se reubicará después.

**Qué se hizo**:
- Leído el PDF oficial "Selección Tema TFG": exige tipo, línea, título ~12 palabras, justificaciones y 4 citas APA verificadas.
- Relevados repositorios: Siglo 21 (sin tesis BCI indexadas → vacancia), UNC, UTN; precedentes de grado en Chile/Ecuador confirman factibilidad.
- Verificada literatura ancla por familia: EEGNet, LaBraM (ICLR 2024), spellers P300 (review ACM 2024), neurofeedback en aulas, Muse/Krigolson, MI-BCI post-ACV, SSVEP, emociones DEAP.
- Escrito [[Temas-Candidatos-TFG]] con 15 fichas (tipo, línea, pregunta, datos, pros/contras, impacto CV, literatura con estado de verificación) + ranking recomendado.

**Recomendación registrada**: 🥇 foundation models EEG (tema 2) · 🥈 transfer learning entre sujetos (4) · 🥉 speller P300 (3). Descartar los dependientes de hardware si no hay equipo en mano.

**Próximo paso**: el usuario elige tema → correr bci-explorer para las 4 citas APA definitivas → redactar el doc de presentación con la plantilla del PDF.

## 2026-08-12 — Integración del harness de subagentes

**Qué se hizo**:
- Analizado el documento `Subagentes-Harness.md` propuesto. Se detectaron tres defectos verificables: la carpeta `Investigación_BCI` no estaba bajo git, los nombres de tools MCP no coincidían con los servidores reales, y convivían tres namespaces de Engram.
- Movidas las 4 skills BCI al repo (`.claude/skills/`), corregidas y versionadas.
- Migrado `bci-tutor` de Notion al vault; creados `obsidian-scribe` y `tfg-editor`.
- Invertida la dependencia Engram↔vault → ver [[Decisiones|D-003]].
- Documentado el harness en [[Subagentes-Harness]] y en `AGENTS.md`.

**Hallazgo clave**: el harness propuesto usaba Engram como bus obligatorio de handoffs. Engram es local a esta máquina, así que el pipeline entero se rompía al cambiar de PC o herramienta — justo lo contrario de D-001. El vault pasó a ser la fuente de verdad.

**Próximo paso**: arrancar Etapa 0, Módulo 1 (neurociencia básica) usando `bci-tutor` + `obsidian-scribe` → [[Plan-Etapa-0]].

## 2026-08-10 — Configuración del repositorio remoto

**Qué se hizo**:
- Definido el remoto: `https://github.com/agustama27/TESIS` (cuenta personal) → ver [[Decisiones]] D-002.
- Remoto configurado localmente con el usuario embebido en la URL.

- Autenticada la cuenta personal en `gh` y ejecutado `gh auth setup-git`, para que git use esa credencial en vez del token de trabajo cacheado en el Windows Credential Manager.
- **Push realizado**: `main` publicado en el remoto y trackeando `origin/main`. El repo es privado.

**Nota para otra máquina**: si el push falla con "repository not found" teniendo permisos, casi seguro es el credential helper reusando la credencial equivocada. Se resuelve con `gh auth switch --user agustama27` + `gh auth setup-git`.

**Próximo paso**: arrancar Etapa 0, Módulo 1 (neurociencia básica) → [[Plan-Etapa-0]].

## 2026-08-09 — Kickoff del proyecto

**Qué se hizo**:
- Leída la documentación oficial del TFG (Siglo 21): programa, guía de Seminario Final, tipos de TFG, líneas temáticas.
- Definido el roadmap por etapas (0 a 5) → ver [[Roadmap]].
- Creada la estructura del vault + harness agnóstico de herramientas (`AGENTS.md`).
- Inicializado repo git.

**Hallazgo clave**: la línea temática es irreversible y solo hay 3 opciones; el tema BCI debe encuadrarse (Transformación digital o Educación digital son las candidatas naturales).

**Próximo paso**: arrancar Etapa 0, Módulo 1 (neurociencia básica) → [[Plan-Etapa-0]].
