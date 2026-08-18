# Prompts para presentaciones en NotebookLM

> 2026-08-14 · Para regenerar las presentaciones de los temas finalistas con estructura controlada.
> Uso: crear un notebook por tema, adjuntar como fuentes los `.md` indicados, pegar el prompt en el cuadro de personalización al generar la presentación.

## Evaluación de la presentación existente (Auditing_Brain_to_Text_Fidelity.pdf, 12 láminas)

**Lo bueno**: arco narrativo correcto tomado de las fuentes (dos motores en serie con analogía del autocorrector; el vacío EEG-vs-intracortical con referencias correctas; diseño experimental como auditoría; matriz de impacto win-win; cierre de agencia comunicativa muy fuerte).

**Para corregir en la regeneración**:
1. Lámina 6: línea duplicada ("Alucinación: Comprobada" ×2).
2. Lámina 11: dice "Trabajo de Fin de Grado" (España) — debe ser **Trabajo Final de Graduación**.
3. Faltan láminas: pregunta de investigación explícita · plan de 4 meses por entregas · viabilidad de recursos · la distinción "auditar, no mejorar el 97,5%" con analogía del examen.
4. Pedir **notas del orador** por lámina.

## Prompt — Tema 19 (Fidelidad)

Fuentes a adjuntar: `Tema-19-Fidelidad-Brain-to-Text.md`, `Fidelidad-Brain-to-Text.md`, `Decodificacion-Brain-to-Text.md`.

```
Presentación de 12-14 láminas en español rioplatense neutro para defender un tema de tesis ante un tutor de Ingeniería en Software que NO conoce el campo BCI. Usar siempre "Trabajo Final de Graduación (TFG)". Una sola idea por lámina, lenguaje simple, explicar todo término técnico con analogía cotidiana (ej.: modelo de lenguaje = autocorrector del teléfono). Estructura obligatoria: (1) portada con título, tipo "Trabajo de Investigación" y línea "Transformación Digital"; (2) el problema humano: parálisis total, ELA, pérdida de comunicación; (3) la solución existente: sistemas brain-to-text, 97,5% de precisión (Card 2024, NEJM); (4) anatomía del sistema: decodificador neural + modelo de lenguaje en serie; (5) LA DISTINCIÓN CENTRAL: esta tesis NO busca mejorar el 97,5%, busca AUDITARLO — analogía del alumno que saca 97,5: ¿sabía o adivinó?; (6) la evidencia de alarma: en EEG no invasivo, modelos con ruido puro generan frases fluidas; (7) el vacío: nadie auditó los sistemas intracorticales; solo existe la afirmación de Willett sin verificación; (8) pregunta de investigación textual; (9) diseño experimental: reproducción → ablación → degradación → medición (PER/WER, tasa de alucinación); (10) validación: datasets públicos de Stanford con respuesta correcta incluida, población = oraciones, test estadístico pareado; (11) valor garantizado: fidelidad alta = verificación de Nature; baja = hallazgo de confiabilidad — ningún resultado es fracaso; (12) plan de 4 meses mapeado a las 4 entregas del Seminario Final; (13) recursos: datos gratis, código público, Colab Pro; (14) cierre emotivo: agencia comunicativa — que las palabras pertenezcan a su autor. Incluir notas del orador por lámina (2-3 oraciones para decir en voz alta). No inventar cifras ni citas: usar solo las de las fuentes.
```

## Prompt — Tema 23 (Compresión)

Fuente a adjuntar: `Tema-23-Compresion-Decodificadores-Tiempo-Real.md` (+ opcional `Decodificacion-Brain-to-Text.md` para contexto).

```
Presentación de 12 láminas en español rioplatense neutro para defender un tema de tesis ante un tutor de Ingeniería en Software que NO conoce el campo BCI. Usar siempre "Trabajo Final de Graduación (TFG)". Una idea por lámina, cero jerga sin explicar. Estructura obligatoria: (1) portada: título, "Trabajo de Investigación", línea "Transformación Digital"; (2) el problema humano: los sistemas que devuelven el habla a personas paralizadas ya existen… pero solo corren en computadoras potentes de laboratorio; (3) la brecha: un dispositivo real exige respuesta en milisegundos y consumo mínimo — analogía: ChatGPT vive en un datacenter, pero versiones achicadas corren en tu celular; (4) la evidencia de demanda: Neuralink pide en sus búsquedas laborales exactamente estas habilidades (cuantización, ML en tiempo real, restricciones de energía) y aclara que no exige neurociencia previa; (5) pregunta de investigación textual; (6) las tres técnicas explicadas simple: cuantización = menos decimales, poda = podar ramas que no aportan, destilación = resumen del libro gordo; (7) método: achicar y medir — cada corrida produce tres números: precisión, velocidad, tamaño; la tabla resultante ES la tesis; (8) el resultado: la frontera precisión-velocidad-tamaño, valiosa en cualquier dirección; (9) validación: dataset público con respuesta correcta, conjunto de evaluación oficial del benchmark; (10) viabilidad de cómputo: medir en CPU propia ES el experimento; escalera de alcance Plan A/B/C con recursos gratuitos; (11) plan de 4 meses por entregas; (12) cierre: del paper al dispositivo — el puente que la industria neurotecnológica necesita cruzar. Incluir notas del orador por lámina. No inventar cifras ni citas: usar solo las de las fuentes.
```

## Prompt — Tema 28 (Resiliencia de pipelines BCI) — 2026-08-16, SIN notas del orador

Fuentes a adjuntar: `Tema-28-Evaluacion-Frameworks-BCI.md` + `Propuesta-Reformulacion-Tema-28.md` (la formulación vigente vive en el segundo).

```
Presentación de 12 láminas en español rioplatense neutro que EXPLICA un tema de tesis a una audiencia de Ingeniería en Software que NO conoce el campo BCI. Usar siempre "Trabajo Final de Graduación (TFG)". Una sola idea por lámina, lenguaje simple, todo término técnico explicado con una analogía cotidiana. Basarse en la formulación del documento "Propuesta-Reformulacion-Tema-28" (es la versión vigente del tema); ignorar las secciones de historia, auditorías, banners y temas descartados. Estructura obligatoria: (1) portada: título "Interfaces cerebro-computadora bajo condiciones adversas: del software a la decodificación", tipo "Trabajo de Investigación", línea "Transformación Digital"; (2) el contexto humano: las interfaces cerebro-computadora devuelven comunicación y control a personas con parálisis, y la ciencia que las desarrolla corre sobre software open source; (3) qué es el pipeline de software de una BCI, explicado simple: la señal del cerebro viaja por una cadena de programas (streaming → procesamiento → decodificador → decisión) — analogía: una cadena de postas donde cada corredor le pasa el testimonio al siguiente; (4) el problema: ese software promete aguantar desconexiones, retrasos y pérdida de datos, pero esas promesas están autodeclaradas y nadie midió de forma independiente qué pasa con la DECISIÓN final de la BCI cuando algo falla en el camino; (5) la idea central con la analogía del crash test: los autos declaran ser seguros, alguien tiene que chocarlos contra la pared con método y medir; esta tesis hace eso con el software BCI: rompe cosas a propósito (inyección de fallos) y mide las consecuencias de punta a punta; (6) la pregunta de investigación textual del documento: cómo se propagan los fallos del streaming hacia el desempeño del pipeline y si la telemetría permite detectar o anticipar la degradación; (7) qué se va a construir: un banco de experimentación Software-in-the-Loop — señal EEG pública reproducida como stream en tiempo real, un inyector de fallos controlados, un pipeline BCI de referencia y telemetría que registra todo; (8) qué fallas se inyectan, cada una en una línea simple: pérdida de muestras, jitter, retraso, desconexión/reconexión; (9) qué se mide: no solo la precisión del decodificador — también integridad de datos, latencia, disponibilidad, tiempo de recuperación, y si el sistema AVISA cuando algo anda mal o falla en silencio; (10) la tercera pregunta: ¿un detector inteligente basado en múltiples señales de telemetría aporta valor frente a simples reglas por umbral? — se compara contra ese baseline, y si las reglas ganan, ese resultado también vale; (11) por qué es viable y honesto: datos públicos, sin hardware ni GPU, metodología adaptada de un benchmark publicado de sistemas de streaming, y un diseño donde CUALQUIER resultado (los fallos degradan / el sistema los absorbe / hay fallas silenciosas) produce conocimiento válido; (12) cierre: qué gana el campo — un protocolo reproducible y la primera medición independiente de cómo las fallas de software llegan hasta la decisión de una interfaz cerebro-computadora. NO incluir notas del orador. No inventar cifras, nombres ni citas: usar solo lo que está en las fuentes. No afirmar que "nadie probó LSL" ni prometer descubrir fallas silenciosas: el estudio investiga si existen.
```

**Checklist al revisar la salida**: ¿dice "Trabajo Final de Graduación" (no "Fin de Grado")? ¿ninguna lámina promete descubrir silent failures? ¿ninguna cifra inventada? ¿la capa IA aparece como pregunta con baseline, no como promesa?

## Consejo de uso

- La presentación acompaña TU relato: vos hablás, ella apoya. Si una lámina no la podés explicar sin leerla, se simplifica o se saca.
- Revisar la salida contra esta checklist: ¿terminología TFG correcta? ¿sin líneas duplicadas? ¿cada cifra existe en las fuentes?

---

## Prompts COMPACTOS (8 láminas: problema → alcance → qué resuelve) — 2026-08-14

Para presentaciones breves de los tres finalistas. Misma estructura: portada / problema / evidencia / pregunta / qué voy a hacer / alcance SÍ-NO / qué resolvería / cierre con plan y recursos. Con notas del orador y prohibición de inventar cifras.

Los tres prompts completos están registrados en la conversación de kickoff y se copian tal cual al cuadro de personalización de NotebookLM, adjuntando como fuente el `.md` del tema correspondiente:
- Tema 24 → `Tema-24-LLM-Comunicacion-Asistida-Espanol.md`
- Tema 19 → `Tema-19-Fidelidad-Brain-to-Text.md` (+ `Fidelidad-Brain-to-Text.md`)
- Tema 25 → `Tema-25-Decodificadores-SNN-Neuromorficos.md`

Regla de los 8: si una lámina no se puede explicar sin leerla, se simplifica o se elimina.
