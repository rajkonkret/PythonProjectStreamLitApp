import streamlit as st

st.title("Demonstracja rozmowy")

if "historia" not in st.session_state:
    st.session_state.historia = []

for rola, tekst in st.session_state.historia:
    st.chat_message(rola).write(tekst)

if pytanie := st.chat_input("Napisz wiadomość:"):
    # wysłane pytanie do LLM
    odp = "Otrzymano:" + pytanie
    st.session_state.historia.extend(
        [
            ("user", pytanie),
            ("assistant", odp)
        ]
    )

    st.chat_message("user").write(pytanie)
    st.chat_message("assistant").write(odp)