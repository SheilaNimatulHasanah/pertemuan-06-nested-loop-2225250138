# Tugas 3: Tabel Perkalian dan Statistik

print("Tabel Perkalian dan Statistik")

# 1. Validasi input n (harus bilangan bulat positif)
n = int(input("n: "))
while n <= 0:
    n = int(input("n: "))

# 2. Inisialisasi total keseluruhan dan counter hasil genap
total_semua = 0
count_genap = 0

# 3. Loop luar (i) untuk baris dari 1 sampai n
for i in range(1, n + 1):
    # Reset total per baris setiap kali masuk baris baru
    total_baris = 0
    
    # Loop dalam (j) untuk kolom dari 1 sampai n
    for j in range(1, n + 1):
        # Hitung hasil perkalian
        hasil = i * j
        
        # Cetak hasil perkalian dengan rapi dalam satu baris
        print(f"{hasil:4d}", end="")
        
        # Tambahkan ke akumulator baris dan akumulator total keseluruhan
        total_baris += hasil
        total_semua += hasil
        
        # Kondisi: cek apakah hasil perkalian genap
        if hasil % 2 == 0:
            count_genap += 1
            
    # Tampilkan total per baris setelah loop dalam selesai
    print(f"  | Jumlah baris {i} = {total_baris}")

# 4. Output statistik akhir setelah seluruh loop selesai
print("-" * 40)
print(f"Total semua       : {total_semua}")
print(f"Banyak hasil genap: {count_genap}")