import cv2
import numpy as np
from io import BytesIO
from pathlib import Path

def read_image(source):
    """
    Lee una imagen desde una ruta (`str`/`Path`) o desde un objeto file-like
    (que implemente `read()`) y la devuelve como un array de OpenCV (BGR).

    Parámetros:
    - source: ruta a archivo de imagen (`str` o `Path`) o un objeto file-like.
    """
    if isinstance(source, (str, Path)):
        with open(str(source), 'rb') as f:
            data = f.read()
    else:
        data = source.read()

    file_bytes = np.frombuffer(data, np.uint8)
    return cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

def save_image(img):
    """
    Guarda una imagen de OpenCV en un objeto BytesIO o en disco si se
    especifica `dest`.

    Parámetros:
    - img: array de imagen OpenCV
    - dest: ruta destino opcional (str/Path). Si se proporciona, guarda la
      imagen en disco y devuelve la ruta como string. Si no, devuelve un
      BytesIO con el contenido PNG.
    - ext: extensión/formato a usar (por ejemplo, '.png')
    """
    pass


def save_image(img, dest=None, ext='.png'):
    if dest is not None:
        dest_path = Path(dest)
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        # cv2.imwrite espera BGR arrays; si la imagen es de un solo canal,
        # imwrite funciona igual.
        cv2.imwrite(str(dest_path), img)
        return str(dest_path)

    _, buffer = cv2.imencode(ext, img)
    return BytesIO(buffer)