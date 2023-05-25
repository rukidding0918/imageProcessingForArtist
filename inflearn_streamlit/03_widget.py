import streamlit as st
import pandas as pd
from datetime import datetime as dt
import datetime

button = st.button('버튼')
if button:
    st.write("버튼이 눌렸습니다.")

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.dataframe(df)
st.download_button(label='다운로드', data=df.to_csv(), file_name='data.csv', mime='text/csv')

agree = st.checkbox('어쩌구저쩌구블라블라')
agree_button = st.button('동의하십니까?')
if agree_button & agree:
    st.write('동의하셨습니다.')
if agree_button & ~agree:
    st.write('동의하지 않으셨습니다.')

mbti = st.radio("당신의 MBTI는?", ('INTJ', 'ENTJ', '모름'))
if mbti == "INTJ":
    st.write("당신은 :blue[INTJ]입니다.")
if mbti == "ENTJ":
    st.write("당신은 :red[ENTJ]입니다.")
if mbti == "모름":
    st.write("당신의 MBTI를 알고싶군요.")

mbti2 = st.selectbox("당신의 MBTI는?", ('INTJ', 'ENTJ', '모름'))
if mbti2 == "INTJ":
    st.write("당신은 :blue[INTJ]입니다.")
if mbti2 == "ENTJ":
    st.write("당신은 :red[ENTJ]입니다.")
if mbti2 == "모름":
    st.write("당신의 MBTI를 알고싶군요.")

options = st.multiselect(
    '당신이 좋아하는 색깔은?',
    ['Red', 'Green', 'Blue'],
    [])
st.write(f'You selected: {options}')
st.write('You selected:', options)

value = st.slider('Select a value', 0.0, 100.0, (25.0, 75.0))
st.write('You selected:', value)

start_time = st.slider(
    "약속 언제로 할까?",
    min_value=dt(2021, 1, 1, 0, 0),
    max_value=dt(2021, 12, 31, 23, 00),
    value=dt(2021, 3, 1, 16, 0),
    step=datetime.timedelta(hours=1),
    format="MM/DD/YY - hh:mm a",
)
st.write('You selected:', start_time)


title = st.text_input(label='제목을 입력하세요', placeholder='제목')
st.write(f'You selected: {title}')

number = st.number_input(label='숫자를 입력하세요', min_value=0, max_value=100, value=50, step =5)
st.write(f'You selected: {number}')