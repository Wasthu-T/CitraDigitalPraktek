# 5220411117
# Wasthutatya 
# Soal 2

# Konversi RGB ke citra grayscale
import cv2
import numpy as np

citra = cv2.imread("Responsi1/uang.jpg")
blue = citra[:,:,0]
green = citra[:,:,1]
red = citra[:,:,2]

#==== Cara 1 Start====#
# blue,green,red = cv2.split(citra) 
# gray = cv2.cvtColor(citra,cv2.COLOR_RGB2GRAY)
#==== Cara 1 End====#

#==== Cara 2 ====#
baris = len(citra)
kolom = len(citra[0])

gray = np.zeros((baris,kolom))

for b in range(baris) :
    for k in range(kolom) :
        gray[b,k] = round(0.299*red[b,k] + 0.587*green[b,k] + 0.114*blue[b,k])
#==== Cara 2 End====#

gray = gray.astype(np.uint8)
cv2.imshow("Uang - gray", gray)
cv2.waitKey()
