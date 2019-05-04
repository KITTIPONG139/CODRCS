from microbit import *
import os

#write to file
with open('myname.txt', 'w') as myFile:
    myFile.write("My name is TONG.")

#a listdir of the file directory
print(os.listdir())

#read the file and print the content
with open('myname.txt', 'r') as myFile:
    a = myFile.read()
    print(a)
    display.scroll(a)

#close()
#name()
#read()
#wrte()

#os.listdir()
#os.remove("file")
#os.size("file")
#os.uname()