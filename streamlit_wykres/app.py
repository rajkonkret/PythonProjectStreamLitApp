import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Dashboaard",
    layout="wide"
)

st.title("Dashboard")

np.random.seed(42)

df = pd.DataFrame({
    "data": pd.date_range(
        "2026-01-01",
        periods=200
    ),

    "region": np.random.choice(
        [
            "Warszawa",
            "Kraków",
            "Gdańsk",
            "Wrocław"
        ],
        200
    ),

    "produkt": np.random.choice(
        [
            "Laptop",
            "Telefon",
            "Tablet"
        ],
        200
    ),

    "sprzedaz": np.random.randint(
        1000,
        15000,
        200
    ),

    "koszty": np.random.randint(
        500,
        10000,
        200
    )
})

st.sidebar.header("Filtry")

region = st.sidebar.selectbox(
    "Region:",

    [
        "Wszystkie",
        "Warszawa",
        "Kraków",
        "Gdańsk",
        "Wrocław"
    ]
)

produkty = st.sidebar.multiselect(
    "Produkty:",
    options=df['produkt'].unique(),
    default=df['produkt'].unique()
)
