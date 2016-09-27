#program to encode and decode messages

import random

#Generates random file name composed of 3 random integers
randname = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + ".txt"

#Function for displaying and choosing encode or decode
def Start():
    choice = raw_input("Do you want to [e]ncode or [d]ecode a message? > ")

    if choice == "e":
        Encode()
    elif choice == "d":
        Decode()
    else:
        Start()

#function to save encoded or decoded message
def Sav(message, name):
    file = open(name, "a")
    file.write(message)

    print "File has been saved to: %r" % name

    exit()

#This function encodes message entered by user in rot13 cipher
def Encode():
    print "Please enter your message to encode: "
    message = raw_input().encode("rot13")
    print "\n"

    Sav(message, randname)

#This function asks foor filename to decode from rot 13 cipher
#and outputs the decoded message
def Decode():
    print "Please choose a file name in file directory? >  "
    name = raw_input("")
    file1 = (open(name, "r+")).read()
    output = "\n\nYour decoded file reads:\n\n " + file1.decode("rot13")
    Sav(output, name)
    #output.write("\n---\nThe docoded message is as follows:\n\n%r") % output

print "This program will encode and decode messages for you. \n "

Start()
