# Prompt de arranque: sesión de la Entrega 3 (Módulo 3: Discusión)

> Copiar como primer mensaje de una sesión nueva en `C:\Users\agustin.tamagusuku\Desktop\TESIS`. Escrito el 2026-10-07.

---

Hola. Soy Agustín, autor del TFG *Interfaces cerebro-computadora bajo condiciones adversas: del software a la decodificación* (Ingeniería en Software, Siglo 21; Trabajo de Investigación, línea Transformación Digital). En esta sesión trabajamos a fondo la **Entrega 3**: Introducción, Métodos y Resultados corregidos, más la **Discusión** (lo nuevo, unas 10 páginas) y un único listado de Referencias.

**Antes de responder, leé en este orden:**
1. `TESIS/30-TFG/Traspaso-Entrega-3.md`: consigna verificada, punto de partida, hallazgos por objetivo, decisiones pendientes y pendientes. Es la nota central.
2. `TESIS/30-TFG/Mejoras-Redaccion-M3.md`, sobre todo la sección C (correcciones pendientes C1-C8).
3. `TESIS/30-TFG/Patrones-Tesis-Cassi.md`: el molde de Discusión de los TFG aprobados.
4. El manuscrito vigente (E2 v6): `TESIS/30-TFG/Entregas/Modulo-2/src/contenido.js` y `resultados.js`.
5. Según lo que haga falta, el detalle de cada hallazgo: `TESIS/30-TFG/Analisis-M3.md`, `Analisis-M3-ensayos-divergencia.md`, `Analisis-M3-campana-exploratoria.md` y `Fundamentos-Diseno-Estadistico.md`.
6. Engram, proyecto `tesis`: buscá `tfg/entregable-2` y la sesión del 2026-10-07.

**Reglas duras:**
- Ninguna cita ni afirmación de hecho sin fuente primaria verificada; lo dudoso va marcado ⚠️ SIN VERIFICAR. El paper interno sobre λ·n (Evoltis) es confidencial: no se cita ni va al vault.
- Commits solo cuando yo lo pida, con *conventional commits* y nunca con atribución de IA.
- No regenerar el PDF ni el Word sin que lo pida. Antes de cada versión nueva, respaldar las fuentes. La versión de la Entrega 3 va en `TESIS/30-TFG/Entregas/Modulo-3/` (copiá `src/` desde `Modulo-2/` cuando arranquemos a editar).
- La Discusión no introduce datos nuevos: todo lo que discuta tiene que estar antes en Resultados.
- No cambiar el tema, el título ni las cifras sin datos; no escribir en primera persona; APA 7 como en el resto del manuscrito.
- **Otra sesión sigue abierta** cerrando una prueba en la VM de AWS (mecanismo del piso de reconexión de LSL con `MulticastMinRTT`). No toques `Analisis-M3-campana-exploratoria.md`, el repo `C:\Users\agustin.tamagusuku\Desktop\bci-fault-bench` ni la VM: esa sesión escribe ahí el resultado.
- Una pregunta por vez. Sé crítico: si algo que propongo está mal, decímelo con la evidencia.
- Yo defiendo esto oralmente: cuando escribas algo, explicame el porqué.

**Cómo arrancamos:** primero resolvemos, de a una, las dos decisiones que bloquean (sección 4 del traspaso): qué dijo el profesor sobre el E2, y si la campaña exploratoria entra al manuscrito o queda como línea futura. Después armamos el esqueleto de la Discusión párrafo por párrafo, siguiendo el orden de los objetivos específicos, y recién entonces redactamos.
