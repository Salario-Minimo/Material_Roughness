import streamlit as st
import pandas as pd

Conversion = ("Milímetros", "Metros", "Pies", "Pulgadas")
Data = pd.read_excel("Material_data.xlsx")

Material = Data["Material"].unique()

sb_material = st.selectbox("Material:", Material)
sb_conversion = st.selectbox("Unidades:", Conversion)


df_front = Data[Data["Material"]==sb_material]

Condicion = df_front["Condicion"].unique()
sb_condicion = st.selectbox("Condicion:", Condicion)

df_front = df_front[df_front["Condicion"]==sb_condicion]



st.write(df_front)

