import streamlit as st
import pandas as pd

def scientific_notation(row):
  it = ("Minimo", "Maximo", "Recomendado")
  for x in it:
    row[x] = row[x]/Conversion[sb_conversion]
    row[x] = "{:.2e}".format(row[x])
    row[x] = str(row[x])
  st.write(row)
  return row

Conversion = {"Milímetros":1, "Metros":1000, "Pies":304.8, "Pulgadas":25.4}
Sufijos = {"Milímetros":"mm", "Metros":"m", "Pies":"ft", "Pulgadas":"inch"}
Data = pd.read_excel("Material_data.xlsx")

sb_conversion = st.selectbox("Unidades:", Conversion)
Data = Data.apply(scientific_notation, axis=1)

Material = Data["Material"].unique()


sb_material = st.selectbox("Material:", Material)

df_front = Data[Data["Material"]==sb_material]

Condicion = df_front["Condicion"].unique()
sb_condicion = st.selectbox("Condicion:", Condicion)

df_front = df_front[df_front["Condicion"]==sb_condicion]





st.write(df_front)

