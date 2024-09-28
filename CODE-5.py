#1

x = 23      #Global Variable

def my_function():
    print(x)
    
my_function()   
print()


#2

x = 23      #Global Variable
y = 32
def my_function():
    print(x)
    
my_function()   
print(x,y)


#3

x = 23      #Global Variable
y = 32
def my_function():
    print(x)
    print(y)
    
my_function()   
print(x,y)




x = 43      #Global Variable
y = 52
def my_function():
    z = 4
    print(z, x, y)
    
my_function()   
print( x, y)

