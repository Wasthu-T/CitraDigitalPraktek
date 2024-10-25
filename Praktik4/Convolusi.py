import cv2
import numpy as np
import matplotlib.pyplot as plt

citra = cv2.imread("asset/Pohon.jpg")
citra_rgb = cv2.cvtColor(citra, cv2.COLOR_BGR2RGB)

# sharpening
kernel_sharpening = np.array(
                            [[-1,-1,-1],
                             [-1,9,-1],
                             [-1,-1,-1]]
                             )

# kernel_sharpening = np.array([[0,-1,0],
#                              [-1,5,-1],
#                              [0,-1,0]])

# bluring
# kernel_bluring = np.array([[1,2,1],
#                              [2,4,2],
#                              [1,2,1]])

kernel_bluring = np.ones((5,5), np.float32) / 25
# atas-bawah, kiri-kanan, nilai konstan
# pad_gambar = np.pad(citra_rgb, ((1,1),(1,1),(0,0)),mode="constant")
pad_gambar = np.pad(citra_rgb, ((2,2),(2,2),(0,0)),mode="constant")

citra_convolusi = np.zeros_like(citra_rgb)

jum_baris = len(citra)
jum_kolom = len(citra[0])

def convolusi(kernel,matriks, citra_convolusi) :
    for row in range(jum_baris) :
        for col in range(jum_kolom) :
            for channel in range(3) :
                region = pad_gambar[row:row+matriks, col:col+matriks, channel]
                citra_convolusi[row,col,channel] = np.sum(region*kernel) / np.sum(kernel)
    return citra_convolusi

citra_convolusi_sharp = convolusi(kernel_sharpening,3,citra_convolusi)
citra_convolusi_sharp = np.clip(citra_convolusi, 0, 255).astype(np.uint8)
citra_convolusi_sharp = citra_convolusi.astype(np.uint8)

citra_convolusi_blur = convolusi(kernel_bluring,5,citra_convolusi)
citra_convolusi_blur = np.clip(citra_convolusi, 0, 255).astype(np.uint8)

plt.figure(figsize=(12,6))
plt.subplot(1,3,1)
plt.imshow(citra_rgb)
plt.title('Citra Asli')
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(citra_convolusi_sharp)
plt.title('Citra sharpening')
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(citra_convolusi_blur)
plt.title('Citra blur')
plt.axis('off')

plt.tight_layout()
plt.show()