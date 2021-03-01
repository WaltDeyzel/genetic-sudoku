import numpy as np
import matplotlib.pyplot as plt
from cv2 import cv2

def image_output(image, gird):

    img = cv2.imread(image)

    width = len(img)//9

    for row in range(9):
        for col in range(9):
            number = int(gird[row, col])
            y = int(row*width + width//2)
            x = int(col*width + col//2)

            cv2.putText(img, str(number), (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))
    
    cv2.imshow('shapes', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
            




