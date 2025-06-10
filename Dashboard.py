# dashboard.py
import streamlit as st

st.set_page_config(
    page_title="Dashboard Prediksi Kelulusan Mahasiswa",
    layout="wide",
    page_icon="🎓"
)

st.title("🎓 Dashboard Prediksi Kelulusan Mahasiswa")
st.markdown("""
Selamat datang!  
Dashboard ini memprediksi apakah mahasiswa akan **lulus cepat** berdasarkan IPK, pelatihan, prestasi, dan kegiatan organisasi.

Gunakan sidebar untuk berpindah antar halaman:
- **EDA**: Eksplorasi Data
- **Modeling**: Pelatihan Model
- **Prediksi**: Input data dan lihat hasil prediksi
""")

menu = st.sidebar.radio("📁 Menu", ["EDA", "Modeling", "Prediksi"])

if menu == "EDA":
    import pages.EDA as eda
    eda.run()

elif menu == "Modeling":
    import pages.Modeling as modeling
    modeling.run()

elif menu == "Prediksi":
    import pages.Predict as predict
    predict.run()
