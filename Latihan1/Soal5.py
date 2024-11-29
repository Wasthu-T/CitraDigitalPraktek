# 5220411117
# Wasthutatya 
# Soal 5
# Jelaskan perbedaan antara gambar hasil penskalaan pada nomor 4 dengan gambar asli pada nomor 1. 
# Berikan penjelasan yang logis disertai alasan-alasannya!

# gambar scaling pada no 4 menggunakan proses backward scaling.
# Prosesnya dimulai dari membuat citra kosong baru terlebih dahulu yang akan diisi dengan citra asli.
# Maka perulangan yang digunakan adalah dengan jumlah baris dan kolom dari citra baru. 
# Scaling yang diubah bukan intensitas namun posisinya. Terdapat 2 scaling yaitu forward dan backward.

# Misalnya citra pada posisi (1,1) dengan scaling 2, maka posisinya akan berubah di (2,2). Jika posisi (2,2) menjadi 4,4
# Jika menggunakan forward scaling, tempat yang kosong seperti (2,1) akan didiamkan saja atau bernilai 0.

# Jika menggunakan backward scaling dari sebaliknya.
# Misalkan pada citra scaling posisi (2,2) dengan scaling 2, maka diambil dari citra aslinya yaitu (1,1)
# lalu pada posisi (2,1) nilai yang diambil dari (1,0.5) 
# karena tidak ada posisi dengan nilai koma, maka dibulatkan kebawah yaitu posisi (1,1)

# Kesimpulan
# Intensitas pada citra asli bisa saja memiliki nilai unik disetiap baris dan kolomnya.
# melakukan scaling dengan 0.5 lalu dikembalikan ke ukuran semula ini dapat menyababkan 
# ada intensitas pixel yang hilang akibat dilakukannya scaling 0.5.
# Dengan mengembalikan ukuran kesemula ini juga hanya mengambil nilai yang berada pada posisi sebelahnya(jika menggunakan backward) 
# Perbedaannya terdapat pada intensitas citra walaupun tidak begitu jauh jika dilihat dengan mata.