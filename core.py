import streamlit as st
import pandas as pd
from math import log10

def scientific_notation(row):
  it = ("Minimo", "Maximo", "Recomendado")
  for x in it:
    row[x] = row[x]/Conversion[sb_conversion]
    if not abs(log10(row[x])) < 2:
      row[x] = "{:.3e}".format(row[x])
    else:
      row[x] = round(row[x], 5)
    row[x] = str(row[x]) + " " + Sufijos[sb_conversion]
  return row

st.header("Rugosidad de una tubería.")

Conversion = {"Milímetros":1, "Metros":1000, "Pies":304.8, "Pulgadas":25.4}
Sufijos = {"Milímetros":"mm", "Metros":"m", "Pies":"ft", "Pulgadas":"inch"}
Data = pd.read_excel("Material_data.xlsx")

sb_conversion = st.selectbox("Unidades:", Conversion)
Data = Data.apply(scientific_notation, axis=1)
df_front = Data

Material = df_front["Material"].unique()


sb_material = st.selectbox("Material:", Material, index=None)

if sb_material is not None:
  df_front = Data[Data["Material"]==sb_material]

Condicion = df_front["Condicion"].unique()
sb_condicion = st.selectbox("Condicion:", Condicion, index=None)

if sb_condicion is not None:
  df_front = df_front[df_front["Condicion"]==sb_condicion]





st.write(df_front)

st.text("Darby, R. (2008). 6 Pipe Flow. Albright's Chemical Engineering Handbook, 393.")
