import streamlit as st
import pandas as pd
import numpy as np


st.title('dataframe tutorial')

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

st.dataframe(df)
st.table(df)

st.metric(label='온도', value='37.5℃', delta='0.5℃')
st.metric(label='삼성전자', value='50,000원', delta='-0.5%')

col1, col2, col3 = st.columns(3)
col1.metric(label='달러', value='1,120원', delta='-0.5%')
col2.metric(label='유로', value='1,300원', delta='0.1%')
col3.metric(label='위안', value='170원', delta='-0.3%')