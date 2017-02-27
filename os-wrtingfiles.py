import os

#build paths in any operation system//  usr/bin/spam
path1=os.path.join("usr", "bin", "spam")

myfiles=["account.txt", "details.csv", "invite.docx"]

for filename in myfiles:
    print (os.path.join("home", "Desktop", "python", filename))
    
    

print (os.getcwd()) #current wprking directory

os.chdir('/home/cesarbartolo/Desktop' ) #change directory

print (os.getcwd())

#create a new folder (difrectorie)

#unlock and unlock
#os.maedirs('/home/cesarbartolo/Desktop/alma/cesar/santiago')


#absolutepath

os.path.abspath(".")


#dirname: everything that comes before the last slash
#basename: everything that comes after the last slash
path='/home/cesarbartolo/Desktop/Quantum mechanics.pdf'

print (os.path.basename(path))
print (os.path.dirname(path))

#togheter in a tuple

bookFilePath='/home/cesarbartolo/Desktop/Fundamentals of Applied Electromagnetics-Prentice Hall (2014).pdf'
print (os.path.split(bookFilePath))


#every folder separated
print (bookFilePath.split(os.path.sep))

#getting the size in bytes

print (os.path.getsize(bookFilePath))

#list of every file in the path
print (os.listdir("/home/cesarbartolo/Desktop/"))


##########
#getting the total size of "DEKSTOP"

totalsize=0
for filename in os.listdir("/home/cesarbartolo/Desktop/"):
    totalsize += os.path.getsize (os.path.join("/home/cesarbartolo/Desktop/", filename))
    
print (totalsize)

#############


