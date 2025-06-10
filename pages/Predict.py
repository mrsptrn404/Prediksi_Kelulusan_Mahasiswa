def run():
    import streamlit as st
    import numpy as np
    import pandas as pd
    from sklearn.naive_bayes import GaussianNB
    from sklearn.neighbors import KNeighborsClassifier

    st.header("🧩 Prediksi Lulus Cepat atau Tidak")

    ipk = st.number_input("IPK", min_value=0.0, max_value=4.0, step=0.01)
    pelatihan = st.slider("Pelatihan Pengetahuan", 0, 10, 0)
    prestasi = st.slider("Prestasi", 0, 50, 0)
    organisasi = st.slider("Kegiatan Organisasi", 0, 10, 0)

    model_choice = st.selectbox("Pilih Model", ["Naive Bayes", "KNN"])

    df = pd.read_csv("data/lulus.csv")
    X = df[['IPK', 'Pelatihan Pengetahuan', 'Prestasi', 'Kegiatan Organisasi']]
    y = df['Lulus Cepat'].map({'Yes': 1, 'No': 0})

    if model_choice == "Naive Bayes":
        model = GaussianNB()
    else:
        model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X, y)

    input_data = np.array([[ipk, pelatihan, prestasi, organisasi]])
    pred = model.predict(input_data)[0]
    pred_label = "Yes (Lulus Cepat)" if pred == 1 else "No (Tidak Lulus Cepat)"

    if st.button("Prediksi"):
        st.success(f"Hasil Prediksi: {pred_label}")
