import cv2
import numpy as np
import os
from io_imagenes import read_image


class diagnosticar_imagen:
    """Luego de un exhaustivo análisis llegamos a la conclusión de que la mejor estructura para llevar adelante este ejercicio, era modulariarlo en funciones.
    De esta forma, cada función se encarga de analizar un aspecto específico de la imagen (brillo, contraste, ruido, etc.) y acumula los resultados en listas de diagnósticos y sugerencias. Al final, se imprime un resumen completo con métricas cuantitativas y recomendaciones de corrección."""

    def __init__(self, ruta_imagen):
        """
        Analiza una imagen y prepara estructuras internas.
        """
        self.ruta_imagen = ruta_imagen
        self.img = read_image(self.ruta_imagen)
        if self.img is None:
            raise FileNotFoundError(f"No se pudo leer la imagen: {ruta_imagen}")
        self.img_rgb = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        self.img_gris = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.img_hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
        self.diagnosticos = []
        self.sugerencias = []
        self.metricas = {}

        # Ejecutar análisis
        self.analizar_brillo()
        self.analizar_contraste()
        self.analizar_ruido()
        self.analizar_nitidez()
        self.analizar_saturacion()
        self.analizar_distribucion_tonal()
        self.analizar_zonas_saturadas()

    def analizar_brillo(self):
        # ─────────────────────────────────────────────
        # 1. BRILLO
        #    Promedio de píxeles en escala de grises.
        #    0 = negro total | 255 = blanco total
        #    Rango saludable: 85 – 170
        # ─────────────────────────────────────────────
        brillo = float(self.img_gris.mean())
        self.metricas["brillo_promedio"] = round(brillo, 2)

        if brillo < 50:
            self.diagnosticos.append("🔴 Imagen MUY oscura (brillo crítico)")
            self.sugerencias.append("Aplicar corrección gamma agresiva o ecualización de histograma (cv2.equalizeHist)")
        elif brillo < 85:
            self.diagnosticos.append("🟡 Imagen subexpuesta (brillo bajo)")
            self.sugerencias.append("Aumentar brillo con cv2.convertScaleAbs(self.img, alpha=1.2, beta=30)")
        elif brillo > 200:
            self.diagnosticos.append("🔴 Imagen MUY sobreexpuesta (brillo crítico)")
            self.sugerencias.append("Reducir brillo con cv2.convertScaleAbs(self.img, alpha=0.7, beta=-30)")
        elif brillo > 170:
            self.diagnosticos.append("🟡 Imagen sobreexpuesta (brillo alto)")
            self.sugerencias.append("Reducir exposición con cv2.convertScaleAbs(self.img, alpha=0.85, beta=-15)")
        else:
            self.diagnosticos.append("✅ Brillo adecuado")

    def analizar_contraste(self):
        # ─────────────────────────────────────────────
        # 2. CONTRASTE
        #    Desviación estándar de los píxeles en grises.
        #    Bajo contraste = píxeles muy similares entre sí
        #    Rango saludable: 40 – 110
        # ─────────────────────────────────────────────
        contraste = float(self.img_gris.std())
        self.metricas["contraste_std"] = round(contraste, 2)

        if contraste < 20:
            self.diagnosticos.append("🔴 Contraste muy bajo (imagen plana/gris)")
            self.sugerencias.append("Aplicar ecualización CLAHE: clahe = cv2.createCLAHE(clipLimit=3.0); clahe.apply(self.img_gris)")
        elif contraste < 40:
            self.diagnosticos.append("🟡 Contraste bajo")
            self.sugerencias.append("Mejorar contraste con cv2.convertScaleAbs(self.img, alpha=1.5, beta=0)")
        elif contraste > 110:
            self.diagnosticos.append("🟡 Contraste muy alto (puede perder detalle en sombras/luces)")
            self.sugerencias.append("Aplicar compresión tonal o reducir alpha en convertScaleAbs")
        else:
            self.diagnosticos.append("✅ Contraste adecuado")

    def analizar_ruido(self):
        # ─────────────────────────────────────────────
        # 3. RUIDO (Variación de alta frecuencia)
        #    Se detecta con el Laplaciano: mide bordes abruptos.
        #    Si la varianza es MUY alta en zonas uniformes → ruido
        #    Umbral orientativo: varianza > 800 en zona lisa = ruido
        # ─────────────────────────────────────────────
        laplaciano    = cv2.Laplacian(self.img_gris, cv2.CV_64F)
        var_laplaciano = laplaciano.var()
        # Guardar varianza también en el objeto para uso en otros métodos
        self.var_laplaciano = float(var_laplaciano)
        self.metricas["varianza_laplaciano"] = round(self.var_laplaciano, 2)

        # Estimación de ruido en zona plana (centro pequeño de la imagen)
        h, w = self.img_gris.shape
        zona_plana = self.img_gris[h//2 - 20 : h//2 + 20, w//2 - 20 : w//2 + 20]
        ruido_estimado = float(zona_plana.std())
        self.metricas["ruido_estimado_zona_central"] = round(ruido_estimado, 2)

        if ruido_estimado > 25:
            self.diagnosticos.append("🔴 Ruido alto detectado (variación fuerte en zonas uniformes)")
            self.sugerencias.append("Aplicar filtro Gaussiano: cv2.GaussianBlur(self.img, (5,5), 0)")
            self.sugerencias.append("O filtro bilateral para preservar bordes: cv2.bilateralFilter(self.img, 9, 75, 75)")
        elif ruido_estimado > 12:
            self.diagnosticos.append("🟡 Ruido moderado")
            self.sugerencias.append("Aplicar suavizado leve: cv2.GaussianBlur(self.img, (3,3), 0)")
        else:
            self.diagnosticos.append("✅ Nivel de ruido aceptable")

    def analizar_nitidez(self):
        # ─────────────────────────────────────────────
        # 4. DESENFOQUE (Nitidez)
        #    El Laplaciano también mide nitidez:
        #    varianza BAJA → imagen desenfocada (pocos bordes)
        #    varianza ALTA → imagen nítida (muchos bordes)
        #    Umbral orientativo: < 100 = desenfocada
        # ─────────────────────────────────────────────
        self.metricas["nitidez_varianza"] = round(float(self.var_laplaciano), 2)

        if self.var_laplaciano < 50:
            self.diagnosticos.append("🔴 Imagen muy desenfocada (pérdida severa de nitidez)")
            self.sugerencias.append("Aplicar enfoque: kernel = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]); cv2.filter2D(self.img,-1,kernel)")
        elif self.var_laplaciano < 100:
            self.diagnosticos.append("🟡 Imagen ligeramente desenfocada")
            self.sugerencias.append("Aplicar Unsharp Mask o cv2.addWeighted para realzar bordes")
        else:
            self.diagnosticos.append("✅ Nitidez adecuada")

    def analizar_saturacion(self):
        # ─────────────────────────────────────────────
        # 5. SATURACIÓN DE COLOR
        #    Canal S del espacio HSV (0 = gris, 255 = color puro)
        #    Rango saludable: 60 – 180
        # ─────────────────────────────────────────────
        saturacion = float(self.img_hsv[:, :, 1].mean())
        self.metricas["saturacion_promedio"] = round(saturacion, 2)

        if saturacion < 20:
            self.diagnosticos.append("🟡 Imagen desaturada (casi en escala de grises)")
            self.sugerencias.append("Aumentar saturación en HSV: img_hsv[:,:,1] = cv2.add(img_hsv[:,:,1], 60)")
        elif saturacion > 200:
            self.diagnosticos.append("🟡 Saturación excesiva (colores artificiales)")
            self.sugerencias.append("Reducir saturación para naturalidad")
        else:
            self.diagnosticos.append("✅ Saturación de color adecuada")

    def analizar_distribucion_tonal(self):
        # ─────────────────────────────────────────────
        # 6. DISTRIBUCIÓN TONAL (Histograma)
        #    ¿Los píxeles están concentrados en sombras, medios tonos o luces?
        #    Se divide el rango 0-255 en tres zonas iguales
        # ─────────────────────────────────────────────
        hist = cv2.calcHist([self.img_gris], [0], None, [256], [0, 256]).flatten()
        total = hist.sum()

        pct_sombras    = hist[:85].sum()  / total * 100   # píxeles oscuros
        pct_medios     = hist[85:170].sum() / total * 100  # medios tonos
        pct_luces      = hist[170:].sum() / total * 100    # píxeles claros

        self.metricas["distribucion_tonal"] = {
            "sombras_%": round(pct_sombras, 1),
            "medios_%":  round(pct_medios, 1),
            "luces_%":   round(pct_luces, 1)
        }

        if pct_sombras > 70:
            self.diagnosticos.append("🟡 Histograma cargado en sombras (imagen muy oscura en la mayoría)")
            self.sugerencias.append("Ecualizar histograma: cv2.equalizeHist(self.img_gris)")
        elif pct_luces > 70:
            self.diagnosticos.append("🟡 Histograma cargado en luces (sobreexposición generalizada)")
            self.sugerencias.append("Aplicar corrección gamma < 1: img_corr = np.power(img/255, 1.5) * 255")
        elif pct_medios > 60:
            self.diagnosticos.append("✅ Distribución tonal balanceada (mayoría en medios tonos)")
        else:
            self.diagnosticos.append("✅ Distribución tonal variada")

    def analizar_zonas_saturadas(self):
        # ─────────────────────────────────────────────
        # 7. ZONAS SATURADAS (recorte de histograma)
        #    Píxeles en 0 (negro puro) o 255 (blanco puro) indican
        #    pérdida irreversible de información (clipping)
        # ─────────────────────────────────────────────
        pct_negros  = float((self.img_gris == 0).sum())   / self.img_gris.size * 100
        pct_blancos = float((self.img_gris == 255).sum()) / self.img_gris.size * 100
        self.metricas["clipping_negros_%"]  = round(pct_negros, 2)
        self.metricas["clipping_blancos_%"] = round(pct_blancos, 2)

        if pct_negros > 5:
            self.diagnosticos.append(f"🟡 {pct_negros:.1f}% de píxeles completamente negros (pérdida en sombras)")
            self.sugerencias.append("Zona irreversible: solo se puede estimar con inpainting")
        if pct_blancos > 5:
            self.diagnosticos.append(f"🟡 {pct_blancos:.1f}% de píxeles completamente blancos (pérdida en luces)")
            self.sugerencias.append("Reducir exposición en captura o aplicar tone mapping")

    def resumen(self):
        # ─────────────────────────────────────────────
        # RESUMEN IMPRESO
        # ─────────────────────────────────────────────
        print("=" * 55)
        print("   DIAGNÓSTICO DE IMAGEN")
        print("=" * 55)
        print(f"  Archivo : {self.ruta_imagen}")
        print(f"  Tamaño  : {self.img_gris.shape[1]} x {self.img_gris.shape[0]} px\n")

        print("── MÉTRICAS ──────────────────────────────────────────")
        print(f"  Brillo promedio      : {self.metricas['brillo_promedio']} / 255")
        print(f"  Contraste (std)      : {self.metricas['contraste_std']}")
        print(f"  Nitidez (var. lap.)  : {self.metricas['nitidez_varianza']}")
        print(f"  Ruido zona central   : {self.metricas['ruido_estimado_zona_central']}")
        print(f"  Saturación promedio  : {self.metricas['saturacion_promedio']} / 255")
        dist = self.metricas['distribucion_tonal']
        print(f"  Distribución tonal   : sombras {dist['sombras_%']}% | "
            f"medios {dist['medios_%']}% | luces {dist['luces_%']}%")
        print(f"  Clipping negro/blanco: {self.metricas['clipping_negros_%']}% / {self.metricas['clipping_blancos_%']}%")

        print("\n── DIAGNÓSTICO ───────────────────────────────────────")
        for d in self.diagnosticos:
            print(f"  {d}")

        print("\n── SUGERENCIAS DE CORRECCIÓN ─────────────────────────")
        for i, s in enumerate(self.sugerencias, 1):
            print(f"  {i}. {s}")

        print("=" * 55)

        return {"metricas": self.metricas, "diagnosticos": self.diagnosticos, "sugerencias": self.sugerencias}

# ── USO ──────────────────────────────────────────────────
if __name__ == "__main__":
    ruta = "mi_foto.jpg"
    diag = diagnosticar_imagen(ruta)
    resultado = diag.resumen()
    # `resumen` ya imprime en pantalla; `resultado` contiene el dict
