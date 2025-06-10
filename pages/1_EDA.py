def run():
    import streamlit as st
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt

    st.header("📊 Eksplorasi Data (EDA)")

    df = pd.read_csv("data/lulus.csv")

    st.subheader("🔍 Data Awal")
    st.write(df.head())

    st.subheader("📈 Statistik Deskriptif")
    st.write(df.describe())

    st.subheader("🎯 Distribusi Target (Lulus Cepat)")
    st.bar_chart(df["Lulus Cepat"].value_counts())

    st.subheader("📌 Visualisasi Histogram IPK")
    fig, ax = plt.subplots()
    sns.histplot(df["IPK"], kde=True, ax=ax)
    st.pyplot(fig)
