import unicodedata

text = "Hello, World! 1234."
filtered_text = ''.join(char for char in text if unicodedata.category(char) not in ['Zs', 'Po'])

print("Teks tanpa spasi dan tanda baca:", filtered_text)
# Fungsi: Menyaring karakter tertentu dari string.
# Kondisi: Ketika Anda hanya ingin menyimpan huruf dan angka.
