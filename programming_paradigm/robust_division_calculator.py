def safe_divide(numerator,denominator):
    try:
        numerator = input("Enter num: ")
        denominator = input("Enter denum: ")
        numerator = float(numerator)
        denominator = float(denominator)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")
    else:
        result = numerator/denominator
        print(f"The result of the division is {result}")
safe_divide(10,5)