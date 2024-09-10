import streamlit as st
import pandas as pd

Data = pd.read_excel("Material_data.xlsx")

Material = Data["Material"].unique()
Condicion = Data["Condicion"].unique()

sb_material = st.selectbox("Material:", Material)
sb_condicion = st.selectbox("Condicion:", Condicion)

df_front = Data[Data["Material"]==sb_material]
st.write(df_front)

