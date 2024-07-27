import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# SIMPLE STOCK PRICE APP
         
Shown are the Stock Closing price , Volume , Opening Price , High , Low , Dividends of Apple
         """)

tickerSymbol="AAPL"

tickerData=yf.Ticker(tickerSymbol)

tickerDF=tickerData.history(period="1d",start="2020-1-01",end="2024-7-26")

st.line_chart(tickerDF.Close)

st.line_chart(tickerDF.Volume)

st.line_chart(tickerDF.Open)

st.line_chart(tickerDF.High)

st.line_chart(tickerDF.Low)

st.line_chart(tickerDF.Dividends)

