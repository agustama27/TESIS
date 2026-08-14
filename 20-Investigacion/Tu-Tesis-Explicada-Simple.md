# Tu tesis explicada simple — sin tecnicismos

> 2026-08-14 · Este documento es TU base. Los otros dos ([[Decodificacion-Brain-to-Text]] y [[Ingenieria-de-Software-y-AI-Engineering]]) son material de profundización para DESPUÉS. Empezá por acá.

---

## Tu tesis en tres frases

1. Hay personas que están **completamente paralizadas** (por ELA u otras enfermedades) pero su mente funciona perfecto: piensan, entienden, quieren hablar — y no pueden mover ni la boca.
2. Científicos de Stanford les pusieron sensores en el cerebro, les pidieron que *intentaran* hablar o escribir, grabaron esas señales, y un **programa de computadora** convierte esas señales en texto. Ya funciona: una persona con ELA volvió a "hablar" con su familia.
3. Tu tesis: **estudiar y mejorar ese programa**. Las grabaciones son públicas — cualquiera puede bajarlas — así que no necesitás pacientes, ni sensores, ni cirugía. Solo tu computadora y lo que ya sabés hacer: programar.

Eso es todo. Todo lo demás son detalles de cómo.

## La analogía que lo explica todo

¿Viste el **autocorrector del teléfono**? Vos tipeás "hoal" y él escribe "hola". Hace dos cosas: lee lo que apretaste (aunque sea impreciso) y usa su conocimiento del idioma para adivinar qué quisiste decir.

El sistema de tu tesis es **exactamente eso**, con una diferencia: en vez de leer teclas apretadas, lee **señales del cerebro** de una persona que intenta hablar. Como las señales son ruidosas e imprecisas (igual que tus dedos en el teclado), el sistema tiene dos partes:

- **Parte 1 — el lector**: un programa que aprende a reconocer patrones en las señales del cerebro y propone sonidos ("creo que quiso decir el sonido 'ma'").
- **Parte 2 — el corrector**: un programa que conoce el idioma y arregla lo que el lector propone ("'ma-ño-na'... seguro quiso decir 'mañana'").

**Tu pregunta de tesis, en criollo: ¿cuánto del mérito es del lector y cuánto del corrector?** Nadie lo midió sistemáticamente. Es como preguntar: ¿el autocorrector funciona porque lee bien tus dedos, o porque es muy bueno adivinando el idioma? Para saberlo, hacés lo obvio: **probás el sistema con y sin corrector, y medís la diferencia**. Eso tiene un nombre técnico ("ablación") pero es literalmente sacar una pieza y ver qué pasa.

## Qué vas a HACER, mes a mes, en palabras llanas

**Mes 1 — Entender el terreno.**
Bajás las grabaciones públicas de Stanford (son archivos, como bajar un dataset de Kaggle). Aprendés cómo están organizadas: qué es cada archivo, qué significa cada número. Leés los dos papers principales (te digo cuáles abajo). Escribís el marco teórico contando esta historia.

**Mes 2 — Hacer andar lo que ya existe.**
Los científicos publicaron su código en GitHub. Tu trabajo: hacerlo correr en tu máquina/Colab y verificar que te da los mismos resultados que publicaron. Esto se llama "reproducir el baseline" y es EXACTAMENTE lo que hacés en el laburo cuando heredás un repo: clonarlo, hacerlo andar, verificar que funciona. Si lográs esto, ya tenés medio TFG: reproducir un resultado de la revista Nature es un logro en sí mismo.

**Mes 3 — Tu experimento.**
Ahora que el sistema anda, jugás con las piezas: lo corrés SIN el corrector de idioma y medís cuánto empeora. Lo corrés con un corrector más simple y con uno más potente. Cambiás el "lector" por otro tipo de programa y comparás. Cada corrida te da un número (cuántas palabras salieron mal de cada 100) y armás la tabla comparativa. Esto es correr experimentos y anotar resultados — como probar configuraciones de un sistema hasta entender qué hace la diferencia.

**Mes 4 — Contarlo bien.**
Escribís qué encontraste, hacés los gráficos, redactás conclusiones, armás el documento final con el formato de la universidad. Publicás tu código en GitHub.

Fijate una cosa: **no hay ningún paso ahí que no sepas hacer hoy**. Bajar datos, hacer andar un repo ajeno, correr experimentos, medir, comparar, documentar. Lo nuevo es el TIPO de datos — y eso se aprende en el Mes 1.

## Qué vas a ESTUDIAR (la lista honesta)

No necesitás saber neurociencia. Necesitás entender **cinco cosas**, y todas están a tu alcance:

1. **Cómo se ven los datos del cerebro** (Mes 1): son series de números en el tiempo, como cualquier señal. Cada sensor da una columna de números. Punto. No hace falta saber POR QUÉ el cerebro los produce — solo qué forma tienen.
2. **Qué es una red recurrente (el "lector")**: un tipo de red neuronal que procesa secuencias — ya trabajaste con redes; esta es una variante. Un tutorial de una tarde.
3. **Qué es un modelo de lenguaje (el "corrector")**: ya lo sabés — es lo que usás todos los días con los LLMs. Acá se usa una versión más simple.
4. **Cómo se mide el error**: de cada 100 palabras decodificadas, cuántas salieron mal. Se llama WER (word error rate). Eso es todo el misterio.
5. **La historia del campo** (para el marco teórico): tres papers, que son tres capítulos de una misma historia — 2021: escribir con la mente; 2023: hablar con la mente; 2024: precisión casi perfecta. Está contada en [[Decodificacion-Brain-to-Text]].

## El guion para tu tutor (dos minutos, palabra por palabra)

Practicalo en voz alta. Es TODO lo que necesitás decir:

> "Profe, mi tema es sobre personas que quedaron completamente paralizadas — por ELA, por ejemplo — pero con la mente intacta. Hoy existe tecnología que les devuelve la comunicación: sensores en el cerebro captan la señal de lo que INTENTAN decir, y un software la convierte en texto. Esto ya funciona: en 2024 salió en el New England Journal of Medicine un caso con 97% de precisión.
>
> Lo importante para nosotros: los datos de esos estudios son públicos. Stanford los liberó, y hay una competencia internacional donde equipos de todo el mundo intentan mejorar el software de decodificación. O sea que yo puedo trabajar sobre el problema real, con datos reales de pacientes reales, sin necesitar ni un paciente ni un sensor.
>
> Mi trabajo tiene tres partes. Primero, hacer funcionar el sistema de referencia que publicaron los autores y verificar que reproduzco sus resultados. Segundo, mi experimento: el sistema tiene dos componentes — uno que lee la señal del cerebro y otro que corrige usando conocimiento del idioma, como un autocorrector — y voy a medir sistemáticamente cuánto aporta cada uno, cosa que nadie publicó. Tercero, documentar todo de forma reproducible.
>
> Es un Trabajo de Investigación en la línea de Transformación Digital, y es cien por ciento ingeniería de software: datos, modelos, experimentos y medición. La neurociencia ya la hicieron los médicos de Stanford — yo trabajo del lado del software, que es donde está el cuello de botella del campo."

Fin. Si el tutor pregunta más, mejor — significa que mordió el anzuelo.

## Las preguntas que te puede hacer, respondidas en criollo

**"¿Y vos sabés de cerebros?"**
> "No necesito: los datos ya están grabados y documentados. Para mí son señales — números en el tiempo — y procesarlas con modelos es lo que hago como ingeniero. El paper explica qué significa cada dato."

**"¿No es muy ambicioso?"**
> "Lo ambicioso ya lo hicieron otros: la cirugía, la recolección, el sistema base. Mi alcance es acotado: reproducir lo publicado y hacer un experimento de comparación bien medido. Si solo lograra la reproducción, ya es un resultado válido — y todo lo que sume encima es aporte."

**"¿Con qué recursos?"**
> "Datos: gratis, públicos. Código base: público en GitHub. Cómputo: Google Colab. Costo total: una suscripción de Colab Pro. No dependo de importar nada ni de conseguir pacientes."

**"¿Por qué esto y no algo más tradicional?"**
> "Porque la universidad no tiene ninguna tesis de este tema — sería de las primeras — y porque es el área donde quiero desarrollarme profesionalmente. Prefiero cuatro meses invertidos en algo que define mi carrera que en un sistema más del montón."

## Por qué NO tenés que saber todo hoy

El tutor no espera un experto — espera tres cosas: **un problema claro** (personas sin comunicación + software que la devuelve), **un plan realista** (reproducir → experimentar → documentar, con datos públicos), y **evidencia de que es posible** (papers publicados, datos abiertos, código disponible, competencia internacional). Las tres las tenés.

Los términos técnicos los vas a incorporar HACIENDO, durante el Mes 1 — igual que aprendiste todo lo demás que sabés. Nadie aprende BCI antes de empezar una tesis de BCI; se aprende adentro. Para eso está la Etapa 0 del [[Roadmap]] y para eso me tenés a mí como tutor de estudio.

## Diccionario de emergencia (por si el tutor usa jerga)

| Término | Qué significa, simple |
|---|---|
| BCI / interfaz cerebro-computadora | Sistema que conecta señales del cerebro con una computadora |
| Intracortical | Sensores puestos DENTRO del cerebro (los datos ya existen; vos no tocás esto) |
| Electrodo | El sensor que capta la señal eléctrica |
| ELA | Enfermedad que paraliza todo el cuerpo dejando la mente intacta |
| Decodificar | Traducir la señal del cerebro a texto |
| RNN / red recurrente | El programa que aprende patrones en las señales (el "lector") |
| Modelo de lenguaje | El programa que conoce el idioma y corrige (el "corrector") |
| WER | De cada 100 palabras, cuántas salieron mal |
| Baseline | El sistema de referencia publicado, contra el que te comparás |
| Ablación | Sacar una pieza del sistema para medir cuánto aportaba |
| Benchmark | Competencia con tabla de posiciones para comparar soluciones |
| Dataset | Las grabaciones, empaquetadas como archivos para bajar |
| Dryad | El sitio donde Stanford publicó los datos |
| Reproducir | Hacer andar el trabajo de otro y verificar que da lo mismo |

## Enlaces

[[Decodificacion-Brain-to-Text]] (la historia completa, para el Mes 1) · [[Ingenieria-de-Software-y-AI-Engineering]] (munición avanzada, para releer DESPUÉS de dominar esta nota) · [[Temas-Candidatos-TFG]] · [[Roadmap]]
