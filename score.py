def hitung_score(transportasi, plastik, listrik, air, sampah):

    score = 100

    if transportasi == "Motor":
        score -= 15
    elif transportasi == "Mobil":
        score -= 25
    elif transportasi == "Sepeda":
        score -= 5

    score -= plastik * 3

    if listrik > 8:
        score -= 15
    elif listrik > 5:
        score -= 8

    if air > 20:
        score -= 10
    elif air > 10:
        score -= 5

    if sampah == "Tidak Dipilah":
        score -= 10

    if score < 0:
        score = 0

    return score