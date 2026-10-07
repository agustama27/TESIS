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

## D-004 · 2026-08-16 · Dominio y tema del TFG: BCI — propuesta 28+28.1+capa IA — **ESTADO: PRELIMINAR**

> ⚠️ **Corrección del mismo día**: horas después de esta elección, el autor aclaró que **la decisión definitiva aún no está tomada**. D-004 queda como preferencia preliminar registrada, no como decisión firme. La decisión definitiva se tomará con/tras el proceso de aprobación del tutor.

**Decisión (preliminar)**: el autor eligió en sesión la propuesta del mentor como tema del TFG: **"Evaluación de resiliencia de frameworks BCI open source mediante inyección de fallos, con medición del impacto en la precisión del decodificador"** (tema 28 + expansión 28.1 + capa IA falla→error del modelo). La decisión se tomó con la alternativa completa sobre la mesa: el documento [[../30-TFG/Seleccion-Tema/Alternativas-Fuera-de-BCI-2026-08-16|Alternativas fuera de BCI]] (temas LLM-agentes A/B/C, dominio laboral del autor) fue presentado explícitamente como opción (a) vs (b) y el autor eligió BCI.

**Por qué**: BCI es el puente declarado de carrera hacia neurotecnología/maestría (meta registrada en `AGENTS.md`). La alternativa LLM-agentes ofrecía curva de aprendizaje nula y motivación presunta máxima, pero el autor priorizó el objetivo de carrera sobre la comodidad del dominio conocido. La propuesta elegida tiene hueco verificado dos veces, plantilla metodológica publicada (arXiv 2404.06203) y es ejecutable sin hardware ni GPU.

**Alternativas descartadas**: temas A/B/C de LLM-agentes (quedan documentados en el vault por si sirven para publicaciones laterales — NO como tema de TFG); temas BCI finalistas 28.2, 24 y 19 (regla de veto no ejercida).

**Consecuencias condicionales** (SI este tema se confirma definitivamente):
- Tipo de TFG: **Trabajo de Investigación**.
- Línea temática (IRREVERSIBLE): **Transformación Digital**.
- Fuente de datos: **datasets públicos, sin hardware propio**.

**Regla vigente aun con la decisión abierta**: NO se generan temas nuevos ni se reabre la exploración — la decisión definitiva es entre los candidatos ya documentados (propuesta 28+28.1+IA, finalistas BCI 19/24/28.2, alternativas LLM A/B/C con citas sin verificar).

## Decisiones pendientes

- [x] **D-004 (definitiva, 2026-09-07)**: el autor entregó el Entregable 1 del Seminario Final con el tema 28 en su formulación vigente ("Interfaces cerebro-computadora bajo condiciones adversas: del software a la decodificación"). La decisión quedó tomada por el acto de entrega; sujeta a la devolución del tutor.
- [x] D-005 (2026-09-07): Tipo = Trabajo de Investigación · Línea = Transformación Digital (declarados en la portada del Entregable 1).
- [x] D-006 (2026-09-07): Fuente de datos = BCI Competition IV 2a (BNCI2014_001 vía MOABB), sin hardware propio.

## D-007 · 2026-09-07 · Modelos de fallo definidos sobre la interfaz de transporte, no como fallas del protocolo LSL

**Decisión**: los cuatro modelos de fallo (pérdida de muestras, *jitter*, retraso, desconexión) se definen como perturbaciones observables del flujo que entra al pipeline. Pérdida se aplica al contenido; *jitter*/retraso al instante de entrega; desconexión al transporte real (cerrar y recrear el flujo), y es la única que ejercita directamente los mecanismos que LSL declara.

**Por qué**: LSL transmite por TCP; una pérdida de paquetes de red no elimina muestras, las demora. La pérdida real ocurre antes de LSL (dispositivo) o por saturación del búfer del consumidor (documentado en la FAQ de LSL). Definirlos como "fallas de LSL" habría sido un error de validez de constructo señalado por un revisor externo y verificado contra las fuentes.

**Alternativas descartadas**: perturbar la red real con herramientas de emulación (evalúa TCP más que el pipeline; queda como extensión); simular solo omisión de datos (no ejercitaría la reconexión declarada).

**Consecuencias**: diseño por bloques (corridas 1-5 campaña, 6 piloto), comparación siempre misma corrida con/sin fallo, umbral y ventana móvil en la misma escala, unidad estadística = sujeto. Detalle en [[../30-TFG/Entregas/Modulo-1/Decisiones-Metodologicas-Entregable-1|Decisiones-Metodologicas-Entregable-1]].

## D-008 · 2026-09-26 · Recorte de alcance del Entregable 2: 2 corridas por bloque en lugar de 5

- **Decisión (autor)**: entregar el 28/09 con campaña reducida en vez de pedir prórroga. Se reduce de 5 a **2 corridas** de la sesión de evaluación por sujeto (corridas 1 y 2); se mantienen los **9 sujetos** y las **12 condiciones de fallo** (4 tipos × 3 severidades). Total: 234 ejecuciones.
- **Por qué así**: la unidad estadística es el sujeto (Métodos); recortar sujetos o condiciones cambiaría la pregunta, recortar réplicas por bloque solo reduce la robustez de la mediana por sujeto. El Métodos corregido lo declara como limitación y reserva el diseño completo (5 corridas) para el módulo siguiente.
- **Regla del ejecutor**: campaña por bloques completos (corrida 1 de todos, luego corrida 2) para que una interrupción deje bloques analizables.

## D-009 · 2026-09-26 · Campaña en VM Linux dedicada (AWS c6i.2xlarge, us-east-1)

- **Decisión (autor)**: correr piloto y campaña en una instancia AWS c6i.2xlarge (8 vCPU, 16 GiB, Ubuntu 24.04), plan pago con crédito inicial.
- **Por qué**: (1) el temporizador de Windows resuelve ~15 ms y la severidad mínima de jitter es 10 ms; (2) máquina dedicada = sin contención de CPU ajena a las mediciones; (3) hardware fijo y documentable para replicabilidad; (4) instancias burstable (t3) y Spot descartadas por estrangulamiento de CPU e interrupción.
- **Costo estimado**: 0,34 USD/h; 10-25 USD en total, cubiertos por el crédito. Terminar (no detener) la instancia al cerrar.

## D-010 · 2026-10-07 · Campaña exploratoria post hoc (familia 3) para el Módulo 3

- **Decisión (autor)**: correr en la VM una tercera familia de condiciones, declarada exploratoria y posterior a ver los resultados del E2: barrido de exposición (2/5/10/20 cortes de 1 s por corrida), retención de la última muestra en el ensayo (`hold_trial` 10/25/40 %), diagnóstico del piso con cortes de 1,25/1,75/2,25 s y una referencia repetida como control de máquina. 387 ejecuciones, 0 fallidas.
- **Por qué**: probar las dos explicaciones de la Discusión (exposición y falla silenciosa) en lugar de solo argumentarlas, y discriminar la forma del piso de reconexión.
- **Estado**: **sin decidir si entra al manuscrito** (Métodos + Resultados corregidos) o queda como línea futura. La Discusión no puede introducir datos que no estén en Resultados. Detalle en [[../30-TFG/Analisis-M3-campana-exploratoria|Analisis-M3-campana-exploratoria]] y [[../30-TFG/Traspaso-Entrega-3|Traspaso-Entrega-3]].
