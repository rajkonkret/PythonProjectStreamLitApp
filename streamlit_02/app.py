import streamlit as st

st.title("Formularz użytkownika")

name = st.text_input(
    "Podaj swoje imię"
)

st.write("Wpisałeś:", name)

age = st.number_input(
    "Podaj wiek",
    min_value=0,
    max_value=130,
    value=18
)
st.write("Twój wiek:", age)

experience = st.slider(
    "Ile lat programujesz?",
    min_value=0,
    max_value=30,
    value=1
)

st.write("Lata:", experience)

language = st.selectbox(
    "Wybierz język programowania",
    [
        "Python",
        "Java",
        "C++",
        "JavaScript",
     ]
)