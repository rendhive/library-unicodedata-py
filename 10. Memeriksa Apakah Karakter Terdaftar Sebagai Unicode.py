import unicodedata

char = '😊'
is_valid = unicodedata.category(char) != 'Cn'

print(f"Apakah '{char}' adalah karakter yang valid?", is_valid)
# Fungsi: Memeriksa apakah karakter adalah karakter Unicode yang dikenal.
# Kondisi: Ketika Anda ingin mendapatkan validasi karakter.
