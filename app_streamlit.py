import streamlit as st
from app import generar_reporte_completo

st.set_page_config(page_title="Detector & Humanizador IA", page_icon="🤖", layout="centered")

st.title("📝 Detector y Humanizador de Texto IA")
st.markdown("Analiza un texto, detecta si fue escrito por IA y humanízalo en el estilo que prefieras.")

texto = st.text_area("✍️ Ingresa tu texto:", height=200)
umbral = st.slider("⚖️ Umbral IA (%)", 0, 100, 70)
estilo = st.selectbox("🎨 Estilo de humanización", ["casual", "formal", "narrativo", "periodístico"])

if st.button("🔎 Analizar"):
    reporte = generar_reporte_completo(texto, umbral_ia=umbral, estilo=estilo)

    if "error" in reporte:
        st.error(reporte["error"])
    else:
        st.subheader("📊 Resultados de detección")
        st.write(f"**Probabilidad IA:** {reporte['prob_ia']}%")
        st.write(f"**Probabilidad Humano:** {reporte['prob_humano']}%")
        
        st.write("**Razones de la detección:**")
        for razon in reporte['razones']:
            st.write(f"- {razon}")

        if reporte['texto_humanizado']:
            st.subheader("✍️ Texto Humanizado")
            st.write(reporte['texto_humanizado'])
