# Registro de decisiones

> Formato ADR-lite: una decisión por entrada. Qué se decidió, por qué, alternativas descartadas.

## D-001 · 2026-08-09 · Vault de Obsidian + Git como sistema de trabajo agnóstico

**Decisión**: todo el conocimiento y progreso vive en este vault (Markdown puro) versionado en GitHub. Las instrucciones para agentes de IA viven en `AGENTS.md`; `CLAUDE.md` solo lo referencia.

**Por qué**: portabilidad total — cualquier PC, cuenta o herramienta (Claude Code, OpenCode, Codex) puede continuar el trabajo clonando el repo. Nada queda atado a una herramienta.

**Alternativas descartadas**: Notion (no versionable en git, atado a la cuenta), memoria interna de una herramienta de IA (no portable).

## D-002 · 2026-08-10 · Repositorio en cuenta personal (agustama27), no en la de trabajo

**Decisión**: el remoto es `https://github.com/agustama27/TESIS`, bajo la cuenta personal de GitHub.

**Por qué**: la tesis es un proyecto personal de años y un antecedente de CV. Alojarla en la cuenta del empleador (agustama-Evoltis) implicaría perder el acceso al cambiar de trabajo — justo lo contrario de la portabilidad que busca este sistema.

**Consecuencia operativa**: `gh` CLI en esta máquina está autenticado con la cuenta de trabajo. Para pushear hay que agregar la cuenta personal (`gh auth login`) y cambiar a ella (`gh auth switch --user agustama27`). El remoto ya quedó configurado con el usuario embebido en la URL para evitar que el credential manager use la credencial equivocada.

## Decisiones pendientes (tomar al cerrar Etapa 0 / en Etapa 1)

- [ ] D-003: Tipo de TFG — Prototipado tecnológico vs. Trabajo de investigación.
- [ ] D-004: Línea temática (IRREVERSIBLE) — Transformación digital vs. Educación digital.
- [ ] D-005: Fuente de datos EEG — hardware propio vs. datasets públicos.
