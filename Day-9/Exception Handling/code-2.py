#finally-clause

try:
    file = open("example.txt","r")
    #some kind of code to raise an exception

except FileNotFoundError:
    print("File not found!")

finally:
    file.close()
    print("File closed.")