import streamlit as st

st.title("Panel użytkownika")

col1, col2 = st.columns(2)

with col1:
    st.header("Użytkownik")
    st.write("Jan Kowalski")

with col2:
    st.header("Statystyki")
    st.metric(
        "Liczba kursów",
        12
    )

left, right = st.columns([2, 1])

with left:
    st.write("Lewa Kolumna")

with right:
    st.write("Prawa kolumna")

# category  =st.sidebar.selectbox(
#     "Kategoria",
#     [
#         "Python",
#         "SQL",
#         "Python",
#     ]
# )

with st.sidebar:

    st.header("Filtry")

    category  =st.sidebar.selectbox(
        "Kategoria",
        [
            "Python",
            "SQL",
            "Python",
        ]
    )

with st.expander("Więcej informacji"):

    st.write(
        "Tutaj możemy umięscić dodatkową treść"
    )