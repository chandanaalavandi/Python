#write a prgm that only accepts positive numbers.
#you can raise an exception if user enters a negative number
def check_positive(number):
    if number < 0:
        raise ValueError("Negative numbers are not allowed!")
try:
    print(check_positive(5))
except ValueError as e:
    print(e)