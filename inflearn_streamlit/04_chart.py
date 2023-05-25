import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# plt.rcParams['font.family'] = 'NanumGothic'
plt.rcParams['axes.unicode_minus'] = False

df = pd.DataFrame({
    'name': ['hong', 'kim', 'lee', 'park'],
    'age': [20, 30, 25, 35],
    'weight': [70, 80, 65, 75]
})

st.dataframe(df)

col1, col2 = st.columns(2)

# plt 사용하여 chart 그리기
fig, ax = plt.subplots()
ax.bar(df['name'], df['age'])
col1.pyplot(fig)

# seaborn 사용하여 chart 그리기
barplot = sns.barplot(data=df, x='name', y='weight', ax=ax, palette='Set2')
fig = barplot.get_figure()
col2.pyplot(fig)