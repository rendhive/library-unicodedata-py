import unicodedata

name = "LATIN SMALL LETTER E WITH ACUTE"
code_point = unicodedata.lookup(name)

print(f"Kode titik untuk '{name}': {hex(ord(code_point))}")
# Fungsi: Mengambil kode titik Unicode berdasarkan nama.
# Kondisi: Ketika Anda ingin mengetahui kode poin dari karakter berdasarkan namanya.
