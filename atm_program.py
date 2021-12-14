import random as rd
import datetime as dt
from customer import Customer

atm = Customer(id)

while True:
    id = int(input("Masukkan nomer pin Anda:"))
    trial = 0
    while (id != int(atm.checkPin()) and trial < 3):
        id = int(input("Pin anda salah. Silakan Masukkan lagi: "))
        trial += 1
        if trial == 3:
            print("Error. Silakan ambil kartu dan coba lagi..")
            exit()
    while True:
        print("Selamat datang di ATM Progate..")
        print("\n1- Cek Saldo \t 2 - Debet \t 3 - Simpan \t 4- Ganti Pin \t 5 - Keluar")
        selectmenu = int(input("\nSilakan pilih Menu:"))
        if selectmenu == 1:
            print("\nSaldo anda sekarang: Rp. " + str(atm.checkBalance()) + "\n")
        elif selectmenu == 2:
            print("Debet")
            nominal = float(input("Masukkan nominal saldo: "))
            verify_withdraw = input("Konfirmasi: Anda akan melakukan debet dengan nominal berikut ? y/n\n" + str(nominal) + "\n")
            if verify_withdraw == "y":
                print("Saldo awal anda adalah: Rp. " + str(atm.checkBalance()) + "")
            else:
                break
            if nominal < atm.checkBalance():
                atm.withdrawBalance(nominal)
                print("Transaksi debet berhasil!")
                print("Saldo sisa sekarang: Rp. " + str(atm.checkBalance()) + "")
            else:
                print("Maaf. Saldo anda tidak cukup untuk melakukan debet!")
                print("Silahkan lakukan penambahan nominal saldo")
        elif selectmenu == 3:
            nominal = float(input("Masukkan nominal saldo: "))
            verify_withdraw = input(
                "Konfirmasi: Anda akan melakukan debet dengan nominal berikut ? y\n " + str(nominal) + " ")
            if verify_withdraw == "y":
                print("Saldo awal anda adalah: Rp. " + str(atm.checkBalance()) + "")
            else:
                break
        elif selectmenu == 4:
            verify_pin = int(input("masukkan pin anda: "))
            while verify_pin != int(atm.checkPin()):
                print("pin anda salah, silakan masukkan pin:")
            updated_pin = int(input("silakan masukkan pin baru:"))
            print("pin anda berhasil diganti!")
            verify_newpin = int(input("coba masukkan pin baru: "))
            if verify_newpin == updated_pin:
                print("pin baru anda sukses!")
            else:
                print("maaf, pin anda salah!")
        elif selectmenu == 5:
            print("Resi tercetak otomatis saat anda keluar.\n Harap simpan tanda terima ini \n sebagai bukti transaksi anda.")
            print("No. Rekord: ", rd.randint(100000, 1000000))
            print("Tanggal: ", dt.datetime.now())
            print("Saldo akhir: ", atm.checkBalance())
            print("Terima kasih telah menggunakan ATM Progate!")
            exit()
        else:
            print("Error. maaf, menu tidak tersedia")
