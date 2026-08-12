# Harness de subagentes — TFG BCI

> Los 6 agentes viven en `.claude/skills/` **dentro de este repo**, versionados y portables.
> `opencode.json` mapea esa misma ruta, así que OpenCode los lee sin cambios. Son archivos Markdown: cualquier herramienta puede leerlos.

## Principio de dirección de dependencia

Esta es la regla de arquitectura que ordena todo el harness:

```
   Vault (fuente de verdad · git · portable)   ←── SIEMPRE se escribe
      ▲
      │ opcionalmente enriquecido por
      │
   Engram (caché operativo · local a una máquina)
```

Engram acelera, no habilita. Un agente que no encuentra Engram **sigue funcionando** leyendo el vault, y lo anota en `risks_and_caveats`.

El motivo es [[Decisiones|D-001]]: portabilidad total. Si el pipeline de estudio dependiera de Engram, la tesis quedaría atada a esta PC — exactamente lo que el sistema busca evitar.

Corolario: **ningún conocimiento queda solo en Engram.** Todo hallazgo relevante termina como nota del vault vía `obsidian-scribe`.

## Los seis agentes

| Agente | Rol | Escribe en el vault |
|---|---|---|
| `bci-explorer` | Busca literatura académica (PubMed, arXiv, IEEE, Semantic Scholar) y evalúa relevancia | No — delega en scribe |
| `bci-tutor` | Explica conceptos con analogías ML/AI/SE, propone ejercicios | Sí — preguntas abiertas |
| `bci-synthesizer` | Sintetiza fuentes; NotebookLM opcional para mapa mental e infografía | No — delega en scribe |
| `bci-concept-mapper` | Meta-agente: consolida, detecta gaps, prioriza qué estudiar | Sí — mapa y roadmap |
| `obsidian-scribe` | **Único escriba estructurado**: notas, bitácora, decisiones, commits | Sí |
| `tfg-editor` | **Verifica** las entregas: formato, citas, línea temática. No redacta | Solo correcciones |

### Por qué un solo escriba

Si cada agente escribiera con su criterio, el vault tendría cinco formatos de nota distintos y el grafo no serviría. La consistencia del formato **es** el producto: es lo que hace que dentro de seis meses puedas navegar 80 notas y entender cómo se conectan.

## Dos reglas duras

**1. Verificación de citas.** Ninguna referencia puede salir de la memoria del modelo. Toda cita APA proviene de una fuente efectivamente descargada o con DOI resoluble. Lo no verificable se marca `⚠️ SIN VERIFICAR` y no entra al TFG hasta resolverse.

Una cita inventada en una tesis no es un bug menor: es un problema de credibilidad que se paga en la defensa.

**2. `tfg-editor` verifica, no redacta.** El TFG se defiende oralmente ante una Comisión Académica Evaluadora que pregunta *por qué* elegiste cada cosa. Un texto que no pensaste no se puede defender, y la autoría del trabajo es tuya. El agente chequea formato, cruza citas y detecta desvíos; vos escribís.

## Pipeline de una sesión de estudio

```
1. bci-concept-mapper (priority-only) ──→ ¿qué estudio hoy?
2. bci-explorer          ──→ fuentes curadas y verificadas
3. bci-synthesizer       ──→ síntesis narrativa (NotebookLM si está disponible)
4. bci-tutor             ──→ dudas puntuales durante el estudio
5. obsidian-scribe       ──→ vuelca todo al vault + bitácora + commit
6. bci-concept-mapper (update) ──→ actualiza mapa y gaps
```

En Etapa 0 el pipeline completo es innecesario: alcanza con **`bci-tutor` + `obsidian-scribe`**. El plan de estudio ya está en [[Plan-Etapa-0]] y responde solo el paso 1. Los demás agentes ganan sentido en Etapa 2, cuando el espacio de búsqueda se abre y hay que relevar estado del arte.

## Convención de Engram

- **Proyecto**: `tesis` (Engram lo autodetecta por el repo git, `project_source: git_child`).
- **Namespace de topics**: `bci/...`
- Recuperación en dos pasos: `mem_search` devuelve resultados truncados → siempre `mem_get_observation(id)` para el contenido completo.

| Artefacto | Topic key |
|---|---|
| Exploración por tema | `bci/{tema}/exploration` |
| Síntesis NotebookLM | `bci/{tema}/notebooklm` |
| Q&A del tutor | `bci/qa/{concepto}` |
| Mapa conceptual | `bci/concept-map` |
| Progreso de estudio | `bci/study-progress` |
| Log de volcado al vault | `bci/vault/sync-log` |
| Estado de entrega TFG | `bci/tfg/{entrega-n}/draft-status` |

## Origen y correcciones aplicadas

Las 4 skills BCI originales vivían en `Desktop\Investigación_BCI\` — **sin control de versiones**. Al integrarlas se corrigió:

| Problema | Corrección |
|---|---|
| Carpeta sin git: pérdida total ante falla de disco | Movidas a este repo, versionadas y pusheadas |
| `mcp__engram__*` no coincide con el servidor real | → `mcp__plugin_engram_engram__*` |
| Tres namespaces conviviendo (`Investigación_BCI`, `bci-thesis`, `tesis`) | Unificado a `tesis` |
| `bci-tutor` escribía en Notion (atado a cuenta, no versionable) | Migrado al vault |
| Engram como bus obligatorio de handoffs | Invertido: vault fuente de verdad, Engram caché |
| NotebookLM como dependencia dura | Degradación a `synthesis-only` si no está disponible |
| `tfg-editor` redactaba las entregas | Reformulado a verificador |
