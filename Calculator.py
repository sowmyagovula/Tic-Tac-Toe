
class calculator:
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        return x / y
    
input1 = int(input("Enter a number: "))
input2 = int(input("Enter another number: "))

input3 = input(" 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n Enter an operation: ")

if input3 == "1":
    print(f" The Addition of {input1} and {input2} is {calculator.add(input1, input2)}")
elif input3 == "2":
    print(f" The Subtraction of {input1} and {input2} is {calculator.subtract(input1, input2)}")
elif input3 == "3":
    print(f" The Multiplication of {input1} and {input2} is {calculator.multiply(input1, input2)}")
elif input3 == "4":
    print(f" The Division of {input1} and {input2} is {calculator.divide(input1, input2)}")
else:
    raise ValueError(" Invalid Operation Selected!!! ")
