import streamlit as st
import joblib

# Load model
model = joblib.load("model_klasifikasi.pkl")

# Title Page
st.markdown(
    """
    <div style='text-align: center; padding: 20px 0'>
        <h1 style='color: #FFFFFF;'>🎓 Klasifikasi Topik Tugas Mahasiswa</h1>
        <p style='font-size: 18px;'>Masukkan judul tugas, dan sistem akan memprediksi topiknya secara otomatis.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Input judul tugas
judul = st.text_input("📌 Masukkan Judul Tugas", placeholder="Contoh: Sistem Monitoring Suhu dan Kelembaban Berbasis IoT")

# Tombol prediksi
if st.button("🔍 Prediksi", use_container_width=True):
    if judul.strip() != "":
        prediksi = model.predict([judul])[0]

        st.markdown(
            f"""
            <div style='background-color: #008060; padding: 20px; border-radius: 10px; text-align: center;'>
                <h3 style='color: white;'>✅ Topik yang diprediksi:</h3>
                <h1 style='color: white;'>{prediksi}</h1>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning("Judul tidak boleh kosong.")

# Footer / spacing
st.markdown("<br><hr><div style='text-align: center;'>© 2025 - Sistem Klasifikasi Topik Mahasiswa</div>", unsafe_allow_html=True)

# Optional: Page config
st.set_page_config(page_title="Klasifikasi Topik", page_icon="🎓", layout="centered")
