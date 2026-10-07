// Resultados del Entregable 2 (versión 2: dos familias de fallo, dos decodificadores).
// Pretérito, orden de los objetivos específicos, sin citas, sin métodos, sin interpretación.
// Tablas 3 a 6 desde tablas.json (scripts/resultados_tablas.py); cifras desde numeros.json
// (scripts/resultados_numeros.py). El texto se adapta a los números (significancias, excepciones).
const T = require("./tablas.json");
const N = require("./numeros.json");

const es = (n) => (typeof n === "number" ? n.toFixed(2).replace(".", ",") : n);
const fr = (k, dict = T.desempeno.friedman) => {
  const f = dict[k];
  if (!f || f[0] === null) return "no calculable por ausencia de variación entre condiciones";
  return `χ²(3) = ${es(f[0])}, ${f[1] < 0.001 ? "p < 0,001" : `p = ${f[1].toFixed(3).replace(".", ",")}`}`;
};
const frSig = (k, dict = T.desempeno.friedman) => { const f = dict[k]; return !!(f && f[1] !== null && f[1] < 0.05); };
const friedmanUniform = () => {
  const parts = [];
  for (const [k, name] of [["loss", "la pérdida de muestras"], ["disconnect", "la desconexión"]]) {
    parts.push(frSig(k)
      ? `para ${name} la prueba de Friedman detectó diferencias globales entre condiciones (${fr(k)}) sin que ninguna severidad difiriera de la referencia tras la corrección de Holm`
      : `para ${name} la prueba de Friedman no detectó diferencias (${fr(k)})`);
  }
  return parts.join("; ") + "; para el *jitter* y el retraso no fue calculable porque las nueve observaciones por sujeto coincidieron exactamente con las de referencia.";
};
const joinES = (arr) => (arr.length === 0 ? "ninguna" : arr.length === 1 ? arr[0] : arr.slice(0, -1).join(", ") + " y " + arr[arr.length - 1]);
const sigSentence = (arr, who) => arr.length === 0
  ? `Para ${who}, ninguna comparación contra la referencia resultó significativa.`
  : `Para ${who}, resultaron significativas las comparaciones contra la referencia de ${joinES(arr)}.`;

const hasNet = !!N.tabla2_has_net;
const hasStruct = !!N.has_struct;

const tabla2Headers = hasNet
  ? ["Sujeto", "CSP+LDA fuera de línea", "CSP+LDA en línea (referencia)", "EEGNet fuera de línea", "EEGNet sobre segmentos (referencia)", "Umbral (mín. de la móvil)"]
  : ["Sujeto", "Fuera de línea", "En línea (referencia)", "Umbral (mín. de la móvil)"];

module.exports = [
  "Los resultados se presentan en el orden de los seis objetivos específicos. Todas las cifras corresponden a la campaña definitiva, salvo cuando se indica la prueba piloto o la primera etapa de la campaña.",

  { h2: "Construcción y verificación del banco de experimentación" },

  `El banco quedó construido con los seis componentes previstos y ejecutó la campaña definitiva de ${N.n_execs_txt} ejecuciones sin intervención manual y sin ejecuciones fallidas, en ${N.horas_campana} horas de reloj con doce ejecuciones simultáneas. En la condición de referencia, el servicio de reproducción entregó cada bloque con un error respecto del instante nominal cuyo percentil 99 fue de ${N.timing_p99_us} microsegundos (máximo entre ejecuciones: ${N.timing_p99_max_us} microsegundos). Ejecutar doce reproducciones simultáneas en lugar de una sola aumentó la latencia media de extremo a extremo de la referencia en ${N.ctrl_lat_ms} ms y la desviación del intervalo entre bloques en ${N.ctrl_ia_ms} ms respecto de la misma corrida ejecutada sola en la prueba piloto, sin cambiar la exactitud.`,

  `La prueba piloto, ejecutada sobre la sexta corrida de los sujetos 1, 5 y 8, confirmó que las doce condiciones de la familia uniforme produjeron efectos medibles en la telemetría y fijó la ventana móvil en ocho ensayos y el umbral de degradación en el mínimo de la referencia de cada sujeto. La primera etapa de la campaña (234 ejecuciones, corridas primera y segunda, familia uniforme) no mostró efecto funcional de ningún fallo; la campaña definitiva que se reporta a continuación incorporó la familia estructurada y las cinco corridas. La Tabla 2 presenta, para cada sujeto, la *balanced accuracy* de cada decodificador sobre la sesión de evaluación calculada fuera de línea, la obtenida en la condición de referencia del banco y el umbral resultante; los valores de CSP y LDA en el banco coincidieron con los de fuera de línea en ${N.tabla2_iguales === 9 ? "los nueve sujetos" : `${N.tabla2_iguales} de los nueve sujetos`}${N.tabla2_distintos ? ` y difirieron en el resto en no más de ${N.tabla2_maxdiff} (sujetos ${N.tabla2_distintos})` : ""}. La reaplicación de CSP y LDA a los segmentos guardados reprodujo la decisión tomada en línea en el ${N.equiv_pct} % de las ${N.equiv_n} decisiones válidas de la campaña.`,

  { table: {
      num: "Tabla 2",
      title: "Desempeño de referencia por sujeto: fuera de línea, en el banco sin fallo y umbral de degradación",
      headers: tabla2Headers,
      rows: N.tabla2,
      note: "Balanced accuracy sobre los ensayos de mano izquierda y derecha de las cinco corridas de evaluación de la campaña. Fuera de línea: mediana de las cinco corridas del decodificador aplicado a las épocas. En el banco: mediana de las cinco reproducciones sin fallo (CSP+LDA en línea; EEGNet sobre los segmentos guardados). Umbral: mínimo de la balanced accuracy móvil de ocho ensayos de CSP+LDA sobre las reproducciones sin fallo del sujeto.",
  } },

  { h2: "Efecto de los fallos sobre la integridad, la temporalidad y la disponibilidad del flujo" },

  `En la familia uniforme, cada modelo de fallo alteró la familia de variables que su definición señalaba y ninguna otra (Tabla 3). La pérdida de muestras redujo la relación entre muestras recibidas y esperadas a ${N.recv_loss} para las severidades de 1, 5 y 10 %, y produjo medianas de ${N.gaps_loss} huecos por corrida, con aumentos de la latencia de extremo a extremo de ${N.lat_loss_delta} ms, inferiores a un milisegundo, y sin cambios en la regularidad de llegada. El *jitter* no perdió muestras y elevó la desviación del intervalo entre bloques de ${N.ia_ref} ms a ${N.ia_jitter} ms, con latencias medias de ${N.lat_jitter} ms. El retraso desplazó la latencia media a ${N.lat_delay} ms, valores que reproducen el desplazamiento inyectado sobre la latencia de referencia de ${N.lat_ref} ms, sin alterar la integridad ni la regularidad. En las tres severidades de estas familias, las comparaciones apareadas contra la referencia resultaron significativas ${N.r_max === N.r_top ? `con un tamaño de efecto r = ${N.r_top}` : `con tamaños de efecto entre ${N.r_max} y ${N.r_top}`} (p corregida ≤ ${N.p_min}).`,

  `La desconexión con cortes en instantes aleatorios afectó a la vez la integridad y la disponibilidad. Con cinco cortes por corrida, la relación de muestras recibidas fue de ${N.recv_disc} para cortes de 0,5, 1 y 3 s, frente a fracciones nominales de corte de ${N.recv_disc_nominal}; la diferencia corresponde al tiempo de recuperación de la conexión. El intervalo máximo entre llegadas fue de ${N.ia_max_disc3} ms para cortes de 0,5, 1 y 3 s respectivamente: el mismo valor para los cortes de 0,5 y 1 s, y ${N.recon_excess} ms por encima de la duración del corte en cada caso. Los segundos sin datos por corrida fueron ${N.nodata_disc}.`,

  ...(hasStruct ? [
  `En la familia estructurada, la pérdida contigua dentro del ensayo redujo la relación de muestras recibidas a ${N.recv_burst} para el 10, 25 y 40 % de la ventana, con ${N.gaps_burst} huecos por corrida, uno por ensayo, y no alteró la temporalidad. La desconexión sincronizada con el inicio de la ventana de decodificación, con un corte por ensayo, redujo la relación de muestras recibidas a ${N.recv_disct} para cortes de 0,5, 1 y 2 s, con ${N.nodata_disct} segundos sin datos por corrida e intervalos máximos entre llegadas de ${N.ia_max_disct} ms; dentro de la ventana de cada ensayo quedaron disponibles, en mediana, ${N.nsamp_disct} de las mil muestras, de modo que la proporción de decisiones válidas fue de ${N.valid_disct}. La Figura 1 muestra la latencia media por tipo y severidad de fallo.`,
  ] : [
  "La Figura 1 muestra la latencia media por tipo y severidad de fallo.",
  ]),

  { table: {
      num: "Tabla 3",
      title: "Integridad, temporalidad y disponibilidad del flujo por tipo y severidad de fallo (mediana entre sujetos)",
      headers: T.infra.headers,
      rows: T.infra.rows,
      note: "Mediana de la mediana por sujeto sobre sus cinco corridas. Huecos: discontinuidades mayores a un intervalo de muestreo en las marcas de tiempo recibidas. Latencia: llegada menos marca de tiempo nominal del último dato del bloque. El asterisco indica p < 0,05 en la comparación de Wilcoxon contra la referencia con corrección de Holm. Cada corrida con desconexión incluyó cinco cortes; cada corrida con desconexión en el ensayo, un corte por ensayo.",
  } },

  { figure: {
      num: "Figura 1",
      title: "Latencia media de extremo a extremo por tipo y severidad de fallo.",
      path: "fig/fig_latencia.png",
      note: "Cada panel corresponde a un tipo de fallo; el primer punto de cada panel es la condición de referencia. Los marcadores indican la mediana entre sujetos y las barras de error el rango intercuartílico (percentiles 25 y 75). Severidades: pérdida en porcentaje de muestras omitidas; jitter en desviación estándar de la demora; retraso en demora constante; desconexión en duración de cada corte; pérdida contigua en porcentaje de la ventana del ensayo; desconexión en el ensayo en duración del corte.",
  } },

  { h2: "Efecto de los fallos sobre el desempeño del decodificador" },

  `Con el decodificador de referencia, CSP y LDA, la *balanced accuracy* no cambió con ningún tipo ni severidad de la familia uniforme (Tabla 4 y Figura 2): la mediana entre sujetos fue de ${N.bacc_ref} en la referencia y en ${N.bacc_n_igual} de las ${N.bacc_n_total} condiciones uniformes${N.bacc_excepciones ? ` (${N.bacc_excepciones})` : ""}, y la mediana de las diferencias apareadas fue de 0,000 en todas. ${friedmanUniform().charAt(0).toUpperCase() + friedmanUniform().slice(1)} La tasa de decisiones válidas fue de 1,000 en todas las condiciones uniformes y la confianza media del clasificador se mantuvo entre ${N.conf_rango}.`,

  `El efecto funcional de los fallos temporales se observó en el retardo de decisión, no en la exactitud: el pipeline emitió cada decisión ${N.dd_ref} ms después del fin nominal del ensayo en la referencia, ${N.dd_delay} ms con retrasos de 50, 100 y 250 ms, y ${N.dd_jitter} ms con *jitter* de 10, 50 y 100 ms; la pérdida de muestras y la desconexión no modificaron ese retardo (${N.dd_otros} ms).`,

  ...(hasStruct ? [
  `En la familia estructurada, la *balanced accuracy* de CSP y LDA fue de ${N.bacc_burst_csp} con pérdida contigua del 10, 25 y 40 % de la ventana (p corregidas de ${N.p_burst_csp}; Friedman: ${fr("burst_trial")}), y de ${N.bacc_disct_csp} con desconexión en el ensayo de 0,5, 1 y 2 s (p corregidas de ${N.p_disct_csp}; Friedman: ${fr("disconnect_trial")}). ${sigSentence(N.sig_struct_csp, "CSP y LDA")}`,
  ] : []),

  ...(hasNet ? [
  `Con el segundo decodificador, EEGNet, la *balanced accuracy* de referencia fue de ${N.bacc_ref_net} y, en la familia uniforme, ${N.bacc_uniform_net_rango.split(" y ")[0] === N.bacc_uniform_net_rango.split(" y ")[1] ? `fue de ${N.bacc_uniform_net_rango.split(" y ")[0]} en las doce condiciones` : `se ubicó entre ${N.bacc_uniform_net_rango} según la condición`} (Tabla 4 y Figura 3). ${sigSentence(N.sig_uniform_net, "EEGNet en la familia uniforme")}${hasStruct ? ` En la familia estructurada, EEGNet obtuvo ${N.bacc_burst_net} con pérdida contigua del 10, 25 y 40 % (p corregidas de ${N.p_burst_net}; Friedman: ${fr("burst_trial", T.desempeno.friedman_eegnet)}) y ${N.bacc_disct_net} con desconexión en el ensayo de 0,5, 1 y 2 s (p corregidas de ${N.p_disct_net}; Friedman: ${fr("disconnect_trial", T.desempeno.friedman_eegnet)}). ${sigSentence(N.sig_struct_net, "EEGNet en la familia estructurada")}` : ""}`,
  ] : []),

  { table: {
      num: "Tabla 4",
      title: "Desempeño funcional de los dos decodificadores por tipo y severidad de fallo",
      headers: T.desempeno.headers,
      rows: T.desempeno.rows,
      note: "Mediana entre sujetos de la mediana por sujeto sobre sus cinco corridas. p: comparación de Wilcoxon contra la referencia con corrección de Holm dentro de cada tipo de fallo; el asterisco indica p < 0,05. Decisiones válidas: proporción de ensayos con decisión, según la regla de medio segundo de señal en la ventana, para el pipeline en línea. Un guion indica que la prueba no fue calculable por ausencia de variación.",
  } },

  { figure: {
      num: "Figura 2",
      title: "Balanced accuracy del decodificador de referencia (CSP y LDA) por tipo y severidad de fallo.",
      path: "fig/fig_degradacion.png",
      note: "Cada panel corresponde a un tipo de fallo; el primer punto es la referencia. Marcadores: mediana entre sujetos; barras de error: rango intercuartílico.",
  } },

  ...(hasNet ? [
  { figure: {
      num: "Figura 3",
      title: "Balanced accuracy del segundo decodificador (EEGNet) por tipo y severidad de fallo.",
      path: "fig/fig_degradacion_eegnet.png",
      note: "Evaluado sobre los segmentos guardados por el pipeline. Cada panel corresponde a un tipo de fallo; el primer punto es la referencia. Marcadores: mediana entre sujetos; barras de error: rango intercuartílico.",
  } },
  ] : []),

  { h2: "Divergencia entre el estado operativo de la infraestructura y el desempeño funcional" },

  `Con la ventana de ocho ensayos y el umbral por sujeto, la proporción máxima de ventanas de un segundo en que la infraestructura se mostró operativa mientras el decodificador de referencia estaba degradado fue de ${N.silent_max}, considerando todas las condiciones (Tabla 5). En la familia uniforme, la divergencia observada fue de signo opuesto y se concentró en la desconexión: ventanas en que el flujo no estaba operativo, por ausencia de muestras, sin que el desempeño funcional cruzara el umbral, en una proporción de ${N.loud_disc} para cortes de 0,5, 1 y 3 s; en la pérdida de muestras, el *jitter* y el retraso, ambas proporciones fueron nulas.${hasStruct ? ` En la familia estructurada, la proporción de ventanas operativas y degradadas fue de ${N.silent_burst} con pérdida contigua del 10, 25 y 40 %, y de ${N.silent_disct} con desconexión en el ensayo de 0,5, 1 y 2 s, condición en la que las ventanas no operativas y no degradadas alcanzaron ${N.loud_disct}.` : ""} En total se registraron ${N.episodios} episodios de degradación funcional en las ${N.n_execs_txt} ejecuciones.`,

  { table: {
      num: "Tabla 5",
      title: "Proporción de ventanas divergentes entre estado operativo y degradación funcional por condición",
      headers: T.divergencia.headers,
      rows: T.divergencia.rows,
      note: "Ventanas de un segundo. Operativo: llegaron muestras y no hubo excepciones en el segundo. Degradado: la última balanced accuracy móvil disponible del decodificador de referencia fue inferior al umbral del sujeto. Valores: mediana entre sujetos de la proporción por ejecución.",
  } },

  { h2: "Detección de la degradación funcional a partir de la telemetría" },

  `La comparación entre el detector por umbrales y los modelos de clasificación se realizó sobre ${N.n_windows} ventanas etiquetadas, de las cuales ${N.n_pos} correspondieron a degradación funcional, agrupadas en los ${N.episodios} episodios mencionados (Tabla 6). El detector por umbrales alcanzó una precisión de ${N.thr_prec}, una sensibilidad de ${N.thr_recall} y una tasa de falsos positivos de ${N.thr_fpr}; la regresión logística, ${N.lr_prec}, ${N.lr_recall} y ${N.lr_fpr}; *random forest*, ${N.rf_prec}, ${N.rf_recall} y ${N.rf_fpr}; y *gradient boosting*, ${N.gb_prec}, ${N.gb_recall} y ${N.gb_fpr}. El mayor puntaje F1 correspondió a ${N.best_detector} (${N.best_f1}). Los retardos de detección medianos fueron de ${N.thr_delay}, ${N.lr_delay}, ${N.rf_delay} y ${N.gb_delay} s respectivamente; un retardo nulo indica que la alarma ya estaba activa en el primer segundo degradado del episodio.`,

  { table: {
      num: "Tabla 6",
      title: "Desempeño de los detectores de degradación funcional con validación dejando un sujeto fuera",
      headers: T.detectores.headers,
      rows: T.detectores.rows,
      note: "Umbrales: alarma cuando alguna variable de telemetría sale del rango observado en las corridas de referencia de los otros ocho sujetos. Modelos entrenados con ocho sujetos y evaluados en el restante, rotando. Retardo de detección: mediana, en segundos, entre el primer segundo degradado de cada episodio y la primera alarma dentro del episodio; un guion indica que no se detectó ningún episodio.",
  } },

  { h2: "Documentación y replicabilidad" },

  `El banco, los guiones de análisis, las decisiones por ensayo y la telemetría por segundo de todas las ejecuciones se publicaron con licencia MIT en el repositorio público https://github.com/agustama27/bci-fault-bench (versión 2.0, 27 de septiembre de 2026)${N.doi ? `, con identificador persistente ${N.doi}` : ""}, junto con las versiones de software utilizadas (Python 3.12, MNE-Python 1.13.2, MNE-LSL 1.14.0, MOABB 1.7.2, scikit-learn 1.9.1, PyTorch 2.14) y la especificación de la máquina (Amazon EC2 c6i.2xlarge, Ubuntu 24.04). Cada ejecución quedó identificada por sujeto, corrida y condición, con su semilla, de modo que la realización del fallo es repetible; por cada una se conservaron el registro del inyector, las decisiones por ensayo, la telemetría por segundo y los segmentos de señal recibidos. El ejecutor no necesitó reanudar la campaña.`,
];
