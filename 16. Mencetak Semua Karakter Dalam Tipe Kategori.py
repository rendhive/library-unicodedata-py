import unicodedata

characters_by_category = {}

for i in range(0x110000):
    char = chr(i)
    cat = unicodedata.category(char)
    if cat not in characters_by_category:
        characters_by_category[cat] = []
    characters_by_category[cat].append(char)

print("Karakter untuk kategori 'Lm':", characters_by_category.get('Lm', [])[:10])
# Fungsi: Mengelompokkan karakter berdasarkan kategori.
# Kondisi: Ketika Anda ingin mengorganisir karakter ke dalam kategori yang sesuai.
