#8.1

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
     
#8.2 


try:
    number = int(input("Enter a number: "))
    print(f"You entered the number: {number}")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")     


#8.3 

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter integers only.")
finally:
    print("Execution of the try-except block is complete.")    