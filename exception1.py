#Write a Python program that opens afile and handles a FileNotFoundError exception if the file does not exist.

def fileRead():
    filename = input("Enter File Name: ")
    try:
        myfile = open(filename, "r")
        print("File Opened Succesfully.")
        myfile.close()
        
    except FileNotFoundError:
        print("File Not Found.")

fileRead()