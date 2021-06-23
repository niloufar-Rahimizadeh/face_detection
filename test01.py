# pip3 install opencv-python
import cv2 as cv

# read image from your local file system
original_image = cv.imread("people.jpg")

window_name = 'original_image'
  

# cv.imshow(window_name, original_image)
# cv.waitKey(0)


# Convert color image to grayscale for Viola-Jones

grayscale_image = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)

# cv.imshow(window_name, grayscale_image)
# cv.waitKey(0)

# Load the classifier and create a cascade object for face detection
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

# The face_cascade object has a method detectMultiScale(), which receives an image 
# as an argument and runs the classifier cascade over the image. The term MultiScale 
# indicates that the algorithm looks at subregions of the image in multiple scales, 
# to detect faces of varying sizes:

detected_face = face_cascade.detectMultiScale(grayscale_image)