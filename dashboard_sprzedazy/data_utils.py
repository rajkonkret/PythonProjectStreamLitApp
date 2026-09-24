"""Wczytywanie i sprawdzanie danych sprzedaży."""
import pandas as pd
import numpy as np

COLUMNS = ['data', 'produkt', 'kategoria', 'liczba_sztuk', 'cena_jednostkowa']

def load_sales(source):
    try:
        df = pd.read_csv(source, sep=None, engine='python', encoding='utf-8-sig', dtype=str)
    except (ValueError, UnicodeError, pd.errors.ParserError) as exc:
        raise ValueError('Nie można odczytać CSV. Użyj kodowania UTF-8 i separatora przecinek lub średnik.') from exc
    df.columns = df.columns.str.strip().str.lower()
    missing = set(COLUMNS) - set(df.columns)
    if missing:
        raise ValueError('Brak wymaganych kolumn: ' + ', '.join(sorted(missing)))
    df = df[COLUMNS].copy()
    if df.empty:
        raise ValueError('Plik nie zawiera żadnych rekordów.')
    df['data'] = pd.to_datetime(df['data'], format='%Y-%m-%d', errors='coerce')
    valid = df['data'].notna()
    for col in ['produkt', 'kategoria']:
        df[col] = df[col].fillna('').str.strip()
        valid &= df[col].ne('')
    for col in ['liczba_sztuk', 'cena_jednostkowa']:
        df[col] = pd.to_numeric(df[col].str.replace(',', '.', regex=False), errors='coerce')
        valid &= np.isfinite(df[col]) & df[col].ge(0) & df[col].le(1_000_000_000)
    valid &= df['liczba_sztuk'].gt(0) & df['liczba_sztuk'].mod(1).eq(0)
    invalid = int((~valid).sum())
    df = df.loc[valid].copy()
    df['liczba_sztuk'] = df['liczba_sztuk'].astype('int64')
    df['cena_jednostkowa'] = df['cena_jednostkowa'].round(2)
    df['wartosc_sprzedazy'] = (df['liczba_sztuk'] * df['cena_jednostkowa']).round(2)
    return df, invalid

def filter_sales(df, categories, start, end):
    return df.loc[df['kategoria'].isin(categories) & df['data'].between(pd.Timestamp(start), pd.Timestamp(end))].copy()

def export_csv(df):
    result = df.copy()
    # Excel nie powinien interpretować nazw produktów jako formuł.
    for col in ['produkt', 'kategoria']:
        result[col] = result[col].map(lambda v: "'" + v if v.startswith(('=', '+', '-', '@', '\t', '\r')) else v)
    return result.to_csv(index=False, date_format='%Y-%m-%d').encode('utf-8-sig')
