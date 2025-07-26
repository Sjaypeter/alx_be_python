from datetime import datetime, timedelta
#1.Display current date and time
def display_current_datetime():
    current_date = datetime.now()
    print(f"{current_date}")
#2.Calculate future date
num_of_days = int(input("Enter the number of days to add to the current date: "))
def  calculate_future_date():
    tday = datetime.today()
    tdelta = timedelta(days= num_of_days)

    future_date = tday + tdelta
    print(future_date)
display_current_datetime()
calculate_future_date()

