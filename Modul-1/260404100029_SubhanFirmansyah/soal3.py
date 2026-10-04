jarak = 100 
konsumsiBensin = 40
sisaBensin = 1.5
hargaBensin = 10000

totalJarak = jarak*2
print ("jarak yang ditempuh :", totalJarak, "kilo meter")

kebutuhanBensin = totalJarak / konsumsiBensin
print("konsumsi bensin : ", konsumsiBensin, "km liter")
print ("bensin yang dibutuhkan :", kebutuhanBensin, "liter")

beliBensin = kebutuhanBensin - sisaBensin
print("jumlah bensin yang harus dibeli :", beliBensin)

totalBeliBensin = hargaBensin * beliBensin
print("total biaya dimas untuk membeli bensin :", totalBeliBensin)