# Import dependencies
import numpy as np
import matplotlib.pyplot as plt
from cv2 import cv2 # This is the OpenCV Python library
import pytesseract # This is the TesseractOCR Python library# Set Tesseract CMD path to the location of tesseract.exe file
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
possible_characters = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,5)
 
#thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#dilation
def dilate(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
    
#erosion
def erode(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

#opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

#canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)

#skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

#template matching
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED) 


def get_number(small_image):

    num = get_grayscale(small_image)
    num = remove_noise(num)
    custom_config = r'--oem 3 --psm 6 outputbase digits'
    return pytesseract.image_to_string(num, config=custom_config)[0]






if __name__ == '__main__':
    problem_grid = np.zeros([9,9])
    print(problem_grid)

    dx = 0
    dy = 0

    img = cv2.imread('puzzle.png')
    imgGry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgGry = cv2.medianBlur(imgGry,5)

    ret , thrash = cv2.threshold(imgGry, 240 , 255, cv2.CHAIN_APPROX_NONE)
    contours , hierarchy = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)


    print(len(imgGry))
    m = len(imgGry)//9-3
    n = len(imgGry)-m
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
        x = approx.ravel()[0]
        y = approx.ravel()[1] 

        perimeter = cv2.arcLength(contour,True)
        #print(perimeter)
        
        if len(approx) == 4 and perimeter < 510 and perimeter > 500:
            x, y , w, h = cv2.boundingRect(approx)
            aspectRatio = float(w)/h
            #print(aspectRatio)
            cv2.drawContours(img, [approx], 0, (0, 0, 255), 1)
            
            
            if aspectRatio >= 0.97 and aspectRatio < 1.016:
                num = img[n-y:n-y+m, n-x:n-x+m]
                number = get_number(num)
                cv2.putText(img, number, (n-x, n-y+60), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))
            
                if number in possible_characters:
                    problem_grid[dy, dx] = number
                else:
                    problem_grid[dy, dx] = 0
                dx += 1

                if dx % 9 == 0 and dx != 0:
                    dy += 1
                    dx = 0
                    if dy == 9:
                        break
            
        
    print(problem_grid)
    cv2.imshow('shapes', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



    #img = thresholding(img)
    # Adding custom options
    # custom_config = r'--oem 3 --psm 6'
    # print(pytesseract.image_to_string(img, config=custom_config))

    # custom_config = r'--oem 3 --psm 6 outputbase digits'
    # print(pytesseract.image_to_string(img, config=custom_config)[0])

    # d = pytesseract.image_to_data(img, output_type=Output.DICT)
    # print(d['text'])
