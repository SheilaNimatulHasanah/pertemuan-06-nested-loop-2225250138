# Latihan 1: Pasangan Indeks

# Inisialisasi counter untuk menghitung jumlah pasangan
count = 0

# Loop luar (i): berjalan dari 1 sampai 3
for i in range(1, 4):
    # Loop dalam (j): berjalan dari 1 sampai 4 untuk setiap nilai i
    for j in range(1, 5):
        # Output: menampilkan pasangan (i, j)
        print(i, j)
        # Akumulator/Counter: menambah 1 setiap kali pasangan dicetak
        count += 1

# Output akhir menampilkan total pasangan
print(f"Banyak pasangan = {count}")