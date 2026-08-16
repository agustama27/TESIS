# BRAND — qué es, para qué se usa, y qué campos abre para una tesis

> Nota de investigación · 2026-08-15 · fuente principal: el paper de BRAND (Ali et al., *Journal of Neural Engineering*, 2024) — [PMC11021878](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11021878/) · [IOPscience](https://iopscience.iop.org/article/10.1088/1741-2552/ad3b3a/meta)
> Nota previa: se descartó la idea "nodo SNN para BRAND" — la motivación de las SNN (energía) no aplica en una plataforma que corre en workstation.

## Qué es, en criollo

**BRAND = el backend de microservicios de una BCI de investigación.**

Si trabajaste con microservicios lo entendés al instante: BRAND organiza el sistema BCI como **procesos independientes ("nodos") conectados en un "grafo"**, que se pasan datos por streams de **Redis** (la misma base en memoria que se usa en la industria). Cada nodo hace una cosa: uno adquiere la señal, otro la filtra, otro corre el decodificador, otro dibuja el cursor. Como son procesos separados hablándose por Redis, **cada nodo puede estar escrito en el lenguaje que quieras** (cualquier lenguaje con cliente Redis — decenas) y correr en paralelo a su propio ritmo.

## El problema que resuelve (por qué existe)

Antes de BRAND, los laboratorios tenían un dilema:

- Los sistemas de tiempo real clásicos de los ensayos clínicos eran **rígidos** (C/Simulink de hace 15 años): confiables, pero incapaces de correr un modelo moderno de deep learning.
- Los modelos modernos viven en **Python/PyTorch**… que nadie consideraba apto para lazo cerrado con presupuesto de milisegundos.

BRAND rompió el dilema: demostró que con la arquitectura correcta (procesos + Redis + diseño asíncrono) podés correr **los mismos modelos de Python que usás offline, en el lazo cerrado en vivo**. Números del paper: comunicación entre procesos **< 600 microsegundos con 1.024 canales a 30 kHz**, y el pipeline completo — señal cruda → red neuronal → predicción de movimiento — en **menos de 8 milisegundos**.

## Para qué se usa HOY (ejemplos reales, del paper)

1. **Control de cursor en lazo cerrado con un participante humano del ensayo clínico BrainGate2** — la demostración central del paper.
2. **Más de 3.800 horas de uso independiente de una BCI en el hogar de un paciente** — no es demo de laboratorio: es infraestructura que sostiene uso domiciliario real.
3. **Adoptado por varios grupos** de investigación (textual del paper) — está camino a ser infraestructura común del campo iBCI académico.

## Qué significa para el mapa que veníamos armando

BRAND es **el puente que creíamos inexistente**: capa de aplicación BCI (decodificadores modernos, lazo cerrado) + escala de datos de implante (1024ch@30kHz), abierto. La "Neuralink App de código abierto" en versión investigación. Corrige la afirmación de los silos — ver [[Software-Neuralink-y-Verificacion-Hueco-28]].

## Campos abiertos para una tesis SOBRE/CON BRAND (modelo UNSAM: extender lo que existe)

⚠️ **Todas requieren la verificación anti-enamoramiento ANTES de comprometerse**: buscar si ya existen en el repo/literatura. Lección aprendida cuatro veces.

| # | Campo | Qué haría la tesis | Rama de la carrera |
|---|---|---|---|
| A | **Reproducibilidad y despliegue** | ¿Puede un laboratorio SIN los recursos de BrainGate desplegar BRAND? Contenedorización, guía reproducible, y **replicación de sus benchmarks de latencia en hardware accesible** — ¿los <8 ms sobreviven fuera de Emory? | DevOps / infraestructura |
| B | **Testing/QA de la plataforma** | Harness de pruebas para grafos BRAND: tests de nodos, regresión por replay de señal, validación de latencia en CI — el espíritu del tema 26 aplicado a una plataforma real con uso clínico | Testing / calidad |
| C | **Seguridad** | BRAND sostiene BCIs **en hogares** sobre Redis — cuya configuración por defecto es históricamente permisiva. Análisis de seguridad + threat model + hardening de una plataforma iBCI domiciliaria real. Conecta temas 18/21 con un objeto concreto | Seguridad |
| D | **Interoperabilidad** | Nodos puente BRAND↔LSL y exportación a BIDS: conectar la plataforma iBCI con el ecosistema EEG/estándares de datos — la versión miniatura y honesta de la tesis de los silos | Arquitectura / integración |
| E | **Observabilidad** | Dashboard de monitoreo de sesiones BRAND: latencias por nodo, salud del grafo, deriva del decodificador en el tiempo — MLOps/observabilidad sobre BCI real | MLOps / operaciones |
| F | Nodo decodificador nuevo | Implementar y evaluar un decodificador adicional como nodo (transformer u otro) | ML engineering |

**Los tres con mejor pinta a priori** (sujeto a verificación): **A** (reproducibilidad — pregunta honesta, universal, y el resultado le sirve a todo laboratorio chico del mundo, incluidos los argentinos), **C** (seguridad — "BCI domiciliaria sobre Redis" es una frase que pide auditoría a gritos), y **B** (testing — plataforma clínica joven, probablemente con poca infraestructura de pruebas).

## Enlaces

[[Software-Neuralink-y-Verificacion-Hueco-28]] · [[Calibracion-Alcance-Tesis-BCI]] (el modelo UNSAM) · [[../10-Fundamentos/Que-Es-Un-Framework-BCI|Qué es un framework BCI]]
