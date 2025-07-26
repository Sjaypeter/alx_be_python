import datetime
#1.Display current date and time
def display_current_datetime():
    current_date = datetime.datetime.now()
    print(f"{current_date}")
#2.Calculate future date
num_of_days = int(input("Enter the number of days to add to the current date: "))
def  calculate_future_date():
    tday = datetime.date.today()
    tdelta = datetime.timedelta(days= num_of_days)

    future_date = tday + tdelta
    print(future_date)
calculate_future_date()

