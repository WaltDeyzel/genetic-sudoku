from cv2 import cv2
from generate import checkForErrorInGrid
def filterDigits(digits):
    numbers = [ '1', '2', '3', '4', '5', '6', '7', '8', '9']
    filtered_digits = []
    for digit in digits:

        if digit.getNumber() in numbers:
            filtered_digits.append(digit)
            numbers.remove(digit.getNumber())
            
            if len(numbers) == 0:
                break
    
    return filtered_digits

def getImg(digits, number):
    
    for digit in digits:
        if int(digit.getNumber()) == number:
            return digit
    return -1


def image_output(image, grid, digits):

    image = image.copy()
    width = len(image)//9
    ofsety = int(width / 3)
    ofsetx = int(width / 6)
    errorNumbersXY = checkForErrorInGrid(grid)
    
    for row in range(9):
        for col in range(9):
            number = int(grid[row, col])
            y = int(row*width)
            x = int(col*width)
            num = getImg(filterDigits(digits), number)
            if num == -1:
                cv2.putText(image, str(number), (x + ofsetx, y + ofsety), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))
            else:
                cut = 10
                m = len(num.getNumImg()) - cut+3
                image[y+cut:y+m, x+cut:x+m] = num.getNumImg()[cut:m, +cut:m]
            
            # TOD0: Create toggle 
            if True:
                for cor in errorNumbersXY:
                    # print('Check4Error implementation')
                    x = int(cor[0]*width)
                    y = int(cor[1]*width)
                    startPoint = (x,  y)
                    endPoint = (x + width, y + width)
                    # print(startPoint, endPoint)
                    cv2.rectangle(image, startPoint, endPoint, (0, 0, 255), 3)
    
    cv2.imshow('shapes', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
            
if __name__ == '__main__':
    import numpy as np
    from inputSudoku import image_input
    problem_grid = np.array([
    [1,0,0, 0,0,0, 0,0,0],
    [0,2,0, 0,0,0, 0,0,0],
    [0,0,0, 0,3,0, 0,3,0],

    [0,0,0, 0,0,0, 0,0,0],
    [0,2,0, 0,0,0, 0,0,0],
    [0,0,0, 0,4,4, 4,0,0],

    [1,0,0, 0,0,0, 0,0,0],
    [0,2,0, 0,0,0, 0,0,0],
    [0,0,0, 0,0,0, 0,0,0],
    ])
    # Name of puzzle image 
    # Note image does not correspond to input grid
    img = 'images/p2.jpg'  
    # Locate Sudoku grid and return only the grid
    puzzle_img = image_input(img)
    cv2.imshow('shapes', puzzle_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    image_output(puzzle_img, problem_grid, [])


