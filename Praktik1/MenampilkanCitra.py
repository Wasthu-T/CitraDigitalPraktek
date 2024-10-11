# cv=computer vision
import cv2
import numpy as np

# Membaca citra digital dari direktori
citra = cv2.imread("Praktik1/Pohon.jpg")

# Menampilkan gambar dari variabel citra
# cv2.imshow("Pohon", citra)

# Memisahkan channel warna
blue = citra[:,:,0]
green = citra[:,:,1]
red = citra[:,:,2]
# cv2.imshow("Pohon - Blue", blue)
# cv2.imshow("Pohon - Green", green)
# cv2.imshow("Pohon - Red", red)

# Rumus Grayscale 0.299 R + 0.587 G + 0.114 B
#==== Cara 1 Start ====#
# gray = np.around(0.299*red + 0.587*green + 0.114*blue)

#==== Cara 1 End ====#

#==== Cara 2 ====#
# baris x kolom
# baris = len(citra)
# kolom = len(citra[0])

# citra baru dengan array 0
# gray = np.zeros((baris,kolom))

# mengubah ke grayscale
# for b in range(baris) :
#     for k in range(kolom) :
#         gray[b,k] = round(0.299*red[b,k] + 0.587*green[b,k] + 0.114*blue[b,k])

#==== Cara 2 End====#

#==== Cara 3 Start====#
b,g,r = cv2.split(citra) 
gray = cv2.cvtColor(citra,cv2.COLOR_RGB2GRAY)
#==== Cara 3 End====#

# menghilangkan koma
gray = gray.astype(np.uint8)
cv2.imshow("Pohon - gray", gray)

# Menunggu user menekan sembarang tombol
cv2.waitKey()