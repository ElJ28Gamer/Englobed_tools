import cv2 as cv            #Camera lib

def cam():
 cap = cv.VideoCapture(0)

 if not cap.isOpened():     #Opens cam, if isn't opened
    print("NO")
    exit()

 while True:
    ret, frame = cap.read()

    if not ret:
        print("exit")
        break

    color = cv.cvtColor(frame, cv.COLOR_BGR2BGRA)
    cv.imshow("CUSTOM CAMERA", color)                               #Custom name
    if cv.waitKey(1) == ord("q") or cv.waitKey(1) == ord("Q"):      #Keys to exit
        break

 cap.release()                  #Stops capture
 cv.destroyAllWindows()         #Closes window
