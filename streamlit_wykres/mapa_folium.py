import streamlit as st
from streamlit_folium import st_folium
import folium
from folium.plugins import MarkerCluster
import pandas as pd

# przykładowe dane
df = pd.DataFrame({
    "lat": [52.23, 50.06, 54.35, 52.40, 50.10],
    "lon": [21.01, 19.94, 18.65, 21.05, 19.90],
    "miasto": ["Warszawa", "Kraków", "Gdańsk", "Warszawa 2", "Kraków 2"]
})

# mapa startowa
m = folium.Map(location=[52.0, 19.0], zoom_start=6)

# klaster markerów
cluster = MarkerCluster().add_to(m)

# dodawanie markerów
for _, row in df.iterrows():
    folium.Marker(
        location=[row.lat, row.lon],
        popup=row.miasto
    ).add_to(cluster)

# wyświetlenie mapy
result = st_folium(m, width=700, height=500)

# wynik kliknięcia
st.write("Kliknięcie:", result)
