import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(layout="wide")

st.title("📊 Kliknij słupek, aby filtrować dane")

# -----------------------------------------
# DANE
# -----------------------------------------

df = pd.DataFrame({
    "region": [
        "Warszawa", "Warszawa", "Warszawa",
        "Kraków", "Kraków", "Kraków",
        "Gdańsk", "Gdańsk", "Gdańsk",
        "Wrocław", "Wrocław", "Wrocław",
    ],
    "produkt": [
        "Laptop", "Telefon", "Tablet",
        "Laptop", "Telefon", "Tablet",
        "Laptop", "Telefon", "Tablet",
        "Laptop", "Telefon", "Tablet",
    ],
    "sprzedaz": [
        12000, 8000, 5000,
        9000, 11000, 4000,
        7000, 6000, 9000,
        10000, 7000, 6000,
    ]
})

# -----------------------------------------
# AGREGACJA DO WYKRESU
# -----------------------------------------

regiony = (
    df.groupby("region", as_index=False)["sprzedaz"]
    .sum()
)

# -----------------------------------------
# DEFINICJA KLIKNIĘCIA
# -----------------------------------------

wybor_regionu = alt.selection_point(
    name="wybor_regionu",
    fields=["region"],
    on="click"
)

# -----------------------------------------
# WYKRES SŁUPKOWY
# -----------------------------------------

chart = (
    alt.Chart(regiony)
    .mark_bar()
    .encode(
        x=alt.X(
            "region:N",
            title="Region"
        ),
        y=alt.Y(
            "sprzedaz:Q",
            title="Sprzedaż"
        ),
        opacity=alt.condition(
            wybor_regionu,
            alt.value(1),
            alt.value(0.4)
        ),
        tooltip=[
            "region:N",
            "sprzedaz:Q"
        ]
    )
    .add_params(wybor_regionu)
)

event = st.altair_chart(
    chart,
    use_container_width=True,
    on_select="rerun"
)

# -----------------------------------------
# ODCZYT KLIKNIĘTEGO SŁUPKA
# -----------------------------------------

selection = event.selection

if (
    "wybor_regionu" in selection
    and selection["wybor_regionu"]
):

    wybrane = selection["wybor_regionu"]

    # Altair zwraca listę wybranych wartości
    if len(wybrane) > 0:

        region = wybrane[0]["region"]

        st.success(
            f"Wybrany region: {region}"
        )

        filtered_df = df[
            df["region"] == region
        ]

    else:
        filtered_df = df

else:
    filtered_df = df


# -----------------------------------------
# DRUGI WYKRES — JUŻ PRZEFILTROWANY
# -----------------------------------------

st.subheader("Sprzedaż produktów")

produkty = (
    filtered_df
    .groupby("produkt", as_index=False)["sprzedaz"]
    .sum()
)

st.bar_chart(
    produkty,
    x="produkt",
    y="sprzedaz"
)


# -----------------------------------------
# TABELA
# -----------------------------------------

st.subheader("Dane")

st.dataframe(
    filtered_df,
    use_container_width=True
)