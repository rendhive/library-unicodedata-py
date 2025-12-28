import unicodedata

for codepoint in range(65, 91):  # Rentang karakter A-Z
    char = chr(codepoint)
    print(f"{char}: {unicodedata.name(char)}")
# Fungsi: Menampilkan nama untuk setiap karakter dalam range.
# Kondisi: Ketika Anda ingin mencetak nama semua karakter huruf besar.
