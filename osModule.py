import os
from datetime import datetime


# Return all method of os module
print(dir(os))


# Return present current directory
print(os.getcwd())


# Change current working directory
os.chdir('E:/Programming/PythonLibrary')
print(os.getcwd())


# Return all files in current working directory
print(os.listdir())


# Make Directory
os.mkdir("folder1")
os.makedirs("folder2/folder3")
print(os.listdir())


# Delete Directory
os.rmdir("folder1")
os.removedirs("folder2/folder3")
print(os.listdir())


# Rename Directory Or File
os.rename("f1.txt","f2.txt")
print(os.listdir())


# Return File Description
print(os.stat("f2.txt"))
print(os.stat("f2.txt").st_size)                    # Return File Size
mod_time = os.stat("f2.txt").st_mtime               # Return Last Modified Time Of File
print(datetime.fromtimestamp(mod_time))


# Return folder structure in form of generator
for dirpath,dirname,filename in os.walk('E:/'):
    print("Current Path : ",dirpath)
    print("Directories : ",dirname)
    print("Files : ",filename)


# Get Environment Variable
print(os.environ.get('HOME'))


# Create file in Home Directory
file_path = os.path.join(os.environ.get('HOME'),'test.txt')
print(file_path)


# Return BaseName
print(dir(os.path))
print(os.path.basename("E:/Programming/PythonLibrary/Data.txt"))     # Return base name of the file
print(os.path.dirname("E:/Programming/PythonLibrary/Data.txt"))      # Return directory name of base file
print(os.path.split("E:/Programming/PythonLibrary/Data.txt"))        # Return directory and base file
print(os.path.exists("E:/Programming/PythonLibrary/Data.txt"))       # Return path exist or not
print(os.path.isfile("E:/Programming/PythonLibrary/Data.txt"))       # Return isFile Or Not
print(os.path.isdir("E:/Programming/PythonLibrary"))                 # Return isDirectory Or Not
print(os.path.splitext("E:/Programming/PythonLibrary/Data.txt"))     # Return file path and extension file
