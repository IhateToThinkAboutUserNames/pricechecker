import streamlit as st
import pandas as pd

page_title = "Medartis pricer checker"
suppliers = ['Medartis']
secret = st.secrets("DATA")
df = pd.read_csv('secret')
df['Product code'] = df['Product code'].str.lower()

st.set_page_config(page_title=page_title, layout="centered")
st.title(page_title)

st.header(f"Separate code with 1 SPACE only !")
with st.form('entry_form', clear_on_submit=True):
    col1, col2 = st.columns(2)
    col1.selectbox("Select Supplier", suppliers, key='suppliers')
    codes = st.text_input('', placeholder="Enter codes here ...")

    "---"
    submitted = st.form_submit_button('Get Your Codes')
    if submitted:
        st.success("Got your codes !")
        listt = codes.split()
        prices = []

        for i in listt:
            for text in df["Product code"]:
                if i in text:
                    prices.append(text)

        prlist = pd.DataFrame(df.loc[df['Product code'].isin(prices)])
        sup = prlist['Supplier'] = "Medartis"
        prlist.drop(labels=['Supplier'], axis=1,inplace=True)
        prlist.insert(2, 'Supplier', sup)
        st.dataframe(prlist)
    else:
        print("nope")
    







# st.header("Price Report")
# with st.form("Raport"):
#     if submitted:
#         col1.metric("Your List",)
