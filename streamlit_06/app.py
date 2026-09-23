import streamlit as st
import pandas as pd
# pip install openpyxl

st.set_page_config(
    page_title="Analiza pliku CSV",
    # layout="wide"
)
st.title("Analiza pliku CSV")

uploaded_file = st.file_uploader(
    "Wybierz plik CSV",
    type=["csv", "xlsx"]
)

if uploaded_file is None:
    st.info(
        "Wgraj plik CSV."
    )

    st.stop()

if uploaded_file.name.endswith(".csv"):
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_excel(uploaded_file)

st.dataframe(
    df,
    use_container_width=True
)
