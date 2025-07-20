#1.Prompt user for task
task = input("Enter your task: ").lower()
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
#2.Pocess task based on priority
match priority:
    case "high":
            reminder = f"Reminder:{task} is a high priority task"
    case "medium":
            reminder = f"Reminder:{task} is a medium priority task"
    case "low":
            reminder = f"Reminder:{task} is a low priority task"
    case _:
        print("Invalid response. Please enter a task")
#3. Print reminder
if time_bound == "yes":
    reminder += "that requires immediate attention today!"
elif time_bound == "no":
    reminder += "Consider completing it when you have free time."
else:
    print("Invalid time response")
print(f"Reminder: {reminder}")
        
