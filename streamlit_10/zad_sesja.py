import streamlit as st

st.title("Licznik sesji")

if "licznik" not in st.session_state:
    st.session_state.licznik = 0


def wyzeruj():
    st.session_state.licznik = 0


st.metric("Licznik:", st.session_state.licznik)

st.button("Wyzeruj", on_click=wyzeruj)

if st.button("Zwiększ"):
    st.session_state.licznik += 1
    st.rerun()
