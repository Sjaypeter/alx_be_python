#This calculator will prompt the user to enter two numbers and select an operation
#Prompt user for numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
#Operation type
Operation = input("Choose the operation (+, -, *, /): ")
#Calculation
match Operation :
    case "+":
       result = num1 + num2
    case "-":
        result = num1-num2
    case "*":
        result = num1*num2
    case "/":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            result = num1 / num2
    case _:
        print("Invalid choice")
        
print(f"The result is {result}")
