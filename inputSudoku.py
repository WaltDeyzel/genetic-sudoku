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
    cv2.waitKey(300)
    cv2.destroyAllWindows()

def get_number(small_image):
    
    num = get_grayscale(small_image)
    #num = remove_noise(num)
    #num = thresholding(num)
    #num = opening(num)
    #num = erode(num)
    #num = dilate(num)
    thresh = 127
    im_bw = cv2.threshold(num, thresh, 255, cv2.THRESH_BINARY)[1]
    im_bw = 255-im_bw
    #show(im_bw)
    num = small_image
    custom_config = r'--oem 3 --psm 6 outputbase digits'
    return pytesseract.image_to_string(num, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')[0]



def input_puzzle(img):

    problem_grid = np.zeros([9,9])
    digits = []

    width = len(img)//9
    size = len(img)
    for row in range(9):
        for col in range(9):
            # Cut c pixels from surrounding Border
            c = 5
            num = img[row*width+c:row*width+width-c, col*width+c:col*width+width-c]
            number = get_number(num)
            
            num = img[row*width:row*width+width, col*width:col*width+width]
            digits.append(Digit(num, number))
            #print(number)
            r = int(100*(row*width)/(11*size))
            c = int(100*(col*width)/(11*size))
            
            if number in possible_characters:
                    problem_grid[r, c] = number
            else:
                problem_grid[r, c] = 0

    return problem_grid, digits


def image_input(path):
    problem_grid = np.zeros([9,9])

    img = cv2.imread(path)
    imgGry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    _ , thrash = cv2.threshold(imgGry, 127 , 255, cv2.CHAIN_APPROX_NONE)
    contours , _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
       
        perimeter = cv2.arcLength(contour,True)
        
        if  perimeter > 900:
            x, y , w, h = cv2.boundingRect(approx)
            puzzle = img[y:y+h, x:x+w]
            # Return cropped image.
            cv2.drawContours(img, [approx], 0, (0, 143, 255), 1)
            return puzzle
        
        else:
            print('Return original image')
            return img
            
    return problem_grid


if __name__ == '__main__':
    grid_image = image_input('p2.jpg') # This returns either a cropped image or the original.
    grid, digits = input_puzzle(grid_image)
    print(grid)
   
