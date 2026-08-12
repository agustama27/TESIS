# AGENTS.md — Instrucciones para agentes de IA

> Este archivo es la fuente de verdad para CUALQUIER herramienta de IA (Claude Code, OpenCode, Codex, Cursor, etc.).
> Si sos un agente leyendo esto: seguí estas reglas antes que cualquier default propio.

## Contexto del proyecto

Este repositorio es un **Vault de Obsidian** que contiene todo el trabajo del **Trabajo Final de Graduación (TFG)** de Agustín Tamagusuku para la carrera **Ingeniería en Software** (Universidad Siglo 21).

- **Tema objetivo**: NeuroIngeniería / Interfaces Cerebro-Computadora (BCI), encuadrado en una línea temática de la universidad.
- **Meta de carrera**: que la tesis sirva como antecedente para maestría/doctorado o trabajo en neurotecnología.
- **Restricciones de la universidad**: ver `Trabajo Final de Graduación-Notas/` (líneas temáticas, formato de entregas, 4 entregas en 4 meses).

## Estructura del vault

| Carpeta | Contenido |
|---|---|
| `00-Sistema/` | Roadmap, bitácora de sesiones, registro de decisiones |
| `10-Fundamentos/` | Notas de aprendizaje de la Etapa 0 (neurociencia, BCI, señales) |
| `20-Investigacion/` | Papers, estado del arte, resúmenes con cita APA |
| `30-TFG/` | Documentos de las entregas oficiales del Seminario Final |
| `40-Prototipo/` | Código y experimentos (cuando exista) |
| `.claude/skills/` | Los 6 subagentes del harness (Markdown, legibles por cualquier herramienta) |
| `Trabajo Final de Graduación-Notas/` | Documentación oficial de la universidad (solo lectura) |

## Loop de trabajo (obligatorio para agentes)

Al **iniciar** una sesión:
1. Leer `00-Sistema/Roadmap.md` → identificar etapa actual y próximo hito.
2. Leer las últimas entradas de `00-Sistema/Bitacora.md`.

Al **cerrar** una sesión (o completar trabajo significativo):
1. Agregar entrada en `00-Sistema/Bitacora.md` (fecha, qué se hizo, próximo paso).
2. Registrar decisiones importantes en `00-Sistema/Decisiones.md`.
3. Commit en git con conventional commits (`docs:`, `feat:`, `chore:`...). **Nunca** agregar "Co-Authored-By" ni atribución de IA.

## Subagentes

Seis agentes especializados en `.claude/skills/`. Detalle completo en `00-Sistema/Subagentes-Harness.md`.

`bci-explorer` (busca literatura) · `bci-tutor` (explica conceptos) · `bci-synthesizer` (sintetiza fuentes) · `bci-concept-mapper` (consolida y prioriza) · `obsidian-scribe` (escribe el vault) · `tfg-editor` (verifica las entregas)

Tres reglas que gobiernan a todos:

1. **El vault es la fuente de verdad; Engram es un caché opcional.** Si Engram no está disponible, el agente sigue funcionando leyendo el vault. Ningún conocimiento queda solo en Engram.
2. **`obsidian-scribe` es el único con escritura estructurada.** Los demás investigan y delegan en él. Así el formato de las notas se mantiene consistente y el grafo sirve para algo.
3. **Ninguna cita sale de la memoria del modelo.** Toda referencia APA proviene de una fuente descargada o con DOI resoluble. Lo dudoso se marca `⚠️ SIN VERIFICAR`.

`tfg-editor` **verifica, no redacta**: el TFG se defiende oralmente y la autoría es del estudiante.

## Convenciones

- Idioma: **español** para todas las notas (el TFG se entrega en español). Términos técnicos en inglés se mantienen.
- Formato: Markdown compatible con Obsidian. Usar wikilinks `[[Nota]]` para conectar conceptos (esto construye el grafo de conocimiento).
- Toda fuente/paper citada debe registrarse en formato **APA** en la nota correspondiente de `20-Investigacion/`.
- Nombres de archivo: sin caracteres especiales problemáticos, con guiones (`Plan-Etapa-0.md`).
- No modificar los documentos de `Trabajo Final de Graduación-Notas/` (material oficial de la universidad).

## Reglas duras del TFG (de la universidad — no negociables)

- La línea temática se elige UNA vez y no se cambia: opciones = Transformación digital | Plataformas de desarrollo | Educación digital.
- Tipos de TFG: Trabajo de investigación **o** Prototipado tecnológico.
- Entregas en Word: Times New Roman 12, interlineado 1,5, sangría 1,27 cm, justificado. Títulos TNR 14 negrita centrado, subtítulos TNR 12 cursiva a la izquierda.
- Citas bajo normas APA.
- Aprobar 3 primeras entregas con ≥50% y la cuarta (obligatoria) con ≥50%.
