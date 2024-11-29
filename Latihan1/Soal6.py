# 5220411117
# Wasthutatya 
# Soal 6
# pencerminan horizontal (horizontal flipping) pada citra asli
# Hasil pencerminan lakukan rotasi sebesar 90derajat berlawanan jarum jam (counter clockwise).

import cv2
import numpy as np

citra = cv2.imread("Latihan1/apel merah.jpg")
def getxyCitraFlip(citra):
    jml_baris = len(citra)
    jml_kolom = len(citra[0])
    citra_flip = np.zeros_like(citra)
    return jml_baris, jml_kolom, citra_flip

def pencerminanH(citra):
    jml_baris,jml_kolom,citra_flip = getxyCitraFlip(citra)
    nilai_tengah_h = jml_kolom/2

    for row in range(jml_baris):
        for col in range(jml_kolom):
            if col > nilai_tengah_h:
                new_col = jml_kolom - 1 - col
                citra_flip[row][col] = citra[row][new_col]
            else:
                citra_flip[row][col] = citra[row][col]

    return citra_flip

def rotasi_lawan(sudut_rotasi, citra):
    citra_rotasi = np.zeros_like(citra)
    jml_baris = len(citra)
    jml_kolom = len(citra[0])
    theta = np.radians(sudut_rotasi)
    pusat_x = jml_kolom // 2
    pusat_y = jml_baris // 2

    for row in range(jml_baris):
        for col in range(jml_kolom):

            new_col = col - pusat_x
            new_row = row - pusat_y

            original_x = int(pusat_x - (new_col * np.cos(-theta) + new_row*np.sin(-theta)))
            original_y = int(pusat_y - (new_col * np.sin(-theta) - new_row*np.cos(-theta)))

            if 0 <= original_y < jml_baris and 0 <= original_x < jml_kolom :
                citra_rotasi[row,col] = citra[original_y,original_x]
    return citra_rotasi

citra_flip_h = pencerminanH(citra)
citra_rot90 = rotasi_lawan(90,citra_flip_h)
cv2.imshow("Pohon - Asli", citra)
cv2.imshow("Pohon - Pencerminan Horizontal", citra_flip_h)
cv2.imshow("Pohon - Rotasi berlawanan jarum jam", citra_rot90)
cv2.waitKey()