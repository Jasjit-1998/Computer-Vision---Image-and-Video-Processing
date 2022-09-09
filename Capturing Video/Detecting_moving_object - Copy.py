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
    # <SYNTAX>.thresh_delta = cv2.threshold(delta_frame, diffrence between frames , 255, cv.THRESH_BINARY)
    thresh_delta = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]     # Accesing second item of the tuple as we are using the threshold binary
    thresh_frame = cv2.dilate(thresh_delta, None, iterations = 2)   # Smoothning of the threshold

# Finding the Countour   (Soring the countour in the Tupil)
# Checking the Area of the countour
    # <SYNTAX> = (cnts,_) = cv2.findCountours(thresh_frame.copy(), cv2.RETR_EXTERNAL (external Countour retrival), cv2.CHAIN_APPROX_SIMPLE(approximation method used by the open cv))
    (cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue

   # If countour is greater than 1000 pixel then we have to draw the rectangle arounf that frame
   # Perameters defining the rectangle
        (x, y, w, h) = cv2.boundingRect(contour) # Creating the rectagle
        cv2.rectangle(frame, (x,y), (x+w, y+w), (0,255,0), 3)  # Drawing the rectangle on the frame


    cv2.imshow("Gray Frame", gray)
    cv2.imshow("DeltaFrame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Color Frame", frame)

    key=cv2.waitKey(1)
    print(gray)

    if key == ord('q'):
        break
        #cv2.imshow("delta_frame",delta_frame)

    #time.sleep(3)    # Holding the script for 3 seconds



# If statement will break the while loop when 'q' key is pressed


video.release()
cv2.detroyAllWindows()


# Creating the frame object which will read video of that Object
