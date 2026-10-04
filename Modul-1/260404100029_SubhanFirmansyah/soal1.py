uang = 100000*2
buku = 25000*3
bolpoin = 8000*2
flashdisk = 75000

total = buku + bolpoin + flashdisk
diskon = total * 0.10
setelahDiskon = total - diskon
pajak = setelahDiskon * 0.11
totalBayar = setelahDiskon + pajak
kembalian = uang - totalBayar

print("total uang adalah : Rp.",uang)
print("total harga buku adalah : Rp.",buku)
print("total harga bolpoin adalah : Rp.",bolpoin)
print("total harga flashdisk adalah : Rp.",flashdisk)
print("total harga sebelum diskon dan di sebelum dipotong pajak adalah : Rp.",total)
print("total diskon nya adalah : Rp.",diskon)
print("total harga setelah diskon adalah : Rp.",setelahDiskon)
print("total pajaknya adalah : Rp.",pajak)
print("total harga semuanya adalah : Rp.",totalBayar)
print("total kembalian nya adalah : RP.", kembalian)
