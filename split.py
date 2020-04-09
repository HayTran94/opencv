import cv2

img = cv2.imread('image.jpg')

subimg = img[100:200, 300:400]

cv2.imshow('image', subimg)


cv2.waitKey(0)

cv2.destroyAllWindows()