import unicodedata

for codepoint in range(0x20, 0x7F):  # Rentang dari spasi hingga tilde
    char = chr(codepoint)
    print(f"{char}: {unicodedata.name(char, 'UNKNOWN')}")
# Fungsi: Mencetak nama karakter untuk karakter yang dapat dicetak.
# Kondisi: Ketika Anda ingin melihat nama untuk karakter dalam rentang spesifik.
