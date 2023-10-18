import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
#import altair as alt
#from altair.vegalite.v4.api import Chart
import streamlit as st

######upload the datasets
df_bp = pd.read_csv("dataset/business_performance.csv")
df_bp = df_bp.drop(["Unnamed: 0"], axis=1)
df_c = pd.read_csv("dataset/cross_price_elasticity.csv")
col = {'coef','std err','t','P>|t|','[0.025','0.975]', 'pvalue', 'mean', 'price_elasticity'}
df_e = pd.read_csv("dataset/df_elasticity.csv")

######layout streamlit
st.set_page_config(layout="wide")
st.header("Price Elasticity")

tab1, tab2, tab3 = st.tabs(["Elasticity","Business Performance", "Cross Price Elasticity"])

with tab1:
    tab4, tab5 = st.tabs(["Elasticity - figure","Elasticity - table"])
    
    with tab4:
        st.header("Elasticity - plot")
        ######create ranking column
        df_e['ranking'] = df_e.loc[:,'price_elasticity'].rank(ascending=False).astype(int)
        df_e = df_e.reset_index(drop=True)
        fig, ax = plt.subplots()
        plt.figure(figsize=(12,4))
        ax.hlines(y=df_e['name'], xmin=0, xmax=df_e['price_elasticity'], alpha=0.5, linewidth=3)

        #ax.gca().set(ylabel= 'Ranking Number', xlabel= 'Price Elasticity')
        #ax.title('Price Elasticity', fontdict={'size': 13})
        ax.grid(linestyle = '--')
        st.pyplot(fig)
           
    with tab5:
        st.header("Elasticity - table")
        df_order_elasticity =df_e[['ranking', 'name', 'price_elasticity']].sort_values('ranking', ascending=True)
        df_order_elasticity = df_order_elasticity.set_index("name")
        st.dataframe(df_order_elasticity, use_container_width=True)

with tab2:
    st.header("Business Performance")
    df_bp = df_bp.set_index("name")
    st.dataframe(df_bp, use_container_width=True)

with tab3:
    st.header('Cross Price Elasticity')
    df_c = df_c.drop(["Unnamed: 0"], axis=1)
    df_c = df_c.set_index("name")
    df_c = df_c.drop('const')
    df_c = df_c.drop(columns=col)
    st.dataframe(df_c, use_container_width=True)
    
