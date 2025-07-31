class safe_divide():
    
    def safe_divide(numerator, denominator):
        try:
            numerator = input("Enter the numerator: ")
            denominator = input("Enter the denominator: ")
        except  ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        except ValueError:
            print("Error: Please enter numeric values only.")
        else:
            result = numerator/denominator
            return result