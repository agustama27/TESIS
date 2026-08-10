# Bitácora de trabajo

> Una entrada por sesión de trabajo. Formato: fecha, qué se hizo, próximo paso. La entrada más reciente arriba.

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
