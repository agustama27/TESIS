# Bitácora de trabajo

> Una entrada por sesión de trabajo. Formato: fecha, qué se hizo, próximo paso. La entrada más reciente arriba.

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
