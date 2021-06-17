import cv2

# first change environment to pycv
# second run <export DISPLAY=:0> in Ubuntu

img = cv2.imread('assets/logo.jpg', 1) # try using 0,-1,1

# img = cv2.resize(img, (400, 400))
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('new_img.jpg', img)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

