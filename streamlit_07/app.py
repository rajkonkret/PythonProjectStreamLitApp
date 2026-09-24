import streamlit as st

st.title("Licznik sesji")

if "licznik" not in st.session_state:
    st.session_state.licznik = 0

if st.button("Dodaj", key="dodaj"):
    st.session_state.licznik += 1

st.metric("Kliknięcia", st.session_state.licznik)