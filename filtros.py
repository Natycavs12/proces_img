import cv2
from pathlib import Path
from io_imagenes import read_image, save_image
from rembg import remove
from PIL import Image, ImageEnhance

def filtro_bilateral(file, kernel=5):
    """
    Aplica un filtro bilateral a la imagen recibida.
    """
    input_path = None
    if isinstance(file, (str, Path)):
        p = Path(file)
        if p.exists():
            input_path = p
        else:
            candidate = Path('img_input') / p
            if candidate.exists():
                input_path = candidate

    img = read_image(input_path or file)
    filtered = cv2.bilateralFilter(img, kernel, 75, 75)

    if input_path is not None:
        out_dir = Path('img_output')
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{input_path.stem}_bilateral.png"
        return save_image(filtered, dest=out_path)

    return save_image(filtered)

def mejorar_contraste(file):
    """
    Mejora el contraste de la imagen recibida.
    """
    input_path = None
    if isinstance(file, (str, Path)):
        p = Path(file)
        if p.exists():
            input_path = p
        else:
            candidate = Path('img_input') / p
            if candidate.exists():
                input_path = candidate
    img = read_image(input_path or file)
    # Convertir a PIL Image para usar ImageEnhance
    img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    contraste = ImageEnhance.Contrast(img_pil).enhance(2.0)
    if input_path is not None:
        out_dir = Path('img_output')
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{input_path.stem}_contraste.png"
        return save_image(contraste, dest=out_path)
    return save_image(contraste)

def filtro_gaussiano(file, kernel=5):
    """
    Aplica filtro gaussiano a la imagen recibida.
    """
    input_path = None
    if isinstance(file, (str, Path)):
        p = Path(file)
        if p.exists():
            input_path = p
        else:
            candidate = Path('img_input') / p
            if candidate.exists():
                input_path = candidate

    img = read_image(input_path or file)
    filtered = cv2.GaussianBlur(img, (kernel, kernel), 0)

    if input_path is not None:
        out_dir = Path('img_output')
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{input_path.stem}_gaussian.png"
        return save_image(filtered, dest=out_path)

    return save_image(filtered)

def to_grayscale(file):
    """
    Convierte a escala de grises la imagen recibida.
    """
    # Resolver ruta de entrada si se pasa solo nombre
    input_path = None
    if isinstance(file, (str, Path)):
        p = Path(file)
        if p.exists():
            input_path = p
        else:
            candidate = Path('img_input') / p
            if candidate.exists():
                input_path = candidate

    img = read_image(input_path or file)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Si tenemos ruta de entrada, escribir en img_output
    if input_path is not None:
        out_dir = Path('img_output')
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{input_path.stem}_gray.png"
        return save_image(gray, dest=out_path)

    return save_image(gray)

def detect_edges(file):
    """
    Detecta y muestra los bordes en la imagen recibida.
    """
    input_path = None
    if isinstance(file, (str, Path)):
        p = Path(file)
        if p.exists():
            input_path = p
        else:
            candidate = Path('img_input') / p
            if candidate.exists():
                input_path = candidate

    img = read_image(input_path or file)
    edges = cv2.Canny(img, 100, 200)

    if input_path is not None:
        out_dir = Path('img_output')
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{input_path.stem}_edges.png"
        return save_image(edges, dest=out_path)

    return save_image(edges)

def aplicar_blur(file, kernel=5):
    """Aplica desenfoque gaussiano.

    Args:
        file: Archivo de la imagen.
        kernel: Tamaño del kernel gaussiano.

    Returns:
        Imagen suavizada.
    """
    input_path = None
    if isinstance(file, (str, Path)):
        p = Path(file)
        if p.exists():
            input_path = p
        else:
            candidate = Path('img_input') / p
            if candidate.exists():
                input_path = candidate

    img = read_image(input_path or file)
    blurred = cv2.blur(img, (kernel, kernel))

    if input_path is not None:
        out_dir = Path('img_output')
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{input_path.stem}_blur.png"
        return save_image(blurred, dest=out_path)

    return save_image(blurred)

def remove_background(file):
    """
    Elimina el fondo de la imagen ingresada.
    """
    # img = read_image(file)
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # _, mask = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY_INV)
    # wobg = cv2.bitwise_and(img, img, mask=mask)
    # return save_image(wobg)
    #-------------------------
    input_path = None
    if isinstance(file, (str, Path)):
        p = Path(file)
        if p.exists():
            input_path = p
        else:
            candidate = Path('img_input') / p
            if candidate.exists():
                input_path = candidate

    input_img = read_image(input_path or file)
    output_img = remove(input_img)

    if input_path is not None:
        out_dir = Path('img_output')
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{input_path.stem}_nobg.png"
        return save_image(output_img, dest=out_path)

    return save_image(output_img)