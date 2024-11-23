import cv2
import numpy as np

citra = cv2.imread("asset/Pohon.jpg")


citra_rotasi = np.zeros_like(citra)

def rotasi(sudut_rotasi, citra):
    jml_baris = len(citra)
    jml_kolom = len(citra[0])
    theta = np.radians(sudut_rotasi)
    pusat_x = jml_kolom // 2
    pusat_y = jml_baris // 2

    for row in range(jml_baris):
        for col in range(jml_kolom):

            new_col = col - pusat_x
            new_row = row - pusat_y

            original_x = int(pusat_x + (new_col * np.cos(-theta) - new_row*np.sin(-theta)))
            original_y = int(pusat_y + (new_col * np.sin(-theta) + new_row*np.cos(-theta)))

            if 0 <= original_y < jml_baris and 0 <= original_x < jml_kolom :
                citra_rotasi[row,col] = citra[original_y,original_x]
    return citra_rotasi

def rotasilibrary(sudut_rotasi,citra):
    jml_baris = len(citra)
    jml_kolom = len(citra[0])
    pusat_x = jml_kolom // 2
    pusat_y = jml_baris // 2
    M = cv2.getRotationMatrix2D((pusat_x,pusat_y),sudut_rotasi,1.0)
    citra_rotasi = cv2.warpAffine(citra,M,(jml_kolom,jml_baris))
    return citra_rotasi

gambar_rotasi = rotasi(45,citra)
library_rotasi = rotasilibrary(55,citra)
library = cv2.rotate(citra,cv2.ROTATE_90_CLOCKWISE)


cv2.imshow("Pohon - Asli", citra)
cv2.imshow("Pohon - Rotasi", gambar_rotasi)
cv2.imshow("Pohon - Rotasi Library", library)
cv2.imshow("Pohon - Rotasi Library1", library_rotasi)
cv2.waitKey()
