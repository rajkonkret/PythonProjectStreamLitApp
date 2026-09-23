import streamlit as st

st.title("Rejestracja")

with st.form("formularz"):

    name = st.text_input("Imię")

    email = st.text_input("E-mail")

    age = st.number_input(
        "Wiek",
        min_value=18,
        max_value=100
    )

    submitted = st.form_submit_button(
        "Wyślij"
    )

if submitted:
    st.success("Formularz wysłany")

    st.write("Imię:", name)
    st.write("E-mail:", email)
    st.write("Wiek:", age)