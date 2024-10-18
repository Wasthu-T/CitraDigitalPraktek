# matriks x konstanta
import cv2
import numpy as np
import matplotlib.pyplot as plt

citra = cv2.imread("asset/Pohon.jpg")

citra_rgb = cv2.cvtColor(citra, cv2.COLOR_BGR2RGB)
beta = 50
alpha = 1.5

citra_float = citra_rgb.astype(np.float32)

# citra_brigness = citra_float + beta
citra_brigness = citra_float * alpha

citra_brigness = np.clip(citra_brigness, 0, 255)

citra_brigness = citra_brigness.astype(np.uint8)

plt.figure(figsize=(12,6))
plt.subplot(1,2,1)
plt.imshow(citra_rgb)
plt.title('Citra sebelum menambahkan kecerahan')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(citra_brigness)
plt.title('Citra sebelum menambahkan kecerahan')
plt.axis('off')

plt.show()
