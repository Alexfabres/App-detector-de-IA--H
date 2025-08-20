import random

def humanizar_texto(texto, estilo="casual"):
    """
    Reescribe el texto para que suene más humano en diferentes estilos.
    """
    frases = texto.split(". ")
    nuevas_frases = []

    for frase in frases:
        if not frase.strip():
            continue

        if estilo == "casual":
            frase = frase.replace("algoritmo", "método").replace("predicción", "idea aproximada")
            nuevas_frases.append(f"{frase}, como lo diría cualquiera en una conversación.")
        
        elif estilo == "formal":
            nuevas_frases.append(f"En este contexto, {frase.lower()}.")

        elif estilo == "narrativo":
            nuevas_frases.append(f"Imagina esto: {frase.lower()}.")

        elif estilo == "periodístico":
            nuevas_frases.append(f"Según lo observado, {frase.lower()}.")

        else:
            nuevas_frases.append(frase)

    return " ".join(nuevas_frases)
