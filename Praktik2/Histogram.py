# Histogram
import cv2
import numpy as np
import matplotlib.pyplot as plt

citra = cv2.imread("asset/Pohon1.jpg")

# conversi ke gray
citra_gray = cv2.cvtColor(citra, cv2.COLOR_RGB2GRAY)

# menyimpan jumlah baris dan jumlah kolom 
jum_baris = len(citra)
jum_kolom = len(citra[0])
total_pix = jum_kolom + jum_baris

# menghitung nilai pixel grayscale
hist_gray = np.zeros(256) #inisiasi histogram
# membuat array kosong dengan 256

for i in range(jum_baris) :
    for j in range(jum_kolom) : 
        pixel = int(citra_gray[i][j])
        hist_gray[pixel] += 1 

# menampilkan histogram
plt.bar(range(256),hist_gray)

# tampilkan gray image
gray = citra_gray.astype(np.uint8)
cv2.imshow("Pohon - gray", gray)
plt.show()

# Menunggu user menekan sembarang tombol
cv2.waitKey()