# 5220411117
# Wasthutatya 
# Soal 5
# Melakukan gausian blur
import cv2
citra = cv2.imread("Latihan2/plat nomor kendaraan.jpg")

gray = cv2.cvtColor(citra,cv2.COLOR_RGB2GRAY)
# image
(h, w) = citra.shape[:2]
(cX, cY) = (w // 2, h // 2)
M = cv2.getRotationMatrix2D((cX, cY), -5, 1.0)
rotated = cv2.warpAffine(gray, M, (w, h))

# Soal 5 mulai
Gaussian = cv2.GaussianBlur(rotated, (7, 7), 0) 

cv2.imshow("Plat - Rotated", rotated)
cv2.imshow("Plat - Gaussian", Gaussian)
cv2.waitKey()
# Soal 5 selesai
