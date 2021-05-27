hahah = open("readtext.txt", "r") 
#"r"read "w"write "a" append 
#"r+" means read and write

print(hahah.readable())

#print(hahah.readline()) #read the first line only
#print(hahah.readline())
#print(hahah.readlines()) 

#either above or below , only one from 

for eachline in hahah.readlines():
    print(eachline)

hahah.close();