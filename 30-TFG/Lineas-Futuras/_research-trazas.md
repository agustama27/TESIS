---
tipo: investigacion
tema: trazas medidas de enlaces reales (Bluetooth EEG, Wi-Fi congestionado) + recuperación de LSL
fecha: 2026-09-27
estado: verificado (salvo lo marcado ⚠️ SIN VERIFICAR)
---

# Trazas medidas para reemplazar los modelos sintéticos del inyector

**Objetivo.** Reemplazar los modelos sintéticos del inyector (pérdida aleatoria/ráfaga 1/5/10 %, jitter gaussiano 10/50/100 ms, retraso 50/100/250 ms, cortes 0,5/1/3 s) por comportamiento **medido** en enlaces reales.

**Cómo se verificó.** Cada DOI se consultó en `https://api.crossref.org/works/<DOI>`. Los DOI de Zenodo son de DataCite y se verificaron con `https://zenodo.org/api/records/<id>`. Los números salen del texto completo, que se leyó por Europe PMC (XML), el PDF del editor, el PDF del autor o el informe técnico. Si solo se accedió al abstract, se aclara.

---

## 1. Mediciones publicadas

### 1a. Bluetooth / EEG inalámbrico (5 verificadas)

| # | Fuente (verificada en Crossref) | Equipo / enlace | Número medido (cita textual) | Acceso |
|---|---|---|---|---|
| B1 | Krigolson et al. (2017), *Frontiers in Neuroscience*, 11. DOI 10.3389/fnins.2017.00109 | Muse (Bluetooth → muse-io → MATLAB) | Método: 5000 pulsos TTL. Resultado: "This test demonstrated a mean lag of 40 ms (±20 ms)". Aclaran que "this variability was in part due to a few samples (n < 10) with extreme latencies". | Texto completo (PMC5344886) |
| B2 | Dasenbrock et al. (2022), *Frontiers in Neuroscience*, 16, 904003. DOI 10.3389/fnins.2022.904003 | SMARTING (mBrainTrain) → Bluetooth → Android → **LSL**, 250 Hz | "The jitter in Scenarios II and III was around 3 ms in both cases". También: "the lag did not stay constant, but changed from session to session, indicated by a ΔR of up to 52 ms". Y: "sporadic outliers up to 150 ms occurred for single samples". | Texto completo (PMC9475108) |
| B3 | Arpaia et al. (2025), *IEEE TNSRE*, 33, 2151–2159. DOI 10.1109/TNSRE.2025.3575695 (CC BY 4.0) | 3 EEG inalámbricos anonimizados (Device 1–3; el Device 2 sale por LSL) | Device 1: "the mean delay was 20 ms". Device 2: "the mean delay was 102 ms" a 512 Sa/s y "88 ms" a 1024 Sa/s. Device 3: "a 47 ms mean delay". Sobre pérdidas: "excluding that data packets were lost during the tests". | PDF completo (IEEE, OA). ⚠️ No se pudo extraer de la Tabla I qué protocolo radio usa cada equipo. |
| B4 | Epinat-Duclos et al. (2026), *PeerJ*, 14, e20416. DOI 10.7717/peerj.20416 (CC BY 4.0) | EMOTIV EPOC Flex (Bluetooth, 128 Hz) vs LiveAmp (Wi-Fi) vs BrainAmp (cable) | "The EM headset had to be changed in the middle of a session for two participants due to a lost connection". Triggers perdidos (Tabla 3, media [rango]): EM 4.10 [0–19], LA 0.05 [0–1], BA 0.00 [0–0]. | Texto completo (Europe PMC, PMC12782033) |
| B5 | Mahmud, Kasera, Ji y Agarwal (2023), informe técnico INL/RPT-23-74719 (OSTI). DOI 10.2172/2242485 | BLE (100 B, ~15 paquetes/s) con Wi-Fi en canal 6 (iperf3 UDP a 40 Mbps) | "the average throughput of BLE experiences a degradation, dropping from the baseline of 12.06 Kbps to 7.08 Kbps". Y: "the PER of BLE fluctuates from 2 to 9%". | PDF completo (INL digital library) |

**Qué se lleva el inyector de esto.**
- **Latencia de extremo a extremo de EEG por Bluetooth:** de 20 a 102 ms de media según el equipo (B1, B3). Es un **offset por sesión** que puede variar hasta ~50 ms entre sesiones (B2).
- **Jitter:** ~3 ms de desvío en un sistema bien integrado con LSL (B2). ±20 ms en Muse con muse-io (B1).
- **Outliers:** muestras sueltas de hasta 150 ms (B2).
- **Pérdida de paquetes:** con Wi-Fi interfiriendo, BLE pierde entre 2 y 9 % de paquetes (PER) (B5). En uso real con un headset de consumo aparecen **desconexiones completas** que obligan a cambiar el equipo (B4). Ninguna fuente revisada publica duraciones de dropout en ms.

**Descartadas (con motivo):**
- **Ratti et al. (2017)**, DOI 10.3389/fnhum.2017.00398, y **Radüntz (2018)**, DOI 10.3389/fphys.2018.00098. Son reales en Crossref, pero el texto completo (PMC5540902 y PMC5817086) **no trae ningún número** de pérdida, latencia ni jitter del enlace. Evalúan calidad de señal, no transporte.
- **Iwama et al. (2024)**, *Neuroscience Research*, 203, DOI 10.1016/j.neures.2023.12.003. El jitter es **simulado** (gaussiano de 0 a 20 ms) sobre datos de un equipo cableado. No es una medición de un enlace inalámbrico.
- **Kavousi Ghafi et al. (2021)**, EURASIP JWCN, DOI 10.1186/s13638-021-02005-2. Trabaja a nivel de capa física (BER/PER contra Eb/N0 en laboratorio). No da tasas de pérdida de un enlace en uso.
- **"Gemborn Nilsson et al."**: no se encontró ningún trabajo con ese nombre sobre latencia de EEG inalámbrico. Descartado por no localizable.
- **Foro de OpenBCI** (Ganglion: ~6,5 % de pérdida a 20 cm; 4 y 11 pérdidas en 120 s a 60 cm). Es literatura gris y no está revisada por pares. ⚠️ SIN VERIFICAR: solo se vio el resumen del buscador, no se leyó el hilo.

### 1b. Wi-Fi / WLAN (3 verificadas)

| # | Fuente (verificada en Crossref) | Contexto | Número medido (cita textual) | Acceso |
|---|---|---|---|---|
| W1 | Aguayo, Bicket, Biswas, Judd y Morris (2004), *ACM SIGCOMM CCR*, 34(4), 121–132. DOI 10.1145/1030194.1015482 | Roofnet, 802.11b en malla. Broadcast de 1500 B sin retransmisiones, 90 s por tasa de bits. | "loss behaves as if it were independent for time intervals less than about 0.1 seconds". También: "The bursty links all show correlation out to at least 1 second". Y: "most links vary in loss rate by only a few percent from one second to the next, but ... a small minority of links ... vary by 10% or more". | PDF completo (copia de curso en UCSD) |
| W2 | Jardosh, Ramachandran, Almeroth y Belding-Royer (2005), *IMC '05*. DOI 10.1145/1330107.1330140 | Red 802.11b de la reunión 62 del IETF (1138 asistentes, 38 AP). Es la traza CRAWDAD `ucsb/ietf2005`. | "the network [is] highly congested when the channel utilization level is greater than 84%". Y: "For channel utilization between 84% and 98%, we observe a significant decrease in throughput, from 4.9 Mbps to 2.8 Mbps". El retardo de aceptación (Fig. 15) está graficado en un eje de 0 a 0,08 s. ⚠️ El valor exacto por punto no se extrajo porque está solo en la figura. | PDF completo (USENIX) |
| W3 | Sui et al. (2016), *MobiSys '16*, 347–360. DOI 10.1145/2906388.2906393 | Campus de Tsinghua, más de 47 000 dispositivos | "WiFi latency follows a long tail distribution and the 90th (99th) percentile is around 20 ms (250 ms)". | ⚠️ **Solo abstract** (página de Microsoft Research). El PDF no se pudo descargar. |

**Qué se lleva el inyector de esto.**
- En Wi-Fi, la pérdida **no es i.i.d. por encima de ~100 ms**: en los enlaces malos está correlacionada hasta ≥1 s (W1). Esto respalda usar un **modelo de ráfagas tipo Gilbert-Elliott** en lugar de la pérdida aleatoria.
- La latencia tiene **cola larga**: p90 ≈ 20 ms y p99 ≈ 250 ms (W3). Un jitter gaussiano de 10/50/100 ms no reproduce esa cola. Una distribución empírica o lognormal se ajusta mejor a esos percentiles.

**Descartadas:**
- La DOI 10.1109/INFOCOM.2008.93 **no** corresponde a Rayanchu et al. En Crossref es "Power Awareness in Network Design and Routing" (Chabarek et al.). Era una pista errónea.
- La DOI 10.1145/1015467.1015491 **no** es Roofnet. Es "Locating internet routing instabilities". La correcta es la de W1.

---

## 2. Trazas descargables

Estado de registro comprobado para cada una. Ranking por utilidad para reproducir un stream EEG de 250 Hz en chunks de 40 ms durante ~6,5 min (390 s):

| Rank | Traza | URL | Licencia | ¿Registro? | Formato | Tamaño | Resolución | Duración | Comentario |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **Muse S pilot, Mind Monitor** (Iwendi et al., 2026) | https://zenodo.org/records/22093536 | CC BY 4.0 | **No** (se descargó con curl) | CSV con `TimeStamp` (ms, hora de llegada al teléfono), `RAW_TP9..TP10`, `AUX_*`, bandas, acelerómetro/giróscopo, `Elements` (eventos) | 10,1 MB | 1 ms, por muestra | 66,9 s | **Es un enlace BLE real de EEG.** Llegada en paquetes de 12 muestras, con distancias reales entre paquetes. No se ve pérdida. Para 390 s hay que hacer bucle o remuestreo en bloques. |
| 2 | Mahimahi cellular traces (Netravali et al., 2015; trazas de Winstein et al., 2013) | https://github.com/ravinet/mahimahi/tree/master/traces | GPL-3.0 (licencia del repo) | No | Un timestamp en ms por línea. Según el README: "represents an opportunity for one 1500-byte packet to be drained from the bottleneck queue" | 0,1–7,8 MB por archivo | 1 ms | Minutos (`*-short`) | Da **capacidad**, no pérdida ni retardo directos. Necesita emular la cola (`mm-link`). Es celular, no Wi-Fi. |
| 3 | FlockLab link quality (Jacob et al., 2019) | https://zenodo.org/records/3731498 | CC BY 4.0 | No | ZIP con el éxito o fallo de cada paquete (100 *strobes* por nodo) | Preprocesado 0,6–2,8 MB; crudo 49–115 MB | Por paquete | Ráfagas de 100 paquetes cada 2 h | Es 802.15.4 a 2,4 GHz (TelosB) y otra radio en sub-GHz, no BLE. Sirve para patrones de pérdida, no como serie continua. |
| 4 | NeSt-VR, VR sobre Wi-Fi 6 (Casasnovas, Maura Rivero y Bellalta, 2025) | https://zenodo.org/records/14832268 | CC BY 4.0 | No | Logs JSON de ALVR y CSV de tshark por paquete | **110,9 MB** | Por paquete | Por test | Hay Wi-Fi real, pero en la Sección VI las pérdidas son **emuladas** (0,5/1/2 %). ⚠️ No se abrió el ZIP. |
| 5 | CRAWDAD `ucsb/ietf2005` (Jardosh et al.) | https://ieee-dataport.org/open-access/crawdad-ucsbietf2005 | Open access en IEEE DataPort | **Sí** (cuenta IEEE gratuita, según la página: "accessible to all logged in users") | Capturas 802.11 por canal (`day_channel_1/6/11`, `plenary_channel_*`) | ⚠️ sin tamaño publicado (el paper habla de 45 GB en total) | Por trama | 2 días | Es la traza de congestión real ideal, pero requiere login y pesa mucho. |
| 6 | Arpaia et al., acquisition delay | https://ieee-dataport.org/documents/acquisition-delay-wireless-eeg | Suscripción | **Sí, pago/suscripción** | .mat | 108,45 MB | — | — | No se puede usar sin pagar. |
| — | Roofnet (MIT) | https://pdos.csail.mit.edu/archive/roofnet/ | — | — | — | — | — | — | **HTTP 403** ("Access forbidden!"). No disponible. |

### Traza descargada

- **Archivo:** `C:\Users\agustin.tamagusuku\Desktop\bci-fault-bench-futuro\traces\raw\mindMonitor_2025-07-01--14-56-05.csv`
- **Tamaño:** 10 148 373 bytes. El MD5 coincide con el publicado por Zenodo (`649f4f36a794e3d4c944863a3fedbefa`).
- **SHA-256:** `4a200d535c8d9f0ce207863053ed1276c6fab85cb9eafa5da159f35c5c96094e`
- **Criterios:** sin registro ✔, < 50 MB ✔, CC BY 4.0 ✔, resolución 1 ms ✔.

**Caracterización propia** (pandas sobre las filas con `RAW_TP9`):

| Métrica | Valor |
|---|---|
| Filas con EEG crudo | 17 136 en 66,89 s (~256,8 Hz efectivos) |
| Tamaño de ráfaga (muestras por paquete) | mediana 12 (IQR 12–12), máximo 48, es decir hasta 4 paquetes BLE que llegan juntos |
| Intervalo entre ráfagas | mediana 49 ms; p5/p95 = 27/71 ms; máximo 94 ms |
| Huecos entre muestras | > 50 ms: 199; > 100 ms: 0 |
| Pérdida | no se detecta: se observan 17 136 muestras contra ~17 081 esperadas a 256 Hz |

**Cuidado con la pérdida:** la aplicación puede haber reordenado o interpolado. ⚠️ No se verificó cómo Mind Monitor timbra las muestras.

**Primeras 10 líneas** (recortadas a 400 caracteres):

```
TimeStamp,Delta_TP9,Delta_AF7,Delta_AF8,Delta_TP10,Theta_TP9,Theta_AF7,Theta_AF8,Theta_TP10,Alpha_TP9,Alpha_AF7,Alpha_AF8,Alpha_TP10,Beta_TP9,Beta_AF7,Beta_AF8,Beta_TP10,Gamma_TP9,Gamma_AF7,Gamma_AF8,Gamma_TP10,RAW_TP9,RAW_AF7,RAW_AF8,RAW_TP10,AUX_RIGHT,AUX_LEFT,Accelerometer_X,Accelerometer_Y,Accelerometer_Z,Gyro_X,Gyro_Y,Gyro_Z,HeadBandOn,HSI_TP9,HSI_AF7,HSI_AF8,HSI_TP10,Battery,Elements
2025-07-01 14:56:05.422,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,/muse/event/connected MuseS-84AC
2025-07-01 14:56:05.592,0.4980847221289046,-0.2755523400041398,-0.3079192631932369,0.3675393082910433,0.7322345551724218,-0.2895977974691829,-0.3266897989133,0.3503466423256933,0.7790919440098653,0.5105457265831637,0.07354541472932494,0.3606673244736989,0.6150888670822856,0.3149053128221208,0.6090137970036722,0.2030016061896133,0.04198901474591207,0.2138504183674269,0.216801492415646,-0.1908111613
2025-07-01 14:56:05.593,0.4980847221289046,-0.2755523400041398,... (idéntica a la anterior en bandas)
2025-07-01 14:56:05.593,0.4980847221289046,-0.2755523400041398,...
2025-07-01 14:56:05.594,0.4842413180704228,-0.2567717639090616,-0.292630894245048,0.3756845348240321,0.7137920511466925,...
2025-07-01 14:56:05.595,0.4842413180704228,-0.2567717639090616,...
2025-07-01 14:56:05.596,0.4842413180704228,-0.2567717639090616,...
2025-07-01 14:56:05.596,0.4842413180704228,-0.2567717639090616,...
2025-07-01 14:56:05.596,0.4842413180704228,-0.2567717639090616,...
```

**Cómo usarla para reproducir el enlace:** tomar los tiempos de llegada de cada ráfaga como el calendario de entrega. El outlet retiene las muestras y las libera en bloques de 12 a 48 muestras según ese calendario, que se repite en bucle hasta cubrir los 390 s. Así se obtiene jitter de llegada **real** de BLE, en lugar de un jitter gaussiano. Para la pérdida hace falta otra fuente: con esta traza, la mejor opción empírica es parametrizar un Gilbert-Elliott con el PER de 2–9 % de B5 y la correlación ≤1 s de W1.

---

## 3. LSL: recuperación y temporizaciones

**Fuente:** `sccn/liblsl`. En la rama `master` el HEAD es `42118f80` (= tag `v1.18.0.b5`). Se contrastó con la rama por defecto `dev`.

**Valores por defecto** (`src/api_config.cpp`, líneas 302–308 en master y 315–324 en dev). Coinciden con la documentación oficial (https://labstreaminglayer.readthedocs.io/info/lslapicfg.html):

| Clave `[tuning]` | Default |
|---|---|
| `WatchdogCheckInterval` | 15.0 s |
| `WatchdogTimeThreshold` | 15.0 s |
| `MulticastMinRTT` | 0.5 s |
| `MulticastMaxRTT` | 3.0 s |
| `UnicastMinRTT` | 0.75 s |
| `UnicastMaxRTT` | 5.0 s |
| `ContinuousResolveInterval` | 0.5 s |

**Flag `recover`** (`include/lsl/inlet.h`): "Try to silently recover lost streams that are recoverable (=those that that have a source_id set)". Si el stream no tiene `source_id`, `inlet_connection.cpp` desactiva la recuperación con un warning.

**Mecánica de recuperación** (en `src/inlet_connection.cpp` y `src/data_receiver.cpp`):

1. Cuando se cae el TCP, `data_receiver` atrapa el error y llama a `try_recover_from_error()`, que a su vez llama a `try_recover()`.
2. `try_recover()` lanza `resolver_.resolve_oneshot(query, 1, FOREVER, attempt == 0 ? 1.0 : 5.0)`. Es decir, el **primer intento busca durante al menos 1,0 s**.
3. En modo oneshot (`fast_mode_`), la búsqueda manda una ola multicast cada `MulticastMinRTT` = 0,5 s (`resolver_impl.cpp`, `next_resolve_wave`).
4. Después de cada intento, el receptor espera **500 ms fijos** antes de reconectar. En master: `std::this_thread::sleep_for(std::chrono::milliseconds(500))`. En dev (PR #299): `connected_upd_.wait_for(lock, std::chrono::milliseconds(500), ...)`, con el comentario "Back off between reconnects".
5. El watchdog (15 s / 15 s) **no interviene** en cortes cortos. Solo actúa si no llegan datos durante más de 15 s.

**Explicación del ≈560–570 ms de la tesis.** Es una inferencia a partir del código, no algo documentado por LSL. En el piloto, el hueco máximo sin datos fue 1563 ms para cortes de 1 s y 3563 ms para cortes de 3 s: un exceso **constante de ~563 ms**. Ese exceso cierra con:
- **500 ms** de back-off fijo del `data_receiver`;
- más unas decenas de ms de ola multicast, handshake TCP y primer chunk.

Es constante porque 1 s y 3 s son múltiplos de la ola de 0,5 s, así que la fase queda alineada.

**Predicción:** los cortes de **0,5 s** deberían costar más de ~560 ms de exceso, porque el piso de 1,0 s de `resolve_oneshot` se suma al back-off: hueco ≈ 1,0 + 0,5 + ε s. Conviene contrastarlo con `ia_max_ms` de `disconnect-0.5`.

**Issues relevantes** (`gh api search/issues`):

| Repo | # | Título | Fecha | Relevancia |
|---|---|---|---|---|
| sccn/liblsl | #35 | "Recover a stream with the same uid" | 2019-09-10 | Abierto |
| sccn/liblsl | #195 | "Fix recovery issues" | PR mergeado 2023-05-22 | Remite a sccn/labstreaminglayer#105 |
| sccn/liblsl | #299 | "Fix inlet reception after close and reopen" | PR mergeado 2026-09-20 | Cita la "reconnect back-off" y que "recovery can wait indefinitely for a missing outlet" |
| labstreaminglayer/pylsl | #88 | "Trouble catching LostError?" | 2024-11-18 | — |
| labstreaminglayer/pylsl | #93 | "`source_id` should default to having a non-empty value" | 2024-12-10 | — |

**Ningún issue documenta una medición del tiempo de reconexión.** Hasta donde se buscó, el ~560 ms de la tesis sería un aporte original.

---

## Referencias verificadas (APA 7)

Aguayo, D., Bicket, J., Biswas, S., Judd, G. y Morris, R. (2004). Link-level measurements from an 802.11b mesh network. *ACM SIGCOMM Computer Communication Review, 34*(4), 121–132. https://doi.org/10.1145/1030194.1015482

Arpaia, P., Esposito, A., Galdieri, F. y Natalizio, A. (2025). Acquisition delay of wireless EEG instruments in time-sensitive applications. *IEEE Transactions on Neural Systems and Rehabilitation Engineering, 33*, 2151–2159. https://doi.org/10.1109/TNSRE.2025.3575695

Dasenbrock, S., Blum, S., Maanen, P., Debener, S., Hohmann, V. y Kayser, H. (2022). Synchronization of ear-EEG and audio streams in a portable research hearing device. *Frontiers in Neuroscience, 16*, Artículo 904003. https://doi.org/10.3389/fnins.2022.904003

Epinat-Duclos, J., Rossignon, A., Prado, J., Van der Henst, J., Paulignan, Y., Beaudoin-Gobert, M., Lecaignard, F. y Bedoin, N. (2026). Evaluating portable EEG: A comparison between two wireless systems (EPOC Flex and LiveAmp) and the wired BrainAmp system. *PeerJ, 14*, e20416. https://doi.org/10.7717/peerj.20416

Iwendi, C., NWibo, E. y Uwah, S. E. (2026). *EEG and motion signals pilot dataset* [Conjunto de datos]. Zenodo. https://doi.org/10.5281/zenodo.22093536

Jacob, R., Da Forno, R., Trüb, R., Biri, A. y Thiele, L. (2020). *Wireless link quality estimation on FlockLab – and beyond* [Conjunto de datos]. Zenodo. https://doi.org/10.5281/zenodo.3731498

Jardosh, A., Ramachandran, K., Almeroth, K. y Belding-Royer, E. (2005). Understanding congestion in IEEE 802.11b wireless networks. En *Proceedings of the 5th ACM SIGCOMM Conference on Internet Measurement (IMC '05)*. ACM Press. https://doi.org/10.1145/1330107.1330140

Krigolson, O., Williams, C., Norton, A., Hassall, C. y Colino, F. (2017). Choosing MUSE: Validation of a low-cost, portable EEG system for ERP research. *Frontiers in Neuroscience, 11*, Artículo 109. https://doi.org/10.3389/fnins.2017.00109

Mahmud, S. A., Kasera, S., Ji, M. y Agarwal, V. (2023). *Experimental evaluation of interference in 2.4 GHz wireless network* (Informe INL/RPT-23-74719). Idaho National Laboratory; Office of Scientific and Technical Information. https://doi.org/10.2172/2242485

Sui, K., Zhou, M., Liu, D., Ma, M., Pei, D., Zhao, Y., Li, Z. y Moscibroda, T. (2016). Characterizing and improving WiFi latency in large-scale operational networks. En *Proceedings of the 14th Annual International Conference on Mobile Systems, Applications, and Services* (pp. 347–360). ACM. https://doi.org/10.1145/2906388.2906393

Swartz Center for Computational Neuroscience. (2026). *liblsl* (versión v1.18.0.b5) [Software]. GitHub. https://github.com/sccn/liblsl

Netravali, R., Sivaraman, A., Das, S., Goyal, A., Winstein, K., Mickens, J. y Balakrishnan, H. (2015). Mahimahi: Accurate record-and-replay for HTTP. En *2015 USENIX Annual Technical Conference* (pp. 417–429). USENIX Association. ⚠️ SIN VERIFICAR en Crossref (USENIX no emite DOI). Las páginas no se verificaron; el repositorio sí: https://github.com/ravinet/mahimahi (GPL-3.0).
