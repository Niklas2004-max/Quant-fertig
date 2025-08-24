import streamlit as st
from core.data import load_data  # nur load_data importieren

st.set_page_config(page_title="Quant Tool", layout="wide")
st.title("Quant Tool - Backtesting & Analyse")

# --- Datenquelle ---
ticker = st.text_input("Ticker eingeben (z.B. AAPL)", "AAPL")

if st.button("Daten laden"):
    try:
        data = load_data(ticker)
        st.success(f"Daten für {ticker} geladen!")
        st.dataframe(data.tail(10))
    except Exception as e:
        st.error(f"Fehler beim Laden der Daten: {e}")

# --- Optionaler Platzhalter für Backtest ---
if 'data' in locals():
    if st.button("Backtest starten"):
        st.info("Backtest-Funktion momentan nicht aktiviert.")
