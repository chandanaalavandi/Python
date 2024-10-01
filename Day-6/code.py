file = open("example.txt", "r")
for line in file: 
    print(content)
file.close()


#_______________________________________________________________________________________________________________________________________________

#writing in writeMode
file = open("example.txt","w")   #overwriting the existing file.
file.write("Welcome to python session.")
file.close()

#If file 
#____________________________________________________________________________________________________________________________________

#Appending
file = open("example1.txt","a") 
file.write("\n we are appending new line in example1.txt file ")
file.close()


#--------------------------------------ASSIGNMENT---------------------------------------------------------------------------

file = open("data.txt","r")
total = 0

#data.txt contains a list of numbers, one per line
for line in file:
    total += int(line.strip())    # convert each line to an integer and add to total

#Prints the total sum while closing the file to realse memory
file.close()
print("The sum of numbers is :",total)
