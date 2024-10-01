file = open("data.txt","r")
total = 0

#data.txt contains a list of numbers, one per line
for line in file:
    total += int(line.strip())    # convert each line to an integer and add to total

#Prints the total sum while closing the file to realse memory
file.close()
print("The sum of numbers is :",total)