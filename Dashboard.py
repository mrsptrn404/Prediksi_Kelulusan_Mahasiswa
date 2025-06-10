import streamlit as st

# Konfigurasi awal tampilan dashboard
st.set_page_config(
    page_title="Dashboard Prediksi Kelulusan Mahasiswa",
    layout="wide",
    page_icon="🎓"
)

# Judul utama
st.title("🎓 Dashboard Prediksi Kelulusan Mahasiswa")

# Deskripsi singkat
st.markdown("""
Selamat datang di dashboard prediksi kelulusan mahasiswa!  
Gunakan sidebar untuk berpindah antar halaman:

- **EDA**: Eksplorasi Data
- **Modeling**: Pelatihan Model
- **Prediksi**: Input data dan lihat hasil prediksi
""")

# Sidebar untuk navigasi
menu = st.sidebar.radio("📁 Menu", ["EDA", "Modeling", "Prediksi"])

# Routing halaman
if menu == "EDA":
    import pages.EDA as eda
    eda.run()

elif menu == "Modeling":
    import pages.Modeling as modeling
    modeling.run()

elif menu == "Prediksi":
    import pages.Predict as predict
    predict.run()
