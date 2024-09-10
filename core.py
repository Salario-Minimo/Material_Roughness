import streamlit as st
import pandas as pd

Data = pd.read_excel("Material_data.xlsx")

Material = Data["Material"].unique()


sb_material = st.selectbox("Material:", Material)


df_front = Data[Data["Material"]==sb_material]

Condicion = df_front["Condicion"].unique()
sb_condicion = st.selectbox("Condicion:", Condicion)

st.write(df_front)

