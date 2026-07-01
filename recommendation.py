def rekomendasi(data):

    saran = []

    if data["transportasi"] == "Motor":
        saran.append("Gunakan jalan kaki atau sepeda untuk perjalanan dekat.")

    if data["transportasi"] == "Mobil":
        saran.append("Gunakan transportasi umum bila memungkinkan.")

    if data["plastik"] >= 2:
        saran.append("Gunakan tumbler agar mengurangi sampah plastik.")

    if data["listrik"] > 8:
        saran.append("Kurangi penggunaan AC atau matikan alat listrik yang tidak digunakan.")

    if data["air"] > 15:
        saran.append("Kurangi durasi mandi agar lebih hemat air.")

    if data["sampah"] == "Tidak Dipilah":
        saran.append("Mulailah memilah sampah organik dan anorganik.")

    if len(saran) == 0:
        saran.append("Kebiasaanmu sudah sangat baik. Pertahankan!")

    return saran