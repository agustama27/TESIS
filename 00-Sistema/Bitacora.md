# Bitácora de trabajo

> Una entrada por sesión de trabajo. Formato: fecha, qué se hizo, próximo paso. La entrada más reciente arriba.

## 2026-08-10 — Configuración del repositorio remoto

**Qué se hizo**:
- Definido el remoto: `https://github.com/agustama27/TESIS` (cuenta personal) → ver [[Decisiones]] D-002.
- Remoto configurado localmente con el usuario embebido en la URL.

**Bloqueo**: el push todavía no se hizo. El `gh` CLI de esta máquina está autenticado con la cuenta de trabajo (agustama-Evoltis), que no tiene acceso al repo; además el repo `agustama27/TESIS` no aparece entre los públicos de la cuenta, así que o no existe todavía o es privado.

**Próximo paso**: autenticar la cuenta personal (`gh auth login` → `gh auth switch --user agustama27`), crear el repo si no existe, y `git push -u origin main`.

## 2026-08-09 — Kickoff del proyecto

**Qué se hizo**:
- Leída la documentación oficial del TFG (Siglo 21): programa, guía de Seminario Final, tipos de TFG, líneas temáticas.
- Definido el roadmap por etapas (0 a 5) → ver [[Roadmap]].
- Creada la estructura del vault + harness agnóstico de herramientas (`AGENTS.md`).
- Inicializado repo git.

**Hallazgo clave**: la línea temática es irreversible y solo hay 3 opciones; el tema BCI debe encuadrarse (Transformación digital o Educación digital son las candidatas naturales).

**Próximo paso**: arrancar Etapa 0, Módulo 1 (neurociencia básica) → [[Plan-Etapa-0]].
