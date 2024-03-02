import time
import cv2
import pytesseract

image_path = 'frame1900.png'
a = 1
last_time = time.time()

while(True):
    input_image = cv2.imread(image_path)
    x, y, w, h = 750, 720, 350, 100
    screen = input_image[y - h:y, x - w:x]

    # What for all this code bellow?!
    print('loop took {} seconds' .format(time.time()-last_time))
    last_time = time.time()
    cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    cv2.imwrite('newI.png', screen)
    a += 1
    print(a)
    if a == 2:
        cv2.destroyAllWindows()
        break

img = cv2.imread('newI.png')
text = pytesseract.image_to_string(img)
print(text)