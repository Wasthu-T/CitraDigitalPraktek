# 5220411117
# Wasthutatya 
# Soal 4
# Lanjutan Soal 3, memperbesar gambar menjadi 100% (2 kali lipat) dari ukuran citra saat ini (kembali ke ukuran semula). 
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

def backward(scaling, citra):
    jml_baris, jml_kolom, scale, citra_scaling, new_baris, new_kolom = getxyCitraScaling(scaling, citra)
    for row in range(new_baris):
        for col in range(new_kolom):
            new_row = int(row/scale)
            new_col = int(col/scale)

            if 0<= new_row < jml_baris and 0 <= new_col < jml_kolom:
                citra_scaling[row][col] = citra[new_row][new_col]

    return citra_scaling

citra_forward = forward(0.5, citra)
citra_forward_backward = backward(2, citra_forward)
cv2.imshow("Apel - Asli", citra)
cv2.imshow("Apel - Scaling Forward", citra_forward)
cv2.imshow("Apel - Scaling Forward Bacward", citra_forward_backward)
cv2.waitKey()