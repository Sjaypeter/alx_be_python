class safe_divide():
    
    def safe_divide(numerator, denominator):
        try:
            numerator = float(input("Enter the numerator: "))
            denominator = float(input("Enter the denominator: "))
        except  ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        except ValueError:
            print("Error: Please enter numeric values only.")
        else:
            result = numerator/denominator
            return result