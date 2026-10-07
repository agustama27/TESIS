// Resultados del Entregable 2 (versión 4: ajustados a la extensión de la consigna, ~5 páginas).
// Pretérito, orden de los objetivos específicos, sin citas, sin métodos, sin interpretación.
// El texto destaca el patrón y las cifras centrales; los valores completos van en tablas y figuras.
// Tablas desde tablas.json y cifras desde numeros.json (scripts del banco); versión 3 en resultados.v3.js.
const T = require("./tablas.json");
const N = require("./numeros.json");

const es = (n) => (typeof n === "number" ? n.toFixed(2).replace(".", ",") : n);
const fr = (k, dict) => {
  const f = dict[k];
  if (!f || f[0] === null) return "no calculable";
  return `χ²(3) = ${es(f[0])}, ${f[1] < 0.001 ? "p < 0,001" : `p = ${f[1].toFixed(3).replace(".", ",")}`}`;
};
const joinES = (arr) => (arr.length === 0 ? "ninguna" : arr.length === 1 ? arr[0] : arr.slice(0, -1).join(", ") + " y " + arr[arr.length - 1]);

// rango de la balanced accuracy de referencia de CSP y LDA en el banco (columna 3 de la tabla por sujeto)
const baccRef = N.tabla2.map((r) => parseFloat(r[2].replace(",", ".")));
const rango = `${Math.min(...baccRef).toFixed(3).replace(".", ",")} y ${Math.max(...baccRef).toFixed(3).replace(".", ",")}`;

// Tabla 2 compacta: la variable que cada modelo de fallo perturba directamente
const INFRA = T.infra.rows;
const refRow = INFRA[0];
const COLS = { recv: 2, lat: 4, ia: 5, nodata: 6 };
const VAR = [
  ["Pérdida de muestras", "Muestras recibidas / esperadas", "recv", "1, 5 y 10 %"],
  ["*Jitter*", "Desv. del intervalo entre bloques (ms)", "ia", "10, 50 y 100 ms"],
  ["Retraso", "Latencia media (ms)", "lat", "50, 100 y 250 ms"],
  ["Desconexión", "Segundos sin datos por corrida", "nodata", "0,5, 1 y 3 s"],
  ["Pérdida contigua en el ensayo", "Muestras recibidas / esperadas", "recv", "10, 25 y 40 %"],
  ["Desconexión en el ensayo", "Muestras recibidas / esperadas", "recv", "0,5, 1 y 2 s"],
];
const infraRows = VAR.map(([tipo, variable, col, sevs]) => {
  const vals = INFRA.filter((r) => r[0] === tipo).map((r) => r[COLS[col]]);
  if (vals.length !== 3) throw new Error(`Tabla 2: faltan filas de ${tipo}`);
  return [tipo, variable, sevs, refRow[COLS[col]], ...vals];
});

const loudBurst40 = T.divergencia.rows.find((r) => r[0] === "Pérdida contigua en el ensayo" && r[1].startsWith("40"));

module.exports = [
  "Los resultados se presentan en el orden de los objetivos específicos. Salvo indicación, las cifras son medianas entre sujetos de la mediana de cada sujeto sobre sus cinco corridas.",

  { h2: "Construcción y verificación del banco de experimentación" },

  `El banco ejecutó las ${N.n_execs_txt} ejecuciones de la campaña definitiva sin intervención manual ni ejecuciones fallidas, en ${N.horas_campana} horas de reloj. En la referencia, el servicio de reproducción despertó para emitir cada bloque con un error cuyo percentil 99 fue de ${N.timing_p99_us} microsegundos, y ejecutar doce reproducciones simultáneas modificó la latencia media en ${N.ctrl_lat_ms} ms y la desviación del intervalo entre bloques en ${N.ctrl_ia_ms} ms respecto de una ejecución aislada. La *balanced accuracy* de CSP y LDA en el banco sin fallo coincidió con la calculada fuera de línea en ${N.tabla2_iguales === 9 ? "los nueve sujetos" : `${N.tabla2_iguales} de los nueve sujetos`}, con valores entre ${rango}, y la reaplicación de CSP y LDA a los segmentos guardados reprodujo el ${N.equiv_pct} % de las ${N.equiv_n} decisiones válidas tomadas en línea. La primera etapa de la campaña (234 ejecuciones, familia uniforme) no mostró efecto funcional de ningún fallo.`,

  { h2: "Efecto de los fallos sobre la integridad, la temporalidad y la disponibilidad del flujo" },

  `Cada modelo de fallo alteró la variable que su definición perturba, y las comparaciones de esa variable contra la referencia resultaron significativas en todas las severidades (Tabla 2); en la pérdida de muestras, el *jitter* y el retraso, con p corregida ≤ ${N.p_min} y r = ${N.r_top}. La pérdida de muestras no modificó la regularidad de llegada, y el *jitter* y el retraso no eliminaron muestras. Con desconexión, la relación de muestras recibidas (${N.recv_disc} para cortes de 0,5, 1 y 3 s) quedó por debajo de la fracción nominal no cortada (${N.recv_disc_nominal}). El intervalo máximo entre llegadas fue de ${N.ia_max_disc3} ms para cortes de 0,5, 1 y 3 s y de ${N.ia_max_disct} ms para desconexiones en el ensayo de 0,5, 1 y 2 s, igual para los cortes de 0,5 y 1 s en ambas familias (Figura 6). Con desconexión en el ensayo quedaron disponibles, en mediana, ${N.nsamp_disct} de las mil muestras de la ventana, y todas las decisiones fueron válidas.`,

  { table: {
      num: "Tabla 2",
      title: "Variable perturbada por cada modelo de fallo, por severidad (mediana entre sujetos)",
      headers: ["Tipo de fallo", "Variable", "Severidades", "Ref.", "Baja", "Media", "Alta"],
      widths: [1750, 2150, 1450, 700, 800, 800, 854],
      rows: infraRows,
      note: "Baja, media y alta: las tres severidades, en el orden indicado. El asterisco indica p < 0,05 en la comparación de Wilcoxon contra la referencia con corrección de Holm. La tabla completa de variables por condición se publica con el banco.",
  } },

  { figure: {
      num: "Figura 6",
      title: "Intervalo máximo entre llegadas según la duración del corte inyectado, en las dos familias de desconexión.",
      path: "fig/fig_reconexion.png",
      note: "La línea discontinua marca un intervalo igual a la duración del corte. Los marcadores de 0,5 y 1 s se desplazaron levemente en horizontal para que no se superpongan.",
  } },

  { h2: "Efecto de los fallos sobre el desempeño del decodificador" },

  `La *balanced accuracy* de referencia fue de ${N.bacc_ref} con CSP y LDA y de ${N.bacc_ref_net} con EEGNet, y ninguna de las ${N.bacc_n_total} condiciones de la familia uniforme la modificó en ninguno de los dos decodificadores (Figura 7). En la familia estructurada, CSP y LDA obtuvo ${N.bacc_burst_csp} con pérdida contigua del 10, 25 y 40 % de la ventana y ${N.bacc_disct_csp} con desconexión en el ensayo de 0,5, 1 y 2 s, y EEGNet, ${N.bacc_burst_net} y ${N.bacc_disct_net}. Resultaron significativas, para CSP y LDA, ${joinES(N.sig_struct_csp)}, y para EEGNet, ${joinES(N.sig_struct_net)}. Las pruebas de Friedman de la familia estructurada fueron significativas para ambos decodificadores (CSP y LDA: ${fr("burst_trial", T.desempeno.friedman)} y ${fr("disconnect_trial", T.desempeno.friedman)}; EEGNet: ${fr("burst_trial", T.desempeno.friedman_eegnet)} y ${fr("disconnect_trial", T.desempeno.friedman_eegnet)}). El efecto de los fallos temporales apareció en el retardo de decisión: ${N.dd_ref} ms en la referencia, ${N.dd_delay} ms con retrasos de 50, 100 y 250 ms y ${N.dd_jitter} ms con *jitter* de 10, 50 y 100 ms.`,

  { figure: {
      num: "Figura 7",
      title: "Balanced accuracy de los dos decodificadores por tipo y severidad de fallo.",
      path: "fig/fig_desempeno.png",
      note: "Marcadores: mediana entre sujetos; barras: rango intercuartílico; ref.: referencia. EEGNet se evaluó sobre los segmentos guardados por el pipeline. El asterisco indica p < 0,05 en la comparación de Wilcoxon contra la referencia con corrección de Holm.",
  } },

  { h2: "Divergencia entre el estado operativo de la infraestructura y el desempeño funcional" },

  `La proporción de segundos en que la infraestructura se mostró operativa mientras CSP y LDA estaba degradado fue de ${N.silent_max} en las 18 condiciones. La divergencia inversa, segundos sin datos en los que el desempeño no cruzó el umbral, fue de ${N.loud_disc} con desconexiones de 0,5, 1 y 3 s, de ${N.loud_disct} con desconexiones en el ensayo de 0,5, 1 y 2 s y de ${loudBurst40[3]} con pérdida contigua del 40 %, y nula en las demás condiciones. Se registraron ${N.episodios} episodios de degradación funcional.`,

  { h2: "Detección de la degradación funcional a partir de la telemetría" },

  `De las ${N.n_windows} ventanas evaluadas, ${N.n_pos} correspondieron a degradación funcional (prevalencia ${N.prevalencia}, precisión esperable de un detector aleatorio). La precisión de los cuatro detectores se ubicó entre ${N.gb_prec} y ${N.rf_prec} (Tabla 3), y la del detector por umbrales (${N.thr_prec}) fue inferior a la prevalencia. La regresión logística alcanzó la mayor sensibilidad (${N.lr_recall}) con una tasa de falsos positivos de ${N.lr_fpr}, y *random forest*, la menor tasa de falsos positivos entre los detectores que emitieron alarmas (${N.rf_fpr}) con una sensibilidad de ${N.rf_recall}.`,

  { table: {
      num: "Tabla 3",
      title: "Desempeño de los detectores de degradación funcional con validación dejando un sujeto fuera",
      headers: T.detectores.headers,
      rows: T.detectores.rows,
      note: "Retardo de detección: mediana, en segundos, entre el primer segundo degradado de cada episodio y la primera alarma dentro de él; un guion indica que no se detectó ningún episodio. Precisión promedio: área bajo la curva de precisión y sensibilidad.",
  } },

  { h2: "Documentación y replicabilidad" },

  "El banco, los guiones de análisis, las decisiones por ensayo, la telemetría por segundo y los segmentos de señal de todas las ejecuciones se publicaron con licencia MIT en https://github.com/agustama27/bci-fault-bench (versión 2.0), cada ejecución identificada por sujeto, corrida, condición y semilla, de modo que la realización de cada fallo es repetible.",
];
