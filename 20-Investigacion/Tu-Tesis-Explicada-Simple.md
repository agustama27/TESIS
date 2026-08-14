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

## ¿Cómo vas a VALIDAR que el programa mejora? (la pregunta del tutor)

Esta es la pregunta metodológica central, y tiene respuesta sólida. Vamos por partes.

### La clave: los datos vienen con la respuesta correcta

Cuando Stanford grabó a los participantes, les mostraba **una oración en pantalla** y les pedía que intentaran decirla. O sea que cada grabación tiene dos cosas: la señal del cerebro Y **la oración que la persona intentó decir** (la "respuesta correcta").

Validar es entonces como **corregir un examen**: tu programa produce un texto a partir de la señal, y lo comparás palabra por palabra contra la oración correcta. Si la persona intentó decir "quiero agua fría" y tu programa decodificó "quiero agua fina", erró 1 palabra de 3. Ese porcentaje de palabras erradas es el **WER** — la nota del examen. Es un número objetivo, automático, sin opiniones: no necesitás médicos, jueces ni encuestas.

### ¿Cuál es tu "población estadística"?

Acá está el matiz que tenés que tener CLARO para el tutor: **tu unidad de análisis no son personas — son oraciones grabadas.**

- El dataset de escritura tiene **1.000 oraciones** (43.501 caracteres) grabadas en 10 sesiones.
- El de habla tiene cientos de oraciones por sesión, a lo largo de semanas.

Tu población es ese conjunto de oraciones/sesiones. Cada oración es una observación. Con cientos de observaciones por condición podés hacer estadística seria — igual que un test A/B sobre miles de requests, aunque venga de un solo servidor.

**¿Y no es un problema que sea UNA persona?** Es la pregunta trampa, y la respuesta honesta es la mejor defensa: los papers de Nature de este campo son con N=1 o N=2 participantes — es lo normal, porque cada participante requiere neurocirugía. La validez INTERNA de tu experimento (¿el cambio que hice mejora la decodificación en estos datos?) es fuerte; la generalización a otras personas se **declara como limitación**, igual que lo declaran los papers de Nature. Un tesista que conoce las limitaciones de su método impresiona más que uno que promete de más.

### Las cuatro reglas que hacen que la medición sea seria

1. **Datos de examen separados** ("held-out test set"): dividís las oraciones — con unas entrenás el programa, con OTRAS lo evaluás. El programa se mide con oraciones que nunca vio, como un alumno que estudia con una guía y rinde con un examen distinto. El benchmark internacional ya define esta división oficialmente — la usás tal cual, así tus números son comparables con los de todos los equipos del mundo.
2. **Comparación justa**: todas las variantes que compares (con corrector / sin corrector / lector A / lector B) se evalúan sobre EXACTAMENTE las mismas oraciones de examen. Misma cancha para todos.
3. **Controlar el azar del entrenamiento**: entrenar una red tiene componente aleatorio (como barajar un mazo). Entrenás cada variante varias veces con semillas distintas y reportás el promedio y la variación — no un número de una corrida con suerte.
4. **Test estadístico**: para afirmar "A es mejor que B" no alcanza con que el promedio dé mejor — hacés un test pareado sobre las oraciones (¿A le ganó a B consistentemente en las mismas oraciones, o fue ruido?). Es el mismo concepto que la significancia en un test A/B.

### El párrafo listo para el tutor

> "La validación es objetiva y automática: los datasets incluyen la oración que el participante intentó decir, así que cada variante del sistema se evalúa comparando su salida contra esa referencia, con la métrica estándar del campo — el porcentaje de palabras erradas (WER). Mi población estadística son las oraciones grabadas: mil en el dataset de escritura, cientos por sesión en el de habla. Uso la división oficial entrenamiento/evaluación del benchmark internacional, para que mis números sean directamente comparables con los publicados. Cada comparación se repite con varias semillas de entrenamiento y se somete a un test estadístico pareado sobre las oraciones. Y declaro explícitamente la limitación de que los datos provienen de pocos participantes — que es la norma del campo, incluso en los papers de Nature, por la naturaleza quirúrgica de la recolección."

Si soltás ese párrafo cuando pregunte cómo validás, la reunión la ganaste.

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
