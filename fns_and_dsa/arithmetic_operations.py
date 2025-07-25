
def perform_operation(num1 :float, num2: float, operation: str):
    operation = operation.lower()
    match operation:
        case"add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                print("Cannot divide by zero")
                return num2
            else:
                return num1/num2
        case _:
            print("Error: Invalid operator")
print(perform_operation(num1= 10, num2= 5, operation= "divide"))
        
        
            