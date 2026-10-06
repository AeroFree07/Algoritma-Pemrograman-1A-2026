print("Perhitungan Volume Kerucut")

jari_jari = float(input("Masukkan panjang jari-jari alas (cm): "))
tinggi = float(input("Masukkan tinggi kerucut (cm): "))

volume = (1/3) * 22/7 * (jari_jari ** 2) * tinggi

print("Volume kerucut dengan jari-jari alas", jari_jari, "cm dan tinggi", tinggi,"cm")
print("adalah:", volume)