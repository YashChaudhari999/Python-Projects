# pip install opencv-python

import cv2

image_convert = cv2.imread('D:\\Yash\\Coding\\Python\\Image converting to Gray Scale\\download.jpg',
cv2.IMREAD_UNCHANGED)

im_gray = cv2.cvtColor(image_convert, cv2.COLOR_BGR2GRAY)

thresh, im_black = cv2.threshold(im_gray, 170, 255, cv2.THRESH_BINARY)

cv2.imshow('download.jpg', im_black)
cv2.imwrite('im_grayscale.png', im_gray)
# cv2.imwrite('im_black.png', im_black)

cv2.waitKey(0)

cv2.destroyAllWindows()