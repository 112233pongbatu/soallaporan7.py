def hitung_faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * hitung_faktorial(n - 1)

nilai_n = int(input("Jumlah Nilai n : "))

for i in range(nilai_n, 0, -1):
    faktorial = hitung_faktorial(i)
    print(faktorial, end=" ")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
