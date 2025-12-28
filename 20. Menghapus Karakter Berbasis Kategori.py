import unicodedata

text = "Thérè äre m4ny kînds!"
filtered_text = ''.join(char for char in text if unicodedata.category(char) != 'Mn')  # Menghilangkan tanda diakritik

print("Teks setelah menghapus diakritik:", filtered_text)
# Fungsi: Menghapus karakter berdasarkan kategori (tanda diakritik).
# Kondisi: Ketika Anda ingin membersihkan teks dari tanda yang tidak perlu.
