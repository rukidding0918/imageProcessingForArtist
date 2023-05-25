import streamlit as st
import random
import datetime


def generate_lotto():
    return sorted(random.sample(range(1, 46), 6))


st.title(":sparkles:로또생성기:sparkles:")
button = st.button('로또번호 생성')
if button:
    st.write(f'행운의 번호: {generate_lotto()}')
    st.write(f'생성시간: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')