import streamlit as st

st.set_page_config(page_title="Ustawienia")

st.title("Ustawienia Systemowe")

waluta = st.selectbox("Waluta:", ["PLN", "EUR", "USD"])
tryb_ciemny = st.toggle("Wymuś tryb ciemny", value=False)

if st.button("Zapisz ustawienai"):
    st.success(F"Zapisano! Wybrana waluta: {waluta}")

if "licznik_odwiedzin" not in st.session_state:
    st.session_state.licznik_odwiedzin = 1
else:
    st.session_state.licznik_odwiedzin += 1
