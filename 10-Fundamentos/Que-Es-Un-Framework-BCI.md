# ¿Qué es un framework BCI? — explicado desde cero

> Nota de fundamentos · 2026-08-15 · base para entender el [[../30-TFG/Seleccion-Tema/Tema-28-Evaluacion-Frameworks-BCI|Tema 28]]

## La analogía que lo destraba

¿Qué es Unity para los videojuegos? Nadie que hace un juego programa desde cero el renderizado, la física, el sonido y el manejo de controles — usa Unity, que ya trae todo eso resuelto, y se concentra en SU juego.

**Un framework BCI es el "Unity" de los experimentos con señales cerebrales**: el andamiaje de software que resuelve las partes repetitivas y difíciles, para que el investigador se concentre en su experimento.

## El problema que resuelven: construir una BCI sin framework

Imaginate que querés armar el experimento más simple del mundo: mostrarle letras a una persona con un casco EEG y detectar cuál mira. Sin framework, tenés que programar A MANO:

1. **El driver del casco**: cada marca de EEG (OpenBCI, Emotiv, g.tec, Muse…) habla su propio protocolo. Código distinto para cada una.
2. **La sincronización**: la letra apareció en pantalla a las 14:03:07.482 — ¿qué muestra de señal corresponde a ese instante EXACTO? Si te corrés 50 milisegundos, el experimento no sirve. Este problema solo ya es un proyecto.
3. **El pipeline en tiempo real**: filtrar la señal, cortarla en ventanas, extraer características, clasificar — todo mientras sigue llegando señal nueva, sin atrasarse.
4. **La presentación de estímulos**: pantallas que parpadean a frecuencias exactas, secuencias de letras, con precisión de milisegundos.
5. **El feedback**: mover el cursor, escribir la letra, mostrar el resultado — cerrando el lazo con el usuario.
6. **El registro**: guardar TODO (señal + eventos + respuestas) en formatos que después se puedan analizar.

Son meses de ingeniería **antes de poder empezar el experimento**. Y cada laboratorio del mundo reinventando la misma rueda, con bugs distintos.

## Qué te da un framework BCI

Exactamente esas seis piezas, ya resueltas:

| Pieza | Qué hace el framework |
|---|---|
| **Drivers/adquisición** | Se conecta a decenas de dispositivos EEG con la misma interfaz (LSL soporta 150+) |
| **Sincronización** | Time-stamps unificados entre señal, estímulos y respuestas |
| **Pipeline** | Bloques conectables: filtro → ventana → características → clasificador |
| **Estímulos** | Spellers, estímulos parpadeantes, secuencias con timing preciso |
| **Feedback/aplicaciones** | Teclados virtuales, juegos, cursores — las "apps" de la BCI |
| **Registro** | Graba todo en formatos estándar (XDF, BIDS) para el análisis |

Vos escribís solo lo específico de tu experimento; el resto viene de fábrica.

## Los casos de uso reales (quién los usa y para qué)

1. **Investigación académica** (el uso principal): un laboratorio que estudia, por ejemplo, si el neurofeedback mejora la atención — arma el experimento en semanas en vez de meses.
2. **Prototipos clínicos**: comunicadores para pacientes (spellers P300 como el de la tesis de UNSAM — que usó OpenBCI + código propio, es decir, sufrió a mano parte de lo que un framework regala).
3. **Neurociencia experimental**: registrar EEG + mirada + ritmo cardíaco sincronizados en un mismo experimento.
4. **Docencia y hobby**: estudiantes y makers que prueban paradigmas sin arrancar de cero.
5. **Desarrollo de productos**: empresas que prototipan antes de construir su stack propio.

## Los jugadores, uno por uno

| Framework | En una frase | Su ángulo |
|---|---|---|
| **BCI2000** (2000~) | El abuelo: sistema completo y probadísimo, en C++ | Robustez clínica; tecnología de hace 20 años |
| **OpenViBE** (2009~) | Diseñás el pipeline **dibujando cajas y flechas** (visual) | Accesible para no-programadores |
| **Lab Streaming Layer (LSL)** | No es un framework completo: es **la capa de transporte y sincronización** que casi todos usan por debajo (150+ dispositivos) | El estándar de facto para mover señal |
| **Timeflux** (Python) | Pipelines en tiempo real definidos en archivos de configuración | Moderno, generalista, MIT |
| **BciPy** (Python) | Especializado en spellers y paradigmas ERP con PsychoPy | Foco en comunicación asistiva |
| **MEDUSA** (Python) | Ecosistema con muchos paradigmas y hasta deep learning | Amplio, pero solo Windows y sin gráficos en tiempo real |
| **NeuXus** (Python) | Similar a Timeflux, arquitectura de nodos | Alternativa liviana |
| **PyNoetic** (2025, Python) | BCI **sin escribir código** (no-code) | El más nuevo; apunta a democratizar |

Fijate el patrón: **todos resuelven el mismo problema con arquitecturas distintas** — C++ monolítico vs. cajas visuales vs. nodos configurables vs. no-code. Y cada paper elogia el propio.

## Por qué esto hace tesis (el puente al Tema 28)

Ponete en los zapatos de quien arranca un proyecto BCI hoy — un laboratorio, una empresa, un tesista: **¿cuál elige?** No hay respuesta fundada: no existe una comparación sistemática con criterios de ingeniería (¿cuál rinde mejor en tiempo real? ¿cuál es más fácil de extender? ¿cuál está mejor mantenido? ¿cuál tiene la mejor experiencia de desarrollo?).

Esa elección a ciegas es exactamente la que el [[../30-TFG/Seleccion-Tema/Tema-28-Evaluacion-Frameworks-BCI|Tema 28]] resuelve: evaluar los frameworks con método (ISO/IEC 25010 + benchmarks + caso de estudio) y publicar la guía de decisión que falta.

## Fuentes

- BCI-HIL / Timeflux: [Frontiers in Human Neuroscience (2023)](https://doi.org/10.3389/fnhum.2023.1129362)
- PyNoetic: [PLOS One (2025)](https://doi.org/10.1371/journal.pone.0327791)
- LSL y ecosistema (XDF, dispositivos): [Imaging Neuroscience (MIT Press)](https://direct.mit.edu/imag/article/doi/10.1162/IMAG.a.136/132678/) · [dispositivos soportados](https://labstreaminglayer.readthedocs.io/info/supported_devices.html)
- MEDUSA: [medusabci.com / GitHub](https://github.com/medusabci/medusa-platform) — ⚠️ completar cita formal
- BCI2000 y OpenViBE: referenciados en los papers anteriores — ⚠️ completar citas primarias si se usan en el TFG

## Enlaces

[[../30-TFG/Seleccion-Tema/Tema-28-Evaluacion-Frameworks-BCI|Tema 28]] · [[Cadena-de-Senal-Neural]] · [[Como-Funciona-un-Implante-Intracortical]]
