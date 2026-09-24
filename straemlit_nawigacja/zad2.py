import streamlit as st
import pandas as pd

def strona_glowna():
    st.title("Strona Głowna")
    st.write("Witaj w sklepie")

    st.info("Boczny panel - menu")
    st.metric("Licznik odwiedzin:", st.session_state.licznik_odwiedzin)

