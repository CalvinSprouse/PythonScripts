import cv2


def rgbToHEX(red, green, blue):
    return '%02X%02X%02X ' % (red, green, blue)


img = cv2.imread('warren.jpg')
headerString = ('%02X' % len(img[0])) + "\n" + ('%02X' % len(img)) + "\n" + ('%02X' % 24) + "\n"
pixelArray = [headerString]

for pixRow in img:
    for pixel in pixRow:
        pixelArray.append(rgbToHEX(pixel[2], pixel[1], pixel[0]))

with open('output.txt', 'w+') as output:
    output.writelines(pixelArray)
