# For Face detection we have xml files that contain the features of the face
# hese xml files are created using the training samples then software like opencv are used to create such xml files
# In this we have haarcascade_frontalface


# Algorith
# Loading image in python  --> USing xml model pythnon will start searching all the Windows

import cv2

# <SYNTAX> face_cascade=cv2.CascadeClassifier("PAth of the harcascade classifier")
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# USing the gray scale image we can have better image detection
img = cv2.imread(".\Face Detection\photo.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Creating face object to store width and height of the object
faces = face_cascade.detectMultiScale(gray_img,
scaleFactor = 1.05,
minNeighbors = 5)

print(type(faces))
print(faces)

cv2.imshow("gray", gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
