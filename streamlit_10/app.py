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
    return df


@st.cache_data
def pobierz_dane_z_cache(kategoria: str):
    time.sleep(2)
    np.random.seed(42)
    df = pd.DataFrame(
        {
            "Produkt": [f"{kategoria} #{i}" for i in range(1, 6)],
            "Cena": np.random.randint(50, 500, size=5),
            "Pobrano_o": time.strftime("%H:%M:%S")
        }
    )
    return df


st.subheader("Zmiana na na stronie wymusza rerun")
col_ctrl1, col_ctrl2 = st.columns([1, 2])

with col_ctrl1:
    wybrana_kategoria = st.selectbox("Kategorie:", ["Elektronika", "Książki", "AGD"])

with col_ctrl2:
    suwak = st.slider("Przesuń", 0, 100, 2)

st.divider()

col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Bez Cache (zwykłą funkcja)")
    st.caption("Blokuje aplikację na 2 sekundy")

    start_time = time.time()
    with st.spinner("Pobieranie danych (bez cache)"):
        dane_bez = pobierz_dane_bez_cache(wybrana_kategoria)
    czas_bez = time.time() - start_time

    st.metric(label="Czas wykonania zapytania:", value=f"{czas_bez:.2f}", delta=f"{czas_bez:.2f}", delta_color="inverse")
    st.dataframe(dane_bez, hide_index=True)
    st.error("Kazde zapytanie 2s")