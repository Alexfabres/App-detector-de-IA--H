import re

def analizar_texto(texto):
    """
    Analiza el texto y devuelve un % de IA, % de humano y razones.
    (Versión simulada, deberías conectar con un modelo real si quieres más precisión)
    """
    razones = []
    score_ia = 0

    # Regla 1: Oraciones repetitivas
    if len(set(texto.split("."))) < len(texto.split(".")) * 0.7:
        score_ia += 20
        razones.append("Repetición excesiva de frases.")

    # Regla 2: Vocabulario demasiado formal
    if re.search(r"(optimizar|eficiencia|algoritmo|procesos)", texto.lower()):
        score_ia += 30
        razones.append("Lenguaje técnico/formal característico de IA.")

    # Regla 3: Poca variación en la longitud de oraciones
    longitudes = [len(p.split()) for p in texto.split(".") if p.strip()]
    if max(longitudes, default=1) - min(longitudes, default=1) < 5:
        score_ia += 20
        razones.append("Poca variación en la longitud de oraciones.")

    prob_ia = min(100, score_ia)
    prob_humano = 100 - prob_ia

    return prob_ia, prob_humano, razones
