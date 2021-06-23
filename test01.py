# pip3 install opencv-python
import cv2 as cv

# read image from your local file system
original_image = cv.imread("people.jpg")

window_name = 'original_image'
  

cv.imshow(window_name, original_image)
cv.waitKey(0)
