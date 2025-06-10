# 🎓 Dashboard Prediksi Kelulusan Mahasiswa (Lulus Cepat atau Tidak)

Dashboard interaktif menggunakan Streamlit untuk memprediksi apakah seorang mahasiswa akan **lulus tepat waktu (lulus cepat)** atau tidak, berdasarkan data IPK, pelatihan pengetahuan, prestasi, dan kegiatan organisasi.

---

## 📊 Fitur Aplikasi

✅ Halaman 1 - **EDA (Exploratory Data Analysis)**  
Menampilkan karakteristik dataset, statistik deskriptif, dan visualisasi hubungan antar fitur.

✅ Halaman 2 - **Train Model**  
Melatih dua model Machine Learning:  
- Naive Bayes  
- K-Nearest Neighbors (KNN)  
Lalu menampilkan metrik akurasi dan classification report.

✅ Halaman 3 - **Form Prediksi**  
User mengisi data input, lalu memilih model (Naive Bayes / KNN) untuk memprediksi apakah akan lulus cepat atau tidak.

---

## 🧠 Dataset

Dataset diambil dari Kaggle:  
📎 [Dataset Kelulusan Mahasiswa - Kaggle](https://www.kaggle.com/datasets/christopherbayuaji/dataset-kelulusan)

### Fitur:
- `IPK`  
- `Pelatihan Pengetahuan` (0–10)  
- `Prestasi` (0–50)  
- `Kegiatan Organisasi` (0–10)  
- `Lulus Cepat` (Yes/No)

---

## 🛠️ Cara Install & Jalankan

### 1. Clone Repository
```bash
git clone https://github.com/username/lulus-cepat-dashboard.git
cd lulus-cepat-dashboard
