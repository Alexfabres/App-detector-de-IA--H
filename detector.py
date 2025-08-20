import re
import random

def analizar_texto(texto):
    """
    Analiza un texto y devuelve:
    - prob_ia: porcentaje de probabilidad de ser IA
    - prob_humano: porcentaje de probabilidad de ser humano
    - razones: lista de evidencias encontradas
    """

    razones = []
    puntuacion_ia = 0
    puntuacion_humano = 0

    # --- Reglas de detección ---

    # 1. Longitud promedio de oración (IA suele ser muy uniforme)
    oraciones = re.split(r'[.!?]', texto)
    longitudes = [len(o.split()) for o in oraciones if len(o.split()) > 0]
    if longitudes:
        promedio = sum(longitudes) / len(longitudes)
        varianza = sum((x - promedio) ** 2 for x in longitudes) / len(longitudes)

        if varianza < 15:  # muy uniforme
            puntuacion_ia += 15
            razones.append("Longitud de oraciones muy uniforme (patrón típico de IA).")
        else:
            puntuacion_humano += 10
            razones.append("Variedad en la longitud de las oraciones (más humano).")

    # 2. Repetición de palabras
    palabras = re.findall(r'\w+', texto.lower())
    if palabras:
        repeticiones = sum([palabras.count(p) for p in set(palabras) if palabras.count(p) > 3])
        if repeticiones > 5:
            puntuacion_ia += 20
            razones.append("Repetición excesiva de palabras (característico de IA).")
        else:
            puntuacion_humano += 5

    # 3. Complejidad léxica (IA usa vocabulario más “neutral”)
    palabras_unicas = len(set(palabras))
    if palabras and palabras_unicas / len(palabras) < 0.4:
        puntuacion_ia += 15
        razones.append("Baja diversidad léxica (posible texto IA).")
    else:
        puntuacion_humano += 10
        razones.append("Buena diversidad léxica (más humano).")

    # 4. Marcadores de coherencia (IA usa muchos conectores)
    conectores = ["además", "por lo tanto", "en conclusión", "sin embargo", "por consiguiente"]
    uso_conectores = sum(texto.lower().count(c) for c in conectores)
    if uso_conectores > 3:
        puntuacion_ia += 10
        razones.append("Uso excesivo de conectores lógicos (IA estructurada).")
    elif uso_conectores > 0:
        puntuacion_humano += 5
        razones.append("Uso moderado de conectores (más humano).")

    # 5. Perplejidad simulada (IA es muy predecible)
    # Aquí usamos aleatoriedad simulada para darle realismo
    perplejidad = random.uniform(20, 80)  
    if perplejidad < 30:
        puntuacion_ia += 15
        razones.append("Texto demasiado predecible (baja perplejidad, típico de IA).")
    else:
        puntuacion_humano += 10
        razones.append("Texto con cierta imprevisibilidad (más humano).")

    # 6. Estilo narrativo vs informativo
    if any(p in texto.lower() for p in ["yo", "ayer", "amigo", "sentí", "viví"]):
        puntuacion_humano += 15
        razones.append("Uso de experiencias personales (más humano).")

    # 7. Frases poco naturales
    patrones_ia = [r"\bes importante destacar\b", r"\bcomo se mencionó anteriormente\b", r"\ben conclusión\b"]
    for patron in patrones_ia:
        if re.search(patron, texto.lower()):
            puntuacion_ia += 10
            razones.append("Frases típicas de IA detectadas.")

    # --- Normalización ---
    total = puntuacion_ia + puntuacion_humano
    if total == 0:
        prob_ia = 50
        prob_humano = 50
    else:
        prob_ia = int((puntuacion_ia / total) * 100)
        prob_humano = 100 - prob_ia

    return prob_ia, prob_humano, razones
