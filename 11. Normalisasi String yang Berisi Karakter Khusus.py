import unicodedata

text = "Déjà vu"
normalized_text = unicodedata.normalize('NFD', text)

print("Normalisasi NFD:", normalized_text)
# Fungsi: Mengkonversi string menjadi bentuk normal dekomposisi.
# Kondisi: Ketika Anda ingin memisahkan karakter aksen dari huruf dasarnya.
