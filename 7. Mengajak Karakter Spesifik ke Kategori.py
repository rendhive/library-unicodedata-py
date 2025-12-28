import unicodedata

text = "Hello, 123! ©"
for char in text:
    print(f"'{char}': {unicodedata.category(char)}")
# Fungsi: Mengambil kategori untuk setiap karakter dalam teks.
# Kondisi: Ketika Anda ingin menganalisis semua karakter dalam string.
