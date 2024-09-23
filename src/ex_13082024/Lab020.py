# Take a user inputs a,b and calculate the sum , multiplication, division , subtraction
num1 = int(input("Enter the num 1"))
num2 = int(input("Enter the num 2"))

#This will not work because data type is string
# We need to convert string -> int

print(type(num1))
print(type(num2))

print("Sum is", num1 + num2)
print("Multiplication is", num1 * num2)
print("Division is", num1 / num2) # Python is very smart Language - 3/2 -> 1.50
print("Subtraction is", num1 - num2)


