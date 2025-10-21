#Imports
from util1 import cam

#Defs
def menu():
    print("")
    print("//  Englobed Tools  //")
    print("")
    print(" - Press 1 to open the camera")
    print(" - Press 2 to ")
    print(" - Press 3 to ")
    print(" - Press 4 to ")
    print(" - To exit, press Enter")
    print("")
    print("//  Englobed Tools  //")
    print("")
    
#Functions
menu()
x = int(input())

if x == 1:
    cam()
    menu()
elif x == 2:
    2()
    menu()
elif x == 3:
    3()
    menu()
elif x == 4:
    4()
    menu()
else:
    exit