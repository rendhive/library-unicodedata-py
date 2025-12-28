import unicodedata

text = "This is a test string with some special characters: α, β, γ."
non_space_chars = [char for char in text if unicodedata.category(char) != 'Zs']

print("Karakter non-spasi:", ''.join(non_space_chars))
# Fungsi: Menyaring karakter non-spasi dari string.
# Kondisi: Ketika Anda ingin mendapatkan hanya karakter yang tidak berupa spasi.
