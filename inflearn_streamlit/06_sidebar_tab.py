from datetime import datetime
import time

import streamlit as st
import FinanceDataReader as fdr



st.title('종목 검색')

with st.sidebar:
    date = st.date_input(label='시작일', value=datetime(2022, 1, 1))
    code = st.text_input(label='종목코드', placeholder='005930')
    button = st.button('조회')

if date and code and button:
    df = fdr.DataReader(code, date)
    data = df['Close'].sort_index(ascending=True)
    tab1, tab2 = st.tabs(['차트', '데이터'])

    with tab1:
        st.line_chart(data)

    with tab2:
        st.dataframe(df.sort_index(ascending=False))

    with st.expander('컬럼 설명'):
        st.markdown('''
            - Open: 시가
            - High: 고가
            - Low: 저가
            - Close: 종가
            - Volume: 거래량
            - Change: 대비
        ''')