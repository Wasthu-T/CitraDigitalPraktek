# 5220411117
# Wasthutatya 
# Soal 2
# Mengubah RGB to Grayscale
import cv2
citra = cv2.imread("Latihan2/plat nomor kendaraan.jpg")

gray = cv2.cvtColor(citra,cv2.COLOR_RGB2GRAY)
cv2.imshow("Plat - Asli", citra)
cv2.imshow("Plat - Gray", gray)
cv2.waitKey()
