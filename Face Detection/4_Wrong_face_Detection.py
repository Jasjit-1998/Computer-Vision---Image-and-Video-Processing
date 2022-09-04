# For Face detection we have xml files that contain the features of the face
# hese xml files are created using the training samples then software like opencv are used to create such xml files
# In this we have haarcascade_frontalface


# Algorith
# Loading image in python  --> USing xml model pythnon will start searching all the Windows

import cv2

# <SYNTAX> face_cascade=cv2.CascadeClassifier("PAth of the harcascade classifier")
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# USing the gray scale image we can have better image detection
img = cv2.imread("news.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Creating face object to store width and height of the object
faces = face_cascade.detectMultiScale(gray_img,
scaleFactor = 1.1,
minNeighbors = 5)



# Drawing the rectangle accross the face -:
for x,y,w,h in faces:
    #<SYNTAX> img = cv2.rectangle(img, starting point,end point (along the diagnol), color, width of rec)
    img = cv2.rectangle(img, (x,y),(x+w,y+h), (0,255,0), 3)

print(type(faces))
print(faces)

# resized = cv2.resize(img,(500,500))   Rather than putting the value it is suggested to extend the shape of the image
resized = cv2.resize(img,(int(img.shape[1]/3), int(img.shape[0]/3)))

cv2.imshow("gray", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()


# Summary - : We first convert the image to the GRAY scale
# Then using image detection classifier we we detect the face and then draw the rectangle on the original face
