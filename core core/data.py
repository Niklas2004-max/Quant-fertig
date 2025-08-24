import yfinance as yf
import pandas as pd

def load_data(ticker: str):
    """
    Lädt 1 Jahr historische Daten von Yahoo Finance
    """
    return yf.download(ticker, period="1y")
