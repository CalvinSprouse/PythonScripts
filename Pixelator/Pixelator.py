import cv2
import numpy as np

threshold = 0.55

img = cv2.imread("image.jpg", 0)
img_reverted = cv2.bitwise_not(img)
new_img = img_reverted / 255

textOut = []
for row in new_img:
    for num in row:
        if num > threshold:
            textOut.append(1)
        elif num <= threshold:
            textOut.append(0)

with open("output.txt", 'w+') as fileOut:
    for num in textOut:
        fileOut.write(str(num))

print("Fin")
