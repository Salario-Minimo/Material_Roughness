import streamlit as st
import pandas as pd

Data = pd.read_excel("Material_data.xlsx")

Material = Data["Material"].unique()
Condicion = Data["Condicion"].unique()

st.write(Material, Condicion)

st.write(Data)
