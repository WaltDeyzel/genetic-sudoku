from cv2 import cv2

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


def image_output(image, gird, digits):

    image = image.copy()
    width = len(image)//9

    for row in range(9):
        for col in range(9):
            number = int(gird[row, col])
            y = int(row*width)
            x = int(col*width)
            num = getImg(filterDigits(digits), number)
            if num == -1:
                cv2.putText(image, str(number), (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))
            else:
                cut = 10
                m = len(num.getNumImg()) - cut+3
                image[y+cut:y+m, x+cut:x+m] = num.getNumImg()[cut:m, +cut:m]
                
                #     cv2.imshow('shapes', image[x:x+m, y:y+m])
                #     cv2.waitKey(0)
                #     cv2.destroyAllWindows()
            #cv2.putText(img, str(number), (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))
    
    cv2.imshow('shapes', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
            




