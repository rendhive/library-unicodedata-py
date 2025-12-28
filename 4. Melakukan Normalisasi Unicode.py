import unicodedata

text = "Café"
normalized = unicodedata.normalize('NFC', text)

print("Normalisasi teks:", normalized)
# Fungsi: Melakukan normalisasi pada string Unicode.
# Kondisi: Ketika Anda ingin memastikan bahwa string dalam bentuk normal yang diinginkan.
