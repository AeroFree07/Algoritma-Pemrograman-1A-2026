jumlahBuku = 3
hargaBuku = 25000
totalBuku = jumlahBuku * hargaBuku
jumlahPulpen = 2
hargaPulpen = 8000
totalPulpen = jumlahPulpen * hargaPulpen
jumlahFlashdisk = 1
hargaFlashdisk = 75000
totalFlashdisk = jumlahFlashdisk * hargaFlashdisk
totalBarang = totalBuku + totalPulpen + totalFlashdisk
diskon = float(totalBarang * 10) / 100
setelahDiskon = totalBarang - diskon
ppn = float(setelahDiskon * 11) / 100
totalBayar = setelahDiskon + ppn
uangDibayar = 200000
kembalian = uangDibayar - totalBayar
print("totalBuku: " + str(totalBuku))
print("totalPulpen: " + str(totalPulpen))
print("totalFlashdisk: " + str(totalFlashdisk))
print("totalBarang: " + str(totalBarang))
print("diskon: " + str(diskon))
print("setelahDiskon: " + str(setelahDiskon))
print("ppn: " + str(ppn))
print("totalBayar: " + str(totalBayar))
print("kembalian: " + str(kembalian))
