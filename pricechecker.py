# import streamlit as st
# import pandas as pd

# sekret = st.secrets["test"]
# data = pd.read_html(sekret)
# st.header(f"Separate code with 1 SPACE only !")
# with st.form('entry_form', clear_on_submit=True):
#     st.write("DB username:", st.secrets["test"])
#     st.write("DB username:", st.secrets[sekret])
#     submitted = st.form_submit_button('Get Your Codes')
#     if submitted:
#         st.success("Got your codes !")


import streamlit as st
import pandas as pd
from io import StringIO
from deta import Deta
import os
from dotenv import load_dotenv


DETA_KEY = "a0b17bjxebi_B6fTbHvU5KSSax9VGb4aKVeZD5wEmWpp"
deta = Deta(DETA_KEY)
drive = deta.Drive("App")
hello = drive.get('Book3.csv')
content = hello.read()
hello.close()
s=str(content,'utf-8')

data = StringIO(s) 

df=pd.read_csv(data)

codes = input('Put your character here')
page_title = "Medartis pricer checker"
suppliers = ['Medartis']
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
