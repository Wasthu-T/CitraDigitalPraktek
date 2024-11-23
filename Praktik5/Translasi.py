import cv2
import numpy as np

citra = cv2.imread("asset/Pohon.jpg")

citra_translasi = np.zeros_like(citra)

# Menggeser sebanyak 50 baris dan kolom
Translasi_baris = 50
Translasi_kolom = 50

def translasi_manual(trans_baris, trans_kolom, citra) :
    jml_baris = len(citra)
    jml_kolom = len(citra[0])
    for row in range(jml_baris):
        for col in range(jml_kolom):
            new_row = row + trans_baris
            new_col = col + trans_kolom

            # cek apakah masih dalam batas? new_row dan new_col harus berada diantara 0 - jml_baris&kolom
            if 0 <= new_row < jml_baris and 0 <= new_col < jml_kolom :
                citra_translasi[new_row][new_col] = citra[row][col]
    return citra_translasi
        
def translasi(trans_baris,trans_kolom, citra) :
    jml_baris = len(citra)
    jml_kolom = len(citra[0])
    
cv2.imshow("Pohon - Asli", citra)
cv2.imshow("Pohon - Translasi", citra_translasi)
cv2.waitKey()

# Cara 2 pakai library
