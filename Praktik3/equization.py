# Meratakan distribusi histogram Contras
import cv2
import numpy as np
import matplotlib.pyplot as plt

citra = cv2.imread("asset/Pohon.jpg")

citra_gray = cv2.cvtColor(citra, cv2.COLOR_BGR2GRAY)

hist_gray = cv2.calcHist([citra_gray],[0],None,[256],[0,256])
citra_gray_equalized = cv2.equalizeHist(citra_gray)

hist_equalized = cv2.calcHist([citra_gray_equalized],[0],None,[256],[0,256])


plt.figure(figsize=(10,5))

plt.subplot(2,2,1)
plt.imshow(citra_gray, cmap="gray")
plt.title('Citra Grayscale sebelum equalized')
plt.axis('off')

plt.subplot(2,2,2)
plt.bar(range(256), hist_gray.ravel(),color="black")
plt.title('Histogram Sebelum equalization')
plt.xlim([0,256])

plt.subplot(2,2,3)
plt.imshow(citra_gray_equalized, cmap="gray")
plt.title('Citra Grayscale setelah equalized')
plt.axis('off')

plt.subplot(2,2,4)
plt.bar(range(256), hist_equalized.ravel(),color="black")
plt.title('Histogram setelah equalization')
plt.xlim([0,256])

plt.show()