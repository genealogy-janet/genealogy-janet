import os 

def main(): 
    directory = input("Enter the directory for your file : ") 
  
    filename = input("Enter the filename : ")
  
    name = input("Enter your name : ") 
  
    address = input("Enter your address : ")
  
    phone_number = input("Enter your phone number : ") 
  
    #check if the directory exists
    if os.path.isdir(directory):
        #create and open the file to write
        writeFile = open(os.path.join(directory,filename),'w') 
        #writing the data by comma seperated writeFile.write(name+','+address+','+phone_number+'\n') 
        # #close the file after writing is done
        writeFile.close() 
  
        print("File contents:")   
        #reading the file for proof of storing
        readFile = open(os.path.join(directory,filename),'r') 
        for line in readFile:
            print(line)
        readFile.close()
    else:
            print("Sorry that directory does not exist...")
main()