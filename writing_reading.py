import os
import shelve
import pprint 

#READING WRITTING PROCESS
""" three basis steps
1. open()
2. read() or write()
3. close()
"""

hellofile=open('/home/cesarbartolo/Desktop/PYTHON_PROGRAMMING/PYTHON_PROGRAMMING/3.Automating the boring stuff/chap8. WRITING-READING/helloworld.txt')

#read is tghe default and returns a string
hellocontent= hellofile.read()
print (hellocontent)


sonnetfile=open('/home/cesarbartolo/Desktop/PYTHON_PROGRAMMING/PYTHON_PROGRAMMING/3.Automating the boring stuff/chap8. WRITING-READING/sonnet29.txt')
print (sonnetfile.readlines())


#putting the things togheter

path="/home/cesarbartolo/Desktop/PYTHON_PROGRAMMING/PYTHON_PROGRAMMING/3.Automating the boring stuff/chap8. WRITING-READING/bacon.txt"
baconfile = open(path,"w")
baconfile.write("There is a plenty of room at the bottom!! \n")
baconfile.close()
baconfile=open(path, "a")
baconfile.write("Lecture deliver by Richard Faynmann at 60's in CALTECH")
baconfile.close()

baconfile=open(path)
content=baconfile.read()
baconfile.close()

print (content)

#SHELVE MODULE FOR BINARY DATA

shelffile=shelve.open("/home/cesarbartolo/Desktop/PYTHON_PROGRAMMING/PYTHON_PROGRAMMING/3.Automating the boring stuff/chap8. WRITING-READING/mydata")
cats=["London", "Pooka", "Simon"]
shelffile["cats"]=cats #like in dictionaries
shelffile.close()

shelffile=shelve.open("/home/cesarbartolo/Desktop/PYTHON_PROGRAMMING/PYTHON_PROGRAMMING/3.Automating the boring stuff/chap8. WRITING-READING/mydata")

print (shelffile)

shelffile.close()

#Saving Variables with the pprint.pformat() Function
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)

fileObj=open("/home/cesarbartolo/Desktop/PYTHON_PROGRAMMING/PYTHON_PROGRAMMING/3.Automating the boring stuff/chap8. WRITING-READING/mycats.py" , "w")
#the file is stored in mycats.py
fileObj.write("cats=" + pprint.pformat(cats) + "\n")

fileObj.close()


os.chdir("/home/cesarbartolo/Desktop/PYTHON_PROGRAMMING/PYTHON_PROGRAMMING/3.Automating the boring stuff/chap8. WRITING-READING" )
print (os.getcwd())

#we can use the python file created
import mycats

print (mycats.cats)

print (mycats.cats[0])

print (mycats.cats[0] ["name"])



