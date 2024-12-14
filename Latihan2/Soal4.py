# 5220411117
# Wasthutatya 
# Soal 4
# Melakukan deteksi tepi Sobel, Prewit, dan Canny pada soal 3.
import cv2
import numpy as np
citra = cv2.imread("Latihan2/plat nomor kendaraan.jpg")

gray = cv2.cvtColor(citra,cv2.COLOR_RGB2GRAY)
h, w = citra.shape[:2]
cX, cY = (w // 2, h // 2)
M = cv2.getRotationMatrix2D((cX, cY), -5, 1.0)
rotated = cv2.warpAffine(gray, M, (w, h))

# mulai soal 4
def sobel_edge_detector(img):
    grad_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    grad = np.sqrt(grad_x**2 + grad_y**2)
    grad_norm = (grad * 255 / grad.max()).astype(np.uint8)
    return grad_norm

def prewit_edge_detector(img):
    kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
    kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
    prewittx = cv2.filter2D(img,-1,kernelx)
    prewitty = cv2.filter2D(img,-1,kernely)
    grad = prewittx + prewitty
    img_prewitt_uint8 = cv2.convertScaleAbs(grad)
    return img_prewitt_uint8

sobel = sobel_edge_detector(rotated)
prewit = prewit_edge_detector(rotated)
canny = cv2.Canny(rotated, 100, 200, 3, L2gradient=True)
cv2.imshow("Plat - Rotate", rotated)
cv2.imshow("Plat - sobel", sobel)
cv2.imshow("Plat - prewit", prewit)
cv2.imshow("Plat - canny", canny)
cv2.waitKey()

# Penjelasan
# Sobel = Melakukan 2 cara convolusi secara horizontal dan vertikal, kemudian digabungkan dan dinormalisasikan.
#         Hasil dari sobel masih memiliki tepi yang kurang menyakinkan atau bewarna abu-abu. 
#         Hasil deteksi tepi bagus, huruf dan angka dapat dilihat dengan jelas.
# Prewitt = Cara dari prewitt tidak jauh dari sobel. Hasil yang prewitt kurang jelas, 
#           tepi yang terbaca jauh tidak terlihat. terdapat bercak-bercak/noisy yang membuat deteksi tepi kurang maksimal
#            Hasil deteksi tepi kurang bagus, huruf dan angka dilihat kurang jelas.
# Canny = Metode Canny paling rumit diantara kedua metode lainnya. Hasil dari Canny begitu jelas. 
#         Tidak memiliki pixel yang meragukan atau hanya bernilai biner. 
#         Hasil paling bagus dari ketiga metode yang digunakan.
# selsai soal 4