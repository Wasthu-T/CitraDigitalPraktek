import cv2
import numpy as np

citra = cv2.imread("asset/Pohon.jpg")

def getxyCitraScaling(scale, citra):
    jml_baris = len(citra)
    jml_kolom = len(citra[0])

    new_baris = int(jml_baris*scale)
    new_kolom = int(jml_kolom*scale)
    citra_scaling = np.zeros((new_baris,new_kolom,3), dtype=np.uint8)
    return jml_baris, jml_kolom, scale, citra_scaling, new_baris, new_kolom

# forward jika nilai kosong tetap kosong
def forward(citra):
    jml_baris, jml_kolom, scale, citra_scaling, new_baris, new_kolom = getxyCitraScaling(1.2, citra)

    for row in range(jml_baris):
        for col in range(jml_kolom):
            # Hitung Koordinat baru
            new_row = int(row * scale)
            new_col = int(col * scale)

            # Cek apakah koordinat sesuai batas
            if 0 <= new_row < new_baris and 0 <= new_col < new_kolom:
                citra_scaling[new_row][new_col] = citra[row][col]
    return citra_scaling


# backward jika nilai kosong akan terisi nilai terdekat (0.5 jadi 0)
def backward(citra):
    jml_baris, jml_kolom, scale, citra_scaling, new_baris, new_kolom = getxyCitraScaling(1.2, citra)
    for row in range(new_baris):
        for col in range(new_kolom):
            new_row = int(row/scale)
            new_col = int(col/scale)

            if 0<= new_row < jml_baris and 0 <= new_col < jml_kolom:
                citra_scaling[row][col] = citra[new_row][new_col]

    return citra_scaling

citra_forward = forward(citra)
citra_backward = backward(citra)

new_heigt = int(len(citra)*1.2)
new_width = int(len(citra[0])*1.2)
forward_library = cv2.resize(citra,(new_width,new_heigt))

cv2.imshow("Pohon - Asli", citra)
cv2.imshow("Pohon - Forward", citra_forward)
cv2.imshow("Pohon - Backward", citra_backward)
# cv2.imshow("Pohon - Forward Library", forward_library)
cv2.waitKey()