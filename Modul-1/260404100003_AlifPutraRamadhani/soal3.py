jarakPerjalanan = 100
konsumsiBahanBakar = 40 
sisaBahanBakar = 1.5 
hargaBahanBakar = 10000

totalJarakPerjalanan = jarakPerjalanan * 2
totalKebutuhanBahanBakar = totalJarakPerjalanan / konsumsiBahanBakar
bahanBakarDibeli = totalKebutuhanBahanBakar - sisaBahanBakar
totalBiayaBahanBakar = bahanBakarDibeli * hargaBahanBakar

print("--- Rincian Perjalanan Dimas ---")
print("Total jarak perjalanan (PP)  : ", totalJarakPerjalanan, "km")
print("Total kebutuhan bahan bakar  : ", totalKebutuhanBahanBakar, "liter")
print("Bahan bakar yang dibeli        : ", bahanBakarDibeli, "liter")
print("Total biaya bahan bakar        : Rp", totalBiayaBahanBakar)
