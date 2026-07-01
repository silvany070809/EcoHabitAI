def eco_challenge(score):

    if score >= 85:

        return [
            "Ajak satu teman ikut peduli lingkungan.",
            "Bawa tumbler setiap hari.",
            "Matikan lampu saat keluar ruangan."
        ]

    elif score >= 60:

        return [
            "Kurangi penggunaan plastik.",
            "Jalan kaki minimal 1 km minggu ini.",
            "Pisahkan sampah."
        ]

    else:

        return [
            "Kurangi penggunaan motor.",
            "Gunakan botol minum isi ulang.",
            "Mandi maksimal 10 menit.",
            "Pisahkan sampah setiap hari."
        ]