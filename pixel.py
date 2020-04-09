import cv2

img = cv2.imread('image.jpg')

px = img[0,0]

for i in range(500):
    img[i,i] = [1,1,1]
    img[i+2,i+2]  = [1,1,1]

cv2.imshow('image', img)

cv2.waitKey(0)

cv2.destroyAllWindows()


