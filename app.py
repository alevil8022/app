import streamlit as st
import pandas as pd
import io

st.set_page_config(layout="wide", page_title="CSV a Excel Converter")

st.markdown(
    """
    <style>
    .st-emotion-cache-18ni7ap {
        width: 100%;
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 1rem;
        padding-right: 1rem;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .st-emotion-cache-10o5j5t {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('🔥 Convertidor de :blue[CSV a Excel] 🔥')
st.divider()

uploaded_file = st.file_uploader("Sube tu archivo CSV", type=["csv"])
if uploaded_file is not None:
    try:
        # Lee el archivo CSV de la memoria
        df = pd.read_csv(uploaded_file, skiprows=3)

        # Genera el archivo Excel en la memoria
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False)
        output.seek(0)

        # Muestra el botón de descarga
        st.success("¡Archivo CSV procesado con éxito!")
        st.download_button(
            label="Descargar archivo Excel",
            data=output,
            file_name="archivo_salida.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    except Exception as e:
        st.error(f"Ocurrió un error al procesar el archivo: {e}")
