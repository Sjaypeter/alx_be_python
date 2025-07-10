#This script calculates savings
#1. User input for financial details
Monthly_income = int(input("Enter your monthly income:$"))
Monthly_expenses = int(input("Enter your total monthly expenses:$"))
#2. Monthly savings 
Monthly_savings = Monthly_income - Monthly_expenses
#3. Project annual savings with an annual rate of 5%
Projected_Savings = (Monthly_savings * 12) + (Monthly_savings * 12 * 0.05)
print(f"Projected savings after one year is: ${Projected_Savings}")
