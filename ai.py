from score import hitung_score
from recommendation import rekomendasi


def analisis(data):

    score = hitung_score(
        data["transportasi"],
        data["plastik"],
        data["listrik"],
        data["air"],
        data["sampah"]
    )

    saran = rekomendasi(data)

    return score, saran