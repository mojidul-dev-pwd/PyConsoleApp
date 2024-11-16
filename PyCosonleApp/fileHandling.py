"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"""
import os
#f = open("demofile.txt")
#f = open("demofile.txt","r")
#f = open("demofile.txt", "rt")
f = open("demofile.txt", "r")
print(f.read())
f = open("E:\\Projects\PYTHON\demofile.txt", "r")
print(f.read())
#You can return one line by using the readline() method
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline()) # return second line of a file
f.close()
f = open("E:\\Projects\PYTHON\demofile.txt", "a")
f.write("Now the file has more content!")
f.close()
f = open("E:\\Projects\PYTHON\demofile.txt", "r")
print(f.read())

f = open("E:\\Projects\PYTHON\demofile.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("E:\\Projects\PYTHON\demofile.txt", "r")
print(f.read())
f.close()
#file delete
os.remove("E:\\Projects\PYTHON\demofile.txt")

if os.path.exists("E:\\Projects\PYTHON\demofile.txt"):
  os.remove("E:\\Projects\PYTHON\demofile.txt")
else:
  print("The file does not exist")
#delete folder
# os.rmdir("myfolder")
