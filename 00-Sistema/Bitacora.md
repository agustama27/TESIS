# Bitácora de trabajo

> Una entrada por sesión de trabajo. Formato: fecha, qué se hizo, próximo paso. La entrada más reciente arriba.

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
