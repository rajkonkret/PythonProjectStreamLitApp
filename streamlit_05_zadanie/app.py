# Zbuduj panel kursanta.
# Sidebar:
# Kurs:
# Python
# Java
# SQL
# Główna część:
# Imię
# E-mail
# Poziom:
# początkujący
# średniozaawansowany
# zaawansowany
# Po przesłaniu formularza wyświetl:
# Dane kursanta
#
# Imię: ...
# E-mail: ...
# Kurs: ...
# Poziom: ...
# Wykorzystaj:
# st.sidebar
# st.form
# st.columns

import streamlit as st

st.set_page_config(page_title="Panel Kursanta", page_icon="")

with st.sidebar:
    st.header("Kursy")
    kurs = st.selectbox(
        "Wybierz kurs:",
        ["Python", "Java", 'SQL'],
        label_visibility="collapsed"
        # label_visibility="hidden"
    )

st.title("Panel Kursanta")

with st.form("formularz_kursanta"):
    col1, col2 = st.columns(2)

    with col1:
        imie = st.text_input("Imię")

    with col2:
        email = st.text_input("E-mail")

    poziom = st.selectbox(
        "Poziom",
        ["początkujący", "średniozaawansowany", "zaawansowany"]
    )

    submitted = st.form_submit_button("Wyślij")

if submitted:
    st.success("Dane zostały zapisane!")

    st.subheader("Dane kursanta")
    st.write(f"**Imię:** {imie}")
    st.write(f"**E-mail:** {email}")
    st.write(f"**Kurs:** {kurs}")
    st.write(f"**Poziom:** {poziom}")