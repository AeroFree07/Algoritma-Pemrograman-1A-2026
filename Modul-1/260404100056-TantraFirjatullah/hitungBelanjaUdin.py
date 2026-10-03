hargaBuku = 25000
jumlahBuku = 3
totalBuku = hargaBuku * jumlahBuku
hargaPulpen = 8000
jumlahPulpen = 2
totalPulpen = hargaPulpen * jumlahPulpen
totalFlashdisk = 75000
totalSebelumDiskon = totalBuku + totalPulpen + totalFlashdisk
print("Buku: Rp" + str(totalBuku) + " (Rp" + str(hargaBuku) + " x " + str(jumlahBuku) + ")")
print("Pulpen: Rp" + str(totalPulpen) + " (Rp" + str(hargaPulpen) + " x " + str(jumlahPulpen) + ")")
print("Flashdisk: Rp" + str(totalFlashdisk))
print("Subtotal: Rp" + str(totalSebelumDiskon))
diskon = totalSebelumDiskon * float(10) / 100
print("Diskon Semester(10%): Rp" + str(diskon))
setelahDiskon = totalSebelumDiskon - diskon
pajak = setelahDiskon * float(11) / 100
totalBayar = setelahDiskon + pajak
print("Total: Rp" + str(setelahDiskon))
print("PPN 11%: Rp" + str(pajak))
print("Total (+PPN): Rp" + str(totalBayar))
uangDibayar = 200000
kembalian = uangDibayar - totalBayar
print("Uang kembalian: Rp" + str(kembalian))
