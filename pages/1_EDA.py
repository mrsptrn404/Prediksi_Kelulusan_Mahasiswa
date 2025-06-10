def run():
    import streamlit as st
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt

    st.subheader("📊 Eksplorasi Data (EDA)")

    df = pd.read_csv("data/lulus.csv")
    st.write("Data sample:", df.head())

    st.markdown("### 📌 Distribusi Lulus Cepat")
    st.bar_chart(df["Lulus Cepat"].value_counts())

    st.markdown("### 📈 Histogram IPK")
    fig, ax = plt.subplots()
    sns.histplot(df["IPK"], kde=True, ax=ax)
    st.pyplot(fig)

    st.markdown("### 📉 Korelasi Antar Fitur")
    corr = df.drop(columns=["Lulus Cepat"]).corr()
    fig2, ax2 = plt.subplots()
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax2)
    st.pyplot(fig2)

