import numpy as np
from cv2 import cv2

img = cv2.imread('puzzle.PNG')
imgGry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgGry = cv2.medianBlur(imgGry,5)

ret , thrash = cv2.threshold(imgGry, 240 , 255, cv2.CHAIN_APPROX_NONE)
contours , hierarchy = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)


print(len(imgGry))
i = 1
n = 1067
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
    x = approx.ravel()[0]
    y = approx.ravel()[1] 

    perimeter = cv2.arcLength(contour,True)
    #print(perimeter)
    
    if len(approx) == 4 and perimeter < 510 and perimeter > 500:
        i+= 1
        x, y , w, h = cv2.boundingRect(approx)
        aspectRatio = float(w)/h
        #print(aspectRatio)
        cv2.drawContours(img, [approx], 0, (0, 0, 255), 1)
        
        
        if aspectRatio >= 0.97 and aspectRatio < 1.016:
            # cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0))
            num = img[n-y:n-y+133, n-x:n-x+133]

        cv2.imshow('grid', img)
        cv2.imshow('shapes', num)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        # cv2.imshow('shapes', img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
print(i)

cv2.imshow('shapes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()