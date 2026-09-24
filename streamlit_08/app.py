import streamlit as st

st.set_page_config(page_title="Streamlit: Problem Sesji", layout="wide")

st.title("Problem przeładowania skryptu (rerun)")
st.write("""
W Streamlit za kazdyą zmianą plik jest wykonywany od początku""")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Zwykła zmienna")

    zwykly_licznik = 0

    if st.button("Zwiększ", key="btn_bad"):
        zwykly_licznik += 1

    st.metric(label="Wartość zwykłęgo licznika", value=zwykly_licznik)

    st.error(
        "Gdy skrypt rusza , wartość od 0"
    )

with col2:
    st.subheader("session_state")

    if "dobry_licznik" not in st.session_state:
        st.session_state.dobry_licznik = 0

    if st.button("Zwiększ (sesion_state)", key="btn_good"):
        st.session_state.dobry_licznik += 1

    st.metric(label="Wartość licznika w sesji", value=st.session_state.dobry_licznik)

    st.success(
        "działa z zapamiętaniem"
    )

st.divider()

st.subheader("Formularz wieloetapowy")

with st.expander("Kliknij aby rozwinąć"):
    st.write("Formularz")

    col_a, col_b = st.columns(2)

    with col_a:
        st.write("Przycisk w przycisku")
        if st.button("Krok 1"):
            imie = st.text_input("Twoje imię")
            if st.button('Zatwierdź'):
                st.write(f"Cześć {imie}!")
        st.caption("Po wpisaniu imienia formularz zniknie")

    with col_b:
        st.write("Prawidłowe podejście")

        if "krok" not in st.session_state:
            st.session_state.krok = 1

        if st.session_state.krok == 1:
            if st.button("Przejdz do kroku 2"):
                st.session_state.krok = 2
                st.rerun()

        if st.session_state.krok == 2:
            imie_poprawne = st.text_input("Twoje imię (w sesji):", key="user_name")
            if st.button("Zapisz i zakończ"):
                st.session_state.krok = 3
                st.rerun()

        if "user_name" not in st.session_state:
            st.session_state.user_name = ""

        if st.session_state.krok == 3:
            st.write(f"Cześć **{st.session_state.user_name}**!")
            if st.button("Zacznij od nowa"):
                st.session_state.krok = 1
                st.rerun()