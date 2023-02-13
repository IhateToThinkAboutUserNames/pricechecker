import streamlit as st
import pandas as pd
"""

Please fill up the code you need and i will generete the file for you.

"""

codes = st.text_input('Enter your codes here')
sterile = st.checkbox('Do you want them sterile ?')
price_list = st.secrets['pl']
df = pd.read_csv(SECRET_DB)
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
