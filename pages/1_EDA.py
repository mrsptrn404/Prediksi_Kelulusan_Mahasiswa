import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("1. EDA Dataset Kelulusan")

df = pd.read_csv("data/lulus.csv")
st.write("### Dataset Sample", df.head())
st.write("### Statistik Deskriptif")
st.write(df.describe())

# Visualisasi distribusi IPK
:contentReference[oaicite:4]{index=4}
:contentReference[oaicite:5]{index=5}
:contentReference[oaicite:6]{index=6}
:contentReference[oaicite:7]{index=7}

# Crosstab fitur dengan target
:contentReference[oaicite:8]{index=8}
    :contentReference[oaicite:9]{index=9}
    :contentReference[oaicite:10]{index=10}
    :contentReference[oaicite:11]{index=11}
    :contentReference[oaicite:12]{index=12}
