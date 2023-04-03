
import cv2
import numpy as np


img = cv2.imread('img/rubix.png')

img[np.where((img == [0, 255, 255]).all(axis=2))] = [255, 0, 0]
img[np.where((img == [255, 0, 255]).all(axis=2))] = [0, 255, 0]
img[np.where((img == [255, 255, 0]).all(axis=2))] = [0, 0, 255]

cv2.imwrite('rubik-solved.jpg', img)
