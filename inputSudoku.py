# Import dependencies
import numpy as np
import matplotlib.pyplot as plt
from cv2 import cv2 # This is the OpenCV Python library
import pytesseract # This is the TesseractOCR Python library# Set Tesseract CMD path to the location of tesseract.exe file
from pytesseract import Output

from digit import Digit

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
    return cv2.threshold(image, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

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

def show(img):
    cv2.imshow('shapes', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def get_number(small_image):

    num = get_grayscale(small_image)
    #num = remove_noise(num)
    num = thresholding(num)
    num = opening(num)
    num = erode(num)
    num = dilate(num)
    #show(num)

    custom_config = r'--oem 3 --psm 6 outputbase digits'
    return pytesseract.image_to_string(num, config=custom_config)[0]



def input_puzzle(img):

    problem_grid = np.zeros([9,9])
    digits = []

    width = len(img)//9
    size = len(img)
    for row in range(9):
        for col in range(9):

            num = img[row*width:row*width+width, col*width:col*width+width]
            r = int(100*(row*width)/(11*size))
            c = int(100*(col*width)/(11*size))

            number = get_number(num)
            digits.append(Digit(num, number))
            if number in possible_characters:
                    problem_grid[r, c] = number
            else:
                problem_grid[r, c] = 0

    return problem_grid, digits


def image_input(path):
    problem_grid = np.zeros([9,9])

    img = cv2.imread(path)
    imgGry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #imgGry = thresholding(imgGry)
    #imgGry = remove_noise(imgGry)
    imgGry = opening(imgGry)
    #imgGry = cv2.medianBlur(imgGry,5)

    _ , thrash = cv2.threshold(imgGry, 127 , 255, cv2.CHAIN_APPROX_NONE)
    contours , _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
       
        perimeter = cv2.arcLength(contour,True)
        print(perimeter)
        
        if  perimeter > 900:
            x, y , w, h = cv2.boundingRect(approx)
            #cv2.putText(img, 'HERE', (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))
            puzzle = img[y:y+h, x:x+w]
            #problem_grid = input_puzzle(puzzle)
            cv2.drawContours(img, [approx], 0, (0, 143, 255), 1)
            return puzzle
        
        else:
            print('Return original image')
            return img
            
            
    cv2.imshow('shapes', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return problem_grid



    #img = thresholding(img)
    # Adding custom options
    # custom_config = r'--oem 3 --psm 6'
    # print(pytesseract.image_to_string(img, config=custom_config))

    # custom_config = r'--oem 3 --psm 6 outputbase digits'
    # print(pytesseract.image_to_string(img, config=custom_config)[0])

    # d = pytesseract.image_to_data(img, output_type=Output.DICT)
    # print(d['text'])

if __name__ == '__main__':
    grid = image_input('puzzle.PNG')
