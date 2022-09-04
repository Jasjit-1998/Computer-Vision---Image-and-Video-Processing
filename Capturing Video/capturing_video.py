import cv2

# Videos are just seris of images
# We will be reading images/frames one by one

# Trigger Video Capture Object to capture the video from the webcamp
# In the below code camera will immidiately turn on and off
video = cv2.VideoCapture(0)
video.release()
