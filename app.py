import streamlit as st
import pandas as pd
import os

from ai import analisis
from history import simpan
from challenge import eco_challenge

st.set_page_config(
    page_title="EcoHabit AI",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 EcoHabit AI")
st.subheader("Ubah Kebiasaan Kecil Menjadi Dampak Besar")

st.write("""
Selamat datang di **EcoHabit AI**.

Aplikasi ini membantu menganalisis kebiasaan harianmu
dan memberikan rekomendasi berbasis AI agar lebih
ramah lingkungan.
""")

st.divider()

st.header("📝 Input Aktivitas Harian")

nama = st.text_input(
    "Nama",
    placeholder="Masukkan nama"
)

transportasi = st.selectbox(
    "Transportasi Utama",
    [
        "Jalan Kaki",
        "Sepeda",
        "Motor",
        "Mobil"
    ]
)

plastik = st.slider(
    "Berapa botol plastik sekali pakai hari ini?",
    0,
    10,
    0
)

listrik = st.slider(
    "Lama penggunaan listrik / AC (jam)",
    0,
    24,
    5
)

air = st.slider(
    "Durasi mandi (menit)",
    1,
    30,
    10
)

sampah = st.selectbox(
    "Apakah sampah dipilah?",
    [
        "Dipilah",
        "Tidak Dipilah"
    ]
)

if st.button("🔍 Analisis EcoHabit"):

    data = {
        "transportasi": transportasi,
        "plastik": plastik,
        "listrik": listrik,
        "air": air,
        "sampah": sampah
    }

    score, saran = analisis(data)

    simpan(nama, score)

    st.divider()

    st.header("🌍 Hasil Analisis")

    st.metric(
        "Eco Score",
        f"{score}/100"
    )

    if score >= 85:

        st.success("🟢 Sangat Ramah Lingkungan")

    elif score >= 70:

        st.info("🟡 Cukup Baik")

    elif score >= 50:

        st.warning("🟠 Perlu Perbaikan")

    else:

        st.error("🔴 Kurang Ramah Lingkungan")
        
    st.subheader("🤖 Analisis AI")

    if score >= 85:

        st.write("""
Kebiasaanmu sudah cukup baik.

Pertahankan gaya hidup ramah lingkungan
dan ajak orang lain untuk ikut peduli.
""")

    elif score >= 70:

        st.write("""
Masih ada beberapa kebiasaan yang dapat
ditingkatkan agar dampaknya terhadap
lingkungan menjadi lebih kecil.
""")

    else:

        st.write("""
AI menemukan beberapa kebiasaan yang
cukup berdampak terhadap lingkungan.
Perubahan kecil setiap hari akan sangat membantu.
""")
        
    st.subheader("💡 Rekomendasi AI")

    for item in saran:

        st.write("✅", item)
        
    st.subheader("🎯 Eco Challenge")

    daftar = eco_challenge(score)

    for c in daftar:

     st.checkbox(c)
    
     st.divider()

     st.header("📊 Dashboard EcoHabit AI")

try:

    df = pd.read_csv("history.csv")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Jumlah Pengguna",
            len(df)
        )

    with col2:
        st.metric(
            "Rata-rata Eco Score",
            round(df["Score"].mean(),1)
        )

    st.subheader("Grafik Eco Score")

    st.bar_chart(df["Score"])

except:
    st.info("Belum ada data.")
    
st.divider()

st.subheader("🏆 Top 5 Eco Score")

try:

    top = df.sort_values(
        by="Score",
        ascending=False
    )

    st.dataframe(top.head(5))

except:
    pass

    st.divider()

    st.subheader("📜 Riwayat Analisis")

try:

    st.dataframe(df)

except:
    pass
