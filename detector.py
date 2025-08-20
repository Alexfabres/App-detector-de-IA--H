import re

def analizar_texto(texto):
    razones = []
    score_ia = 0

    # Longitud del texto
    if len(texto.split()) > 80:
        score_ia += 20
        razones.append("Texto muy largo y estructurado, típico de IA.")

    # Palabras formales
    if re.search(r"(optimizar|eficiencia|proceso|herramienta|dimensiones|estructurado)", texto.lower()):
        score_ia += 30
        razones.append("Lenguaje técnico o académico detectado.")

    # Oraciones similares
    frases = [f.strip() for f in texto.split(".") if f.strip()]
    if len(frases) > 3 and max(len(f.split()) for f in frases) - min(len(f.split()) for f in frases) < 5:
        score_ia += 30
        razones.append("Oraciones con longitudes muy similares.")

    prob_ia = min(100, score_ia)
    prob_humano = 100 - prob_ia

    return prob_ia, prob_humano, razones

