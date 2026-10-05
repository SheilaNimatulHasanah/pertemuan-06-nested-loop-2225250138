# Latihan 3: Jumlah per Baris

# Loop luar (i): berjalan dari 1 sampai 4
for i in range(1, 5):
    # Akumulator: diinisialisasi 0 di setiap awal baris baru
    total_baris = 0
    
    # Loop dalam (j): berjalan dari 1 sampai 3
    for j in range(1, 4):
        # Akumulasi: menambahkan hasil perkalian i * j ke total_baris
        total_baris += i * j
        
    # Output: menampilkan hasil jumlah per baris
    print(f"Jumlah baris {i} = {total_baris}")