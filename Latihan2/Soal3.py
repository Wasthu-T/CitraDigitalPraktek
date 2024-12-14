# 5220411117
# Wasthutatya 
# Soal 3
# Melakukan rotasi agar posisi angka dan huruf tegak lurus 
import cv2
citra = cv2.imread("Latihan2/plat nomor kendaraan.jpg")

gray = cv2.cvtColor(citra,cv2.COLOR_RGB2GRAY)
# image
(h, w) = citra.shape[:2]
(cX, cY) = (w // 2, h // 2)
# rotate our image by 45 degrees around the center of the image
M = cv2.getRotationMatrix2D((cX, cY), -5, 1.0)
rotated = cv2.warpAffine(gray, M, (w, h))

cv2.imshow("Plat - Gray", gray)
cv2.imshow("Plat - Rotate", rotated)
cv2.waitKey()