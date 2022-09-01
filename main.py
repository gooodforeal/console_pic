# import cv2
import time
import numpy as np
from PIL import Image
from pyfiglet import Figlet


COLOR = 130 # Color RGB code

# img = cv2.imread("C:\Users\23906\Desktop\YYGconsole\img.jpeg", cv2.IMREAD_GRAYSCALE)
# thresh = 128
# bin_img = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)[1]

img = np.asarray(Image.open('img4.jpg').convert('RGB'))
TEXT = Figlet(font="slant")
print(TEXT.renderText(200* " " + "BY TIMOTHY"))

# print(img)

# Lines
for line in img:
    print(200*" ", end="")
    # Dots
    for dot in line:
        if dot[0] < COLOR and dot[1] < COLOR and dot[2] < COLOR:
            print("#", end="")
        else:
            print("-", end="")
        print("    ", end="")
    print("\n")
    time.sleep(0.1)