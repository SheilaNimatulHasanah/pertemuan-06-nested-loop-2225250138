# Latihan 2: Pola Segitiga

# Menerima input n positif dari pengguna
n = int(input("n: "))

# Loop luar (i): mengontrol jumlah baris dari 1 sampai n
for i in range(1, n + 1):
    # Loop dalam (j): mengontrol jumlah bintang pada baris ke-i (sebanyak i kali)
    for j in range(i):
        # Output: mencetak bintang tanpa pindah baris
        print("*", end=" ")
    # Output: mencetak baris baru setelah loop dalam selesai
    print()