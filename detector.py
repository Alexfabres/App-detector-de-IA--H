# detector.py
import re
import math
import numpy as np

# --------------------------
# Funciones auxiliares
# --------------------------

def aproximar_perplexity(texto):
    """Calcula una aproximación simple de perplexity basada en frecuencia de palabras"""
    palabras = texto.split()
    if not palabras:
        return 0
    freqs = {}
    for w in palabras:
        freqs[w] = freqs.get(w, 0) + 1
    probs = [freqs[w] / len(palabras) for w in palabras]
    entropy = -sum(p * math.log2(p) for p in probs if p > 0)
    perplexity = 2 ** entropy
    return perplexity

def medir_burstiness(texto):
    """Mide la variación de perplexity entre frases"""
    frases = [f.strip() for f in texto.split(".") if f.strip()]
    if not frases:
        return 0
    perps = [aproximar_perplexity(fra) for fra in frases]
    return np.std(perps) / (np.mean(perps) + 1e-9)

# --------------------------
# Analizador principal
# --------------------------

def analizar_texto(texto):
    razones = []
    score_ia = 0
    palabras = texto.split()

    # 1. Longitud del texto
    if len(palabras) > 150:
        score_ia += 20
        razones.append("Texto muy largo y estructurado, típico de IA.")
    elif len(palabras) < 20:
        score_ia -= 10
        razones.append("Texto breve, más común en escritura humana.")

    # 2. Repetición de palabras
    repetidas = [p for p in palabras if palabras.count(p) > 3]
    if len(set(repetidas)) > 3:
        score_ia += 15
        razones.append("Repetición notable de palabras o frases.")

    # 3. Vocabulario técnico / académico
    if re.search(r"(optimizar|eficiencia|proceso|herramienta|dimensiones|estructurado|implementación|estrategia|metodología|evidencia|parámetro|análisis)", texto.lower()):
        score_ia += 20
        razones.append("Lenguaje técnico o académico detectado.")

    # 4. Oraciones con longitudes similares
    frases = [f.strip() for f in texto.split(".") if f.strip()]
    if len(frases) > 3:
        longitudes = [len(f.split()) for f in frases]
        if max(longitudes) - min(longitudes) < 6:
            score_ia += 15
            razones.append("Las oraciones tienen longitudes muy similares.")

    # 5. Sintaxis compleja
    if any(c in texto for c in [";", ":", "—"]):
        score_ia += 10
        razones.append("Uso de estructuras complejas, típico de IA.")

    # 6. Frases prefabricadas comunes en IA
    unnatural = ["en este contexto", "de manera general", "es importante destacar", "en conclusión", "cabe señalar"]
    if any(phrase in texto.lower() for phrase in unnatural):
        score_ia += 15
        razones.append("Frases prefabricadas detectadas, comunes en IA.")

    # 7. Diversidad léxica
    vocabulario_unico = len(set(palabras))
    if len(palabras) > 0 and vocabulario_unico / len(palabras) < 0.35:
        score_ia += 15
        razones.append("Poca diversidad léxica (palabras repetidas).")

    # 8. Métricas estilo GPTZero (Perplexity y Burstiness)
    perp = aproximar_perplexity(texto)
    burst = medir_burstiness(texto)

    if perp < 40:  # texto demasiado predecible
        score_ia += 20
        razones.append(f"Baja perplexity ({perp:.2f}): muy predecible, típico de IA.")
    elif perp > 150:  # humano suele tener más riqueza
        score_ia -= 10
        razones.append(f"Perplexity alta ({perp:.2f}): más riqueza lingüística, típico de humano.")

    if burst < 0.2:  # poca variación
        score_ia += 20
        razones.append(f"Burstiness baja ({burst:.2f}): poca variación en frases, típico de IA.")
    elif burst > 0.5:  # mucha variación
        score_ia -= 10
        razones.append(f"Burstiness alta ({burst:.2f}): variación natural en frases, típico de humano.")

    # --------------------------
    # Balance final
    # --------------------------
    prob_ia = min(100, max(0, score_ia))
    prob_humano = 100 - prob_ia

    return prob_ia, prob_humano, razones

