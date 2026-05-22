# Procesamiento de Imágenes con Python, Pillow, OpenCV, Pathlib y Rembg

## Integrantes del equipo
- Barrón, Natalia
- Campos, Cecilia
- Gómez, Florencia
- Palma, Michelle

---

## Descripción del proyecto

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

## Tecnologías utilizadas
- Python
- OpenCV (`cv2`)
- Pillow (`PIL`)
- Rembg
- NumPy
- Pathlib
- argparse

---

## Estructura del proyecto

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
```

---

## Cómo usar el programa

1. Abrir la terminal en la carpeta del proyecto.
2. Ejecutar el comando principal indicando la ruta de la imagen:

```bash
python main.py imagen.jpg --kernel 5 --umbral1 100 --umbral2 200
```

3. Observar el diagnóstico estadístico que aparecerá en la pantalla.
4. Seleccionar un número del menú (1 al 7) para elegir qué filtro aplicar.
5. Buscar la imagen procesada final dentro de la carpeta `img_output/`.

---

## Técnicas aplicadas

**Escala de grises**
Convierte la imagen a una versión en blanco y negro. Sirve como paso previo para muchos análisis, ya que simplifica la imagen eliminando la información de color y dejando solo la intensidad de la luz.

**Filtro Gaussiano (desenfoque leve)**
Suaviza la imagen de forma natural, dando más importancia a los píxeles cercanos al centro. Se usa para reducir ruido leve antes de aplicar otras técnicas, sin destruir demasiado los bordes.

**Desenfoque (Blur)**
Suaviza la imagen promediando los píxeles vecinos por igual. Es más agresivo que el gaussiano y se usa cuando se necesita un suavizado rápido sin importar tanto la pérdida de detalle.

**Filtro Bilateral**
Suaviza el ruido de la imagen pero respeta los bordes de los objetos. Es el filtro más inteligente de los tres: distingue entre zonas uniformes (donde aplica el suavizado) y bordes (donde no mezcla los píxeles).

**Mejora de contraste**
Aumenta la diferencia entre las zonas claras y oscuras de la imagen, haciendo que los objetos se vean con más definición y los detalles sean más nítidos.

**Detección de bordes (Canny)**
Marca los contornos de los objetos presentes en la imagen. Usa dos umbrales para decidir qué cambios de intensidad son bordes reales y cuáles son ruido, generando una imagen donde solo se ven las líneas de borde en blanco sobre fondo negro.

**Eliminación de fondo (Rembg)**
Detecta el objeto principal de la imagen y elimina el fondo automáticamente, dejando solo el sujeto con fondo transparente.

---

## Decisiones técnicas

**Diagnóstico previo antes de elegir la técnica**
Decidimos que el programa analice la imagen automáticamente antes de que el usuario elija qué hacer. Esto le permite ver métricas concretas (brillo, contraste, ruido, nitidez, saturación) y entender el estado real de la imagen antes de aplicar cualquier corrección.

**El usuario toma la decisión final**
Aunque el diagnóstico sugiere qué técnica aplicar, la elección final queda en manos del usuario. Lo hicimos así porque el algoritmo mide números pero no conoce el contexto: una foto nocturna puede parecer "muy oscura" para el programa pero estar perfecta artísticamente.

**Modularización del código**
Separamos el proyecto en varios archivos (`filtros.py`, `deteccion.py`, `io_imagenes.py`) para que cada uno se encargue de una cosa específica. Esto hace el código más fácil de leer, mantener y ampliar.

**Parámetros por línea de comandos**
Usamos `argparse` para que el usuario pueda ajustar el kernel y los umbrales sin tocar el código, haciendo el programa más flexible.

**Agregado de mejora de contraste**
Durante el desarrollo nos dimos cuenta de que el diagnóstico sugería correcciones de contraste que no teníamos implementadas, así que la agregamos. Esto refleja cómo el diagnóstico guió la evolución del proyecto.
```

---




