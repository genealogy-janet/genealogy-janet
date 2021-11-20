

import os

def main():
    directory = input("Enter the directory that you want to save the file : ")
    filename = input("Enter the filename : ")
    name = input("Enter your name : ")
    address = input("Enter your address : ")
    phone_number = input("Enter your phone number : ")

#check to see if the directory exists
if os.path.isdir(directory):
    #create and open file to write
    writeFile = open(os.path.join(directory,filename),'w')
    #write data separate with a comma   
    writeFile.write(name+','+address+','+phone_number+'\n')
    #close file after written
    writeFile.close()

    print("File contents:")
    #reading the file for proof of storing
    readFile = open(os.path.join(directory,filename),'r')
    for line in readFile:
        print(line)
    readFile.close()
else:
    print("Sorry that directory doesn't exist...")
main()

