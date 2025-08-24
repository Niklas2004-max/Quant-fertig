import yfinance as yf
import pandas as pd

def load_data(ticker: str) -> pd.DataFrame:
    return yf.download(ticker, period="1y")
