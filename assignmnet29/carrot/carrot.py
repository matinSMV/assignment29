import cv2
import numpy as np

img = cv2.imread('img/Carrot.jpg')

b , g , r = cv2.split(img)

b_new = np.zeros_like(b)
r_new = np.zeros_like(r)
r_new = g
res = cv2.merge((b,g,r_new))

cv2.imwrite('res.jpg', res)