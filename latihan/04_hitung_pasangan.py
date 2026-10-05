# Latihan 4: Menghitung Pasangan

# Input n dari pengguna
n = int(input("n: "))

# Counter: diinisialisasi 0 untuk menghitung pasangan yang memenuhi kondisi
count = 0

# Loop luar (i): dari 1 sampai n
for i in range(1, n + 1):
    # Loop dalam (j): dari 1 sampai n
    for j in range(1, n + 1):
        # Kondisi: mengecek apakah i + j <= n
        if i + j <= n:
            # Counter: bertambah 1 jika kondisi terpenuhi
            count += 1

# Output hasil
print(f"Banyak pasangan = {count}")