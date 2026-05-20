import argparse
from filtros import to_grayscale, detect_edges, aplicar_blur, remove_background,filtro_gaussiano, mejorar_contraste, filtro_bilateral
from deteccion import diagnosticar_imagen

if __name__ == "__main__":

    """
    # Módulo principal de programa
    ## Este módulo se encarga de:
    - leer los argumentos enviados por línea de comandos;
    - cargar la imageb indicada por el usuario;
    - ejecutar las dintintas técnicas/funciones de procesamiento de imágenes;
    - guardar los resultados intermedios y finales;

    ## Para pasar los argumentos por línea de comandos:
    obligarorio: ruta de la/s imagen/es a procesar
    opcional: umbrales para técnicas de segmentación, etc.

    ## Ejemplo de uso:
    ## python main.py imagen.jpg --kernel 5 --umbral1 100 --umbral2 200
    """
    parser = argparse.ArgumentParser(description="Argumentos para procesamiento de imágenes")

    parser.add_argument("imagen", help="Ruta de la imagen a procesar")
    parser.add_argument("--kernel", type=int, default=5, help="Tamaño del kernel gaussiano")
    parser.add_argument("--umbral1", type=int, default=100, help="Primer umbral para detección de bordes")
    parser.add_argument("--umbral2", type=int, default=200, help="Segundo umbral para detección de bordes")

    args = parser.parse_args()
    args.imagen = args.imagen.strip('"')  # Eliminar comillas si las hay
    print(f"ruta de imagen: {args.imagen}")

    # Decidimos realizar un análisis diagnóstico previo para determinar qué técnicas es la más conveniente aplicar; sin embargo, dejarle la decisión final al usuario.
    diag = diagnosticar_imagen(args.imagen)
    resultado = diag.resumen()

    try:
        opc = int(input("Seleccione la técnica a aplicar:\n1) Escala de grises\n2) Detección de bordes\n3) Desenfoque Alto\n4) Eliminar fondo\n5) Filtro Gaussiano (Desenfoque leve)\n6) Mejorar Contraste\n7) Filtro Bilateral\nOpción: "))
        if opc == 1:
            resultado = to_grayscale(args.imagen)
            print(f"Imagen en escala de grises guardada en: {resultado}")
        elif opc == 2:
            resultado = detect_edges(args.imagen)
            print(f"Imagen con bordes detectados guardada en: {resultado}")
        elif opc == 3:
            resultado = aplicar_blur(args.imagen, args.kernel)
            print(f"Imagen suavizada guardada en: {resultado}")
        elif opc == 4:
            resultado = remove_background(args.imagen)
            print(f"Imagen sin fondo guardada en: {resultado}")
        elif opc == 5:
            resultado = filtro_gaussiano(args.imagen, args.kernel)
            print(f"Imagen con filtro gaussiano aplicada guardada en: {resultado}")
        elif opc == 6:
            resultado = mejorar_contraste(args.imagen)
            print(f"Imagen con contraste mejorado guardada en: {resultado}")
        elif opc == 7:
            resultado = filtro_bilateral(args.imagen, args.kernel)
            print(f"Imagen con filtro bilateral aplicado guardada en: {resultado}")
    except ValueError:
        print("Opción no válida. Por favor, ingrese un número del 1 al 7.")
        exit(1)

        """En la práctica nos dimos cuenta que la función de diagnóstico nos sugería algunas mejoras o sugerencias de tecnicas que no teniamos implementadas previamente, como por ej. el contraste. Por lo tanto, decidimos agregar la función de mejora de contraste y dejarle la decisión final al usuario sobre qué técnica aplicar, aunque el diagnóstico le sugiera alguna en particular."""



"""
Pasos:
1) obtener o subir 1 o varias imagenes
2) aplicar tecnicas
3) guardar resultados intermedios y finales
4) por cli

Mejoras a implementar:
- poder combinar las distintas tecnicas (por ejemplo, aplicar filtro gaussiano y luego detección de bordes)
- agregar más técnicas de procesamiento de imágenes (por ejemplo, segmentación, detección de objetos, etc.)
"""