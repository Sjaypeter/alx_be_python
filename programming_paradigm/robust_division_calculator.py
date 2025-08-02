def safe_divide(numerator,denominator):
    try:
        numerator = float(input("Enter numerator: "))
        denominator = float(input("Enter denominator: "))
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")
    else:
        result = numerator/denominator
        print(f"The result of the division is {result}")
safe_divide(10,5)