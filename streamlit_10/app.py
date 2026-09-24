import streamlit as st
import time
import pandas as pd
import numpy as np

st.set_page_config(page_title="Streamlit: Istota Cache", layout="wide")

st.title("@st.cache_data")

st.divider()

def pobierz_dane_bez_cache(kategoria: str):
    time.sleep(2)
    np.random.seed(42)
    df = pd.DataFrame(
        {
            "Produkt": [f"{kategoria} #{i}" for i in range(1, 6)],
            "Cena": np.random.randint(50, 500, size=5),
            "Pobrano_o": time.strftime("%H:%M:%S")
        }
    )