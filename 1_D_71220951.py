nilaihujan = float(input("Masukkan nilai curah hujan : "))

print("Cuaca Terang/Berawan") if (nilaihujan == 0) else print ("Curah hujan ringan") if (0.5 <= nilaihujan <= 20) else print ("Curah hujan sedang") if (21 <= nilaihujan <= 50) else print("Curah hujan lebat") if (51 <= nilaihujan <= 100 ) else print("Curah hujan ekstrem") if (nilaihujan >= 100) else print("tidak teridentifikasi")