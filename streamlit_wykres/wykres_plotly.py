import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    "region": [
        "Warszawa", "Warszawa",
        "Kraków", "Kraków",
        "Gdańsk", "Gdańsk"
    ],
    "produkt": [
        "Laptop", "Telefon",
        "Laptop", "Telefon",
        "Laptop", "Telefon"
    ],
    "sprzedaz": [
        12000, 18000,
        9000, 13000,
        11000, 10000
    ]
})

region = st.selectbox(
    "Wybierz region:",
    ["Wszystkie"] + list(df["region"].unique())
)

if region == "Wszystkie":
    filtered_df = df
else:
    filtered_df = df[df["region"] == region]

fig = px.bar(
    filtered_df,
    x="produkt",
    y="sprzedaz",
    color="produkt",
    title=f"Sprzedaż — {region}"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
