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

minimalna_sprzedaz = st.sidebar.slider(
    "Minimalna sprzedaż:",
    min_value=0,
    max_value=15000,
    value=0,
    step=500
)

filtered_df = df.copy()


if region != "Wszystkie":
    filtered_df = filtered_df[
        filtered_df["region"] == region
    ]


filtered_df = filtered_df[
    filtered_df["produkt"].isin(produkty)
]


filtered_df = filtered_df[
    filtered_df["sprzedaz"] >= minimalna_sprzedaz
]
