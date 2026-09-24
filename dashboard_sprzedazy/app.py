from pathlib import Path
import hashlib

import pandas as pd
import streamlit as st

from data_utils import load_sales, filter_sales, export_csv

st.set_page_config(page_title="Dashboard Sprzedązy", layout='wide')
st.title("Dashboard sprzedaży sklepu")
st.markdown("Wczytaj dane i filtruj")

with st.sidebar:
    st.header("Dane i filtry")
    source = st.radio("Źródło danych", ["Dane przykłądowe", "Własny plik CSV"])

    uploaded = st.file_uploader(
        "Wczytaj plik CSV",
        type=['csv']
    ) if source == "Własny plik CSV" else None
    sample = Path(__file__).parent / 'sprzedaz_przyklad.csv'
    st.download_button(
        "Pobierz przykłądowy csv",
        sample.read_bytes(),
        "sprzedaz_przyklad.csv",
        "text/csv")

if source == "Własny plik CSV" and uploaded is None:
    st.info("Dodaj plik CSV w panelu po lewej stronie")
    st.code('data,produkt,kategoria,liczba_sztuk,cena_jednostkowa\n2026-01-10,Klawiatura,Elektronika,2,149.98',
            language="text")
    st.stop()

try:
    df, invalid = load_sales(uploaded if uploaded is not None else sample)
except ValueError as exc:
    st.error(str(exc))
    st.stop()

if invalid:
    st.warning(f"Pominięto {invalid} niepoprawnych wierszy")

if df.empty:
    st.error("Brak danych")
    st.stop()

# nowy plik otrzymuje nowe filtry
identity = hashlib.sha256(uploaded.getvalue()).hexdigest()[:12] if uploaded is not None else 'demo'

with st.sidebar:
    categories = sorted(df["kategoria"].unique())
    chosen = st.multiselect(
        "Kategorie produktów",
        categories,
        default=categories,
        key=f"categories_{identity}"
    )

    date_min, date_max = df['data'].min().date(), df['data'].max().date()

    dates = st.date_input(
        "Zakres dat",
        value=(date_min, date_max),
        min_value=date_min,
        max_value=date_max,
        key=f"dates_{identity}"
    )

    st.caption("Wszystkie kwoty w PLN")

if len(dates) != 2:
    st.info("Wybierz datę początkową i końcową")
    st.stop()

filtered = filter_sales(df, chosen, *dates)

if filtered.empty:
    st.info("Brak sprzedaży dla wybranych filtrów.")
    st.stop()

revenue = filtered['wartosc_sprzedazy'].sum()
units = int(filtered['liczba_sztuk'].sum())
ranking = filtered.groupby('produkt')['liczba_sztuk'].sum().sort_values(ascending=False)
bestsellers = ranking[ranking == ranking.max()]

a, b, c = st.columns(3)
a.metric("Wartość sprzedaży", f"{revenue:,.2f}".replace(",", " ").replace(".", " "))
b.metric("Sprzedane sztuki", f"{units:,.2f}".replace(",", " "))
c.metric("Bestseller", str(bestsellers.index[0]))
if len(bestsellers) > 1:
    st.caption("Remis: " + ', '.join(bestsellers.index))

left, right = st.columns(2)
with left:
    st.subheader('Sprzedaż w miesiącach')
    monthly = filtered.set_index('data')['wartosc_sprzedazy'].resample('MS').sum()
    months = pd.date_range(pd.Timestamp(dates[0]).replace(day=1), pd.Timestamp(dates[1]).replace(day=1), freq='MS')
    monthly = monthly.reindex(months, fill_value=0)
    monthly.index.name = 'Miesiąc'
    monthly.name = 'Sprzedaż (PLN)'
    st.line_chart(monthly)
with right:
    st.subheader('Sprzedaż według kategorii')
    category_sales = filtered.groupby('kategoria')['wartosc_sprzedazy'].sum().rename('Sprzedaż (PLN)')
    st.bar_chart(category_sales)

st.subheader('Dane po filtrowaniu')
st.caption(f'Liczba pozycji sprzedaży: {len(filtered)}')
st.dataframe(filtered.sort_values('data'), hide_index=True)
st.download_button('Pobierz przefiltrowane dane CSV', export_csv(filtered.sort_values('data')), 'sprzedaz_filtrowana.csv', 'text/csv')

with st.expander('Jak przygotować własny CSV?'):
    st.markdown('Wymagane kolumny: `data`, `produkt`, `kategoria`, `liczba_sztuk`, `cena_jednostkowa`. Daty: `RRRR-MM-DD`. Kodowanie: UTF-8. Separator: przecinek lub średnik. Dla cen z przecinkiem użyj separatora średnik. Jeden wiersz to jedna pozycja sprzedaży. Zwroty z wartościami ujemnymi nie są obsługiwane.')
