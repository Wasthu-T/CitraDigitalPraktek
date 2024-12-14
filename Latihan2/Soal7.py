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

# Soal 7 mulai
kernel_sharpening = np.array([[0,-1,0],
                             [-1,5,-1],
                             [0,-1,0]])

Sharpen = cv2.filter2D(rotated, -1, kernel_sharpening)

cv2.imshow("Plat - Rotated", rotated)
cv2.imshow("Plat - Sharpening", Sharpen)
cv2.waitKey()
# Soal 7 selesai
