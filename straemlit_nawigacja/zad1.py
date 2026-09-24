import streamlit as st


def raport():
    st.title("Raport")
    st.write("Tutaj umiesc podsumowanie danych")


def pomoc():
    st.title("Pomoc")
    st.write("Daty w CSV: RRRR-MM-DD")


strony = st.navigation(
    [
        st.Page(raport, title="Raport"),
        st.Page(pomoc, title="Pomoc")
    ]
)

strony.run()
