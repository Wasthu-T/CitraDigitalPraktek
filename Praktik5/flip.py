import cv2
import numpy as np

citra = cv2.imread("asset/Pohon.jpg")

def getxyCitraFlip(citra):
    jml_baris = len(citra)
    jml_kolom = len(citra[0])
    citra_flip = np.zeros_like(citra)
    return jml_baris, jml_kolom, citra_flip

def pencerminanV(citra):
    jml_baris,jml_kolom,citra_flip = getxyCitraFlip(citra)

    for row in range(jml_baris):
        for col in range(jml_kolom):
            new_row = jml_baris - 1 - row
            citra_flip[row][col] = citra[new_row][col]
    return citra_flip

def pencerminanH(citra):
    jml_baris,jml_kolom,citra_flip = getxyCitraFlip(citra)
    
    for row in range(jml_baris):
        for col in range(jml_kolom):
            new_col = jml_kolom - 1 - col
            citra_flip[row][col] = citra[row][new_col]
    return citra_flip

citra_flip_h = pencerminanH(citra)
citra_flip_v = pencerminanV(citra)

# Library
citra_pencerminanH = cv2.flip(citra,1)
citra_pencerminanV = cv2.flip(citra,-1)

cv2.imshow("Pohon - Asli", citra)
cv2.imshow("Pohon - Pencerminan Horizontal", citra_flip_h)
cv2.imshow("Pohon - Pencerminan Vertikal", citra_flip_v)
cv2.imshow("Pohon - Pencerminan Horizontal Library", citra_pencerminanH)
cv2.imshow("Pohon - Pencerminan Vertikal Library", citra_pencerminanV)
cv2.waitKey()