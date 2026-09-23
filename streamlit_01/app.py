import streamlit as st

# (.venv) PS C:\Users\CSComarch\PycharmProjects\PythonProjectStreamLitApp> streamlit --version
# Streamlit, version 1.64.0

st.title("Moja pierwsza aplikacja Streamlit")

st.write("Witaj w aplikacji napisanej w Pythonie")

st.header("O Aplikacji")

st.write(
    "Streamlit pozwala tworzyć aplikację webowe "
    "bez pisania HTML, CSS, JS.")

st.write("Witaj")
st.write("123")
st.write(123)
st.write(10 + 20)

st.info("To jest informacja")
st.success("Operacja zakończona sukcesem")
st.error("Wystąpił błąd")
st.warning("To jest ostrzeżenie")

st.markdown("""
### Informacje

To jest **ważny tekst**.
- Python
- Streamlit
- Pandas
""")

st.markdown("# Nagłówek H1")

st.markdown(
    '<p style="color:red;">Czerwony tekst</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p style="color:red;">Czerwony tekst</p>',
    unsafe_allow_html=False
)

st.markdown("---")
st.markdown("[Kliknij](https://naukapythona.pl)")

