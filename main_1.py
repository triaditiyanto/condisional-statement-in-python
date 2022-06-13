from fileinput import close


print("====APLIKASI PERHITUNGAN====")
print("1. Pertambahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Menghitung luas persegi")
print("----------------------")

menu = input("Pilih Menu : ")

if menu == "1":
    x = input("Masukan nilai pertama: ")
    y = input("Masukan nilai kedua: ")
    res = int(x)+int(y)
    print("Hasil penjumlahan dari ", x ,"+", y, "adalah = ", res)

elif menu == "2":
    y = input("Masukan nilai pertama: ")
    z = input("Masukan nilai kedua: ")
    res = int(y)-int(z)
    print("Hasil pengurangan dari ", y, "-", z,"adalah = ", res)   

elif menu == "3":
    a = input("Masukan nilai pertama: ")
    b = input("Masukan nilai kedua: ")
    resu = int(a)*int(b)
    print("Hasil Perkalian dari ", a, "*", b, "adalah = ", resu)

elif menu == "4":
    p = input("Masukan panjang: ")
    l = input("Masukan lebar: ")
    sol = int(p)*int(l)
    print("Luas persegi adalah: ",sol)