jarakDestinasi  = 100
jarakPerLiter   = 40
bensinPerLiter  = 10000
bensinSaatIni   = 1.5

jarakPulangPergi = jarakDestinasi * 2
totalBahanBakar = jarakPulangPergi / jarakPerLiter
bahanBakarDiisi = totalBahanBakar - bensinSaatIni
totalBiaya = bahanBakarDiisi * bensinPerLiter

print(f"Jarak yang harus ditempuh: {jarakPulangPergi}km")
print(f"Banyak Bahan Bakar yang dibutuhkan: {totalBahanBakar}L")
print(f"Banyak Bahan Bakar yang perlu di-isi: {bahanBakarDiisi}L")
print(f"Total Biaya: Rp{totalBiaya}")

hargaBesinSendiri = bensinSaatIni * bensinPerLiter
print(f"Nilai Harga Bensin Dimas Rp{hargaBesinSendiri}")