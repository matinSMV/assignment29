import cv2 
import numpy as np
from PIL import ImageFont, ImageDraw, Image


logo = np.ones((630, 1260 , 3), dtype = 'uint8')*80

logo[210:310, 210:310] = (242,80,32)
logo[320:420, 210:310] = (0,161,241)
logo[210:310, 320:420] = (124,187,0)
logo[320:420, 320:420] = (255,187,0)


fontpath = "font/seguisb.ttf"     
font = ImageFont.truetype(fontpath, size=130)

img_pil = Image.fromarray(logo)
draw = ImageDraw.Draw(img_pil)
draw.text((450, 230),  "Microsoft", font = font)
logo = np.array(img_pil)


logo = cv2.cvtColor(logo, cv2.COLOR_RGB2BGR)
cv2.imwrite('logo.jpg', logo)

