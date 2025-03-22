def bilangan_prima(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def bilangan(n):
    for i in range(n - 1, 1, -1):
        if bilangan_prima(i):
            return i
    return None 

n = int(input("Masukkan bilangan: "))
nilai_terdekatnya = bilangan(n)

if nilai_terdekatnya:
    print(f"Bilangan prima terdekat < {n} adalah {nilai_terdekatnya}")
else:
    print("Tidak ada bilangan prima yang lebih kecil dari n.")
