# Registro de decisiones

> Formato ADR-lite: una decisión por entrada. Qué se decidió, por qué, alternativas descartadas.

## D-001 · 2026-08-09 · Vault de Obsidian + Git como sistema de trabajo agnóstico

**Decisión**: todo el conocimiento y progreso vive en este vault (Markdown puro) versionado en GitHub. Las instrucciones para agentes de IA viven en `AGENTS.md`; `CLAUDE.md` solo lo referencia.

**Por qué**: portabilidad total — cualquier PC, cuenta o herramienta (Claude Code, OpenCode, Codex) puede continuar el trabajo clonando el repo. Nada queda atado a una herramienta.

**Alternativas descartadas**: Notion (no versionable en git, atado a la cuenta), memoria interna de una herramienta de IA (no portable).

## Decisiones pendientes (tomar al cerrar Etapa 0 / en Etapa 1)

- [ ] D-002: Tipo de TFG — Prototipado tecnológico vs. Trabajo de investigación.
- [ ] D-003: Línea temática (IRREVERSIBLE) — Transformación digital vs. Educación digital.
- [ ] D-004: Fuente de datos EEG — hardware propio vs. datasets públicos.
