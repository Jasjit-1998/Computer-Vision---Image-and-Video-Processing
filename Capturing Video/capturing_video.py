import cv2, time

# Videos are just seris of images
# We will be reading images/frames one by one

# Trigger Video Capture Object to capture the video from the webcamp
# In the below code camera will immidiately turn on and off
# So we will be using the time Library


video = cv2.VideoCapture(0)

check, frame = video.read()
print(check)
print(frame)

time.sleep(3)    # Holding the script for 3 seconds
cv2.imshow("Capturing", frame)

cv2.waitKey(0)
video.release()
cv2.detroyAllWindows()


# Creating the frame object which will read video of that Object
