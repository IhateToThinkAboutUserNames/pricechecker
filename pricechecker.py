import streamlit as st
import pandas as pd

sekret = st.secrets["test"]

st.header(f"Separate code with 1 SPACE only !")
with st.form('entry_form', clear_on_submit=True):
    ol1, col2 = st.columns(2)
    col1.selectbox("Select Supplier", sekret, key='suppliers')
