import streamlit as st
import pandas as pd

def scientific_notation(value):
  return "{:.2e}".format(num)

Conversion = {"Milímetros":1, "Metros":1000, "Pies":304.8, "Pulgadas":25.4}
Data = pd.read_excel("Material_data.xlsx")

sb_conversion = st.selectbox("Unidades:", Conversion)
# Aquí ocurre la conversión
Data["Minimo"] = Data["Minimo"]/Conversion[sb_conversion]
Data["Minimo"] = Data.apply(scientific_notation)

Material = Data["Material"].unique()


sb_material = st.selectbox("Material:", Material)

df_front = Data[Data["Material"]==sb_material]

Condicion = df_front["Condicion"].unique()
sb_condicion = st.selectbox("Condicion:", Condicion)

df_front = df_front[df_front["Condicion"]==sb_condicion]





st.write(df_front)

