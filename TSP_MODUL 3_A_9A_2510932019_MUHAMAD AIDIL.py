nama = input(' masukkan nama anda : ')
PIN = input("masukkan NIM anda : ")
percobaan = 0
kesempatan = 3

while percobaan < kesempatan:
    pin_admin= input('masukkan PIN admin bioskop anda :')
    if pin_admin == PIN :
        print('PIN adnda benar! selamat datang di bisokop!')
        while True:
            print('===LIST FLIM DAN HARGA DI BIOSKOP===')
            print('1. KIMETSU NO YAIBA (50000)')
            print('2. MARVEL(45000)')
            print('3. ONE PIECE(40000)')
            print('4. SPIDER-MAN(35000)')
            
            pilih_flim = input('pilih flim yang ingin anda tonton (1/2/3/4): ')
            jumlah_pesanan = int(input('masukkan jumlah tiket yang ingin anda beli: '))
            

            if pilih_flim == '1':
                     total_biaya = 50000 * jumlah_pesanan
                     print('flim pilihan anda adalah kimetsu no yaiba dan total biaya adalah', total_biaya)

            elif pilih_flim == '2':
                     total_biaya = 45000 * jumlah_pesanan
                     print('flim pilihan anda adalah marvel dan total biaya adalah', total_biaya)

            elif pilih_flim == '3':
                     total_biaya = 40000 * jumlah_pesanan
                     print('flim pilihan anda adalah one piece dan total biaya adalah', total_biaya)

            elif pilih_flim == '4':
                     total_biaya = 35000 * jumlah_pesanan
                     print('flim pilihan anda adalah spider-man dan total biaya adalah', total_biaya)
            else:
                  print('maaf pilihan tidak tersedia')
                    
            pilih = input('apakah anda ingin melakukan transaksi lagi? (ya/tidak) : ')
            if pilih == 'ya':
                continue
            elif pilih == 'tidak':
                print('terimakasih sudah menonton di bioskop ini')
                exit()
    else :
        kesempatan = kesempatan - 1
        if percobaan < kesempatan:
            print('PIN anda salah! coba lagi')
        elif percobaan == kesempatan:
            print('kesempatan habis! program selesai')
            break
           
print('terimakasih sudah menonton di bioskop ini')

            