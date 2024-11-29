# 5220411117
# Wasthutatya 
# Soal 2
# menampilkan ukuran pixel dari gambar tersebut 
import cv2

citra = cv2.imread("Latihan1/apel merah.jpg")
baris = len(citra)
kolom = len(citra[0])

print(f"baris: {baris}, \nkolom: {kolom}")
