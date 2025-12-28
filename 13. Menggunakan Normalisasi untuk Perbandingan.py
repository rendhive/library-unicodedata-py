import unicodedata

text1 = "Mañana"
text2 = "Mañana"  # 'n' dengan tilde terpisah

# Normalisasi kedua teks ke bentuk NFC
normalized1 = unicodedata.normalize('NFC', text1)
normalized2 = unicodedata.normalize('NFC', text2)

print("Teks sama setelah normalisasi:", normalized1 == normalized2)
# Fungsi: Membandingkan dua string setelah normalisasi.
# Kondisi: Ketika Anda perlu memeriksa kesamaan antara dua string yang serupa.
