import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px



st.title('広告費と売上')
df=pd.read_csv('ad_expense_sales.csv')

with st.sidebar:
    st.title('抽出条件')
    st.subheader('製品カテゴリ')
    product=st.multiselect('製品カテゴリを選択してください(複数選択可)',
            df['prod_category'].unique())
    st.subheader('公告媒体')
    ad=st.selectbox('広告媒体を指定してください',
            df['media'].unique())
    st.subheader('色分け')
    colorvar=st.selectbox('分類を選択',
            ['性別','年齢層','季節'])

if colorvar=='性別':
    color='sex'
elif colorvar=='年齢層':
    color='age'
elif colorvar=='季節':
    color='season'

df=df[df['prod_category'].isin(product)]
df=df[df['media']==ad]

st.write('単位:万円')
fig=px.scatter(df,x='ad_expense',y='sales',color=color,
        labels={'ad_expense':'広告費','sales':'売上'},
        range_x=[0,df['ad_expense'].max()*1.1],
        range_y=[0,df['sales'].max()*1.1],
        trendline='ols')
st.plotly_chart(fig)