import streamlit as st
import pandas as pd
import requests
import urllib2
import cookielib



"""

Please fill up the code you need and i will generete the file for you.

"""
site= st.secrets['DATA']
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

req = urllib2.Request(site, headers=hdr)
page = urllib2.urlopen(req)
codes = st.text_input('Enter your codes here')
sterile = st.checkbox('Do you want them sterile ?')
df = pd.read_csv(page)
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
