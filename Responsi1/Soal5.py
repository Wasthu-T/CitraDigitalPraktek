# 5220411117
# Wasthutatya 
# Soal 5

# Konversi ke black white
import cv2
import numpy as np

citra = cv2.imread("Responsi1/uang.jpg")
citra_gray = cv2.cvtColor(citra, cv2.COLOR_RGB2GRAY)


def check_highest_pixel_gray(citra) :
    highest_pixel = 0
    baris = len(citra)
    kolom = len(citra[0])
    for b in range(baris) :
        for k in range(kolom) :
            if highest_pixel < citra[b][k] :
                highest_pixel = citra[b][k]
    return highest_pixel*20/100

brigness = check_highest_pixel_gray(citra_gray).astype(np.float32)
citra_float = citra_gray.astype(np.float32)

citra_brigness = citra_float + brigness
citra_brigness = np.clip(citra_brigness, 0, 255)

citra_brigness = citra_brigness.astype(np.uint8)

def convert_black_white(citra, trehsold) :
    baris = len(citra)
    kolom = len(citra[0])
    citra_black_white = np.zeros((baris,kolom))
    for b in range(baris) :
        for k in range(kolom) :
            if citra[b][k] > trehsold:
                citra_black_white[b][k] = 1
            else :
                citra_black_white[b][k] = 0
    return citra_black_white

citra_black_white = convert_black_white(citra_gray, 160)
cv2.imshow("Uang - brigness", citra_brigness)
cv2.imshow("Uang - black and white", citra_black_white)
cv2.waitKey()