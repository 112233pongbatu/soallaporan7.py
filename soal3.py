jumlah_tinggi = int(input("Tinggi : "))
jumlah_lebar = int(input("Lebar : "))

nilai_n = 1

for i in range(jumlah_tinggi):
    for j in range(jumlah_lebar):
        print(nilai_n, end=" ")
        nilai_n += 1
    print() 
