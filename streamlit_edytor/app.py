import pandas as pd
import streamlit as st

start = pd.DataFrame({
    "produkt": ["Notes", "Kubek"],
    "sztuki": [3, 2]
})

zmiany = st.data_editor(
    start, num_rows="fixed", key="edycja"
)

if st.button("Sprawdź sumę"):
    if zmiany["sztuki"].isna().any():
        st.error("Uzupełnij liczbę sztuk.")
    elif (zmiany['sztuki'] < 0).any():
        st.error("Liczba nie może być ujemna.")
    else:
        st.write("Suma", zmiany['sztuki'].sum())