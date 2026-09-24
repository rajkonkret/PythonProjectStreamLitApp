import streamlit as st
import pandas as pd


def strona_glowna():
    st.title("Strona Głowna")
    st.write("Witaj w sklepie")

    st.info("Boczny panel - menu")
    st.metric("Licznik odwiedzin:", st.session_state.licznik_odwiedzin)


def strona_raport():
    st.title("Raport")
    st.write("Podsumowanie")

    dane = pd.DataFrame({
        "Produkt": ["Klawiatura", "Mysz", "Monitor"],
        "SPrzedaż": [1200, 450, 2100]
    })

    st.dataframe(dane, hide_index=True)
    st.bar_chart(dane.set_index("Produkt"))
