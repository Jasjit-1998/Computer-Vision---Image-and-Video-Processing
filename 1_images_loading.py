import cv2

# PAth of the image
# Reading Color imiga = 1, black and white = 0
img = cv2.imread("galaxy.jpg",1)
print(type(img))
