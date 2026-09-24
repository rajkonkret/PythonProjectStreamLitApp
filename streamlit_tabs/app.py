import streamlit as st

st.title("Zakładki")

tab1, tab2 = st.tabs(["Raport", "Pomoc"])

with tab1:
    st.write("To jest raport")
    st.write("Można tutaj dac wykres")

with tab2:
    st.write("To jest pomoc")
    st.write("Można tutaj dać FAQ")
