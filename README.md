# 🎓 Klasifikasi Topik Tugas Mahasiswa Berdasarkan Judul 🤖

📌 **Natural Language Processing + Machine Learning**  
📌 **Prediksi Otomatis Berdasarkan Judul Tugas**  
📌 **Tampilan Interaktif dengan Streamlit**  
📌 **Bisa Prediksi Judul di Luar Dataset!**

---

## 🚀 FITUR UNGGULAN

✨ Pembersihan Teks Otomatis  
📊 TF-IDF untuk Ekstraksi Fitur  
🤖 SVM (Support Vector Machine) sebagai Model Klasifikasi  
📈 Evaluasi Akurat: Precision, Recall, F1-Score, Confusion Matrix  
🖥️ Aplikasi Web Interaktif (GUI) dengan Streamlit  
🆕 Bisa Prediksi Judul Baru!

---

## 🗂️ STRUKTUR PROYEK

- `app.py` → Aplikasi GUI Streamlit  
- `train_model.py` → Latih & Simpan Model  
- `model_klasifikasi.pkl` → File Model  
- `dataset_topik_judul_100_expanded.csv` → Dataset  
- `README.md` → Dokumentasi Proyek Ini  

---

## ⚙️ CARA MENJALANKAN

### 1️⃣ Clone Repositori
```bash
git clone https://github.com/username/nama-repo.git
cd nama-repo
```

### 2️⃣ Install Semua Dependensi
```bash
pip install pandas numpy matplotlib seaborn scikit-learn wordcloud streamlit joblib
```

### 3️⃣ Latih Model (Kalau Belum Ada)
```bash
python train_model.py
```

### 4️⃣ Jalankan Aplikasinya
```bash
streamlit run app.py
```

---

## 🧪 CONTOH PREDIKSI

📝 **Input Judul:**  
`Klasifikasi Citra Udara Menggunakan Machine Learning`

✅ **Hasil Prediksi:**  
`Machine Learning`

Aplikasi mampu mengenali pola meskipun judul **tidak terdapat di dalam dataset pelatihan**. Ini menunjukkan bahwa model memiliki **kemampuan generalisasi yang baik**.

---

## 📊 EVALUASI MODEL

✔️ **Confusion Matrix** menunjukkan prediksi model tepat pada tiap topik  
✔️ Nilai **Precision, Recall, dan F1-Score** konsisten tinggi di semua kelas  
✔️ Diuji dengan berbagai judul baru dan memberikan hasil yang akurat  

---

## 📚 TOPIK YANG DIDUKUNG

- IoT  
- Web  
- Mobile Apps  
- Machine Learning  
- AI  
- Jaringan  
- Kesehatan  
- Data Mining  

---

## 👨‍💻 DEVELOPER

Kelompok 4 - Tema 8:  
- Rafly Akbar Ravsanjani  
- Idham Kholid Nur Azizi  

---

## 📝 LISENSI

🔓 Bebas digunakan untuk edukasi & pengembangan lebih lanjut  
📌 Silakan dimodifikasi dengan tetap mencantumkan atribusi  
🚀 Dibangun menggunakan Python, Streamlit, dan Scikit-learn
