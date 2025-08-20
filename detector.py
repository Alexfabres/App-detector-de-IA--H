# detector.py
import re

def analizar_texto(texto):
    razones = []
    score_ia = 0
    palabras = texto.split()

    # ----------------------------
    # 1. Longitud del texto
    # ----------------------------
    if len(palabras) > 150:
        score_ia += 20
        razones.append("Texto muy largo y estructurado, típico de IA.")
    elif len(palabras) < 20:
        score_ia -= 10  # textos muy cortos suelen ser humanos
        razones.append("Texto breve, más común en escritura humana.")

    # ----------------------------
    # 2. Repetición de palabras/frases
    # ----------------------------
    repetidas = [p for p in palabras if palabras.count(p) > 3]
    if len(set(repetidas)) > 3:
        score_ia += 15
        razones.append("Repetición notable de palabras o frases.")

    # ----------------------------
    # 3. Vocabulario técnico / académico
    # ----------------------------
    if re.search(r"(optimizar|eficiencia|proceso|herramienta|dimensiones|estructurado|implementación|estrategia|metodología)", texto.lower()):
        score_ia += 20
        razones.append("Lenguaje técnico/abstracto característico de IA.")

    # ----------------------------
    # 4. Longitud de las oraciones (uniformidad)
    # ----------------------------
    frases = [f.strip() for f in texto.split(".") if f.strip()]
    if len(frases) > 3:
        longitudes = [len(f.split()) for f in frases]
        if max(longitudes) - min(longitudes) < 6:
            score_ia += 15
            razones.append("Las oraciones tienen longitudes muy similares.")

    # ----------------------------
    # 5. Complejidad sintáctica
    # ----------------------------
    if any(c in texto for c in [";", ":", "—"]):
        score_ia += 10
        razones.append("Uso de estructuras complejas y conectores, típico de IA.")

    # ----------------------------
    # 6. Palabras poco naturales o repetitivas
    # ----------------------------
    unnatural = ["en este contexto", "de manera general", "es importante destacar", "en conclusión"]
    if any(phrase in texto.lower() for phrase in unnatural):
        score_ia += 15
        razones.append("Frases prefabricadas detectadas, comunes en IA.")

    # ----------------------------
    # 7. Diversidad léxica
    # ----------------------------
    vocabulario_unico = len(set(palabras))
    if vocabulario_unico / len(palabras) < 0.35:  # poca variedad
        score_ia += 15
        razones.append("Poca diversidad léxica (palabras repetidas).")

    # ----------------------------
    # 8. Balance final
    # ----------------------------
    prob_ia = min(100, max(0, score_ia))
    prob_humano = 100 - prob_ia

    return prob_ia, prob_humano, razones
