Procesamiento de Imágenes con Python, Pillow, OpenCV, Pathlib y Rembg

Integrantes del equipo

- Barrón, Natalia
- Campos, Cecilia
- Gómez, Florencia
- Palma, Michelle

---

# Descripción del proyecto

Este proyecto implementa una herramienta modular de procesamiento digital de imágenes utilizando Python, Pillow, OpenCV y Rembg. 

A diferencia de un editor común, el programa primero realiza un **diagnóstico estadístico automático** de la imagen para evaluar su brillo, contraste, ruido y nitidez, recomendando al usuario qué mejoras aplicar a través de un menú interactivo.

El programa permite:
- Cargar imágenes desde el sistema de archivos de forma segura.
- Realizar un diagnóstico previo de la calidad de la imagen (brillo, contraste, ruido, nitidez, saturación y cortes de histograma).
- Convertir imágenes a escala de grises.
- Reducir ruido mediante suavizado Gaussiano, desenfoque de caja y Filtro Bilateral (que preserva los bordes).
- Detectar bordes utilizando el algoritmo de Canny.
- Mejorar el contraste de la imagen utilizando Pillow.
- Eliminar el fondo de forma automática utilizando la librería Rembg.
- Guardar los resultados finales en una carpeta específica.

---

# Tecnologías utilizadas

- Python
- OpenCV (`cv2`)
- Pillow (`PIL`)
- Rembg
- NumPy
- Pathlib
- argparse

---

# Estructura del proyecto

```text
procesamiento_imagenes/
│
├── main.py              # Orquestador, lee los comandos y muestra el menú
├── filtros.py           # Contiene los filtros (grises, desfoques, contraste, rembg)
├── deteccion.py         # Contiene la clase de diagnóstico de la imagen
├── io_imagenes.py       # Encargado de abrir y guardar los archivos
├── img_input/           # Carpeta para colocar las imágenes a procesar
├── img_output/          # Carpeta donde se guardan los resultados automáticos
├── conversaciones_ia/   # Carpeta obligatoria con los registros de uso de IA
└── README.md

```

---

# Cómo usar el programa

Para ejecutar el programa, se debe abrir la terminal y pasarle como argumento obligatorio la ruta de la imagen. También se pueden modificar los parámetros de los filtros de forma opcional.

### Ejemplo de uso básico:

```bash
python main.py img_input/tu_imagen.jpg

```

### Ejemplo usando parámetros opcionales:

* `--kernel`: Tamaño del filtro de desenfoque (por defecto es 5).
* `--umbral1` y `--umbral2`: Umbrales para la detección de bordes de Canny (por defecto 100 y 200).

```bash
python main.py img_input/tu_imagen.jpg --kernel 7 --umbral1 150 --umbral2 250

```

Al ejecutar el comando, el programa mostrará el diagnóstico técnico en la pantalla y desplegará un menú numérico para que elijas qué filtro aplicar.

---

```

```
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
- Rembg
- NumPy
- Pathlib
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

**
# Cómo usar el programa**

Para ejecutar el programa, se debe abrir la terminal y pasarle como argumento obligatorio la ruta de la imagen. También se pueden modificar los parámetros de los filtros de forma opcional.

### Ejemplo de uso básico:

```bash
python main.py img_input/tu_imagen.jpg

```

