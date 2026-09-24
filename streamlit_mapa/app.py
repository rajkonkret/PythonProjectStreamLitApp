import pandas as pd
import streamlit as st

st.title("Przykładowe punkty")

df = pd.DataFrame(
    {
        "lat": [52.23, 50.06, 54.35],
        "lon": [21.01, 19.94, 18.65],
        "miasto": ["Warszawa", "Kraków", "Gdańsk"]
    }
)

wybor = st.multiselect(
    "Miasta", df.miasto.tolist(),
    default=df.miasto.tolist()
)

st.map(df[df.miasto.isin(wybor)])
