from pathlib import Path
import hashlib

import pandas as pd
import streamlit as st

from data_utils import load_sales, filter_sales, export_csv

st.set_page_config(page_title="Dashboard Sprzedązy", layout='wide')
st.title("Dashboard sprzedaży sklepu")
st.markdown("Wczytaj dane i filtruj")

with st.sidebar:
    st.header("Dane i filtry")
    source = st.radio("Źródło danych", ["Dane przykłądowe", "Własny plik CSV"])

    uploaded = st.file_uploader(
        "Wczytaj plik CSV",
        type=['csv']
    ) if source == "Własny plik CSV" else None
    sample = Path(__file__).parent / 'sprzedaz_przyklad.csv'
