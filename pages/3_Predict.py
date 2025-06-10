def run():
    import streamlit as st
    import numpy as np
    import pandas as pd
    from sklearn.naive_bayes import GaussianNB
    from sklearn.neighbors import KNeighborsClassifier

    st.subheader("🤖 Prediksi Kelulusan Mahasiswa")

    ipk = st.number_input("Masukkan IPK", 0.0, 4.0, step=0.01)
    pelatihan = st.slider("Pelatihan Pengetahuan (0-10)", 0, 10)
    prestasi = st.slider("Jumlah Prestasi (0-50)", 0, 50)
    organisasi = st.slider("Kegiatan Organisasi (0-10)", 0, 10)

    model_choice = st.radio("Pilih Model", ("Naive Bayes", "KNN"))

    df = pd.read_csv("data/lulus.csv")
    X = df[['IPK', 'Pelatihan Pengetahuan', 'Prestasi', 'Kegiatan Organisasi']]
    y = df['Lulus Cepat'].map({'Yes': 1, 'No': 0})

    if model_choice == "Naive Bayes":
        model = GaussianNB()
    else:
        model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X, y)

    pred_input = np.array([[ipk, pelatihan, prestasi, organisasi]])
    pred = model.predict(pred_input)[0]

    if st.button("Prediksi"):
        hasil = "Lulus Cepat" if pred == 1 else "Tidak Lulus Cepat"
        st.success(f"🔮 Hasil Prediksi: **{hasil}**")
