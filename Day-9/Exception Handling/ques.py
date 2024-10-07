#write a python code 
try:
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))
    result = num1 / num2
    print(f"The result is: {result}")

except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numbers.")
finally:
    print("Program execution completed.")
