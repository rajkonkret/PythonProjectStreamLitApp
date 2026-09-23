import streamlit as st
import pandas as pd

st.title("Analiza pliku CSV")

uploaded_file = st.file_uploader(
    "Wybierz plik CSV",
    type=["csv"]
)