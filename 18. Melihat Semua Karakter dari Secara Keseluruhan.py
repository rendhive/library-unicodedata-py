import unicodedata

for i in range(128):  # Hanya akan mencetak karakter ASCII
    char = chr(i)
    print(f"{i}: {char} --> {unicodedata.name(char, 'UNKNOWN')}")
# Fungsi: Mengeluarkan semua karakter Unicode dan nama mereka.
# Kondisi: Ketika Anda ingin menyediakan daftar karakter dan nama mereka.
