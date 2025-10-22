#Imports
import cv2 as cv                 #Camera lib

#Variables
numberlist = [1, 2, 3, 4]

#Defs
def menu():                      #Prints what tools have
    print("")
    print("//  Englobed Tools  //")
    print("")
    print(" - Press 1 to open the camera")
    print(" - Press 2 to ?")
    print(" - Press 3 to ?")
    print(" - Press 4 to ?")
    print(" - To exit, press Enter")
    print("")
    print("//  Englobed Tools  //")
    print("")

def selection():
    if x == 1:          #Opens tool 1
     cam()
     loop()
    elif x == 2:        #Opens tool 2
     cam()
     loop()
    elif x == 3:        #Opens tool 3
     cam()
     loop()
    elif x == 4:        #Opens tool 4
     cam()
     loop()

    
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

def loop():
    menu()
    x = int(input())    #Waits until a number is written
    selection()
    if x != numberlist:
        return False
    

while True:
    menu()
    x = int(input())    #Waits until a number is written
    selection()
    if x != numberlist:
        break
    loop()