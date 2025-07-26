#1.Define global varibles
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR= 9/5
#2.Conversion functions
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
        return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
#3. Prompt user for temperature(c/f)
try:
    temp = float(input("Enter the temperature to convert: "))
    Unit_of_Conversion = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
    if Unit_of_Conversion == "C":
        result = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {result}°F")
    elif Unit_of_Conversion == "F":
        result = convert_to_fahrenheit(temp)
        print(f"{temp}°F is {result}°C")
        
    else:
        print("Invalid unit of conversion")
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")        
