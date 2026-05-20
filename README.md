# Procesamiento de Imágenes con Python, Pillow, OpenCV, Pathlib y Rembg

## Integrantes del equipo

- Barrón, Natalia
- Campos, Cecilia
- Gómez, Florencia
- Palma, Michelle

---

# Descripción del proyecto

Este proyecto implementa un pipeline básico de procesamiento digital de imágenes utilizando Python, Pillow y OpenCV.

El objetivo principal es aplicar distintas técnicas de procesamiento para mejorar la imagen, reducir ruido y detectar bordes y contornos presentes en los objetos.

El programa permite:

- cargar imágenes desde el sistema de archivos;
- convertir imágenes a escala de grises;
- reducir ruido mediante suavizado gaussiano;
- detectar bordes utilizando el algoritmo de Canny;
- detectar contornos sobre los objetos presentes;
- guardar resultados intermedios y finales;
- configurar parámetros desde línea de comandos.

---

# Tecnologías utilizadas

- Python
- OpenCV (`cv2`)
- Pillow (`PIL`)
- NumPy
- argparse

---

# Estructura del proyecto

```text
procesamiento_imagenes/
│
├── main.py
├── filtros.py
├── deteccion.py
├── io_imagenes.py
├── utils.py
├── output/
└── README.md
