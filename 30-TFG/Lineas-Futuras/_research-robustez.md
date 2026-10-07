# Fuentes verificadas · Líneas 4 y 5 (robustez de EEGNet e híbrido con vigía)

> Informe de soporte · 2026-09-27 · Sesión autónoma. Alimenta [[Linea-4-Endurecer-EEGNet]], [[Linea-5-Hibrido-Vigia]] y [[_propuestas-robustez]].

## 1. Registro de verificación

Método: cada DOI se consultó en la API de Crossref (`curl -s https://api.crossref.org/works/<DOI>`) el 2026-09-27; el preprint sin DOI se verificó en la API de arXiv (`export.arxiv.org/api/query?id_list=…`) y en los metadatos `citation_*` de la página del resumen. Se copian título, autores, año y revista **tal como los devolvió la fuente**. Nada se citó de memoria.

| # | Candidato recibido | DOI / id | Resultado | Título devuelto | Autores devueltos | Año | Revista / sede, vol.(n.º), pág. |
|---|---|---|---|---|---|---|---|
| 1 | Rommel, Paillard, Moreau y Gramfort (2022) | 10.1088/1741-2552/aca220 | ✅ coincide | Data augmentation for learning predictive models on EEG: a systematic comparison | Rommel, Cédric; Paillard, Joseph; Moreau, Thomas; Gramfort, Alexandre | 2022 (28-11) | Journal of Neural Engineering, 19(6), 066020 |
| 2 | Lashgari, Liang y Maoz (2020) | 10.1016/j.jneumeth.2020.108885 | ✅ coincide | Data augmentation for deep-learning-based electroencephalography | Lashgari, Elnaz; Liang, Dehua; Maoz, Uri | 2020 (12) | Journal of Neuroscience Methods, 346, 108885 |
| 3 | Park et al. (2019), SpecAugment | 10.21437/Interspeech.2019-2680 | ✅ coincide | SpecAugment: A Simple Data Augmentation Method for Automatic Speech Recognition | Park, Daniel S.; Chan, William; Zhang, Yu; Chiu, Chung-Cheng; Zoph, Barret; Cubuk, Ekin D.; Le, Quoc V. | 2019 (15-09) | Interspeech 2019, pp. 2613-2617 |
| 4 | DeVries y Taylor (2017), Cutout | arXiv:1708.04552 (sin DOI) | ✅ coincide (arXiv) | Improved Regularization of Convolutional Neural Networks with Cutout | DeVries, Terrance; Taylor, Graham W. | 2017 (15-08; v2 29-11-2017) | arXiv preprint, cs.CV |
| 5 | Che, Purushotham, Cho, Sontag y Liu (2018), GRU-D | 10.1038/s41598-018-24271-9 | ✅ coincide | Recurrent Neural Networks for Multivariate Time Series with Missing Values | Che, Zhengping; Purushotham, Sanjay; Cho, Kyunghyun; Sontag, David; Liu, Yan | 2018 (17-04) | Scientific Reports, 8(1), 6085 |
| 6 | Lawhern et al. (2018), EEGNet (ya en el manuscrito) | 10.1088/1741-2552/aace8c | ✅ coincide | EEGNet: a compact convolutional neural network for EEG-based brain–computer interfaces | Lawhern, Vernon J; Solon, Amelia J; Waytowich, Nicholas R; Gordon, Stephen M; Hung, Chou P; Lance, Brent J | 2018 (27-07) | Journal of Neural Engineering, 15(5), 056013 |

Los seis candidatos resultaron correctos; no hay entradas ⚠️ SIN VERIFICAR. **Solo se verificaron los metadatos bibliográficos**: el contenido que se les atribuye abajo sale del resumen (Cutout, leído en la API de arXiv) o del título; no se leyó el texto completo de 1, 2, 3 y 5. Las afirmaciones de la columna "para qué" se limitan a lo que el título y el resumen sostienen.

## 2. Para qué se cita cada una

| Fuente | Qué sostiene en estas líneas | Cuidado |
|---|---|---|
| Rommel et al. (2022) | que el aumento de datos para EEG se compara sistemáticamente entre transformaciones (incluidas las de enmascarado temporal); justifica tratar el borrado de tramos como una técnica conocida, no inventada | no afirmar qué transformación "ganó" sin leer el texto completo |
| Lashgari et al. (2020) | revisión del aumento de datos para aprendizaje profundo sobre EEG | ídem |
| Park et al. (2019) | *time masking*: borrar bloques contiguos de tiempo de la entrada durante el entrenamiento (en habla) es el antecedente directo del aumento con huecos | es otro dominio (habla, espectrogramas) |
| DeVries y Taylor (2017) | enmascarar regiones contiguas de la entrada al entrenar mejora robustez y desempeño de redes convolucionales (resumen) | imágenes, no series temporales |
| Che et al. (2018) | pasar a la red un **indicador de faltante** (máscara) junto con la serie, en lugar de imputar, es un diseño establecido para series multivariadas con valores ausentes | GRU-D es recurrente; aquí la máscara entra como canal extra a una red convolucional |
| Lawhern et al. (2018) | arquitectura de EEGNet | ya citado en E1/E2 |

## 3. Referencias (APA 7, "y" antes del último autor)

Che, Z., Purushotham, S., Cho, K., Sontag, D., y Liu, Y. (2018). Recurrent neural networks for multivariate time series with missing values. *Scientific Reports, 8*(1), 6085. https://doi.org/10.1038/s41598-018-24271-9

DeVries, T., y Taylor, G. W. (2017). *Improved regularization of convolutional neural networks with Cutout* (arXiv:1708.04552). arXiv. https://arxiv.org/abs/1708.04552

Lashgari, E., Liang, D., y Maoz, U. (2020). Data augmentation for deep-learning-based electroencephalography. *Journal of Neuroscience Methods, 346*, 108885. https://doi.org/10.1016/j.jneumeth.2020.108885

Lawhern, V. J., Solon, A. J., Waytowich, N. R., Gordon, S. M., Hung, C. P., y Lance, B. J. (2018). EEGNet: A compact convolutional neural network for EEG-based brain-computer interfaces. *Journal of Neural Engineering, 15*(5), 056013. https://doi.org/10.1088/1741-2552/aace8c

Park, D. S., Chan, W., Zhang, Y., Chiu, C.-C., Zoph, B., Cubuk, E. D., y Le, Q. V. (2019). SpecAugment: A simple data augmentation method for automatic speech recognition. En *Proceedings of Interspeech 2019* (pp. 2613-2617). https://doi.org/10.21437/Interspeech.2019-2680

Rommel, C., Paillard, J., Moreau, T., y Gramfort, A. (2022). Data augmentation for learning predictive models on EEG: A systematic comparison. *Journal of Neural Engineering, 19*(6), 066020. https://doi.org/10.1088/1741-2552/aca220
