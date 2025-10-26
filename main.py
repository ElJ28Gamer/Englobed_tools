#Imports
import cv2 as cv                 #Camera lib
import os

#Variables
numberlist = [1, 2, 3, 4]

#Defs
def menu():                      #Prints what tools have
    print("")
    print("//  Englobed Tools  //")
    print("")
    print(" - Press 1 to open the camera")
    print(" - Press 2 to open a list of all the WIFI's you have connected to. (Only in Windows)")
    print(" - Press 3 to ")
    print(" - Press 4 to ")
    print(" - To exit, press Enter")
    print("")
    print("//  Englobed Tools  //")
    print("")

def selection():
    if x == 1:          #Opens tool 1
     cam()
     loop()
    elif x == 2:        #Opens tool 2
     showifi()
     loop()
    elif x == 3:        #Opens tool 3
     showifi()
     loop()
    elif x == 4:        #Opens tool 4
     showifi()
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
    cv.imshow("Camera", color)                               #Custom name
    if cv.waitKey(1) == ord("q") or cv.waitKey(1) == ord("Q"):      #Keys to exit
        break

 cap.release()                  #Stops capture
 cv.destroyAllWindows()         #Closes window

def showifi():
    print("")
    os.system("C://Users/Usuario/Desktop/Codes/Englobed_tools/wifi.bat")
    print("")

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