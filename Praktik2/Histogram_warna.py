# Nama : Wasthutatya
# Npm  : 5220411117
# Histogram_warna
import cv2
import numpy as np
import matplotlib.pyplot as plt

citra = cv2.imread("asset/Pohon1.jpg")
# menyimpan jumlah baris dan jumlah kolom 
def histogram_rgb(citra) :
    jum_baris = len(citra)
    jum_kolom = len(citra[0])

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

    return hist_red, hist_green, hist_blue

hist_red, hist_green, hist_blue = histogram_rgb(citra)

# Menampilkan semua bar
fig2, (ax, ax2, ax3) = plt.subplots(ncols=3, sharey=True)
ax.bar(range(256),hist_red,color="red")
ax2.bar(range(256),hist_blue,color="blue")
ax3.bar(range(256),hist_green,color="green")
ax.set_box_aspect(1)
ax.set_title("Histogram merah")
ax2.set_box_aspect(1)
ax2.set_title("Histogram biru")
ax3.set_box_aspect(1)
ax3.set_title("Histogram hijau")
plt.show()

# Menampilkan masing-masing bar
# plt.bar(range(256),hist_red,color="red")
# plt.title("Histogram warna merah")
# plt.xlabel("Pixel")
# plt.ylabel("Total")
# plt.show()
# plt.bar(range(256),hist_blue,color="blue")
# plt.title("Histogram warna biru")
# plt.xlabel("Pixel")
# plt.ylabel("Total")
# plt.show()
# plt.bar(range(256),hist_green,color="green")
# plt.title("Histogram warna hijau")
# plt.xlabel("Pixel")
# plt.ylabel("Total")
# plt.show()
