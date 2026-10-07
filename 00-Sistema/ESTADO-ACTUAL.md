# ESTADO ACTUAL DEL PROYECTO — documento de traspaso entre sesiones

> **Escrito: 2026-08-16, al cierre de la sesión de kickoff/selección de tema (sesión larga, ~2 semanas).**
> **Toda sesión nueva debe leer este documento PRIMERO**, después [[Bitacora]] y [[Roadmap]].

---

## 🎯 Dónde está parado el proyecto HOY

> **Actualizado: 2026-10-07.** E2 **v6 entregado el 28/09** (`30-TFG/Entregas/Modulo-2/v6/`). Fase actual: **Entrega 3 (Módulo 3: Discusión ≈ 10 págs + Intro, Métodos y Resultados corregidos)**. **Leer primero [[../30-TFG/Traspaso-Entrega-3|Traspaso-Entrega-3]]**: consigna, hallazgos por objetivo, decisiones pendientes del autor y pendientes. Prompt de arranque: [[Prompt-Sesion-Entrega-3]]. El bloque del 27/09 que sigue quedó como historia.

> **Actualizado: 2026-09-27, 12:40 ART.** Sesión larga del 26-27/09 (≈ 24 h). **Entregable 2 versión 2 generada** (PDF de 41 págs, 855/855 ejecuciones, dos familias de fallo, dos decodificadores); falta la lectura del autor y la subida el 28 antes de las 23:59. El bloque del 2026-09-07 quedó superado y se conserva abajo como historia.

**Fase**: **Entregable 2 (Módulo 2: Resultados) LISTO para revisión del autor**; fecha límite **2026-09-28**. Devolución del E1: 8/10 sin comentarios.

**Qué existe hoy** (todo verificado en esta sesión):

| Pieza | Estado | Dónde |
|---|---|---|
| Banco Software-in-the-Loop completo (loader MOABB, CSP+LDA congelado, reproductor LSL + marcadores, inyector de 4 fallos con semilla, consumidor con telemetría por segundo, ejecutor por bloques reanudable, análisis Friedman/Wilcoxon+Holm, ventana móvil, divergencia, detectores LOSO, figuras APA) | ✅ funciona, 0 ejecuciones fallidas en 234 | `40-Prototipo/` (README con comandos) y público en https://github.com/agustama27/bci-fault-bench (MIT, README con diagramas Mermaid) |
| VM AWS `i-04143f832b56121c0` c6i.2xlarge Ubuntu 24.04, us-east-1, IP 3.82.210.73 (cambia si se detiene), clave `~/.ssh/tfg-bench.pem`, banco en `~/bcibench` | ⏹️ **apagada** (detenida) el 27/09 02:15 ART tras descargar todo; el autor debe **terminarla** desde la consola | [[Decisiones\|D-009]] |
| Piloto (sujetos 1, 5, 8 × corrida 6 × 13 condiciones) + control de paralelismo | ✅ 42/42 | `40-Prototipo/results/vm/piloto`, `piloto-solo`; `scripts/pilot_report.py` |
| Campaña 9 sujetos × corridas 1-2 × 13 condiciones = 234 ejecuciones | ✅ **234/234 ok en 259,6 min (4,3 h)**, 0 fallidas | VM `~/bcibench/results/campana`; copia local `results/vm/campana` |
| Manuscrito E2 (Intro y Métodos corregidos + Resultados + Referencias) | ✅ **versión definitiva** (36 págs, 9.358 palabras; Intro 21 párrafos, Métodos, Resultados con Tablas 2-6 y Figuras 1-2, Referencias) | `30-TFG/Entregas/Modulo-2/` (`src/contenido.js`, `resultados.js`, `tablas.json`, `numeros.json`, `build.js` con figuras; `scripts/final_pipeline.sh` lo regenera todo) |
| Panorama visual para el autor | ✅ v4 | https://claude.ai/artifact/3v1xQbqYt9SCTwbhvNpzfn |

**Decisiones tomadas por el autor en esta sesión**: recorte de alcance a 2 corridas por bloque, 9 sujetos y 12 condiciones intactos ([[Decisiones|D-008]]); campaña en VM Linux ([[Decisiones|D-009]]); severidades = Tabla 1 del E1; ventana móvil W = 8 y umbral = mínimo de la referencia del sujeto (regla `min`); publicar el banco en GitHub; terminar el E2 de madrugada sin esperar al autor.

**Hallazgos (234/234 ejecuciones, definitivos)**:
1. La infraestructura responde exacta a cada modelo de fallo: latencia 52,7/102,6/252,7 ms para retrasos de 50/100/250; recibido 0,990/0,950/0,900 para pérdidas de 1/5/10 %; dispersión entre bloques 8,3/30,6/56,4 ms para jitter de 10/50/100 ms; 3/3/13 s sin datos para cortes de 0,5/1/3 s. Todas las comparaciones apareadas significativas (r 0,89-0,96, p Holm = 0,012).
2. **LSL tarda ≈ 572 ms en reconectar** además de cada corte (intervalo máximo 1.563 ms para cortes de 1 s, 3.581 para 3 s). Es el número que nadie había medido.
3. **El decodificador no se degrada** en ninguna condición (mediana 0,812 en la referencia y en 11 de 12 condiciones, 0,833 en pérdida 5 %; mediana de diferencias apareadas 0,000 en las 12; Friedman p = 0,45 y 0,59; decisiones válidas 100 %). El efecto funcional es temporal: el retardo de decisión pasa de 1.033 ms a 1.082/1.132/1.282 ms con retraso y a 1.085 con jitter de 100 ms.
4. Divergencia: cero ventanas "operativo pero degradado" (silent failure); sí ventanas "no operativo pero no degradado" en desconexión (0,6-3,5 %). Solo 14 episodios de degradación (546 de 70.044 ventanas) en 234 ejecuciones → la comparación de detectores (objetivo 5) es degenerada (precisión < 0,02) y se reporta como tal. Con la regla percentil 5 la referencia ya marca 3 % de ventanas sanas (documentado en `results/analysis-alt-p5`).
5. Efecto piso en el sujeto 5 (0,50 = azar, también fuera de línea) y techo en el 8 (1,00): declarado.

**Reglas aprendidas hoy** (además de las del 07/09): el texto entre llamadas a herramientas no le llega al autor, solo el mensaje final; los pasos a paso van en un mensaje propio. Gotchas técnicos en engram (`tfg/entregable-2/*`): MOABB desplaza anotaciones +2 s (usar `STI`); `pull_chunk` de mne_lsl devuelve vistas (copiar); µV vs V; instante de entrega = última muestra del bloque; Windows temporizador ~15 ms.

## 🔁 Versión 2 del Entregable 2 (decidida por el autor el 27/09 ~03:30 ART, en curso)

El profesor confirmó por chat de la materia que "pueden hacer todos los cambios que quieran; si lo hacés, modificá el diseño metodológico". Con 45 h hasta el cierre (lunes 28 23:59), el autor decidió una segunda iteración:

| Mejora | Estado |
|---|---|
| Cinco corridas por sujeto (deuda D-008) | ✅ campaña 2: **855/855 ok en 486 min (8,1 h)**, 12 workers, 0 fallidas; VM apagada 14:19 UTC; datos locales en `40-Prototipo/results/vm/campana2` (1,3 GB con segmentos) |
| Segunda familia de fallos **estructurados** (criterio: escala del ensayo, no magnitud) | ✅ `injector.py`: `burst_trial` (bloque contiguo del 10/25/40 % de la ventana [2,6] s, todos los ensayos) y `disconnect_trial` (corte de 0,5/1/2 s al inicio de la ventana, todos los ensayos). Humo local OK: el corte de 1 s deja 610/1000 muestras (1 s + 0,56 s de reconexión) |
| Segmentos guardados por ensayo (`segments.npz`) | ✅ consumidor; permite re-decodificar fuera de línea; CSP re-aplicado = 7/7 decisiones idénticas a las de línea |
| EEGNet como segundo decodificador | ✅ 9 modelos (mediana 0,743 vs CSP 0,722 fuera de línea); evaluado sobre segmentos; en el banco, fuera de línea = banco exactamente en 9/9 sujetos para ambos decodificadores; CSP re-aplicado reproduce el 99,0 % de 20.511 decisiones en línea |
| DOI Zenodo | ⏸️ pospuesto por el autor para después de la entrega (Módulo 3) |
| Métodos v2 | ✅ `contenido.js` reescrito (diseño secuencial, 855, dos familias en Tabla 1, segmentos, EEGNet, control de paralelismo); copia v1 en `contenido.v1-234.js` |
| Resultados v2 | ✅ generado con los 855: **hallazgos** — familia uniforme: ningún decodificador cambia (CSP 0,708 en 12/12; EEGNet 0,750 en 12/12); familia estructurada: CSP cae solo en la severidad máxima (burst 40 % p=0,012; corte 2 s p=0,012), **EEGNet cae con cualquier corte en el ensayo** (0,583/0,583/0,500, p=0,012) y con burst 40 % (p=0,023); **reconexión LSL: piso de ≈ 1,56 s** (hueco máximo 1.561/1.560/3.598 ms para cortes de 0,5/1/3 s → exceso 1.061/560/598 ms; no es un peaje fijo: corrección aportada por revisión externa el 27/09 y verificada; el mecanismo, búsqueda de 1 s + 0,5 s en liblsl según la sesión de líneas futuras, queda ⚠️ a verificar en el código antes de citarlo); retardo de decisión = retraso; cero fallos silenciosos (umbral `min` con 5 corridas es más bajo); 77 episodios; detectores aún degenerados (RF F1 0,058). Repo público **v2.0** con datos (128 MB) y análisis |

Fuera de la v2 (Módulo 3 como líneas futuras): segundo framework, trazas reales, intracortical, issue a LSL.

## ⏭️ Próximos pasos

**Hecho en la madrugada del 27 (Claude, autorizado)**: `final_pipeline.sh` corrido con los 234 resultados; cifras del texto verificadas y hechas dependientes de los datos (`numeros.json`); repo público con datos, análisis y etiqueta **v1.0** (https://github.com/agustama27/bci-fault-bench/releases/tag/v1.0); VM apagada. Para regenerar el manuscrito: `cd 30-TFG/Entregas/Modulo-2/src && NODE_PATH=$(npm root -g) node build.js .. && python topdf.py "../Tamagusuku_Agustin - Entregable 2 - Resultados.docx"`.

**Mañana (autor)**: leer el manuscrito completo y apropiárselo (defensa oral); autoevaluación en la plataforma; subir el PDF el 28; **terminar** (no detener) la instancia desde la consola de AWS.

**Después del E2**: ver [[../30-TFG/Trabajo-Futuro|Trabajo-Futuro]] (nueve líneas ordenadas por módulo: 5 corridas, EEGNet, detector en vivo, segundo framework, trazas reales, intracortical, issue a LSL, DOI Zenodo, Open Lab) y [[../30-TFG/Fundamentos-Diseno-Estadistico|Fundamentos-Diseno-Estadistico]] (argumentos y objeciones para la defensa). Vault sin commitear desde el 07/09: commit cuando el autor lo pida.

---

# Historia — selección de tema (agosto 2026, SUPERADA por la entrega)

## (histórico) Dónde estaba parado el proyecto al 2026-08-16

**Fase**: selección de tema — **decisión definitiva PENDIENTE**. El 2026-08-16 el autor eligió preliminarmente BCI (propuesta 28+28.1+capa IA) en sesión, pero horas después aclaró que **aún no tiene la decisión tomada de forma definitiva**. Ver [[Decisiones|D-004]] (estado: preliminar).

**Tema candidato principal** (elegido por el mentor tras ~30 temas explorados; preferencia preliminar del autor el 2026-08-16 con la alternativa LLM-agentes sobre la mesa):

> **"Evaluación de resiliencia de frameworks BCI open source mediante inyección de fallos, con medición del impacto en la precisión del decodificador."**
> Tema 28 + expansión 28.1 (robustez/chaos engineering) + capa IA (función de transferencia falla-de-software → error-del-modelo).
> Trabajo de Investigación · línea Transformación Digital · sin hardware, sin GPU, datos públicos.

**Estado de la decisión**: 🟡 **PRELIMINAR, NO definitiva** (corrección del autor, 2026-08-16). En sesión el autor eligió BCI frente a la alternativa LLM-agentes (por el puente de carrera hacia neurotecnología), pero luego aclaró que la decisión definitiva sigue abierta. El proceso real de la universidad es el que decide: se presentan idea(s) en Word al tutor y él aprueba. El Word del tema 28 ya está generado y listo. Consecuencias condicionales al tema (tipo=Investigación, línea=Transformación Digital, datos públicos) en [[Decisiones|D-004]]. **Regla que sigue vigente**: NO se generan temas nuevos — la decisión es entre los candidatos ya documentados.

**Esquema visual de la propuesta** (para mostrar al tutor): https://claude.ai/code/artifact/2b87500e-b857-4f89-b859-f614e57479ae

## ✅ Qué respalda la propuesta

- Hueco verificado DOS veces y **REFINADO el 2026-08-16 tras auditoría externa**: el paper de LSL (PMC12434378, verificado por fetch) SÍ declara mecanismos de recuperación y dice hacer stress-tests con desconexiones — pero **sin métricas cuantitativas** (ni tasas de pérdida, ni tiempos de recuperación), con pruebas formales solo en condiciones ideales, y **sin medir jamás el impacto sobre el decodificador aguas abajo**. Formulación correcta del hueco: *no existe evaluación independiente y cuantitativa del comportamiento bajo fallas, ni medición de su propagación a la decodificación* — el mismo patrón que Secure LSL (<5% autoreportado → la verificación independiente es el aporte). La frase absoluta "nadie evaluó la capa de software" NO debe usarse.
- Plantilla metodológica publicada: benchmark de fault recovery en stream processing (arXiv 2404.06203, hecho para Flink/Spark).
- Frameworks objetivo según tabla de salud GitHub (2026-08-16): BciPy y MEDUSA activos, LSL activo, Timeflux posiblemente estancado (~20 meses sin push) — eso también es un dato del estudio.
- Antecedente citable para la capa IA: literatura de degradación de señal sobre modelos EXISTE (se cita); lo nuevo verificado es la cadena con software real en el medio.
- Es justo (no hombre de paja): los frameworks DECLARAN recuperación de conexión — se testea lo que prometen.

## 📚 Las reglas aprendidas en esta sesión (NO repetir errores)

1. **Calibración UNSAM**: la vara de un TFG es ejecución rigurosa de un problema delimitado, NO originalidad mundial. Referencia: tesis UNSAM (Helguera 2021) extendió un sistema existente de 2 a 4 opciones y aprobó. Ver [[../20-Investigacion/Calibracion-Alcance-Tesis-BCI|Calibración]].
2. **Verificar antes de enamorarse**: toda afirmación de hueco/hecho se verifica con búsqueda propia ANTES de proponerla. Errores históricos que enseñaron esto: Bluetooth del N1 (sin fuente primaria), "el futuro es decodificar adentro" (sin evidencia), tema 25 vs NeuroBench (ya hecho), silos frameworks/ephys (BRAND ya existía), "nadie midió overhead de Secure LSL" (los autores sí, <5% autoreportado).
3. **Los temas de áreas calientes financiadas mueren**: SNN neuromórficas e infraestructura intracortical están cubiertas por consorcios (NeuroBench, BrainGate/BRAND). Los huecos viables para TFG son "ausencias verificables" o "extensiones declaradas de lo existente".
4. **El patrón del autor**: talento para objeciones agudas (corrigió al mentor 3+ veces) + tendencia a búsqueda infinita (30 temas, todos con grieta). La exploración fue declarada TERMINADA — no reabrirla.
5. **Ninguna cita sin fuente verificada** — regla dura de todo el harness.

## 📂 Mapa de documentos clave

| Qué | Dónde |
|---|---|
| Propuesta actual detallada + expansiones auditadas | [[../30-TFG/Seleccion-Tema/Sprint-Descubrimiento-Frameworks|Sprint-Descubrimiento-Frameworks]] (secciones 2 y 4) |
| Tema 28 base con gancho y objeciones respondidas | [[../30-TFG/Seleccion-Tema/Tema-28-Evaluacion-Frameworks-BCI|Tema-28]] |
| Índice de TODOS los temas (30) con estados | [[../30-TFG/Seleccion-Tema/00-Indice|00-Indice]] |
| La calibración de vara (documento correctivo central) | [[../20-Investigacion/Calibracion-Alcance-Tesis-BCI|Calibracion-Alcance-Tesis-BCI]] |
| Fundamentos aprendidos (implantes, señal, frameworks, BRAND) | `10-Fundamentos/` y `20-Investigacion/` |
| Word oficiales ya generados (temas 19 y 23, como plantilla) | `30-TFG/Seleccion-Tema/*.docx` |
| Prompts NotebookLM para presentaciones | [[../30-TFG/Seleccion-Tema/Prompts-NotebookLM|Prompts-NotebookLM]] |

**Artifacts publicados**: deck de 18 temas (HISTÓRICO, superado — https://claude.ai/code/artifact/9a29cb16-f79b-4d1d-9cbc-e2daac96f838) · esquema visual de la propuesta actual (VIGENTE — https://claude.ai/code/artifact/2b87500e-b857-4f89-b859-f614e57479ae).

**Memoria Engram**: proyecto `tesis`, topic keys `bci/*` (seleccion-tema/estado, seleccion-tema/calibracion, brain-to-text/*, se4ai/*).

## 🔀 Giro de dominio evaluado (2026-08-16): preferencia preliminar por BCI

Al cerrar la sesión se encontró en el vault un documento nuevo — [[../30-TFG/Seleccion-Tema/Alternativas-Fuera-de-BCI-2026-08-16|Alternativas fuera de BCI]] — que plantea **temas de Ingeniería de Software × sistemas LLM/agentes** (testing de regresión de agentes conversacionales, evaluación de agentes de voz en español, benchmarks): el dominio que el autor ejerce a diario en Evoltis. El documento sigue la calibración correcta y contiene una observación clave: *tras 30 temas BCI sin que ninguno encienda — incluido el de mayor motivación declarada — el candidato a problema puede ser el dominio, no la lista.*

**Estado (2026-08-16)**: el dilema (a) BCI vs (b) LLM-agentes fue presentado al autor con ambas opciones completas. El mentor recomendó el tema B (evaluación de agentes de voz); el autor eligió **preliminarmente** BCI priorizando el puente de carrera hacia neurotecnología/maestría — pero luego aclaró que la decisión definitiva sigue pendiente. Registrado en [[Decisiones|D-004]] (preliminar). Las citas de los temas A/B/C siguen ⚠️ SIN VERIFICAR — si vuelven a considerarse, la verificación completa es prerequisito.

## ⏭️ Próximos pasos (en orden)

**Corrección de proceso (2026-08-16, aportada por el autor)**: NO existe una fecha de Módulo 0. El proceso real es: presentar el/los temas en Word según el estándar oficial → el tutor aprueba o rechaza las ideas. Estrategia acordada: presentar la propuesta confirmada; si el autor luego quiere un seguro contra rechazo, el tema 19 ya tiene su Word listo como segunda idea (misma línea temática). Regla vigente: dos ideas EN EL DOCUMENTO es aceptable; trabajar dos temas en paralelo hasta etapas avanzadas, NO (es el patrón de búsqueda infinita).

1. **[BLOQUEANTE — en manos del autor] Tomar la decisión definitiva de tema** (entre candidatos ya documentados: propuesta BCI 28+28.1+IA, finalistas BCI 19/24/28.2, alternativas LLM A/B/C) **y/o enviar al tutor el Word de idea(s)** para que el proceso de aprobación decida. **Entregable listo**: `30-TFG/Seleccion-Tema/Tamagusuku_Agustin - Trabajo de Investigacion.docx` (regenerado 2026-08-17 contra el PDF oficial "Selección Tema TFG - Seminario Final - ING SOFT": Arial 12, conteos de renglones respetados, 4 citas APA con autores verificados, contenido en la formulación vigente de pipelines). Antes de enviar: **completar Documento y Legajo**.
2. **Prueba de humo v3 — escalera de 4 PoCs** (sábado; reemplaza a la v2): según [[../30-TFG/Seleccion-Tema/Propuesta-Reformulacion-Tema-28|Propuesta-Reformulacion-Tema-28]] §22 — (1) BNCI2014_001 + CSP/LDA offline; (2) replay con MNE-LSL PlayerLSL; (3) primer fallo inyectado + comparación funcional; (4) detector de reglas vs modelo básico. Criterio de cierre en §23: si dataset+decoder+replay+una perturbación+telemetría+consecuencia medible funcionan → **el tema queda técnicamente viable y la decisión prácticamente cerrada**. ⚠️ Verificar ese día: docs de MNE-LSL PlayerLSL y carga de BNCI2014_001 vía MOABB.
3. Regenerar presentación NotebookLM del tema confirmado (prompts listos).
4. Pendientes menores: repositorio PUCE caído (reintentar); texto completo tesis Uniandes (anti-bot); completar revista/DOI exactos de la cita de MEDUSA (quedó fuera del Word por estar incompleta).

## 🗂️ Estado del repo

- Rama de trabajo: `feat/temas-candidatos-tfg` (~25 commits de selección de tema) → **mergeada a `main` al cierre de esta sesión** para que toda sesión/herramienta nueva vea el estado completo.
- Remoto: https://github.com/agustama27/TESIS (privado, cuenta personal).
