def safe_divide(numerator, denominator):
    try:
        numerator = input("Enter numerator: ")
        denominator = input("Enter denominator: ")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only")
    else:
        return numerator/denominator