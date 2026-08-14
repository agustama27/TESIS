# Tema 7 — Framework/SDK para pipelines BCI en tiempo real

> Estado: 🟢 En reserva (único tema natural en Plataformas de Desarrollo)

## Definiciones Iniciales (formato oficial)

- **Tipo de TFG**: Prototipado Tecnológico · **Línea**: Plataformas de Desarrollo

### Título tentativo (~12 palabras)

Plataforma de desarrollo para prototipado rápido de interfaces cerebro-computadora en tiempo real

### Justificación de la línea (3 renglones)

La producción de software BCI carece de herramientas modernas de developer experience: las piezas existen (MNE, BrainFlow) pero no la orquestación. Un SDK que las unifique acompaña la metodología de desarrollo de un dominio emergente — el corazón de la línea.

### Explicación del tema (5-15 renglones)

Prototipar una BCI hoy exige integrar manualmente herramientas dispares: MNE (análisis offline), BrainFlow (solo adquisición), BCI2000 (C++ legado). Un desarrollador sin formación en neurociencia tarda semanas en un "hola mundo". Este trabajo diseña y prototipa un SDK en Python que abstrae el pipeline completo (fuente → filtro → features → clasificador → salida de eventos) con arquitectura de plugins, permitiendo construir una BCI funcional en pocas líneas. El core demostrable: motor de streaming, plugin de reproducción de datasets públicos, un paradigma implementado (P300) y una aplicación de ejemplo construida sobre el SDK.

### Problema / pregunta (3-5 renglones)

¿Cómo debe diseñarse una capa de abstracción para pipelines BCI en tiempo real que reduzca de semanas a horas el tiempo de prototipado, manteniendo extensibilidad para nuevos paradigmas y fuentes de señal?

### Revisión de literatura (4 trabajos, APA)

1. Systematic review de headsets EEG de bajo costo. *Frontiers in Neuroinformatics* (2020). https://doi.org/10.3389/fninf.2020.553352
2. MOABB como antecedente de infraestructura BCI open source. https://moabb.neurotechx.com
3. ⚠️ Paper de BCI2000 (Schalk et al.) — verificar referencia exacta.
4. ⚠️ Documentación técnica de BrainFlow/MNE como antecedentes — formalizar citas.

### Justificación del TFG (borrador)

Con la industria BCI creciendo al 18% anual, la fricción de developer experience es un cuello de botella documentable. El entregable es puro Software Engineering: diseño de API, arquitectura de plugins, testing de sistemas en tiempo real, CI/CD y distribución. Demo definitiva: la misma BCI en 10 líneas sobre el SDK vs ~300 sin él. *(Expandir a 15-20 renglones si se activa.)*

## Ampliación

Ficha completa: [[../../20-Investigacion/Temas-Candidatos-TFG|lista maestra]] (ficha 7). Riesgo principal: scope creep — v1 recortada por contrato.
