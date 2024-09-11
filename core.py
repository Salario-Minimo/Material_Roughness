import streamlit as st
import pandas as pd
from math import log10

def scientific_notation(row):
  it = ("Minimo", "Maximo", "Recomendado")
  for x in it:
    row[x] = round(row[x]/Conversion[sb_conversion], 5)
    if not abs(log10(row[x])) < 2:
      row[x] = "{:.3e}".format(row[x])
    row[x] = str(row[x]) + " " + Sufijos[sb_conversion]
  return row

st.header("Rugosidad de una tubería.")

Conversion = {"Milímetros":1, "Metros":1000, "Pies":304.8, "Pulgadas":25.4}
Sufijos = {"Milímetros":"mm", "Metros":"m", "Pies":"ft", "Pulgadas":"inch"}
Data = pd.read_excel("Material_data.xlsx")

sb_conversion = st.selectbox("Unidades:", Conversion)
df_front = Data.apply(scientific_notation, axis=1)

Material = Data["Material"].unique()


sb_material = st.selectbox("Material:", Material, index=None)

if sb_material is not None:
  df_front = Data[Data["Material"]==sb_material]

Condicion = df_front["Condicion"].unique()
sb_condicion = st.selectbox("Condicion:", Condicion, index=None)

if sb_condicion is not None:
  df_front = df_front[df_front["Condicion"]==sb_condicion]





st.write(df_front)

