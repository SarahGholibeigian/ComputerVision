import cv2
import random

# first change environment to pycv
# second run <export DISPLAY=:0> in Ubuntu

img = cv2.imread('assets/logo.jpg', -1)

print(img)
print(type(img))
print(img.shape)
print(img[180][160])

# Change first 100 rows to random pixels
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# Copy part of image
tag = img[500:700, 600:900]
img[100:300, 650:950] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()