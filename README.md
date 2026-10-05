# Pertemuan 06 Nested Loop Python

Nama: Sheila Ni'matul Hasanah
NIM: 2225250138
Kelas: 3B

## Tujuan
Menggunakan nested loop, pola, akumulasi, dan pencacahan.

## Cara Menjalankan
```bash
python3 tugas/tabel_perkalian_dan_statistik.py

## Algoritma 3
- Loop Luar (for i in range(1, n + 1)): Berfungsi mengontrol iterasi per baris dari 1 hingga n, serta mengatur reset nilai total_baris = 0 pada setiap baris baru.
- ​Loop Dalam (for j in range(1, n + 1)): Berfungsi mengontrol iterasi per kolom pada baris berjalan, menghitung nilai perkalian hasil = i * j, dan mencetak hasilnya secara bersandingan.
- ​Akumulator (total_baris dan total_semua): total_baris menjumlahkan nilai perkalian dalam satu baris, sedangkan total_semua menampung jumlah keseluruhan dari seluruh tabel perkalian.
- ​Counter (count_genap): Menghitung banyaknya hasil perkalian i * j yang nilainya merupakan bilangan genap (kondisi hasil % 2 == 0).

## Hasil Pengujian
1. Input n = 1
- ​Hasil Diharapkan: Jumlah Pasangan = 1, Total semua = 1, Banyak hasil genap = 0
- ​Keluaran Aktual: Jumlah Pasangan = 1, Total semua = 1, Banyak hasil genap = 0
- ​Status: Sesuai
2. ​Input n = 2
- ​Hasil Diharapkan: Jumlah Pasangan = 4, Total semua = 9, Banyak hasil genap = 3
- ​Keluaran Aktual: Jumlah Pasangan = 4, Total semua = 9, Banyak hasil genap = 3
- ​Status: Sesuai
3. ​Input n = 3
- ​Hasil Diharapkan: Jumlah Pasangan = 9, Total semua = 36, Banyak hasil genap = 5
- ​Keluaran Aktual: Jumlah Pasangan = 9, Total semua = 36, Banyak hasil genap = 5
- ​Status: Sesuai

## Analisis Efisiensi
Badan loop dalam berjalan sebanyak n^2 kali (atau n x n kali) untuk input sebesar n.
- ​Penjelasan: Loop luar berjalan sebanyak n kali. Di setiap 1 kali iterasi loop luar, loop dalam mengeksekusi badannya sebanyak n kali. Sehingga total eksekusi badan loop dalam adalah n x n = n^2.
- ​Jika n = 1, maka 1 x 1 = 1 kali.
- ​Jika n = 2, maka 2 x 2 = 4 kali.
- ​Jika n = 3, maka 3 x 3 = 9 kali.

## Refleksi
- Kesalahan yang Sering Ditemukan: Menempatkan inisialisasi akumulator total_baris = 0 di luar loop luar (sebelum loop dimulai) alih-alih di dalam loop luar.
- ​Akibat Kesalahan: Nilai total_baris tidak ter-reset menjadi 0 di setiap baris baru, sehingga jumlah baris ke-2 dan seterusnya akan terus terakumulasi dari baris sebelumnya dan menghasilkan nilai yang salah.
- ​Cara Memperbaiki: Memindahkan baris kode total_baris = 0 ke dalam loop luar, tepat sebelum loop dalam dimulai, agar nilainya kembali bersih (0) setiap kali berpindah ke baris baru.