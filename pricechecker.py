import streamlit as st
import pandas as pd
import lxml

"""

Please fill up the code you need and i will generete the file for you.

"""


codes = st.text_input('Enter your codes here')
df['Product code'] = df['Product code'].str.lower()

listt = codes.split()
prices = []

for i in listt:
    for text in df["Product code"]:
        if i in text:
            prices.append(text)
        else:
            continue

prlist = pd.DataFrame(df.loc[df['Product code'].isin(prices)])
sup = prlist['Supplier'] = "Medartis"
prlist.drop(labels=['Supplier'], axis=1,inplace=True)
prlist.insert(2, 'Supplier', sup)
prlist
