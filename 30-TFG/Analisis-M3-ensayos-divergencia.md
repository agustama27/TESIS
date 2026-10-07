# Análisis M3b: ensayos tocados vs. no tocados, posición del hueco y sensibilidad de la divergencia

> 2026-10-07. Campaña definitiva `campaign-2026-09-27` (855 ejecuciones = 9 sujetos x 5 corridas x 19 condiciones). Nota nueva; no modifica el manuscrito ni el código del banco. Complementa a [[Analisis-M3]] (piso de reconexión, exposición, IC).
>
> **Estos análisis son EXPLORATORIOS y post hoc.** No estaban en el plan de análisis previo; se hicieron después de ver los resultados principales. No hay corrección por multiplicidad entre tablas y los p valores deben leerse como descriptivos (con n = 9 sujetos el p exacto bilateral mínimo de Wilcoxon es 0,0039).
>
> **Convenciones.** `B = C:\Users\agustin.tamagusuku\Desktop\bci-fault-bench`; datos `D = B\campaign-2026-09-27`; salidas en `D\analysis-m3b\`; scripts en `B\scripts\m3b_*.py` (ejecutados con `C:\Users\agustin.tamagusuku\.venvs\bcibench\Scripts\python`). Las tablas usan punto decimal; en el texto, coma. Cada cifra lleva `[script -> archivo]`. Decodificadores: CSP+LDA en línea (`trials.csv`) y EEGNet fuera de línea sobre los segmentos recibidos (`trials_eegnet.csv`). "Cambio" = la decisión difiere de la que tomó el mismo decodificador en el mismo ensayo de la ejecución de referencia; un ensayo inválido (sin decisión) cuenta como cambio y como error. "pp" = puntos porcentuales.
>
> **Dato de partida.** Los segmentos guardados (`segments.npz`) no están en la copia local (se subieron a Zenodo); `fault_log.jsonl` de `burst_trial` está vacío. La Tarea B se resolvió igual (sección 2).

## 0. Resumen ejecutivo

1. **A. Los ensayos no tocados no cambian nunca; los tocados sí.** En 9.484 ensayos con ventana íntegra (jitter, retraso y los no cortados de la desconexión uniforme) hay **0 cambios de decisión** en ambos decodificadores (incluidos 79 ensayos con el relleno de filtrado de 1 s dañado). En desconexión uniforme, el 7,3 % de los ensayos queda tocado (236 de 3.240) y en ellos cambia el 17,4 % (CSP+LDA) y el 23,3 % (EEGNet) de las decisiones: 9 de 9 sujetos, p = 0,004. El daño queda confinado al ensayo donde cae la falla (sin contagio a los vecinos), que es la prueba directa de "importa dónde cae".
2. **A. Cambiar no es lo mismo que errar más.** Los cambios son entre dos clases: en la desconexión uniforme el 71 % son perjudiciales (acertaba y deja de acertar) y el 29 % favorables, en ambos decodificadores. El acierto de los tocados baja 6,8 pp (CSP+LDA, p = 0,098 por sujeto) y 9,8 pp (EEGNet, p = 0,031) respecto de la referencia en esos mismos ensayos.
3. **A. Dosis-respuesta monótona, EEGNet el doble de sensible.** Cambio por fracción de ventana recibida (1000 / 900-999 / 750-899 / 500-749 / 125-499): CSP+LDA 0 / 4,7 / 7,6 / 12,7 / 21,1 %; EEGNet 0 / 4,0 / 11,9 / 25,4 / 41,2 %. El acierto solo cae de forma apreciable con menos de 750 muestras (CSP+LDA -4,2 y -9,3 pp; EEGNet -11,0 y -21,7 pp). Con la pérdida uniforme (siempre 870-998 muestras) el cambio es de 1-6 % y el acierto casi no se mueve.
4. **A. La forma del hueco importa para EEGNet, no para CSP+LDA.** A igual pérdida (n = 900) un hueco contiguo cambia 7,9 % de las decisiones de EEGNet contra 4,4 % de la pérdida dispersa (p = 0,008, 8 de 9 sujetos); en CSP+LDA, 6,0 % contra 6,0 %.
5. **B. La posición del hueco dentro de la ventana no se pudo distinguir.** Se recuperó la posición exacta de los 3.240 huecos (reproduciendo la semilla del inyector; 3.240/3.240 coinciden con la telemetría). La tasa de cambio no depende de la posición (Friedman p entre 0,37 y 1,00). Solo en EEGNet el Δ acierto tiende a ser peor con el hueco al inicio (-7,1 pp) que al final (-1,8 pp; p = 0,055 inicio vs. fin): coherente con la hipótesis de [[Analisis-M3]] punto 7, pero no demostrada.
6. **C. El "0 operativo y degradado" es cierto como mediana, no como conteo.** Con W = 8 y umbral = mínimo se reproduce exactamente `t_divergencia.csv` (mediana 0 en las 18 condiciones) y `windows.csv`. Pero hay **2.888 segundos silenciosos de 229.500 (1,26 %) en 57 de 810 ejecuciones con fallo**: el 88,7 % de los segundos degradados son operativos. Hasta 7,4 % en desconexión en el ensayo de 2 s y 69 % en una ejecución.
7. **C. Robustez de la mediana.** La mediana entre sujetos sigue en 0 en las 18 condiciones para W = 4, 6, 8, umbral mínimo o mínimo − 0,05, y operativo base o estricto. Aparece > 0 con W = 12 (una condición, desconexión en el ensayo de 2 s: 14,3 %; 2,2 % con mínimo − 0,05) y con el percentil 5 (4 condiciones en todo W, hasta 21,2 %), donde por construcción también marca el 2,9-4,4 % de la propia referencia.
8. **C. Operativo estricto: la falla silenciosa baja poco y la alarma falsa explota.** Latencia < 50 ms y sin huecos reduce los segundos silenciosos de 1,26 % a 1,06 % (W = 8), pero marca "no operativo y no degradado" en el 40,5 % de los segundos (100 % con retraso, 92-100 % con pérdida), porque el decodificador sigue intacto.
9. **Límites principales.** n = 9 sujetos; los ensayos tocados de la desconexión uniforme son pocos (236, unos 26 por sujeto); los bins de dosis mezclan familias de fallo; la Tarea B tiene poca potencia (unos 360 ensayos por celda, 9 sujetos); la mediana oculta una cola real en C; todo es post hoc.
10. **Implicancia para el manuscrito.** Reformular "0 segundos operativos y degradados" como "mediana de 0 entre sujetos; 1,26 % de los segundos y 7 % de las ejecuciones con fallo tienen al menos un segundo operativo y degradado", y no usar la posición del hueco como explicación firme de EEGNet.

---

## 1. Tarea A: ensayos tocados vs. no tocados

### 1.1 Método

- **Emparejamiento.** Cada ensayo de cada ejecución se une con el mismo ensayo (mismo sujeto, corrida e índice) de la ejecución de referencia de esa corrida (`sNN-rR-ref`). Verificado en las 855 ejecuciones: 24 ensayos, etiquetas idénticas, onsets idénticos (diferencia máxima 1,9e-12 s). Contra sí misma la referencia da 0 cambios y 0 ensayos tocados. `[m3b_common.py (load_paired) -> m3b_A_trials.csv]`
- **Tocado** = `n_samples < 1000` en `trials.csv` (muestras recibidas dentro de [onset+2, onset+6] s) o ensayo inválido. Se usa el `n_samples` en línea para ambos decodificadores (en `trials_eegnet.csv` el conteo difiere en alguna fracción pequeña de ensayos; no se exploró por qué).
- **Acierto** = decisión válida e igual a la etiqueta (inválido = error, como en la balanced accuracy móvil). **Perjudicial** = acertaba en la referencia y ya no; **favorable** = fallaba y ahora acierta.
- **Unidad de inferencia = sujeto.** Se agregan los ensayos de las 5 corridas de cada sujeto y recién ahí se prueba: Wilcoxon apareado bilateral (exacto) entre sujetos que tienen ambos tipos de ensayo (A2), o de Δ acierto contra 0 (A1). `[m3b_ensayos.py -> m3b_A_subject.csv, m3b_A_cond.csv]`
- **Qué contrastes existen.** En `loss`, `burst_trial` y `disconnect_trial` TODOS los ensayos quedan tocados (n_samples 870-998, 900/750/600 y 360-620); en `jitter` y `delay` NINGUNO (n = 1000 siempre). El contraste tocado vs. no tocado dentro de una misma condición solo existe en la desconexión uniforme. Por eso la pérdida uniforme se reporta aparte (A1) y el resto de la evidencia es de dosis-respuesta (A3).

### 1.2 Resultados por condición

`[m3b_ensayos.py -> m3b_A_cond.csv; tabla: m3b_tablas_md.py -> m3b_tablas.md]`. Δ acierto = acierto de los tocados menos el acierto de la referencia en esos mismos ensayos (controla la dificultad de cada ensayo).

**TABLA A1 · CSP+LDA**

| Condición | Ens. tocados | Ens. no tocados | Cambio tocados (%) | Cambio no tocados (%) | Acierto tocados (%) | Acierto de la ref. en esos ensayos (%) | Δ acierto (pp) | Perjudicial (%) | Favorable (%) | Δ acierto mediana sujeto (pp) | p (Wilcoxon sujeto, Δ vs ref) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| pérdida 1 % | 1080 | 0 | 1.9 | — | 75.6 | 75.9 | -0.4 | 1.1 | 0.7 | +0.0 | 0.375 |
| pérdida 5 % | 1080 | 0 | 5.1 | — | 74.7 | 75.9 | -1.2 | 3.1 | 1.9 | -0.8 | 0.328 |
| pérdida 10 % | 1080 | 0 | 6.0 | — | 74.7 | 75.9 | -1.2 | 3.6 | 2.4 | +0.0 | 0.445 |
| jitter 10/50/100 ms (3 filas idénticas) | 0 | 1080 c/u | — | 0.0 | — | — | — | — | — | — | — |
| retraso 50/100/250 ms (3 filas idénticas) | 0 | 1080 c/u | — | 0.0 | — | — | — | — | — | — | — |
| desconexión 0,5 s | 75 | 1005 | 8.0 | 0.0 | 77.3 | 80.0 | -2.7 | 5.3 | 2.7 | +0.0 | 0.750 |
| desconexión 1 s | 67 | 1013 | 10.4 | 0.0 | 82.1 | 83.6 | -1.5 | 6.0 | 4.5 | +0.0 | 0.250 |
| desconexión 3 s | 94 | 986 | 29.8 | 0.0 | 64.9 | 78.7 | -13.8 | 20.2 | 6.4 | -11.1 | 0.094 |
| pérdida contigua 10 % | 1080 | 0 | 6.0 | — | 75.1 | 75.9 | -0.8 | 3.4 | 2.6 | -0.8 | 0.223 |
| pérdida contigua 25 % | 1080 | 0 | 9.0 | — | 74.0 | 75.9 | -1.9 | 5.5 | 3.5 | -2.5 | 0.156 |
| pérdida contigua 40 % | 1080 | 0 | 14.0 | — | 70.3 | 75.9 | -5.6 | 9.8 | 4.2 | -5.8 | 0.004 |
| desc. en ensayo 0,5 s | 1080 | 0 | 12.1 | — | 72.3 | 75.9 | -3.6 | 7.9 | 4.3 | -2.5 | 0.027 |
| desc. en ensayo 1 s | 1080 | 0 | 12.1 | — | 72.3 | 75.9 | -3.6 | 7.9 | 4.3 | -2.5 | 0.027 |
| desc. en ensayo 2 s | 1080 | 0 | 20.4 | — | 67.0 | 75.9 | -8.9 | 14.6 | 5.7 | -6.7 | 0.004 |

**TABLA A1 · EEGNet**

| Condición | Ens. tocados | Ens. no tocados | Cambio tocados (%) | Cambio no tocados (%) | Acierto tocados (%) | Acierto de la ref. en esos ensayos (%) | Δ acierto (pp) | Perjudicial (%) | Favorable (%) | Δ acierto mediana sujeto (pp) | p (Wilcoxon sujeto, Δ vs ref) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| pérdida 1 % | 1080 | 0 | 1.1 | — | 76.9 | 77.4 | -0.6 | 0.8 | 0.3 | -0.8 | 0.062 |
| pérdida 5 % | 1080 | 0 | 3.0 | — | 77.0 | 77.4 | -0.4 | 1.7 | 1.3 | +0.0 | 0.688 |
| pérdida 10 % | 1080 | 0 | 4.4 | — | 76.3 | 77.4 | -1.1 | 2.8 | 1.7 | -0.8 | 0.016 |
| jitter 10/50/100 ms (3 filas idénticas) | 0 | 1080 c/u | — | 0.0 | — | — | — | — | — | — | — |
| retraso 50/100/250 ms (3 filas idénticas) | 0 | 1080 c/u | — | 0.0 | — | — | — | — | — | — | — |
| desconexión 0,5 s | 75 | 1005 | 24.0 | 0.0 | 65.3 | 70.7 | -5.3 | 14.7 | 9.3 | +0.0 | 0.781 |
| desconexión 1 s | 67 | 1013 | 14.9 | 0.0 | 74.6 | 83.6 | -9.0 | 11.9 | 3.0 | -11.1 | 0.047 |
| desconexión 3 s | 94 | 986 | 28.7 | 0.0 | 62.8 | 76.6 | -13.8 | 21.3 | 7.4 | -16.7 | 0.031 |
| pérdida contigua 10 % | 1080 | 0 | 7.9 | — | 75.8 | 77.4 | -1.6 | 4.7 | 3.1 | -1.7 | 0.016 |
| pérdida contigua 25 % | 1080 | 0 | 15.1 | — | 73.4 | 77.4 | -4.0 | 9.5 | 5.6 | -2.5 | 0.012 |
| pérdida contigua 40 % | 1080 | 0 | 24.2 | — | 69.9 | 77.4 | -7.5 | 15.8 | 8.3 | -9.2 | 0.008 |
| desc. en ensayo 0,5 s | 1080 | 0 | 26.0 | — | 64.7 | 77.4 | -12.7 | 19.4 | 6.7 | -10.0 | 0.004 |
| desc. en ensayo 1 s | 1080 | 0 | 26.0 | — | 64.7 | 77.4 | -12.7 | 19.4 | 6.7 | -10.0 | 0.004 |
| desc. en ensayo 2 s | 1080 | 0 | 41.7 | — | 55.2 | 77.4 | -22.2 | 31.9 | 9.7 | -20.8 | 0.008 |

Lectura:

- **No tocados: 0 cambios.** En jitter y retraso (6.480 ensayos, ventana íntegra) y en los 3.004 no tocados de la desconexión uniforme, ningún decodificador cambia una sola decisión. Es lo esperado de un pipeline determinista; sirve de control del emparejamiento. Control del relleno: 79 de esos 3.004 tienen un déficit de muestras en el segundo previo o posterior a la ventana (el relleno de 1 s del filtro IIR) y tampoco cambian `[m3b_pad.py -> m3b_A_pad.csv]`. La definición "tocado" mira solo los 4 s de la ventana.
- **Pérdida uniforme (aparte).** Todos los ensayos pierden muestras sueltas (n = 870-998) y el cambio es de 1,9 / 5,1 / 6,0 % (CSP+LDA) y 1,1 / 3,0 / 4,4 % (EEGNet), con Δ acierto de -0,4 a -1,2 pp (solo EEGNet con 10 % llega a p = 0,016). No hay ensayos no tocados con los que contrastar.
- **Los dos cortes de la desconexión en el ensayo de 0,5 y 1 s son la misma condición** para el decodificador (idénticas filas): el piso de reconexión de [[Analisis-M3]] hace que ambos dejen una ventana de unas 620 muestras.
- Con 1 s (CSP+LDA) los tocados aciertan más (82,1 %) que los no tocados (75,4 %) por azar de muestreo: son 67 ensayos (unos 7 por sujeto). Por eso el Δ contra la referencia en los mismos ensayos es la comparación que corresponde, no tocado vs. no tocado.

### 1.3 Contraste directo tocado vs. no tocado (desconexión uniforme)

`[m3b_ensayos.py -> m3b_A_cond.csv]`. Solo sujetos con ambos tipos de ensayo (9 de 9).

**TABLA A2 · CSP+LDA**

| Condición | Sujetos con ambos tipos | Cambio tocados (mediana suj., %) | Cambio no tocados (mediana suj., %) | p cambio (Wilcoxon apareado) | Sujetos con más cambio en tocados | Δ acierto toc. − no toc. (mediana suj., pp) | p acierto (Wilcoxon apareado) | Δ acierto toc. vs ref. (mediana suj., pp) | p (vs ref.) |
|---|---|---|---|---|---|---|---|---|---|
| desconexión 0,5 s | 9 | 10.0 | 0.0 | 0.062 | 5/9 | 2.7 | 1.000 | +0.0 | 0.750 |
| desconexión 1 s | 9 | 11.1 | 0.0 | 0.031 | 6/9 | 9.0 | 0.570 | +0.0 | 0.250 |
| desconexión 3 s | 9 | 27.3 | 0.0 | 0.008 | 8/9 | -8.4 | 0.496 | -11.1 | 0.094 |
| desconexión uniforme (3 sev. juntas) | 9 | 15.4 | 0.0 | 0.004 | 9/9 | 0.6 | 0.820 | -7.7 | 0.098 |

**TABLA A2 · EEGNet**

| Condición | Sujetos con ambos tipos | Cambio tocados (mediana suj., %) | Cambio no tocados (mediana suj., %) | p cambio (Wilcoxon apareado) | Sujetos con más cambio en tocados | Δ acierto toc. − no toc. (mediana suj., pp) | p acierto (Wilcoxon apareado) | Δ acierto toc. vs ref. (mediana suj., pp) | p (vs ref.) |
|---|---|---|---|---|---|---|---|---|---|
| desconexión 0,5 s | 9 | 22.2 | 0.0 | 0.008 | 8/9 | -6.1 | 0.129 | +0.0 | 0.781 |
| desconexión 1 s | 9 | 14.3 | 0.0 | 0.016 | 7/9 | -5.7 | 0.496 | -11.1 | 0.047 |
| desconexión 3 s | 9 | 30.0 | 0.0 | 0.008 | 8/9 | -18.1 | 0.039 | -16.7 | 0.031 |
| desconexión uniforme (3 sev. juntas) | 9 | 23.1 | 0.0 | 0.004 | 9/9 | -12.1 | 0.020 | -9.7 | 0.031 |

- Con las 3 severidades juntas (236 tocados, 3.004 no tocados), la tasa de cambio es mayor en los tocados en **9 de 9 sujetos** en ambos decodificadores (p = 0,004, el mínimo posible con n = 9). Pooled en ensayos: 17,4 % (CSP+LDA) y 23,3 % (EEGNet) contra 0,0 %; perjudicial 11,4 % y 16,5 %, favorable 4,7 % y 6,8 % `[m3b_ensayos.py -> m3b_A_cond.csv, fila "disconnect-* (3)"]`.
- El acierto de los tocados cae 6,8 pp (73,7 % contra 80,5 % de la referencia en esos ensayos) en CSP+LDA y 9,8 pp (66,9 % contra 76,7 %) en EEGNet; por sujeto, -7,7 pp (p = 0,098) y -9,7 pp (p = 0,031). La caída del acierto es menos nítida que la del cambio porque los cambios se compensan en parte (los favorables).
- El efecto global es chico solo por **dilución**: el 7,3 % de los ensayos tocado x 6,8-9,8 pp de caída da menos de 1 pp de acierto total. Es consistente con la tabla de exposición de [[Analisis-M3]].

### 1.4 Dosis-respuesta

Todas las condiciones con fallo juntas (19.440 ensayos), bins de `n_samples` (1000 = ventana íntegra; "inválido" = ensayo sin decisión). `[m3b_ensayos.py -> m3b_A_dosis.csv]`. Los p son Wilcoxon apareado por sujeto de cada bin contra el bin 1000, corregidos por Holm entre bins.

**TABLA A3**

| Decodificador | n_samples | Ensayos | Sujetos | Cambio agrupado % [IC Wilson 95 %] | Cambio mediana suj. % (Q1–Q3) | Perjudicial % | Favorable % | Acierto % | Acierto ref. mismos ens. % | Δ (pp) | p Holm cambio vs bin 1000 | p Holm acierto vs bin 1000 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CSP+LDA | 1000 | 9484 | 9 | 0.0 [0.0; 0.0] | 0.0 (0.0–0.0) | 0.0 | 0.0 | 75.8 | 75.8 | +0.0 | — | — |
| CSP+LDA | 900-999 | 3834 | 9 | 4.7 [4.1; 5.4] | 2.8 (1.9–3.5) | 2.8 | 1.9 | 74.9 | 75.7 | -0.9 | 0.020 | 0.406 |
| CSP+LDA | 750-899 | 1644 | 9 | 7.6 [6.4; 9.0] | 6.3 (6.0–8.0) | 4.6 | 3.0 | 75.2 | 76.8 | -1.6 | 0.020 | 0.496 |
| CSP+LDA | 500-749 | 3353 | 9 | 12.7 [11.6; 13.9] | 12.0 (11.0–14.4) | 8.4 | 4.3 | 71.9 | 76.1 | -4.2 | 0.020 | 0.020 |
| CSP+LDA | 125-499 | 1116 | 9 | 21.1 [18.9; 23.6] | 22.2 (20.5–23.8) | 15.2 | 5.9 | 66.4 | 75.7 | -9.3 | 0.020 | 0.020 |
| CSP+LDA | inválido | 9 | 6 | 100.0 [70.1; 100.0] | 100.0 (100.0–100.0) | 66.7 | 0.0 | 0.0 | 66.7 | -66.7 | 0.031 | 0.094 |
| EEGNet | 1000 | 9484 | 9 | 0.0 [0.0; 0.0] | 0.0 (0.0–0.0) | 0.0 | 0.0 | 77.4 | 77.4 | +0.0 | — | — |
| EEGNet | 900-999 | 3834 | 9 | 4.0 [3.4; 4.7] | 3.3 (1.6–5.3) | 2.4 | 1.6 | 76.8 | 77.6 | -0.8 | 0.020 | 0.098 |
| EEGNet | 750-899 | 1644 | 9 | 11.9 [10.4; 13.6] | 10.5 (8.1–14.4) | 7.5 | 4.4 | 73.7 | 76.8 | -3.0 | 0.020 | 0.031 |
| EEGNet | 500-749 | 3353 | 9 | 25.4 [23.9; 26.9] | 25.9 (18.7–30.4) | 18.2 | 7.2 | 66.5 | 77.5 | -11.0 | 0.020 | 0.020 |
| EEGNet | 125-499 | 1116 | 9 | 41.2 [38.4; 44.1] | 40.3 (35.4–45.2) | 31.5 | 9.8 | 55.5 | 77.2 | -21.7 | 0.020 | 0.031 |
| EEGNet | inválido | 9 | 6 | 100.0 [70.1; 100.0] | 100.0 (100.0–100.0) | 100.0 | 0.0 | 0.0 | 100.0 | -100.0 | 0.031 | 0.062 |

- **Monótona.** El cambio crece con la fracción perdida en ambos decodificadores y todos los bins difieren del bin 1000 (p Holm = 0,020, el mínimo con 5 comparaciones y n = 9). EEGNet cambia el doble que CSP+LDA desde 750 muestras hacia abajo (25,4 % contra 12,7 % en 500-749).
- **El acierto cae después que el cambio.** Hasta 750 muestras el acierto casi no se mueve (CSP+LDA -0,9 y -1,6 pp, no significativo); baja con < 750. En el bin 125-499, EEGNet pierde 21,7 pp (55,5 %, cerca del azar) y CSP+LDA 9,3 pp.
- **Los cambios son sobre todo perjudiciales.** La razón perjudicial/favorable llega a 2,6:1 (CSP+LDA) y 3,2:1 (EEGNet) en 125-499. Si la ventana dañada llevara a decisiones al azar sobre un decodificador que acierta ~77 %, la razón esperada sería ~3,3:1: el dato de EEGNet es compatible con eso (observación, no probada).
- **Bin "inválido".** 9 ensayos, todos de desconexión de 3 s (6 sujetos): fuera de las conclusiones (cambio 100 % por definición).
- Spearman a nivel ensayo entre fracción perdida y cambio (ensayos válidos con fallo, n = 19.431): rho = 0,273 (CSP+LDA) y 0,397 (EEGNet); solo entre tocados (n = 9.947) 0,177 y 0,329. Los ensayos no son independientes (anidados en sujeto y corrida): solo descriptivo `[m3b_ensayos.py -> consola (m3b_A_log.txt)]`.

**TABLA A4 · por familia de fallo** `[m3b_ensayos.py -> m3b_A_dosis_familia.csv]`. Los bins mezclan familias (por eso el pooled de A3 no es una curva "limpia"):

| Familia | n_samples | Ensayos | Cambio CSP+LDA % | Δ acierto CSP+LDA (pp) | Cambio EEGNet % | Δ acierto EEGNet (pp) |
|---|---|---|---|---|---|---|
| desconexión en ensayo | 500-749 | 2160 | 12.1 | -3.6 | 26.0 | -12.7 |
| desconexión en ensayo | 125-499 | 1080 | 20.4 | -8.9 | 41.7 | -22.2 |
| desconexión uniforme | 1000 | 3004 | 0.0 | +0.0 | 0.0 | +0.0 |
| desconexión uniforme | 900-999 | 31 | 6.5 | +0.0 | 3.2 | +3.2 |
| desconexión uniforme | 750-899 | 47 | 2.1 | -2.1 | 17.0 | +0.0 |
| desconexión uniforme | 500-749 | 113 | 11.5 | -0.9 | 23.9 | -11.5 |
| desconexión uniforme | 125-499 | 36 | 44.4 | -22.2 | 27.8 | -5.6 |
| desconexión uniforme | inválido | 9 | 100.0 | -66.7 | 100.0 | -100.0 |
| jitter | 1000 | 3240 | 0.0 | +0.0 | 0.0 | +0.0 |
| pérdida contigua en ensayo | 900-999 | 1080 | 6.0 | -0.8 | 7.9 | -1.6 |
| pérdida contigua en ensayo | 750-899 | 1080 | 9.0 | -1.9 | 15.1 | -4.0 |
| pérdida contigua en ensayo | 500-749 | 1080 | 14.0 | -5.6 | 24.2 | -7.5 |
| pérdida uniforme | 900-999 | 2723 | 4.1 | -0.9 | 2.5 | -0.6 |
| pérdida uniforme | 750-899 | 517 | 5.2 | -1.0 | 4.8 | -1.4 |
| retraso | 1000 | 3240 | 0.0 | +0.0 | 0.0 | +0.0 |

(El bin 1000 también incluye `delay`; el bin 125-499 de la desconexión en ensayo corresponde a los 2 s.)

### 1.5 A igual pérdida de muestras, distinta forma y ubicación del hueco

`[m3b_equiv.py -> m3b_A_equiv.csv]`. Por sujeto sobre sus 5 corridas; Wilcoxon apareado, n = 9.

| Par (mediana de n_samples) | Decodificador | Cambio A % | Cambio B % | Diferencia mediana suj. (pp) | Sujetos con B > A | p cambio | Δ acierto A (pp) | Δ acierto B (pp) | p Δ acierto |
|---|---|---|---|---|---|---|---|---|---|
| P1: A = pérdida 10 % dispersa (900), B = contigua 10 % (900) | CSP+LDA | 6.0 | 6.0 | +0.8 | 6/9 | 0.484 | -1.2 | -0.8 | 0.938 |
| P1 | EEGNet | 4.4 | 7.9 | +4.2 | 8/9 | 0.008 | -1.1 | -1.6 | 0.438 |
| P2: A = contigua 40 % al azar (600), B = desc. en ensayo 0,5 s, hueco al inicio (620) | CSP+LDA | 14.0 | 12.1 | -1.7 | 3/9 | 0.367 | -5.7 | -3.6 | 0.250 |
| P2 | EEGNet | 24.2 | 26.0 | 0.0 | 4/9 | 0.711 | -7.5 | -12.7 | 0.063 |

- P1: para EEGNet, juntar las muestras perdidas en un hueco cuesta más cambios que dispersarlas (más ruido en el filtro y en la red cuando el hueco es contiguo y se rellena con ceros). Para CSP+LDA, que descarta las muestras faltantes, no hay diferencia. La explicación mecánica es una hipótesis.
- P2: con el hueco pegado al inicio de la ventana la cantidad de cambios es la misma que con un hueco al azar; lo que cambia en EEGNet es la **dirección**: más perjudiciales (19,4 % contra 15,8 %). Esto retoma la observación 7 de [[Analisis-M3]] (-0,130 contra -0,079): el diferencial no viene de cambiar más decisiones sino de acertar menos al cambiar; p = 0,063, sin respaldo firme.

---

## 2. Tarea B: posición del hueco en `burst_trial`

### 2.1 Se puede recuperar la posición exacta

No hay segmentos ni `fault_log` útil, pero el inyector es determinista. `[m3b_posicion.py]`

1. `injector.py` sortea, para cada uno de los 48 eventos de la corrida (no solo los 24 izquierda/derecha), `u = rng.integers(0, 1000 − L + 1)` con `rng = default_rng(seed)`; L = 100/250/400 muestras. La semilla está en `producer.json` (`fault.seed`). El hueco ocupa las muestras `onset·250 + 500 + u` hasta `+ L` de la corrida.
2. El índice de cada ensayo decodificado entre los 48 eventos se reconstruye con los intervalos entre onsets (≈ 8,0 s por evento): `k_i = k_{i-1} + round(Δonset / 8,0)`; el índice del primero se busca maximizando el acuerdo con la telemetría (en 30 de 135 ejecuciones no es el evento 0).
3. **Validación independiente con `telemetry.csv`:** el déficit de muestras por segundo (250 − `n_samples`) en los segundos de la ventana debe coincidir exactamente con el que predice (u, L).

**TABLA B0 · validación** `[m3b_posicion.py -> m3b_B_validacion.csv]`

| Severidad | Ejecuciones | Ensayos | Ensayos con déficit por segundo idéntico | Ejecuciones con 24/24 |
|---|---|---|---|---|
| 0.1 | 45 | 1080 | 1080 | 45 |
| 0.25 | 45 | 1080 | 1080 | 45 |
| 0.4 | 45 | 1080 | 1080 | 45 |

Los 3.240 ensayos validan al 100 %: la secuencia del generador local (numpy 2.5.3) coincide con la que corrió en la VM.

### 2.2 Resultados

Posición = `u_frac = u/(1000 − L)` en tercios (inicio: el hueco arranca en el primer tercio de los inicios posibles; fin: en el último). Equiprobable por construcción. `[m3b_posicion.py -> m3b_B_posicion.csv, m3b_B_trials.csv]`

**TABLA B1**

| Severidad | Posición | Ensayos | Cambio CSP+LDA % | Δ acierto CSP+LDA (pp) | Cambio EEGNet % | Δ acierto EEGNet (pp) | EEGNet perjudicial % | EEGNet favorable % |
|---|---|---|---|---|---|---|---|---|
| 0.1 | inicio | 367 | 7.6 | +0.0 | 7.9 | -3.5 | 5.7 | 2.2 |
| 0.1 | medio | 364 | 5.2 | -0.3 | 8.2 | -0.5 | 4.4 | 3.8 |
| 0.1 | fin | 349 | 5.2 | -2.3 | 7.4 | -0.6 | 4.0 | 3.4 |
| 0.25 | inicio | 356 | 7.9 | -1.7 | 16.3 | -6.7 | 11.5 | 4.8 |
| 0.25 | medio | 346 | 9.0 | -2.0 | 14.5 | -4.6 | 9.5 | 4.9 |
| 0.25 | fin | 378 | 10.1 | -2.1 | 14.6 | -0.8 | 7.7 | 6.9 |
| 0.4 | inicio | 363 | 15.2 | -9.1 | 25.3 | -11.0 | 18.2 | 7.2 |
| 0.4 | medio | 351 | 12.8 | -4.3 | 24.5 | -7.4 | 16.0 | 8.5 |
| 0.4 | fin | 366 | 13.9 | -3.6 | 22.7 | -4.1 | 13.4 | 9.3 |
| todas | inicio | 1086 | 10.2 | -3.6 | 16.5 | -7.1 | 11.8 | 4.7 |
| todas | medio | 1061 | 9.0 | -2.2 | 15.6 | -4.1 | 9.9 | 5.7 |
| todas | fin | 1093 | 9.8 | -2.7 | 15.0 | -1.8 | 8.4 | 6.6 |

**TABLA B2 · pruebas por sujeto (n = 9)** `[m3b_posicion.py -> m3b_B_pruebas.csv]`. "todas (prom.)" promedia las 3 severidades dentro de cada sujeto y posición.

| Decodificador | Severidad | Variable | Sujetos | Mediana inicio % | Mediana medio % | Mediana fin % | p Friedman | p Wilcoxon inicio vs fin |
|---|---|---|---|---|---|---|---|---|
| CSP+LDA | 0.1 | cambio | 9 | 4.9 | 4.5 | 4.4 | 0.717 | 0.426 |
| CSP+LDA | 0.1 | Δ acierto | 9 | 0.0 | 0.0 | -2.8 | 0.581 | 0.426 |
| CSP+LDA | 0.25 | cambio | 9 | 9.1 | 9.5 | 9.3 | 0.641 | 0.496 |
| CSP+LDA | 0.25 | Δ acierto | 9 | 0.0 | -3.2 | -2.5 | 0.490 | 0.742 |
| CSP+LDA | 0.4 | cambio | 9 | 15.4 | 12.2 | 13.3 | 0.717 | 0.734 |
| CSP+LDA | 0.4 | Δ acierto | 9 | -9.5 | -2.7 | -2.4 | 0.044 | 0.055 |
| CSP+LDA | todas (prom.) | cambio | 9 | 10.0 | 8.6 | 8.4 | 0.717 | 0.570 |
| CSP+LDA | todas (prom.) | Δ acierto | 9 | -3.9 | -2.1 | -2.6 | 0.641 | 0.426 |
| EEGNet | 0.1 | cambio | 9 | 7.7 | 5.0 | 4.9 | 1.000 | 0.910 |
| EEGNet | 0.1 | Δ acierto | 9 | -5.0 | -2.2 | 0.0 | 0.549 | 0.301 |
| EEGNet | 0.25 | cambio | 9 | 14.9 | 12.8 | 9.8 | 0.368 | 0.496 |
| EEGNet | 0.25 | Δ acierto | 9 | -5.6 | -4.7 | -2.1 | 0.169 | 0.055 |
| EEGNet | 0.4 | cambio | 9 | 21.4 | 23.5 | 22.7 | 0.717 | 0.734 |
| EEGNet | 0.4 | Δ acierto | 9 | -11.9 | -9.1 | -4.8 | 0.045 | 0.164 |
| EEGNet | todas (prom.) | cambio | 9 | 17.8 | 14.7 | 10.8 | 0.459 | 0.496 |
| EEGNet | todas (prom.) | Δ acierto | 9 | -6.2 | -4.7 | -2.3 | 0.236 | 0.055 |

- **Tasa de cambio: sin efecto de posición** (8 pruebas de Friedman, p de 0,37 a 1,00). A nivel ensayo, Spearman entre `u_frac` y cambio: |rho| <= 0,046 en todas las severidades y decodificadores (p >= 0,13) `[m3b_posicion.py -> m3b_B_pruebas.csv, filas spearman_*]`. Cinco quintiles de posición tampoco muestran gradiente `[-> m3b_B_quintiles.csv]`. Sensibilidad: clasificar por el centro del hueco (tercios de la ventana) da lo mismo `[-> m3b_B_posicion.csv, clasif = pos_centro]`.
- **Δ acierto (acierto menos el de la referencia en esos ensayos):** en 2 de 8 pruebas el Friedman da p = 0,044 y 0,045 (ambos decodificadores, severidad 0,4), con el hueco al inicio peor. Es nominal: con las 24 pruebas de Friedman calculadas (cambio, acierto, Δ acierto) ninguna sobrevive a Holm. La tendencia de EEGNet (inicio -7,1, medio -4,1, fin -1,8 pp en todas las severidades; p = 0,055 inicio vs. fin) es la que coincide con la hipótesis de [[Analisis-M3]], pero se debe a que con el hueco al inicio hay más cambios perjudiciales (11,8 % contra 8,4 %) y menos favorables (4,7 % contra 6,6 %), no a más cambios (16,5 % contra 15,0 %).
- Parte de la diferencia en Δ acierto puede ser artefacto de composición: la referencia acierta distinto en cada tercio (en 0,4: 79,6 % inicio contra 71,9 % fin en CSP+LDA, tabla de `m3b_B_posicion.csv`), por azar de qué ensayos cayeron en cada posición.
- **Conclusión de B:** con estos datos (unos 360 ensayos por celda, 9 sujetos) no se detecta efecto de la posición del hueco sobre la decisión; un efecto en el acierto de EEGNet es posible pero no está demostrado. Lo que sí determina el daño es **cuánto** y **cómo** (contiguo o disperso, A1.5), no **en qué parte** de la ventana.

---

## 3. Tarea C: sensibilidad de la divergencia operativo/degradado

### 3.1 Método

- Se reproduce primero el caso base con las funciones de `bcibench.metrics` (`rolling_bacc`, `reference_threshold`, `window_table`, `divergence`): W = 8, umbral por sujeto = mínimo de la balanced accuracy móvil en sus 5 corridas de referencia, operativo = llegan muestras y 0 excepciones en el segundo. Verificaciones que pasan (assert): los 9 umbrales coinciden con `analysis/thresholds.json`; las 330.885 filas de `analysis/windows.csv` (`operational`, `rbacc`, `degraded`) se reproducen exactamente; la mediana por condición coincide con `analysis/t_divergencia.csv` (silent y loud, 19/19). `[m3b_divergencia.py -> m3b_C_base.csv]`
- **Variaciones:** W = 4, 6, 8, 12; umbral = mínimo / percentil 5 de la referencia / mínimo − 0,05; operativo base / estricto (base y latencia media del segundo < 50 ms y `n_gaps` = 0 en el segundo). 24 combinaciones x 19 condiciones. `[m3b_divergencia.py -> m3b_C_cond.csv, m3b_C_resumen.csv, m3b_C_exec.csv]`
- **Dos agregados.** *Mediana* (como en `analyze.py`: por ejecución, mediana entre corridas por sujeto, mediana entre sujetos): es el estadístico del manuscrito. *Agrupado*: segundos silenciosos / segundos evaluables, sumando las 45 ejecuciones de la condición (no esconde las colas) y número de ejecuciones con al menos 1 s silencioso.
- Falla silenciosa = operativo y degradado. "No operativo y no degradado" (loud) = alarma sin degradación real.

### 3.2 Caso base

**TABLA C1** (W = 8, mínimo, operativo base) `[m3b_divergencia.py -> m3b_C_cond.csv]`

| Condición | Silenciosa: mediana entre sujetos (%) | Silenciosa: segundos agrupados (%) | Segundos silenciosos | Segundos evaluables | Ejecuciones con ≥ 1 s silencioso | Sujetos con mediana > 0 | Máximo en una ejecución (%) | 'No operativo y no degradado': mediana (%) |
|---|---|---|---|---|---|---|---|---|
| referencia | 0.00 | 0.00 | 0 | 12750 | 0/45 | 0 | 0.0 | 0.00 |
| pérdida 1 % | 0.00 | 0.00 | 0 | 12750 | 0/45 | 0 | 0.0 | 0.00 |
| pérdida 5 % | 0.00 | 0.44 | 56 | 12750 | 1/45 | 0 | 19.6 | 0.00 |
| pérdida 10 % | 0.00 | 0.32 | 41 | 12750 | 1/45 | 0 | 14.3 | 0.00 |
| jitter 10/50/100 ms | 0.00 | 0.00 | 0 | 12750 c/u | 0/45 | 0 | 0.0 | 0.00 |
| retraso 50/100/250 ms | 0.00 | 0.00 | 0 | 12750 c/u | 0/45 | 0 | 0.0 | 0.00 |
| desconexión 0,5 s | 0.00 | 0.00 | 0 | 12750 | 0/45 | 0 | 0.0 | 0.70 |
| desconexión 1 s | 0.00 | 0.20 | 25 | 12750 | 1/45 | 0 | 8.7 | 0.70 |
| desconexión 3 s | 0.00 | 0.93 | 118 | 12750 | 2/45 | 0 | 22.1 | 3.47 |
| pérdida contigua 10 % | 0.00 | 0.97 | 124 | 12750 | 4/45 | 0 | 18.3 | 0.00 |
| pérdida contigua 25 % | 0.00 | 2.89 | 369 | 12750 | 10/45 | 1 | 38.1 | 0.00 |
| pérdida contigua 40 % | 0.00 | 3.42 | 436 | 12750 | 8/45 | 0 | 35.3 | 7.34 |
| desc. en ensayo 0,5 s | 0.00 | 3.02 | 385 | 12750 | 7/45 | 0 | 32.2 | 8.52 |
| desc. en ensayo 1 s | 0.00 | 3.02 | 385 | 12750 | 7/45 | 0 | 32.2 | 8.52 |
| desc. en ensayo 2 s | 0.00 | 7.44 | 949 | 12750 | 16/45 | 2 | 69.3 | 20.63 |

- **El caso base reproduce el 0 como mediana en las 18 condiciones.** Pero **no es 0 como conteo**: 2.888 de 229.500 segundos evaluables (1,26 %), en 57 de 810 ejecuciones con fallo (7,0 %). De los 3.255 segundos degradados de las 18 condiciones, 2.888 (88,7 %) son operativos `[m3b_silenciosa.py -> consola (windows.csv)]`. Es la misma cifra que se obtiene contando directamente sobre `analysis/windows.csv`.
- **No es artefacto de mi código:** la reproducción de `windows.csv` es exacta y el conteo directo sobre el archivo original da los mismos 2.888 segundos.
- **Qué son esos segundos.** El 71,7 % tiene recepción del 100 % y el 83,9 % no tiene huecos en el propio segundo; el 100 % tiene latencia media < 50 ms. Es decir, la telemetría de ese segundo es normal y la balanced accuracy móvil (memoria de 8 ensayos, unos 64 s) sigue por debajo de lo mínimo observado en la referencia: la degradación funcional persiste después de que el transporte se recupera, y en `burst_trial` el segundo casi nunca queda vacío con 10 y 25 % (no operativo y no degradado: 0,0 % y 0,1 % agrupado). Es la brecha que el estado operativo por segundo no ve.
- **Concentración.** Por familia: desconexión en el ensayo 1.719 s en 30 de 135 ejecuciones; pérdida contigua 929 s en 22; desconexión uniforme 143 s en 3; pérdida uniforme 97 s en 2; jitter y retraso 0. Por sujeto: sujeto 5 (834 s, 10 ejecuciones), 9 (600 s, 9), 4 (457 s, 7), 8 (353 s, 7); sujetos 1 y 2, 30 y 42 s `[m3b_silenciosa.py -> m3b_C_silenciosa_base.csv]`. Por qué se concentra en esos sujetos (umbral, calidad de la señal) no se estudió.

### 3.3 Grilla de sensibilidad

**TABLA C2** `[m3b_divergencia.py -> m3b_C_resumen.csv]` (18 condiciones con fallo; "ref." = referencia)

| Umbral | Operativo | W | Cond. con mediana > 0 (de 18) | Máx. mediana (%) | Cond. con segundos agrupados > 0 (de 18) | Máx. agrupado (%) | Agrupado en las 18 (%) | Ejecuciones con silenciosa (de 810) | Ref.: agrupado (%) | Ref.: ejecuciones (de 45) | 'No operativo y no degradado' agrupado, 18 cond. (%) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| mínimo | base | 4 | 0 | 0.0 | 10 | 2.3 | 0.43 | 40 | 0.00 | 0 | 2.8 |
| mínimo | base | 6 | 0 | 0.0 | 10 | 5.8 | 1.15 | 54 | 0.00 | 0 | 2.7 |
| mínimo | base | 8 | 0 | 0.0 | 10 | 7.4 | 1.26 | 57 | 0.00 | 0 | 2.6 |
| mínimo | base | 12 | 1 | 14.3 | 11 | 18.8 | 3.86 | 96 | 0.00 | 0 | 2.4 |
| mínimo | estricto | 4 | 0 | 0.0 | 8 | 1.9 | 0.36 | 38 | 0.00 | 0 | 40.8 |
| mínimo | estricto | 6 | 0 | 0.0 | 8 | 4.9 | 0.97 | 51 | 0.00 | 0 | 40.6 |
| mínimo | estricto | 8 | 0 | 0.0 | 8 | 6.3 | 1.06 | 55 | 0.00 | 0 | 40.5 |
| mínimo | estricto | 12 | 1 | 12.2 | 9 | 15.9 | 3.21 | 92 | 0.00 | 0 | 39.9 |
| mínimo − 0,05 | base | 4 | 0 | 0.0 | 10 | 2.3 | 0.43 | 40 | 0.00 | 0 | 2.8 |
| mínimo − 0,05 | base | 6 | 0 | 0.0 | 10 | 4.7 | 1.04 | 47 | 0.00 | 0 | 2.7 |
| mínimo − 0,05 | base | 8 | 0 | 0.0 | 10 | 5.0 | 0.78 | 44 | 0.00 | 0 | 2.7 |
| mínimo − 0,05 | base | 12 | 1 | 2.2 | 10 | 13.2 | 2.19 | 72 | 0.00 | 0 | 2.6 |
| mínimo − 0,05 | estricto | 4 | 0 | 0.0 | 8 | 1.9 | 0.36 | 38 | 0.00 | 0 | 40.8 |
| mínimo − 0,05 | estricto | 6 | 0 | 0.0 | 8 | 3.9 | 0.89 | 44 | 0.00 | 0 | 40.6 |
| mínimo − 0,05 | estricto | 8 | 0 | 0.0 | 8 | 4.2 | 0.64 | 42 | 0.00 | 0 | 40.6 |
| mínimo − 0,05 | estricto | 12 | 1 | 1.7 | 8 | 11.2 | 1.86 | 69 | 0.00 | 0 | 40.3 |
| percentil 5 | base | 4 | 4 | 4.1 | 18 | 9.8 | 4.26 | 337 | 2.87 | 15 | 2.6 |
| percentil 5 | base | 6 | 4 | 6.9 | 18 | 13.6 | 5.79 | 305 | 4.15 | 14 | 2.5 |
| percentil 5 | base | 8 | 4 | 12.9 | 18 | 18.1 | 6.94 | 300 | 4.42 | 13 | 2.3 |
| percentil 5 | base | 12 | 4 | 21.2 | 18 | 27.8 | 7.96 | 247 | 2.87 | 9 | 2.2 |
| percentil 5 | estricto | 4 | 4 | 3.5 | 13 | 8.3 | 3.00 | 258 | 2.87 | 15 | 39.5 |
| percentil 5 | estricto | 6 | 4 | 6.0 | 13 | 11.5 | 4.14 | 239 | 4.15 | 14 | 38.9 |
| percentil 5 | estricto | 8 | 4 | 10.8 | 13 | 15.3 | 4.92 | 236 | 4.42 | 13 | 38.4 |
| percentil 5 | estricto | 12 | 4 | 18.0 | 13 | 23.5 | 6.01 | 200 | 2.87 | 9 | 38.3 |

**TABLA C3 · segundos silenciosos agrupados (%), operativo base** (umbral mínimo y percentil 5; mínimo − 0,05 en `m3b_tablas.md`)

| Condición | min W=4 | min W=6 | min W=8 | min W=12 | p5 W=4 | p5 W=6 | p5 W=8 | p5 W=12 |
|---|---|---|---|---|---|---|---|---|
| referencia | 0.00 | 0.00 | 0.00 | 0.00 | 2.87 | 4.15 | 4.42 | 2.87 |
| pérdida 1 % | 0.00 | 0.00 | 0.00 | 0.17 | 2.73 | 3.03 | 4.42 | 3.03 |
| pérdida 5 % | 0.20 | 0.46 | 0.44 | 0.98 | 3.12 | 3.24 | 4.35 | 3.95 |
| pérdida 10 % | 0.05 | 0.06 | 0.32 | 1.76 | 2.28 | 2.73 | 4.21 | 5.47 |
| jitter y retraso (6 cond.) | 0.00 | 0.00 | 0.00 | 0.00 | 2.87 | 4.15 | 4.42 | 2.87 |
| desconexión 0,5 s | 0.00 | 0.00 | 0.00 | 0.00 | 2.99 | 4.27 | 4.49 | 2.87 |
| desconexión 1 s | 0.27 | 0.30 | 0.20 | 0.61 | 3.37 | 4.58 | 4.70 | 3.65 |
| desconexión 3 s | 0.10 | 0.35 | 0.93 | 2.43 | 4.23 | 5.78 | 6.75 | 6.82 |
| pérdida contigua 10 % | 0.32 | 1.54 | 0.97 | 2.64 | 4.37 | 5.75 | 7.32 | 7.42 |
| pérdida contigua 25 % | 1.49 | 3.23 | 2.89 | 5.75 | 5.63 | 9.24 | 8.00 | 12.04 |
| pérdida contigua 40 % | 1.31 | 2.62 | 3.42 | 12.90 | 6.97 | 10.97 | 13.35 | 19.21 |
| desc. en ensayo 0,5 s | 0.89 | 3.20 | 3.02 | 11.68 | 6.98 | 8.01 | 11.36 | 16.92 |
| desc. en ensayo 1 s | 0.89 | 3.20 | 3.02 | 11.68 | 6.98 | 8.01 | 11.36 | 16.92 |
| desc. en ensayo 2 s | 2.27 | 5.78 | 7.44 | 18.81 | 9.80 | 13.64 | 18.08 | 27.75 |

**TABLA C4 · operativo estricto**, W = 8, mínimo `[m3b_divergencia.py -> m3b_C_cond.csv]`

| Condición | Silenciosa agrupada estricto (%) | "No operativo y no degradado" estricto (%) | ídem, operativo base (%) |
|---|---|---|---|
| referencia | 0.00 | 0.0 | 0.0 |
| pérdida 1 / 5 / 10 % | 0.00 | 91.9 / 99.6 / 99.7 | 0.0 |
| jitter 10 / 50 / 100 ms | 0.00 | 0.0 / 0.0 / 15.9 | 0.0 |
| retraso 50 / 100 / 250 ms | 0.00 | 100.0 | 0.0 |
| desconexión 0,5 / 1 / 3 s | 0.00 / 0.20 / 0.91 | 2.0 / 2.0 / 4.7 | 0.7 / 0.7 / 3.4 |
| pérdida contigua 10 / 25 / 40 % | 0.86 / 2.53 / 2.99 | 12.2 / 12.0 / 19.1 | 0.0 / 0.1 / 7.2 |
| desc. en ensayo 0,5 / 1 / 2 s | 2.61 / 2.61 / 6.28 | 20.1 / 20.1 / 29.8 | 8.2 / 8.2 / 18.8 |

### 3.4 Lectura

- **¿En qué combinaciones aparece falla silenciosa > 0?**
  - *Mediana entre sujetos* (el estadístico del manuscrito): **0 en las 18 condiciones** con W = 4, 6 y 8, umbral mínimo y mínimo − 0,05, operativo base y estricto (12 combinaciones). Es **> 0** con W = 12 (solo desconexión en el ensayo de 2 s: 14,3 % con mínimo, 12,2 % estricto, 2,2 % con mínimo − 0,05) y con el **percentil 5** en todo W (4 condiciones: pérdida contigua 40 % y desconexión en el ensayo de 0,5/1/2 s; hasta 21,2 % con W = 12).
  - *Agrupado*: **> 0 en todas las combinaciones**: 10-11 condiciones con umbral mínimo/mínimo − 0,05 (8-9 con operativo estricto), de 0,36 % (W = 4, estricto) a 3,86 % (W = 12) de los segundos de las 18 condiciones, y 38-96 ejecuciones. Máximo en una condición: 18,8 % (desc. en ensayo 2 s, W = 12).
- **El percentil 5 no mide falla silenciosa:** marca como degradado el 2,9-4,4 % de la propia referencia (tabla C2, columnas "Ref."), de modo que en jitter y retraso, que dejan las decisiones idénticas a las de la referencia, da exactamente esas cifras. Hay que leerlo como diferencia contra la referencia. Descontando ese piso, la señal se concentra en las mismas condiciones que con el mínimo.
- **W más corta reduce lo silencioso y W más larga lo aumenta**: más memoria de la móvil = degradación que perdura más segundos operativos (W = 4: 0,43 %; W = 12: 3,86 %). Con W = 12 la móvil tiene solo 13 valores por corrida (24 - 11) y el umbral mínimo se apoya en muy pocos datos.
- **Operativo estricto:** reduce la silenciosa un 16 % (1,26 % a 1,06 % con W = 8) y la mediana sigue en 0, pero convierte a la pérdida uniforme (92-100 %) y al retraso (100 %) en "no operativo y no degradado": con un criterio de infraestructura tan estricto, la alarma se dispara cuando el decodificador está intacto. El estado operativo base (llegan muestras) es el que tiene sentido para esta comparación, pero entonces el 0 solo vale como mediana.

---

## 4. Límites

1. **Exploratorio y post hoc.** No hay hipótesis previa ni corrección de multiplicidad; con n = 9 el p exacto mínimo es 0,0039 y Holm solo se aplicó dentro de las comparaciones de bins (A3). Leer los p como descriptivos.
2. **Pocos ensayos tocados en el contraste directo.** Solo la desconexión uniforme tiene tocados y no tocados en la misma condición: 236 tocados (75/67/94), unos 26 por sujeto y 7-10 por sujeto y condición. Las comparaciones por condición son ruidosas (p. ej. el acierto de los tocados de 1 s es mayor que el de los no tocados); la comparación que vale es contra la referencia en los mismos ensayos.
3. **Confusión en los bins de dosis.** Cada bin mezcla familias de fallo (A4): 500-749 combina desconexión en el ensayo, pérdida contigua del 40 % y desconexiones uniformes; el bin 1000 incluye jitter, retraso y no cortados. No es una curva dosis-respuesta controlada, y los ensayos de una misma ejecución no son independientes (los IC de Wilson a nivel ensayo son optimistas; la inferencia es por sujeto).
4. **Inválido como error.** Cuenta como cambio y error; los 9 ensayos inválidos (solo desconexión de 3 s) no sostienen conclusiones.
5. **Mismo `n_samples` para dos decodificadores.** El conteo en línea define "tocado" para EEGNet; el conteo fuera de línea difiere en una fracción pequeña de ensayos (no investigado). EEGNet se decodifica sobre una grilla de 1000 muestras con ceros en los huecos, CSP+LDA sobre las muestras presentes: sus sensibilidades no son comparables como "calidad del decodificador", sino de cómo cada uno recibe el hueco.
6. **Determinismo.** El 0 de los no tocados descansa en que el decodificador es determinista y la ventana es idéntica; el control del relleno (79 ensayos) usa telemetría por segundo y exige >= 4 muestras faltantes, no es una medida a nivel muestra.
7. **B: potencia y dependencia de la reconstrucción.** Unos 360 ensayos por celda de posición y 9 sujetos; la comparación se hizo sobre 3.240 ensayos (1.080 por severidad, con semillas distintas por severidad). La posición viene del generador, no de la medición directa; la validación contra telemetría es a resolución de segundo y no distingue dos posiciones que dejen el mismo déficit por segundo (con L = 100 un hueco totalmente dentro de un segundo solo queda identificado por el sorteo). La reproducción del generador asume que la VM usó el mismo algoritmo de `Generator.integers` que NumPy 2.5.3 local: la coincidencia 3.240/3.240 lo confirma. Un efecto de posición menor a ~5 pp no se descarta; haría falta un diseño dirigido (hueco de posición fija: inicio, medio, fin) con más sujetos.
8. **C: el "0" depende del estadístico.** La mediana entre sujetos es robusta a W = 4-8 y umbral mínimo o mínimo − 0,05, pero oculta una cola real; el agrupado depende de la definición de "operativo por segundo" y de la memoria de la móvil. Ambos usan el mismo umbral y los mismos segundos evaluables que `analyze.py`; las ejecuciones no son independientes y no se calculó un IC. Percentil 5 es un umbral con falsas alarmas por construcción.
9. **Muestra y generalización.** 9 sujetos de un solo conjunto (BCI Competition IV 2a), 24 ensayos por corrida, replay con LSL sobre loopback: las magnitudes absolutas no se trasladan a un sistema real.

## 5. Reproducción

Scripts nuevos (sin tocar `src/` ni el manuscrito), en `B\scripts\`, salidas en `D\analysis-m3b\`:

| Script | Qué hace | Salidas |
|---|---|---|
| `m3b_common.py` | Carga y empareja ensayos con la referencia; Wilson, Wilcoxon | (utilidades) |
| `m3b_ensayos.py` | Tarea A: tocados vs. no tocados, dosis-respuesta | `m3b_A_trials.csv`, `m3b_A_subject.csv`, `m3b_A_cond.csv`, `m3b_A_dosis.csv`, `m3b_A_dosis_familia.csv`, `m3b_A_log.txt` |
| `m3b_pad.py` | Control del relleno de 1 s en no tocados | `m3b_A_pad.csv` |
| `m3b_equiv.py` | Igual pérdida, distinta forma/ubicación | `m3b_A_equiv.csv` |
| `m3b_posicion.py` | Tarea B: recuperación y análisis de posición | `m3b_B_trials.csv`, `m3b_B_posicion.csv`, `m3b_B_subject.csv`, `m3b_B_pruebas.csv`, `m3b_B_validacion.csv`, `m3b_B_quintiles.csv`, `m3b_B_log.txt` |
| `m3b_divergencia.py` | Tarea C: reproducción del caso base y grilla | `m3b_C_base.csv`, `m3b_C_cond.csv`, `m3b_C_resumen.csv`, `m3b_C_exec.csv`, `m3b_C_log.txt` |
| `m3b_silenciosa.py` | Caracterización de los segundos silenciosos del caso base | `m3b_C_silenciosa_base.csv` |
| `m3b_tablas_md.py` | Genera los fragmentos de tablas de esta nota | `m3b_tablas.md` |

Orden: `m3b_ensayos.py` -> `m3b_pad.py`, `m3b_equiv.py`, `m3b_posicion.py` (los tres leen `m3b_A_trials.csv` o recalculan) -> `m3b_divergencia.py` -> `m3b_silenciosa.py` -> `m3b_tablas_md.py`.

## D. ¿La fragilidad de EEGNet es de la arquitectura o del relleno con ceros? (07/10)

**Pregunta del autor:** ¿EEGNet podría estar mal configurado, y por eso cambia el doble de decisiones que CSP+LDA?

**Método.** Se reevaluó EEGNet sobre los mismos segmentos guardados de las 855 ejecuciones con tres formas de completar las muestras faltantes antes de filtrar: ceros (la del E2), interpolación lineal por canal y repetición de la última muestra presente (como el receptor de Simeral et al., 2021). Script: `40-Prototipo/scripts/m3_eegnet_relleno.py`; salidas en `40-Prototipo/results/vm/analysis-m3-eegnet/` y `<exec>/trials_eegnet_<modo>.csv`. Control: el modo ceros reproduce el 99,96 % de las decisiones de `trials_eegnet.csv`.

| Muestras recibidas en la ventana | Cambio con ceros | Con repetición | Con interpolación |
|---|---|---|---|
| 1.000 (intacta) | 0,0 % | 0,0 % | 0,0 % |
| 900-999 | 4,0 % | 4,0 % | 3,1 % |
| 750-899 | 11,9 % | 11,4 % | 11,5 % |
| 500-749 | 25,4 % | 25,9 % | 25,6 % |
| 125-499 | 41,2 % | 41,0 % | 41,0 % |

Diferencia de *balanced accuracy* contra la referencia (mediana entre sujetos de la diferencia apareada): igual en los tres modos salvo la desconexión en el ensayo de 0,5 y 1 s (−0,125 con ceros, −0,083 con los otros dos rellenos, es decir, un ensayo de 24) y la pérdida contigua del 10 % (0,000 contra −0,042).

**Conclusión.** El relleno casi no cambia nada: la mayor sensibilidad de EEGNet no es un artefacto de los ceros sino de la información que falta. EEGNet está bien entrenado (sin fallos rinde igual o mejor que CSP+LDA) y su fragilidad ante huecos es una propiedad del modelo con esta entrada. Límite: EEGNet se entrenó solo con señal limpia; entrenarlo con huecos (aumentación) es la línea futura natural.
