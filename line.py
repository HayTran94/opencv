import cv2

img = cv2.imread('image.jpg')

cv2.line(img, (0, 50), (400, 50), (255,255,0), 5)

cv2.imwrite('writtenImg.jpg', img)

