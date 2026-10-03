konsumsiMontor = 40 
hargaBensin = 10000
bensinAwal = 1.5

print("Rayong ingin pulang kmapung dan dia belum mengetahui total biaya, bantulah Dimas dalam menghitung total biaya perjalanan")

jarakTempuh = int(input("\nMasukkan Jarak Perjalanan Pulang Kampung Rayong = "))

print("\nJarak Tempuh")

pulangPergi = jarakTempuh * 2
print("JARAK PULANG PERGINYA RAYONG = ", pulangPergi, "KM")

print("\nTotal Bensin Yang Dibutuhkan")
kebutuhanBensin = pulangPergi / konsumsiMontor
bensinYangDibeli = kebutuhanBensin - bensinAwal
print("KEBUTUHAAN BENSIN KESELURUHAN =", kebutuhanBensin, "liter")

print("\nBensin Yang Harus Dibeli Di SPBU")
bensinYangHarusDibeli = kebutuhanBensin - bensinAwal
print("BENSIN YANG HARUS DI BELI DIMAS = ", bensinYangHarusDibeli, "Liter")


print("\nTotal Biaya")
totalBiaya = bensinYangDibeli * hargaBensin

print("Total Biaya Yang Dibutuhkan Rayong Ketika Pulkam = Rp", totalBiaya)

hargaBensinSaya = bensinAwal * hargaBensin 
print(hargaBensinSaya)