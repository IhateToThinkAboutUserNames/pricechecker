import streamlit as st
import pandas as pd

sekret = st.secrets["test"]
data = pd.read_html('sekret')
st.header(f"Separate code with 1 SPACE only !")
with st.form('entry_form', clear_on_submit=True):
    st.write("DB username:", st.secrets["test"])
    st.write("DB username:", st.secrets[sekret])
    submitted = st.form_submit_button('Get Your Codes')
    if submitted:
        st.success("Got your codes !")
