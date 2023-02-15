from io import StringIO
from deta import Deta
import pandas as pd
import streamlit as st

key = st.secrets(DETA_KEY)

deta = Deta('key')
drive = deta.Drive("App")
hello = drive.get('Book3.csv')
content = hello.read()
hello.close()
s=str(content,'utf-8')

data = StringIO(s) 

df=pd.read_csv(data)

df['Product code'] = df['Product code'].str.lower()
codes = input('Put your character here')

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
