from datetime import datetime

import streamlit as st
import FinanceDataReader as fdr



st.title('주식 차트')
date = st.date_input(label='시작일', value=datetime(2022, 1, 1))
code = st.text_input(label='종목코드', placeholder='005930')

button = st.button('조회')

if date and code and button:
    df = fdr.DataReader(code, date)
    data = df['Close'].sort_index(ascending=True)
    st.line_chart(data)
