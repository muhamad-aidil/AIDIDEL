# Input data
nim = input ("masukkan NIM anda :")
nama = input ("masukkan nama anda :")
kelompok = input ("masukkan kelompok anda :")
asisten = input ("masukkan nama asisten pembimbing Anda :")

last4=(nim[-4:])
ABC = int(last4[:3])
D= int(last4[-1:])

total_belanja = ABC * 1000 #rumus total belanja
# Tentukan jenis membership
silver = 1-4
gold = 5-7
platinum = 8-9
non_member = 0


if 1 <= D <= 4:
    membership = "silver"
    diskon = 5/100
elif 5 <= D <= 7:
    membership = "gold"
    diskon = 10/100
elif 8 <= D <= 9:
    membership ="platinum"
    diskon = 15/100
elif D == 0:
    membership ="non member"
else:
    print("kode tidak valid")

besar_diskon = total_belanja * diskon #rumusbesar diskon
total_setelah_diskon = total_belanja - diskon #rumus total setelah diskon
# Pilih metode pembayaran
print("Pilih metode pembayaran:")
print("1. Tunai")
print("2. QRIS")
print("3. Debit")
pilihan = int(input("Masukkan pilihan (1/2/3): "))

if pilihan == 1:
    metode = "Tunai"
    biaya_tambahan = 0
elif pilihan == 2:
    metode = "QRIS"
    biaya_tambahan = 2500
elif pilihan == 3:
    metode = "Debit"
    biaya_tambahan = 5000
else:
    metode = "Tidak valid"
    biaya_tambahan = 0

#rumus total biaya akhir keseluruhan
total_akhir = total_setelah_diskon+biaya_tambahan

# Tampilkan hasil
print(f"Total Belanja     : Rp{total_belanja:,}")
print(f"Membership        : {membership} ")
print(f"Diskon            : Rp{besar_diskon:,}")
print(f"Setelah Diskon    : Rp{total_setelah_diskon:,}")
print(f"Metode Pembayaran : {metode}")
print(f"Total Bayar Akhir : Rp{total_akhir:,}")
