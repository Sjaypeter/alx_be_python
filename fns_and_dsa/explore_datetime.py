from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()    
    print(current_date)

Num_of_days = int(input("Enter the number of days to add to current date: "))
def calculate_future_date():
    date = datetime.now()
    future_date = date + timedelta(days=Num_of_days)
    print(f"{future_date}")
calculate_future_date()
display_current_datetime()

