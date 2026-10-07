# Traspaso para la Entrega 3 (Módulo 3: Discusión)

> 2026-10-07. Escrita al cierre de la sesión larga de mejoras del E2 y análisis M3. **Toda sesión que trabaje la Entrega 3 lee esta nota primero.** Relacionada con [[Mejoras-Redaccion-M3]], [[Analisis-M3]], [[Analisis-M3-ensayos-divergencia]], [[Analisis-M3-campana-exploratoria]], [[Fundamentos-Diseno-Estadistico]], [[Patrones-Tesis-Cassi]] y [[Trabajo-Futuro]].

## 1. Qué pide la consigna (Lectura 3, verificada en el PDF)

Fuente: `C:\Users\agustin.tamagusuku\Downloads\Trabajo de investigación - Entrega 3-1.pdf`.

**Entregable 3** = Introducción (corregida) + Métodos (corregido) + Resultados (corregido) + **Discusión (lo nuevo, ≈ 10 págs, flexible)** + un único listado de Referencias.

**Discusión, reglas de la cátedra** (basadas en Day, 2005, y Hernández Sampieri et al., 2010):
- Interpretar los resultados a la luz de la pregunta, los objetivos y los antecedentes. **Los resultados se exponen, no se recapitulan.**
- Primer párrafo: el objetivo general (sin transcribirlo literal), con su importancia o novedad.
- Después, **un párrafo (o bloque) por objetivo específico, en el mismo orden que Resultados**, sin transcribir el objetivo.
- Comparar con antecedentes (con citas): en qué coincide y en qué no, con argumentos propios; explicar los resultados inesperados y las divergencias.
- Señalar anomalías, excepciones y aspectos no resueltos; no ocultar datos que no encajan.
- Si el planteamiento cambió durante la investigación, explicar por qué y cómo (aplica: objetivo 5 acotado a "detectar", familia estructurada agregada como fase exploratoria).
- Limitaciones con su repercusión en los resultados, **articuladas con las fortalezas y aportes**.
- Consecuencias teóricas y aplicaciones prácticas.
- Últimos párrafos: conclusiones (breves, derivadas **solo** de los resultados), recomendaciones y futuras líneas.
- **Tiempo presente. Sin subtítulos.**

**Formato**: TNR 12; márgenes de 3 cm; número de página arriba a la derecha (excepto la portada); doble interlineado (salvo tablas y figuras); justificado; sangría; PDF. Portada tentativa con el **tema** (no el título), nombre, legajo, fecha, carrera, materia, módulo y tutor. La consigna dice APA (2010); el manuscrito usa APA 7 desde el E1 (decisión del autor: no cambiarlo).

## 2. Punto de partida

- **Manuscrito vigente: E2 v6** (subido el 28/09): `30-TFG/Entregas/Modulo-2/v6/` (35 págs). Fuentes en `Modulo-2/src/`: `contenido.js` (Intro, Métodos, Referencias), `resultados.js`, `tablas.json`, `numeros.json`, `figuras.py`, `build.js`. Regenerar: `node build.js ..` y `python topdf.py "../Tamagusuku_Agustin - Entregable 2 - Resultados.docx"` (desde `src/`; solo cuando el autor lo pida).
- **Devolución del profesor sobre el E2: ⚠️ desconocida en esta sesión.** Preguntarle al autor antes de corregir; las correcciones indicadas por el profesor tienen prioridad sobre las propias.
- Objetivos específicos vigentes (`contenido.js`): (1) construir el banco SIL; (2) cuantificar el efecto sobre integridad, temporalidad y disponibilidad del flujo; (3) medir el efecto sobre el decodificador y las curvas de degradación; (4) identificar las condiciones de divergencia entre el estado observable y el desempeño; (5) comparar el detector por umbrales con un clasificador multivariable para **detectar** la degradación; (6) documentar para replicar. Tres interrogantes: efecto por tipo y severidad; divergencia; detector multivariable vs. umbrales.

## 3. Lo que se descubrió (insumo de la Discusión), por objetivo

| Obj. | Hallazgo | Dónde está el detalle | Estado para el manuscrito |
|---|---|---|---|
| 2 | La infraestructura responde exactamente a cada fallo inyectado (validez del banco) | E2 v6, Resultados | Ya en Resultados |
| 2 | **Piso de reconexión de LSL**: hueco = max(1,52; 0,52 + 0,5·ceil(d/0,5)) s. Ajusta 8.954 cortes. **Mecanismo verificado en el código de liblsl v1.17.7** (la versión que empaqueta mne-lsl 1.14, idéntica a `master` en las líneas clave): (a) **1,0 s mínimo** fijo del primer intento de búsqueda (`inlet_connection.cpp`); (b) consultas de búsqueda cada `MulticastMinRTT` = **0,5 s, configurable** en `lsl_api.cfg` (`resolver_impl.cpp`): es la grilla; (c) **pausa fija de 500 ms** antes de reconectar (`data_receiver.cpp`): es el +0,5 constante | [[Analisis-M3]] §1; [[Analisis-M3-campana-exploratoria]] §1 | La regla lineal "d + 0,52" del E2 es válida solo para d múltiplo de 0,5 s: **corregir en Resultados**. Prueba experimental con `MulticastMinRTT = 0,25` corriendo el 07/10 en la VM (ver §6) |
| 2-3 | Consecuencia práctica: **el costo de un corte lo pone la recuperación** (un corte de 0,1 s deja un hueco de 1,52 s). Una parte es ajustable por configuración y 1,5 s no lo son sin recompilar liblsl | Ídem | Discusión (aplicación práctica, recomendación) |
| 3 | **Exposición, no robustez intrínseca**: la familia uniforme no degrada porque toca pocos ensayos (E ≈ N(d+r+w)/T; 6-9 % de los ensayos tocados). La caída sigue a la fracción de ventana perdida (Spearman −0,94/−0,93). Los ensayos no tocados no cambian (1 en 3.760); los tocados sí (11 % CSP+LDA, 19 % EEGNet) | [[Analisis-M3]] §2; [[Analisis-M3-ensayos-divergencia]] §1; [[Analisis-M3-campana-exploratoria]] §2 | Discusión (explica el resultado "inesperado" central) |
| 3 | El barrido de 2/5/10/20 cortes confirma el modelo de exposición pero **no detecta caída de BA**: con 24 ensayos por corrida un ensayo mueve 4,2 pp; falta potencia para efectos < 1 pp | [[Analisis-M3-campana-exploratoria]] §2 | Limitación |
| 3 | **IC de Hodges-Lehmann**: en jitter, retraso y desconexión de 0,5-1 s el IC queda dentro de ±0,03 (equivalencia práctica). Ojo: los IC [0;0] son degenerados (decisiones idénticas), no precisión estadística | [[Analisis-M3]] §3 | Resultados corregidos o Discusión |
| 3 | **EEGNet es más frágil que CSP+LDA ante un corte en el ensayo**, y es intrínseco: rellenar con interpolación o con la última muestra en lugar de ceros no cambia nada (el relleno con ceros reproduce el 99,96 % de las decisiones del E2) | [[Analisis-M3-ensayos-divergencia]] §D | Discusión (no es un artefacto de cómo se armó la entrada) |
| 3 | **Importa dónde cae el hueco** dentro de la ventana (nivel de ensayo) | [[Analisis-M3-ensayos-divergencia]] §2 | Discusión |
| 3 | **Retener la última muestra (como Simeral et al., 2021) daña lo mismo que borrar** | [[Analisis-M3-campana-exploratoria]] §3 | Discusión, si entra la campaña exploratoria |
| 4 | Fallas silenciosas: la mediana es 0, pero en total **1,26 %** de los segundos con fallo fueron operativos y degradados (familia estructurada; parte es eco de la ventana móvil de 8 ensayos). La frase "0,000" del E2 hay que reformularla (ver [[Mejoras-Redaccion-M3]] C2) | [[Analisis-M3-ensayos-divergencia]] §3 | **Corregir en Resultados** |
| 4 | **Falla silenciosa pura**: con retención (`hold_trial`), el 2,08 % de los segundos fueron operativos y degradados, el **100 %** de los segundos degradados fueron operativos, la telemetría no ve nada y el detector por umbrales detecta el 2,6 % (27,6 % con borrado). Los fallos que cortan la señal se notan; los que la corrompen sin cortarla no | [[Analisis-M3-campana-exploratoria]] §4 | El argumento más fuerte para el objetivo 4, si entra la campaña |
| 4 | Argumento de la **deriva neural**: la señal cambia y un decodificador fijo se degrada sin ninguna falla del sistema (Gallego et al., 2020; Karpowicz et al., 2025, *Nat Commun* 16, **4662**). Son registros intracorticales en primates: no extrapolar a EEG sin advertirlo | [[Analisis-M3]] §4 | Discusión: por qué hace falta monitorear la función y no solo la infraestructura |
| 5 | Los detectores fallan: prevalencia 1,34 %; precisión promedio umbrales 0,012 (debajo del azar), regresión logística 0,032, *random forest* 0,024, *gradient boosting* 0,029 (≈ 1,7-2,7 veces el azar). Ningún detector combina sensibilidad y pocas falsas alarmas | E2 v6 Tabla 4; `bci-fault-bench/scripts/detectores_ap.py` | Discusión: por qué falla (lo que se degrada no deja huella en la telemetría) |
| 6 | Reproducibilidad: la referencia repetida el 07/10 dio **1.080 de 1.080 decisiones idénticas** a la de septiembre, en los dos decodificadores. Repo público con datos (v2.0) | [[Analisis-M3-campana-exploratoria]] §5 | Discusión (fortaleza) |

## 4. Decisiones pendientes del autor (bloquean partes de la Entrega 3)

1. **¿La campaña exploratoria (familia 3: barrido de cortes, retención, diagnóstico del piso) entra al manuscrito?** Si entra: Métodos (una familia exploratoria más, declarada post hoc) + Resultados corregidos, y recién entonces se puede discutir. **La Discusión no puede introducir datos nuevos.** Si no entra: queda como línea futura y la Discusión usa solo los 855.
2. **¿Qué correcciones v7 se aplican a Intro, Métodos y Resultados?** Lista en [[Mejoras-Redaccion-M3]], sección C, más la devolución del profesor.
3. Página exacta de Hernández Sampieri (2014) para la tríada de enfoque, alcance y diseño: la busca el autor en eBook21.

## 5. Pendientes (consolidados)

- [ ] Conseguir la devolución del profesor sobre el E2 y priorizarla.
- [ ] Decidir el punto 4.1 (campaña exploratoria) antes de redactar.
- [ ] Correcciones a Resultados: regla del piso (escalonada, con su mecanismo); "0,000" de fallas silenciosas reformulado (C2); IC de HL si se incorporan.
- [ ] Correcciones a Métodos: C1 (ensayo y ventana, Tangermann 2012 §5.2.2, verificado); redactar la semilla como "la semilla de cada ejecución se registra en `plan.json`" (el `hash()` de Python cambia entre procesos, así que no es una función fija del nombre).
- [ ] Introducción: Simeral et al. (2021) como antecedente de pérdida inalámbrica real; Zheng et al. (2025) ya citado (verificar que se leyó el texto completo).
- [ ] Registrar en `20-Investigacion/` con APA: Simeral (2021), Gallego (2020), Karpowicz (2025, art. 4662), liblsl v1.17.7 (código fuente, como software).
- [ ] Redactar la Discusión (≈ 10 págs, presente, sin subtítulos) con el molde de [[Patrones-Tesis-Cassi]].
- [ ] Preparación de la defensa: preguntas probables (9 sujetos; por qué la uniforme no degradó; por qué EEGNet es más frágil; qué aporta si el decodificador no cae).
- [ ] Commit del vault (sin commitear desde el 07/09) y del repo del banco: **solo cuando el autor lo pida**.
- [ ] AWS: detener la instancia al terminar la prueba de `MulticastMinRTT` (§6).

## 6. Trabajo en curso en la otra sesión (no tocar)

La sesión anterior sigue abierta terminando la **prueba experimental del mecanismo del piso**: cortes de 0,5 / 1,1 / 1,25 / 1,75 s × 9 sujetos × 5 cortes, con `MulticastMinRTT` = 0,5 y 0,25 s. Predicción: 1,52 / 2,02 / 2,02 / 2,52 s con 0,5, y 1,52 / 1,77 / 1,77 / 2,27 s con 0,25. VM `54.172.9.9`, resultados en `~/bcibench/results/rtt050` y `rtt025`, script local `bci-fault-bench/scripts/m3d_rtt.py`, familia `m3rtt` en `runner.py`. **Esa sesión escribe el resultado en [[Analisis-M3-campana-exploratoria]] §1.4 y en la [[../00-Sistema/Bitacora|Bitácora]]**; la sesión de la Entrega 3 no edita esa nota ni el repo del banco mientras tanto.

## 7. Reglas vigentes

- Ninguna cita sin fuente primaria verificada; lo dudoso se marca ⚠️ SIN VERIFICAR. El paper interno sobre λ·n (Evoltis) es confidencial: no citarlo ni ponerlo en el vault.
- Commits solo cuando el autor lo pida, con *conventional commits* y sin atribución de IA.
- No regenerar el PDF sin pedido explícito. Conservar respaldos (`*.vN.js`) antes de cada versión; la próxima versión del manuscrito va en `30-TFG/Entregas/Modulo-3/`.
- No cambiar el tema, el título ni las cifras sin datos; no escribir en primera persona.
- El autor defiende oralmente: explicar lo que se escribe y por qué.
