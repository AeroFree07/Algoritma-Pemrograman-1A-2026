saldoUdin = 100000 * 2
totalBuku = 3 * 25000
totalPulpen = 2 * 8000
totalFlashdisk = 1 * 75000
subtotal = totalBuku + totalPulpen + totalFlashdisk
promo = subtotal * 0.1
hargaSetelahPromo = subtotal - promo
ppn = hargaSetelahPromo * 0.11
totalBayar = hargaSetelahPromo + ppn
kembalian = saldoUdin - totalBayar

print("Saldo Udin sekarang adalah : " + str(saldoUdin))
print("Total harga 3 buku : " + str(totalBuku) + chr(13) + "Total harga 2 pulpen : " + str(totalPulpen) + chr(13) + "Total harga 1 flashdisk : " + str(totalFlashdisk) + chr(13) + "Total harga seluruh barang sebelum promo : " + str(subtotal) + chr(13) + "Mendapat promo 10% : " + str(promo) + chr(13) + "Total harga setelah mendapat promo : " + str(hargaSetelahPromo) + chr(13) + "Biaya Admin/PPN sebesar 11% : " + str(ppn) + chr(13) + "Total yang Harus di bayar Udin : " + str(totalBayar) + chr(13) + "Total uang Udin setelah membeli barang-barang : " + str(kembalian))
