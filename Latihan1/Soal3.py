# 5220411117
# Wasthutatya 
# Soal 3
# Memperkecil ukuran gambar menjadi 50% dari ukuran semula
import cv2
import numpy as np

citra = cv2.imread("Latihan1/apel merah.jpg")

def getxyCitraScaling(scale, citra):
    jml_baris = len(citra)
    jml_kolom = len(citra[0])

    new_baris = int(jml_baris*scale)
    new_kolom = int(jml_kolom*scale)
    citra_scaling = np.zeros((new_baris,new_kolom,3), dtype=np.uint8)
    return jml_baris, jml_kolom, scale, citra_scaling, new_baris, new_kolom

# forward jika nilai kosong tetap kosong
def forward(scaling, citra):
    jml_baris, jml_kolom, scale, citra_scaling, new_baris, new_kolom = getxyCitraScaling(scaling, citra)

    for row in range(jml_baris):
        for col in range(jml_kolom):
            # Hitung Koordinat baru
            new_row = int(row * scale)
            new_col = int(col * scale)

            # Cek apakah koordinat sesuai batas
            if 0 <= new_row < new_baris and 0 <= new_col < new_kolom:
                citra_scaling[new_row][new_col] = citra[row][col]
    return citra_scaling

citra_forward = forward(0.5, citra)
cv2.imshow("Apel - Asli", citra)
cv2.imshow("Apel - Scaling Forward", citra_forward)
cv2.waitKey()
