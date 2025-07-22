import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

st.title('Streamlitのグラフ表示')

df = pd.DataFrame(data=np.random.randint(0, 1000, (3, 6)),
                  index=['支店A', '支店B', '支店C'],
                  columns=['1月', '２月', '３月', '４月', '５月', '６月'])

st.header('1. 折れ線グラフの表示')
st.line_chart(df.T)

st.header('2. 棒グラフの表示')
st.bar_chart(df.T)

st.header('3. 面グラフの表示')
st.area_chart(df.T)

st.header('4. 散布図の表示')
df_sales_2023=pd.read_csv('air_conditioner_sales_2023.csv',index_col='date')
st.scatter_chart(df_sales_2023,x='temp',y='sales')


st.header('5. 散布図の表示(Matplotlib)')



st.header('6. 散布図の表示(Plotly)')
fig=px.scatter(df_sales_2023,
    x='temp',y='sales',
    labels={'temp':'temperrature','sales':'sales(thousanddollar)'},
    title='Temp vs Sales')
st.plotly_chart(fig)
