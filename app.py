import streamlit as st
import pandas as pd

from yahoo_historical import Fetcher

from datetime import datetime
from datetime import timedelta, date

start = date.today() - timedelta(days=365)
end = date.today()

start_year = int(start.strftime('%Y-%m-%d').split('-')[0])
start_month = int(start.today().strftime('%Y-%m-%d').split('-')[1])
start_day = int(start.today().strftime('%Y-%m-%d').split('-')[2])
start_date = [start_year, start_month, start_day]

current_year = int(end.today().strftime('%Y-%m-%d').split('-')[0])
current_month = int(end.today().strftime('%Y-%m-%d').split('-')[1])
current_day = int(end.today().strftime('%Y-%m-%d').split('-')[2])
today_date = [current_year, current_month, current_day]


st.write("""
# My first app
Hello *world!*
""")

stock_name = st.text_input("label goes here", 'PTT.BK')

data = Fetcher(stock_name, start_date, today_date)
df_stock = data.getHistorical().dropna()

df = df_stock['Close']
st.line_chart(df)
