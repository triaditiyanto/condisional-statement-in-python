print("==========ATM Statis Dits==========")
print("1. Nabung")
print("2. Tarik Tunai")

menu_atm = input("Pilih menu diatas: ")

if menu_atm == "1":
    nab = input("Masukan nominal yg akan di masukan: ")
    print("Kamu telah memasukan: ", nab)
    # trk = input("Apakah kamu mau tarik tunai ?")

elif menu_atm == "2":
    trk = input("Kamu mau tarik berapa ?: ")
    print("Kamu menarik uang sebesar: ", trk)