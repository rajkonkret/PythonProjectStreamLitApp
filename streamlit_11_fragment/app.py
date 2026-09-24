import streamlit as st
import time


@st.fragment
def zegar():
    placeholder = st.empty()
    while True:
        placeholder.write(f"Czas: {time.time()}")
        time.sleep(1)


@st.fragment
def kalkulator():
    # sztuki = st.slider("Sztuki", 1, 20, 3)
    st.metric("Wartość", f"{3 * 12} zł")

kalkulator()
zegar()
st.divider()
