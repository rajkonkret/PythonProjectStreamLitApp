import streamlit as st

st.set_page_config(page_title="Sklep App - Home", layout="centered")

st.title("Strona Główna")
st.write("Witaj w panelu zarządzania sklepem!")

if "licznik_odwiedzin" not in st.session_state:
    st.session_state.licznik_odwiedzin = 1
else:
    st.session_state.licznik_odwiedzin += 1

st.info("Użyj bocznego menu po lewej stronie, aby przejśc do podstron")
st.metric("Odwiedzenai:", st.session_state.licznik_odwiedzin)
