# Opencv converts the image into the numpy array

import cv2

# PAth of the image
# Reading Color imiga = 1, black and white = 0
img = cv2.imread("galaxy.jpg",1)
print(type(img))
print(img.shape)

# Displaying the image on the window
# <SYNTAX> cv2.imshow("<Windows name>", <imgage variable>)
cv2.imshow("Galaxy", img)
# Waitkey
# 0 --> if user press any button it will close the window
# Or we can also add the timme
cv2.waitKey(0)
cv2.destroyAllWindows()
