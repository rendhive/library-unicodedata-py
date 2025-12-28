import unicodedata

category = 'Lu'  # Huruf kapital
characters = [chr(i) for i in range(0x110000) if unicodedata.category(chr(i)) == category]

print("Karakter huruf kapital:", characters[:10])  # Menampilkan 10 karakter pertama
# Fungsi: Mengambil semua karakter dalam kategori tertentu.
# Kondisi: Ketika Anda ingin mengetahui semua karakter di kategori sangat spesifik.
