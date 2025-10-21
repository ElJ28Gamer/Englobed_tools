#Imports
from util1 import cam           #Tool 1 code and functionality

#Defs
def menu():                     #Prints what tools have
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
    
#Functions
menu()
x = int(input())    #Waits until a number is written

if x == 1:          #Opens tool 1
    cam()
    menu()
elif x == 2:        #Opens tool 1
    2()
    menu()
elif x == 3:        #Opens tool 1
    3()
    menu()
elif x == 4:        #Opens tool 1
    4()
    menu()
else:               #Exits
    exit