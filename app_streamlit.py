import streamlit as st
from detector import analizar_texto

st.title("🕵️ Detector de Texto IA vs Humano")

# Entrada de texto
texto = st.text_area("✍️ Ingresa tu texto:", height=200)

# Parámetros
umbral = st.slider("⚖️ Umbral IA (%)", 0, 100, 70)
estilo = st.selectbox("😎 Estilo de humanización", ["casual", "profesional", "narrativo"])

if st.button("🔍 Analizar"):
    if texto.strip():
        # Llamamos a la función detector
        resultado = analizar_texto(texto)

        # Validar que siempre devuelve 3 elementos
        if len(resultado) == 3:
            prob_ia, prob_humano, razones = resultado

            st.subheader("📊 Resultados")
            st.write(f"**Probabilidad IA:** {prob_ia}%")
            st.write(f"**Probabilidad Humano:** {prob_humano}%")

            # Veredicto final según umbral
            if prob_ia >= umbral:
                st.error("⚠️ El texto parece generado por IA.")
            else:
                st.success("✅ El texto parece humano.")

            # Mostrar razones detectadas
            if razones:
                st.subheader("🔎 Evidencias encontradas:")
                for r in razones:
                    st.write(f"- {r}")
            else:
                st.write("No se encontraron patrones sospechosos.")

        else:
            st.error("❌ Error interno: la función no devolvió 3 valores.")
    else:
        st.warning("Por favor, ingresa un texto para analizar.")

