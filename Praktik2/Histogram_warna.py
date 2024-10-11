# Nama : Wasthutatya
# Npm  : 5220411117
# Histogram_warna
import cv2
import numpy as np
import matplotlib.pyplot as plt

citra = cv2.imread("asset/Pohon1.jpg")
# menyimpan jumlah baris dan jumlah kolom 
jum_baris = len(citra)
jum_kolom = len(citra[0])
total_pix = jum_kolom + jum_baris

# Memisahkan channel
blue = citra[:,:,0]
green = citra[:,:,1]
red = citra[:,:,2]

#inisiasi histogram di setiap channel
hist_blue = np.zeros(256)
hist_green = np.zeros(256)
hist_red = np.zeros(256) 

for i in range(jum_baris) :
    for j in range(jum_kolom) : 
        pixel_red = int(citra[i][j][0])
        pixel_green = int(citra[i][j][1])
        pixel_blue = int(citra[i][j][2])

        # Hitung kemunculan pixel
        hist_red[pixel_red] += 1
        hist_blue[pixel_blue] += 1
        hist_green[pixel_green] += 1


plt.bar(range(256),hist_red,color="red")
plt.title("Histogram warna merah")
plt.xlabel("Pixel")
plt.ylabel("Total")
plt.show()
plt.bar(range(256),hist_blue,color="blue")
plt.title("Histogram warna biru")
plt.xlabel("Pixel")
plt.ylabel("Total")
plt.show()
plt.bar(range(256),hist_green,color="green")
plt.title("Histogram warna hijau")
plt.xlabel("Pixel")
plt.ylabel("Total")
plt.show()
