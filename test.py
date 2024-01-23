import cv2
from imutils import contours
import matplotlib.pyplot as plt
import numpy as np


def show(img):
    plt.figure()
    plt.imshow(img, cmap='gray')

# Load image, grayscale, and adaptive threshold
image = cv2.imread('SudokuClear.jpg')
image = cv2.resize(image, (640, 640))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,57,5)

# Filter out all numbers and noise to isolate only boxes
conts, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for contour in conts:
    area = cv2.contourArea(contour)
    if area < 1000:
        cv2.drawContours(thresh, [contour], -1, (0,0,0), -1)

# Fix horizontal and vertical lines
vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,5))
thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, vertical_kernel, iterations=9)
horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,1))
thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, horizontal_kernel, iterations=4)

# Sort by top to bottom and each row by left to right
invert = 255 - thresh
cnts = cv2.findContours(invert, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
cnts, rects = contours.sort_contours(cnts, method="top-to-bottom")
# for i, cr in enumerate(cnt_rect):
#     area = cv2.contourArea(cr[0][i])
#     if area < 50000:
#         row.append(cr[1][i])
#         if i % 9 == 0:  
#             (cnts, rects) = contours.sort_contours(row, method="left-to-right")
#             bounding_rects.append(rects)
#             row = []
bounding_rects = []
for i in range(len(cnts)):
    area = cv2.contourArea(cnts[i])
    if area < 50000:
        bounding_rects.append(rects[i])






# print(bounding_rects.shape)

# Iterate through each box
# for row in sudoku_rows:
#     for c in row:
#         mask = np.zeros(image.shape, dtype=np.uint8)
        

# cv2.imshow('thresh', thresh)
# cv2.imshow('invert', invert)
# cv2.waitKey()
            
numbers = []
for roi in bounding_rects:
    x, y, w, h = roi
    num = gray[x:x+w,y:y+h]
    numbers.append(num)

for i in numbers:
    show(i)