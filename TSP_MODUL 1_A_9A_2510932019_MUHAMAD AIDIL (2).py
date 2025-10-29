#INFORMASI
print("nama : Muhamad Aidil")
print("NIM  : 2510932019")
print("kelompok: 9A")
print("Asisten pembimbing : Viona Aura Rianni")
print(50*"=")

#1.tampilkan nilai AB CD 
AB  = int(input('masukkan total pemakaian kwh bulan pertama = '))
CD = int(input('masukkan total pemakaian kwh bulan kedua =  '))
print("")
#2. total pemakaian kwh dalam 2 bulan
total_pemakaian_2_bulan = AB + CD
print('total pemakaian dalam 2 bulan ', total_pemakaian_2_bulan, 'kwh')
print("")
#3.biaya energi yang dikeluarkan pada masing masing bulan 
biaya_energi_bulan_1 = AB * 1500 
print('total pemakaian energi bulan pertama adalah', 'Rp', biaya_energi_bulan_1)
biaya_energi_bulan_2 = CD * 1500 
print('total pemakaian energi bulan kedua adalah', 'Rp', biaya_energi_bulan_2)
print("")
#4.biaya yang dikeluarkan selama 2 bulan sebelum adanya pajak dan biaya administrasi
biaya_energi_total = biaya_energi_bulan_1 + biaya_energi_bulan_2
print('total biaya energi total selama dua bulan adalah', 'Rp', biaya_energi_total)
print("")
#5. pajak yang dikeluarkan pada total kedua bulan
pajak = 5/100 * biaya_energi_total
print('total pajak yang dikeluarkan adalah', 'Rp', pajak)
print("")
#6Hitung biaya administrasi yang dikeluarkan pada total kedua bulan!
biaya_beban_tetap = 20000 * 2
total_biaya_A= biaya_energi_total + pajak + biaya_beban_tetap
biaya_administrasi = 2 / 100 * total_biaya_A
print('total biaya adminsitrasi adalah', 'Rp', biaya_administrasi)
print("")
#7. total tagihan dari biaya yang dikeluarkan pada total kedua bulan
total_tagihan = total_biaya_A + biaya_administrasi
print('total tagihan dari kedua bulan adalah', 'Rp', total_tagihan )




