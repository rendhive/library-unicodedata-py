import unicodedata

def is_valid_unicode(char):
    return unicodedata.category(char) != 'Cn'  # 'Cn' adalah karakter yang tidak dikenal

test_char = '€'
print(f"Apakah karakter '{test_char}' valid?", is_valid_unicode(test_char))
# Fungsi: Memvalidasi apakah karakter termasuk dalam Unicode yang terdaftar.
# Kondisi: Ketika Anda ingin memastikan karakter input valid dalam konteks Unicode.
