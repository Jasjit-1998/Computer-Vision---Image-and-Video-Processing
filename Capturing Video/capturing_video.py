import cv2, time

# Videos are just seris of images
# We will be reading images/frames one by one

# Trigger Video Capture Object to capture the video from the webcamp
# In the below code camera will immidiately turn on and off
# So we will be using the time Library


video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    print(check)
    print(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #time.sleep(3)    # Holding the script for 3 seconds
    cv2.imshow("Capturing", gray)
    key=cv2.waitKey(2000)

# If statement will break the while loop when 'q' key is pressed
    if key ==ord('q'):
        break


video.release()
cv2.detroyAllWindows()


# Creating the frame object which will read video of that Object
