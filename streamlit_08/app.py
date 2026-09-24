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
