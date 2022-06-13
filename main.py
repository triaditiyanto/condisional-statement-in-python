print("====APLIKASI BAYAR UTANG====")

uang = input("Silahkan masukan nominal uang nya: Rp.")
utang = input("Masukan utang kamu: Rp.")

if int(uang) < int(utang):
    print("Waduh uang kamu kurang :( ")

elif int(uang) == int(utang):
    print("Selamat kamu terbebas dari hutang !!!")

else:
    # var = int(uang) == int(utang)
    res = int(uang)-int(utang)
    print("Uangnya kelebihan", "Rp.", res,"nih !?!!")