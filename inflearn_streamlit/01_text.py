import streamlit as st

st.title('Streamlit 101: An in-depth introduction')
st.header('This is a header')

sample_code = '''
def hello():
    print("Hello, Streamlit!")
'''

st.code(sample_code, language='python')
st.markdown('This is a **markdown** _cell_')
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
''')
