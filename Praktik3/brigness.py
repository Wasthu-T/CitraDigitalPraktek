# matriks x konstanta
import cv2
import numpy as np
import matplotlib.pyplot as plt

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

citra = cv2.imread("asset/Pohon.jpg")

citra_rgb = cv2.cvtColor(citra, cv2.COLOR_BGR2RGB)
# brigness = gelap makin terang, terang makin terang
beta = 50

# contrass = gelap makin gelap, terang makin terang
alpha = 0.5

# harus diubah ke float, uint8(unsigned int 8, hanya 0-255) ke float32
citra_float = citra_rgb.astype(np.float32)

citra_brigness = citra_float + beta
citra_contrass = citra_float * alpha

# membatasi rentang nilai
citra_brigness = np.clip(citra_brigness, 0, 255)
# mengubah ke tipe data int (tanpa koma)
citra_brigness = citra_brigness.astype(np.uint8)

citra_contrass = np.clip(citra_contrass, 0, 255)
citra_contrass = citra_contrass.astype(np.uint8)

hist_red, hist_green, hist_blue = histogram_rgb(citra_rgb)
hist_red_brigness, hist_green_brigness, hist_blue_brigness = histogram_rgb(citra_brigness)
hist_red_contrass, hist_green_contrass, hist_blue_contrass = histogram_rgb(citra_contrass)

plt.figure(figsize=(12,6))
plt.subplot(2,4,1)
plt.imshow(citra_rgb)
plt.title('Citra Asli')
plt.axis('off')

plt.subplot(2,4,2)
plt.bar(range(256),hist_red,color="red")
plt.title("Citra Asli hist red")

plt.subplot(2,4,3)
plt.bar(range(256),hist_green,color="green")
plt.title("Citra Asli hist green")

plt.subplot(2,4,4)
plt.bar(range(256),hist_blue,color="blue")
plt.title("Citra Asli hist blue")

plt.subplot(2,4,5)
plt.imshow(citra_contrass)
plt.title('Citra dengan Kontras')
plt.axis('off')

plt.subplot(2,4,6)
plt.bar(range(256),hist_red_contrass,color="red")
plt.title("hist_red_contrass")

plt.subplot(2,4,7)
plt.bar(range(256),hist_red_contrass,color="green")
plt.title("hist_red_contrass")

plt.subplot(2,4,8)
plt.bar(range(256),hist_red_contrass,color="blue")
plt.title("hist_red_contrass")

# plt.figure(figsize=(12,6))
# plt.subplot(1,2,1)
# plt.imshow(citra_rgb)
# plt.title('Citra sebelum menambahkan kecerahan')
# plt.axis('off')

# plt.subplot(1,2,2)
# plt.imshow(citra_brigness)
# plt.title('Citra sebelum menambahkan kecerahan')
# plt.axis('off')
plt.show()


