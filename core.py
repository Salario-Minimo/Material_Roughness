import streamlit as st
import pandas as pd

Conversion = {"Milímetros":1, "Metros":1000, "Pies":304.8, "Pulgadas":25.4}
Data = pd.read_excel("Material_data.xlsx")

# Aquí ocurre la conversión
Data["Minimo"] = Data["Minimo"]/666)

Material = Data["Material"].unique()

sb_conversion = st.selectbox("Unidades:", Conversion)
sb_material = st.selectbox("Material:", Material)

df_front = Data[Data["Material"]==sb_material]

Condicion = df_front["Condicion"].unique()
sb_condicion = st.selectbox("Condicion:", Condicion)

df_front = df_front[df_front["Condicion"]==sb_condicion]





st.write(df_front)

