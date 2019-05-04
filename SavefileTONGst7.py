from microbit import *
import os

#write to file
with open('myname.txt', 'w') as myFile:
    myFile.write("MY NAME IS TONG...")
    myFile.write("SNRU...")
    myFile.write("139...")

with open('snru.txt', 'w') as myFile:
    myFile.write("SNRU.")
    myFile.write("191.")

#a listdir of the file directory
print(os.listdir())
#read the file and print the content
with open('myname.txt', 'r') as myFile:
    a = myFile.read()
    print(a)
    display.scroll(a)

with open('snru.txt', 'r') as myFile:
    b = myFile.read()
    print(b)
    display.scroll(b)

#close()
#name()
#read()
#wrte()

#os.listdir()
#os.remove("file")
#os.size("file")
#os.uname()