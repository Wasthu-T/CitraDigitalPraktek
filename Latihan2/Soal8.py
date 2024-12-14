# 5220411117
# Wasthutatya 
# Soal 7
# Melakukan Sharpening
import cv2
import numpy as np
citra = cv2.imread("Latihan2/plat nomor kendaraan.jpg")

gray = cv2.cvtColor(citra,cv2.COLOR_RGB2GRAY)
# image
(h, w) = citra.shape[:2]
(cX, cY) = (w // 2, h // 2)
M = cv2.getRotationMatrix2D((cX, cY), -5, 1.0)
rotated = cv2.warpAffine(gray, M, (w, h))

kernel_sharpening = np.array([[0,-1,0],
                             [-1,5,-1],
                             [0,-1,0]])

sharpen = cv2.filter2D(rotated, -1, kernel_sharpening)

# Soal 8 mulai
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

sobel = sobel_edge_detector(sharpen)
prewit = prewit_edge_detector(sharpen)
canny = cv2.Canny(sharpen, 100, 200, 3, L2gradient=True)
cv2.imshow("Plat - Rotate", sharpen)
cv2.imshow("Plat - sobel", sobel)
cv2.imshow("Plat - prewit", prewit)
cv2.imshow("Plat - canny", canny)
cv2.waitKey()

# Penjelasan
# Proses dari Sharpening digunakan untuk mempertajam gambar.
# Proses ini mengakibatkan memperjelas noisy gambar. 

# Sobel = Hasil deteksi tepi jelas baik didalam plat maupun diluar. namun perlu diperhatikan untuk diluar plat
#         
#          
# Prewitt = Hasil lebih terlihat di bagian dalam plat, diluar plat juga makin kelihatan. 
#           Deteksi tepi yang dihasilkan memiliki banyak noisy atau garis putus-putus.
# 
# Canny = Hasil bagian dalam plat masih sama terlihat jelas, begitu juga diluar plat makin terlihat.
#          

# Kesimpulan dari membandingan dengan hasil no 4 dan 6 tepi di luar plat lebih terlihat. 
# Hasil tersebut kurang bagus karena diluar plat malah terlihat lebih jelas.
# sedangkan ingin melihat angka dan huruf saja.
# Soal 8 selesai