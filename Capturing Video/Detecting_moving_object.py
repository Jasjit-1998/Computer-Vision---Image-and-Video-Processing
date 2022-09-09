# Continuing from the capturing_Video.py
# steps to Proceed : PRocess the Frame in the While loop :
# 1. Capturing the frame into the variable and converting that to the gray scale
# 2. Applying the threhold to the frame
# 3. If the area is of the fram eis more that 500 pixels consuider it as the moving objecty
# 4. The  we will draw the rectangle around the countour with the minimum featureParams


# Now we are going to remove the unnecessary variable - :

import cv2, time

video = cv2.VideoCapture(0)

# Checking how many frames being generated
# Cheating a variable outsid the while loop

first_frame = None


while True:

    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Removing the noise from the immge by blurring it with GaussianBlue
    # gray=cv2.GaussianBlur(gray,size of gaussain blur,standard deviation)
    gray=cv2.GaussianBlur(gray,(21,21),0)
# Link - https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html




    if first_frame is None:
        first_frame = gray         # We will get the first frame in the numpy array
        continue

        # When the object appear in the frame then above if condition will be false
        # Comparing the diffrence between the current frame and the delta frames
        delta_frame = cv2.absdiff(first_frame,gray)


        cv2.imshow("Gray Frame", gray)
        #cv2.imshow("delta_frame",delta_frame)

    #time.sleep(3)    # Holding the script for 3 seconds

    key=cv2.waitKey(1)
    print(gray)q

# If statement will break the while loop when 'q' key is pressed
    if key ==ord('q'):
        break

video.release()
cv2.detroyAllWindows()


# Creating the frame object which will read video of that Object
