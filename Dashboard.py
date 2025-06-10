import streamlit as st

# Konfigurasi tampilan
st.set_page_config(
    page_title="Prediksi Kelulusan Mahasiswa",
    layout="wide",
    page_icon="🎓"
)

st.title("🎓 Dashboard Prediksi Kelulusan Mahasiswa")
st.markdown("Gunakan sidebar di kiri untuk navigasi ke halaman EDA, pelatihan model, atau melakukan prediksi.")

# Sidebar navigasi
menu = st.sidebar.radio(
    "Navigasi Halaman",
    ("1. EDA", "2. Train Model", "3. Prediksi")
)

if menu == "1. EDA":
    import pages.EDA as eda
    eda.run()

elif menu == "2. Train Model":
    import pages.Modeling as modeling
    modeling.run()

elif menu == "3. Prediksi":
    import pages.Predict as predict
    predict.run()
