import cv2
from imutils.contours import sort_contours
import matplotlib.pyplot as plt
import numpy as np

def show(img):
    plt.figure()
    plt.imshow(img, cmap='gray')


def save_images(numbers):
    for i in range(len(numbers)):
        img = numbers[i]
        filename = str(i) + ".jpg"
        cv2.imwrite("number_images/" + filename, img)
        # show(img)

def dig_extract(file_path):
    image = cv2.imread(file_path)
    image = cv2.resize(image, (640, 640))
    # show(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # show(gray)
    thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,57,5)
    img_thresh = np.copy(thresh)
    # show(img_thresh)
    conts, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in conts:
        area = cv2.contourArea(contour)
        if area < 1200:
            cv2.drawContours(thresh, [contour], -1, (0,0,0), -1)
    # show(thresh)
    vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,5))
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, vertical_kernel, iterations=9)
    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,1))
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, horizontal_kernel, iterations=9)
    # show(thresh)
    invert = 255 - thresh
    # show(invert)
    contours, hierarchy = cv2.findContours(invert, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = [cnt for cnt in contours if cv2.contourArea(cnt) < 8000 and cv2.contourArea(cnt) > 2000]
    white = np.ones((640, 640, 3), np.uint8) * 255
    for cnt in contours:
        cv2.drawContours(white, [cnt], -1, (255, 0, 0), 1)
    # show(white)
    rects = [cv2.boundingRect(cnt) for cnt in contours]
    # print(len(contours))
    white = np.ones((640, 640, 3), np.uint8) * 255
    for rect in rects:
        x, y, w, h = rect
        cv2.rectangle(white, (x, y), (x+w, y+h), (255, 0, 0), 1)
    # show(white)
    rects = sorted(rects, key= lambda roi: (roi[1]))
    for i in range(9):
        rects[9*i : 9*(i+1)] = sorted(rects[9*i : 9*(i+1)], key= lambda roi: (roi[0]))
    numbers = []
    for roi in rects:
        x, y, w, h = roi
        num = img_thresh[y:y+h,x:x+w]
        numbers.append(num)
    save_images(numbers)
