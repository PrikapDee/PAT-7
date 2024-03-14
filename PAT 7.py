#Pat 7 ques1 python program 
#function will create a text file with current timestamp

import datetime; # import datetime to get current time stamp
def create_file(filepath): # creating function 
  f=open(filepath,"x") #open function to create file at given location 
  currenttimestamp=str(datetime.datetime.now()) #to calculate current time stamp
  f.writelines(currenttimestamp)#to write in file
  f.close()#to close the file

filepath=input("enter file path") #user will enter file path
create_file(filepath) #call of function


#Pat 7 ques 2 write python function to read from text file. function will take filename and display the text of file in console

def readfile(filename): # creating function to read and display content of file and file name as argument
    path=f"C:\\Users\e3019715\\pythonfiles\\{filename}" #variable to store file path and use of Fstring to contatnate strings
    f=open(path,"r") #to read content of file
    return(f.read()) #return content of file


filename=input ("enter file name") #file name entered through user

readfile(filename) #function call with argument of filename

#if sumthing is not correctly done.. please mention it otherwise i won't correct myself.
		
    
    