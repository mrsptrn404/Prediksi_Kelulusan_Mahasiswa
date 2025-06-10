import streamlit as st
import numpy as np
import pickle

st.title("3. Form Prediksi Lulus Cepat")
st.write("Isi input berikut lalu pilih model:")

ipk = st.sidebar.slider("IPK", 0.0, 4.0, 3.0, 0.01)
pelatihan = st.sidebar.number_input("Pelatihan Pengetahuan (0–10)", 0, 10, 5)
prestasi = st.sidebar.number_input("Prestasi (0–50)", 0, 50, 10)
organisasi = st.sidebar.number_input("Kegiatan Organisasi (0–10)", 0, 10, 2)

model_choice = st.sidebar.selectbox("Pilih Model", ["Naive Bayes", "KNN"])

input_data = np.array([[ipk, pelatihan, prestasi, organisasi]])

# Load model
:contentReference[oaicite:31]{index=31}
    :contentReference[oaicite:32]{index=32}
else:
    :contentReference[oaicite:33]{index=33}

:contentReference[oaicite:34]{index=34}
    :contentReference[oaicite:35]{index=35}
    :contentReference[oaicite:36]{index=36}
    :contentReference[oaicite:37]{index=37}
    :contentReference[oaicite:38]{index=38}
    :contentReference[oaicite:39]{index=39}
