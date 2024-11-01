# 5220411117
# Wasthutatya 
# Soal 4

# Histogram warna
import cv2
import numpy as np
import matplotlib.pyplot as plt


citra = cv2.imread("Responsi1/uang.jpg")
citra_gray = cv2.cvtColor(citra, cv2.COLOR_RGB2GRAY)

def check_highest_pixel_gray() :
    highest_pixel = 0
    baris = len(citra)
    kolom = len(citra[0])
    for b in range(baris) :
        for k in range(kolom) :
            if highest_pixel < citra_gray[b][k] :
                highest_pixel = citra_gray[b][k]
    return highest_pixel*20/100

brigness = check_highest_pixel_gray().astype(np.float32)
citra_float = citra_gray.astype(np.float32)

citra_brigness = citra_float + brigness
citra_brigness = np.clip(citra_brigness, 0, 255)

citra_brigness = citra_brigness.astype(np.uint8)

hist_gray_sebelum = cv2.calcHist([citra_gray],[0],None,[256],[0,256])
hist_gray_sesudah = cv2.calcHist([citra_brigness],[0],None,[256],[0,256])

plt.figure(figsize=(12,6))
plt.subplot(2,2,1)
plt.imshow(citra_gray, cmap="gray")
plt.title('Citra Grayscale Sebelum Menambahkan Brigness')
plt.axis('off')

plt.subplot(2,2,2)
plt.title('Histogram Sebelum Menambahkan Brigness')
plt.bar(range(256),hist_gray_sebelum.ravel(),color="black")
plt.xlim([0,256])

plt.subplot(2,2,3)
plt.imshow(citra_brigness, cmap="gray")
plt.title('Citra Grayscale Sesudah Menambahkan Brigness')
plt.axis('off')

plt.subplot(2,2,4)
plt.title('Histogram Sesudah Menambahkan Brigness')
plt.bar(range(256),hist_gray_sesudah.ravel(),color="black")
plt.xlim([0,256])

plt.show()