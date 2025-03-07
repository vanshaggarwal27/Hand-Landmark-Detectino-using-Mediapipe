import mediapipe as mp
import cv2
import time

# Grabbing the Holistic Model from Mediapipe and
# Initializing the Model

#gives access to Mediapipe's holistic model, which detects face, hands, and body landmarks.
mp_holistic= mp.solutions.holistic

holistic_model=mp_holistic.Holistic(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Initializing the drawing utils for drawing the facial landmarks on image
mp_drawing = mp.solutions.drawing_utils

#capturing image
capture = cv2.VideoCapture(0);

# Initializing current time and precious time for calculating the FPS
previousTime = 0
currentTime = 0

while capture.isOpened():
    # capture frame by frame
    ret,frame = capture.read()
  
    # resizing the frame for better view
    frame=cv2.resize(frame,(800,800))

    # Converting the from BGR to RGB
    image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    # Making predictions using holistic model
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    result = holistic_model.process(image)
    image.flags.writeable = True

    # Converting back the RGB image to BGR
    image = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)

    #drawing facial landmark skip 

    # Drawing Right hand Land Marks
    mp_drawing.draw_landmarks(
        image,
        result.right_hand_landmarks,
        mp_holistic.HAND_CONNECTIONS)
    
    #Drawing Left hand landmark
    mp_drawing.draw_landmarks(
    image,
    result.left_hand_landmarks,
    mp_holistic.HAND_CONNECTIONS)

    #calculating FPS
    currentTime = time.time()
    fps = 1/(currentTime-previousTime)
    previousTime = currentTime

    # Displaying FPS on the image
    cv2.putText(image,str(int(fps)) + "FPS", (10,70),cv2.FONT_HERSHEY_COMPLEX, 1,(0,255,0),2)

    # Display the resulting image
    cv2.imshow("Hand Landmarks", image)

    # Enter key 'q' to break the loop
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# When all the process is done
# Release the capture and destroy all windows
capture.release()
cv2.destroyAllWindows()
    
