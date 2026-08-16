# Oportunidades en neurotecnología para ingenieros de software

> 2026-08-16 · Investigación de CARRERA (no de selección de tema — la selección está cerrada, ver [[../00-Sistema/Decisiones|D-004]]).
> Disparador: el autor encontró https://www.neuroenglab.com/join-us/ (tesis de MSc en neuroingeniería) y pidió mapear el ecosistema: ¿a qué puertas apunta la tesis como puntapié?
> Método: barrido web de esta fecha (labs + empresas + agregadores). Todas las URLs provienen de fetches o resultados de búsqueda reales. Los avisos de empresas rotan rápido — esto es una foto, no un catálogo permanente.

## El hallazgo central (leer esto primero)

**La industria BCI compra perfil de software, no de neurociencia.** Synchron lo dice textual en su internship de ML: *"Knowledge or experience in BCI and Neuroscience is not required"*. Y el nicho MENOS competido es exactamente el de la tesis elegida: **calidad, testing y dependability de software** — la mayoría entra por ML/neurociencia, casi nadie por confiabilidad. Precision Neuroscience tiene un puesto dedicado de Software Quality Engineer; Paradromics pide experiencia en QMS de dispositivos médicos; Neuralink toma interns de infraestructura de testing y CI/CD.

**La tesis de resiliencia ([[../30-TFG/Seleccion-Tema/Tema-28-Evaluacion-Frameworks-BCI|Tema 28]]+28.1) es evidencia directa de esa competencia.** Además encaja con el marco regulatorio: la FDA clasifica el software de BCI implantadas como "major level of concern" (guidance 2021) y la IEC 62304 exige verificación y validación en todo el ciclo de vida — fault injection es antecedente citable para roles de V&V.

## Labs académicos con puerta abierta (tesis MSc / PhD / RA)

| Organización | País | Qué ofrece | URL |
|---|---|---|---|
| NeuroEng Lab (TUM/ETH/UAB/Sant'Anna/MedUni Wien) | CH·DE·ES·IT·AT·RS | 3 tesis MSc (neuroestimuladores inteligentes, motion capture con IA, predicción de dolor con wearables); piden CV+transcript+carta | https://www.neuroenglab.com/join-us/ |
| EPFL — Neuro-X (MSc) | Suiza | Maestría cross-school que admite perfil de Computer Science; tesis de 18-26 semanas en lab, industria u hospital | https://www.epfl.ch/schools/sections/neuro-x/master-program-in-neuro-x/ |
| ETH/UZH — MSc Neural Systems and Computation | Suiza | Maestría con computer science como disciplina de entrada explícita | https://ethz.ch/en/studies/master/degree-programmes/engineering-sciences/neural-systems-and-computation.html |
| TU Graz — Graz BCI Lab (Müller-Putz) | Austria | Tesis de máster; invitan a contactar directo (no publican topics online) | https://www.tugraz.at/institute/ine/people/gernot-mueller-putz |
| Donders Institute / Radboud | Países Bajos | RA de 1 año en ML para BCI (pensada como puente a industria/PhD); PhDs en BCI | https://www.ru.nl/en/donders-institute/working-at/vacancies |
| NeuroRestore (EPFL/CHUV) | Suiza | Publica tesis de máster en su página de posiciones | https://www.neurorestore.swiss/ ⚠️ detalle sin fetchear |
| Wyss Center | Suiza | Portal de empleos (sin vacantes al fetch; se vio antes un Project QA Engineer) | https://wysscenter.ch/ |
| PSL / AI4theSciences | Francia | PhD en decodificación de comunicación — pide exactamente perfil computacional (Python, big data, IA) | https://euraxess.ec.europa.eu/jobs/66405 |

## Empresas que contratan software (con nivel de entrada marcado)

| Empresa | País | Roles de software vistos | URL |
|---|---|---|---|
| Neuralink | EE.UU. | **SWE Intern (Infrastructure)** 🎓, SWE CI/CD, Lab Systems SWE (plataforma de datos) | https://neuralink.com/careers/ |
| Synchron | EE.UU./AU | Embedded SWE (desarrollo y testing), **ML internship sin requisito de neurociencia** 🎓 | https://synchron.com/careers |
| Precision Neuroscience | EE.UU. | Real-Time SWE, full-stack, mobile, **Senior Software Quality Engineer** | https://www.precisionneuro.io/careers |
| Paradromics | EE.UU. | SWE clínico: evaluar software con datos neurales simulados/reales y hardware-in-the-loop; QMS médico "preferred" | https://paradromicsinc.applytojob.com/apply/hQIogsvwhA/Software-Engineer |
| Science Corp | EE.UU. | SWE Devices — SDK "synapse" para terceros | https://science.xyz/careers/open-positions/ |
| Blackrock Neurotech | EE.UU. | Full-Stack SWE para aplicaciones BCI | https://blackrockneurotech.com/careers/ |
| MindMaze | Suiza | **Internship R&D SWE (6 meses)** 🎓, SWE Biosignal Processing, Embedded SWE con V&V | https://jobs.smartrecruiters.com/MindMaze/743999696619501-r-d-software-engineer-internship |
| CorTec | Alemania | Menciona explícitamente **tesis de máster y working students** 🎓 | https://cortec-neuro.com/career/ |
| Bitbrain | España | **Junior SWE C++ Full Stack** 🎓 — entrada en español y nivel junior | https://www.bitbrain.com/careers |
| INBRAIN Neuroelectronics | España | SWE real-time signal processing, Data Architect | https://inbrain-neuroelectronics.jobs.personio.com/?language=en |
| Cognixion | EE.UU./CA | SDK, AI/ML, iOS, Principal SWE MedTech | https://www.cognixion.com/careers |
| OpenBCI | EE.UU. | **Software Intern** 🎓 y **Neural Data Science Intern** 🎓 — máximo fit con una tesis sobre frameworks open source | https://openbci.com/careers/software-intern |
| g.tec | Austria | Jobs + hackathons BR41N.IO (entrada low-cost al campo) | https://www.gtec.at/job/ |

🎓 = nivel estudiante/junior alcanzable durante o justo después del TFG.

## Los 7 patrones de habilidades que el campo repite (≥3 fuentes cada uno)

1. **Procesamiento de señal en tiempo real** (INBRAIN, MindMaze, Precision, Science Corp)
2. **Embedded/firmware de dispositivo médico** (Synchron, MindMaze, Cognixion, g.tec)
3. **ML aplicado a decodificación neural** (Synchron, Donders, Precision, PSL)
4. **Full-stack + plataformas de datos cloud** (Blackrock, Precision, Paradromics, Neuralink)
5. **QA/validación de software médico** (Precision, Paradromics, Wyss, MindMaze; norma IEC 62304) ← **la tesis vive acá**
6. **Infraestructura de testing / hardware-in-the-loop / CI-CD** (Paradromics, Neuralink) ← **y acá**
7. **SDKs y tooling para terceros** (Science Corp, Cognixion, OpenBCI)

## Temas de aplicación futura (post-TFG: maestría/publicaciones)

1. **Neuroseguridad**: de fallos accidentales a maliciosos (flooding, jamming, spoofing) — continuación natural de la tesis. CACM: https://cacm.acm.org/research/eight-reasons-to-prioritize-brain-computer-interface-cybersecurity/ · Neuroethics 2025: https://link.springer.com/article/10.1007/s12152-025-09607-3
2. **V&V regulatoria (IEC 62304 + guidance FDA de BCI)**: la FDA guidance 2021 (https://www.federalregister.gov/documents/2021/05/20/2021-10622/implanted-brain-computer-interface-devices-for-patients-with-paralysis-or-amputation-non-clinical); IEC 62304 ed. 2 incorpora IA — área abierta.
3. **Fault injection en embebidos/HIL para medtech**: extender la metodología del TFG a hardware-in-the-loop (lo que piden Paradromics/Synchron). Survey ACM: https://dl.acm.org/doi/10.1145/2841425
4. **Benchmarking de plataformas BCI open source**: línea activa de papers (MetaBCI: https://www.sciencedirect.com/science/article/pii/S0010482523012714) donde el estudio de resiliencia tiene lugar natural.
5. **Confiabilidad de pipelines ML de decodificación en tiempo real/closed-loop**: fault injection sobre DNNs (https://arxiv.org/pdf/2602.00909) + demanda industrial (Synchron ML).

## Monitoreo permanente (bookmarks)

- NeuroTechX Job Board: https://neurotechx.com/jobs/ · awesome-bci: https://github.com/NeuroTechX/awesome-bci
- Neurotech Futures: https://neurotechjobs.io/
- Lista curada de Fabien Lotte (Inria): https://sites.google.com/site/fabienlotte/bci-community/job-offers
- FindAPhD ("brain computer interfaces"): https://www.findaphd.com/phds/?Keywords=brain+computer+interfaces
- EURAXESS (posiciones UE): https://euraxess.ec.europa.eu/

## Advertencias de rigor

- ⚠️ El indicio "no hay trabajos previos de BCI + fault injection" (búsqueda del agente sin resultados directos) coincide con la verificación doble ya hecha para el tema 28.1, pero la búsqueda sistemática formal en Scopus/IEEE es tarea del Mes 1 del TFG — no citar la ausencia sin ella.
- ⚠️ Snapshot de avisos del 2026-08-16: verificar vigencia antes de aplicar a cualquiera.

## Enlaces

[[../30-TFG/Seleccion-Tema/Tema-28-Evaluacion-Frameworks-BCI|Tema-28]] · [[../00-Sistema/Decisiones|D-004]] · [[Calibracion-Alcance-Tesis-BCI]]
