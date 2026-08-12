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

## D-003 · 2026-08-12 · Harness de subagentes con el vault como fuente de verdad

**Decisión**: se integran 6 subagentes en `.claude/skills/` dentro de este repo. El **vault es la fuente de verdad y Engram un caché opcional** — invirtiendo la dependencia que proponía el documento original, donde Engram era el bus obligatorio de handoffs. `obsidian-scribe` es el único agente con escritura estructurada. `tfg-editor` verifica las entregas pero no las redacta.

**Por qué**: Engram es una base local de esta máquina — no viaja al repo ni existe en OpenCode o Codex. Un pipeline que lo requiere ataría la tesis a esta PC, contradiciendo [[Decisiones|D-001]]. Con la dependencia invertida, el harness funciona en cualquier herramienta y el conocimiento sobrevive en git.

Sobre `tfg-editor`: el TFG se defiende oralmente ante una Comisión Académica Evaluadora y la autoría es del estudiante. Un agente redactor comprometería la integridad del trabajo y la capacidad de defenderlo.

**Alternativas descartadas**: dejar las skills en `Desktop\Investigación_BCI\` (carpeta sin control de versiones — se perdía todo ante una falla de disco); mantener Notion como capa de conocimiento (atado a cuenta, no versionable); NotebookLM como dependencia dura (MCP no oficial con sesión que expira — quedó como opcional con degradación a `synthesis-only`).

**Correcciones técnicas aplicadas**: nombres de tools `mcp__engram__*` → `mcp__plugin_engram_engram__*`; namespace de Engram unificado a `tesis` (convivían `Investigación_BCI`, `bci-thesis` y `tesis`).

## Decisiones pendientes (tomar al cerrar Etapa 0 / en Etapa 1)

- [ ] D-004: Tipo de TFG — Prototipado tecnológico vs. Trabajo de investigación.
- [ ] D-005: Línea temática (IRREVERSIBLE) — Transformación digital vs. Educación digital.
- [ ] D-006: Fuente de datos EEG — hardware propio vs. datasets públicos.
