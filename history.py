import csv
import os

FILE = "history.csv"


def simpan(nama, score):

    file_baru = not os.path.exists(FILE)

    with open(FILE, "a", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)

        if file_baru:
            writer.writerow(["Nama", "Score"])

        writer.writerow([nama, score])