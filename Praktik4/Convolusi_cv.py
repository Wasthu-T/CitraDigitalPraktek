import cv2
import numpy as np

citra = cv2.imread("asset/Pohon.jpg")
citra_rgb = cv2.cvtColor(citra, cv2.COLOR_BGR2RGB)

# sharpening
kernel_sharpening1 = np.array(
                            [[-1,-1,-1],
                             [-1,9,-1],
                             [-1,-1,-1]])

kernel_sharpening2 = np.array([[0,-1,0],
                             [-1,5,-1],
                             [0,-1,0]])

sharpen_gambar1 = cv2.filter2D(citra, -1, kernel_sharpening1)
sharpen_gambar2 = cv2.filter2D(citra, -1, kernel_sharpening2)

cv2.imshow("original img", citra)
cv2.imshow("sharpen1 img", sharpen_gambar1)
cv2.imshow("sharpen2 img", sharpen_gambar2)

cv2.waitKey()