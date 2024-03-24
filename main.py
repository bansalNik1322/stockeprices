import yfinance as yf
import streamlit as st
import pandas as pd


st.write('''
Shown are the stock **closing price** and **volume** of Google!

''')

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDF = tickerData.history(period='10d', start="2010-5-31", end="2020-5-31")

st.write("Closing Price")
st.line_chart(tickerDF['Close'])
st.write("Volume")
st.line_chart(tickerDF['Volume'])


