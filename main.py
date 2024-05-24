from datetime import date

import streamlit as st

from currency_trends import get_currency_codes, get_currency_trend

if "today" not in st.session_state:
    st.session_state.today = date.today()

with st.sidebar:
    currency_code = st.selectbox("Currency code", get_currency_codes())[:3]

today = st.session_state.today

df = get_currency_trend(currency_code, today.replace(year=today.year - 1), today)
last_date = df["Date"].iloc[-1]
formatted_date = f"{last_date.day}.{last_date.month}.{last_date.year}"

st.text(f"Exchange rate for {currency_code} is {df["Exchange Rate"].iloc[-1]} kr as of {formatted_date}.")

st.line_chart(df, x="Date", y="Exchange Rate")
