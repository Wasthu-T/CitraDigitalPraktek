# 5220411117
# Wasthutatya 
# Soal 6
# Melakukan deteksi tepi Sobel, Prewit, dan Canny pada soal 5.
import cv2
import numpy as np
citra = cv2.imread("Latihan2/plat nomor kendaraan.jpg")

gray = cv2.cvtColor(citra,cv2.COLOR_RGB2GRAY)
# image
(h, w) = citra.shape[:2]
(cX, cY) = (w // 2, h // 2)
# rotate our image by 45 degrees around the center of the image
M = cv2.getRotationMatrix2D((cX, cY), -5, 1.0)
rotated = cv2.warpAffine(gray, M, (w, h))

Gaussian = cv2.GaussianBlur(rotated, (7, 7), 0) 

# Soal 6 mulai
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

sobel = sobel_edge_detector(Gaussian)
prewit = prewit_edge_detector(Gaussian)
canny = cv2.Canny(Gaussian, 100, 200, 3, L2gradient=True)
cv2.imshow("Plat - Rotate", Gaussian)
cv2.imshow("Plat - sobel", sobel)
cv2.imshow("Plat - prewit", prewit)
cv2.imshow("Plat - canny", canny)
cv2.waitKey()

# Penjelasan
# Proses dari gaussian blur digunakan untuk menghilangkan noisy dari gambar.
# Bisa saja noisy tersebut mengganggu dari deteksi tepi.

# Sobel = Memiliki warna lebih menonjol di angka dan huruf. Diluar plat masih jelas terlihat yang mana kurang dibutuhkan
#          
# Prewitt = Hasil lebih terlihat di bagian dalam plat, diluar plat juga sudah berkurang. 
#           Namun hasilnya masih terlihat kurang menyakinkan untuk membaca angka dan hurufnya.
# 
# Canny = Hasil bagian dalam plat masih sama terlihat jelas, sedangkan diluar plat sudah banyak yang hilang.
#         Huruf dan angka dapat dibaca dengan jelas. 

# Kesimpulan dari membandingan dengan hasil no 4 tepi di luar plat sudah tidak terlalu terlihat. 
# Hasil tersebut bagus karena ingin melihat angka dan huruf saja. Gambar dengan tepi jauh lebih terlihat.
# selsai soal 6

