#1.Prompt user for task description
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time bound? (yes/no): ")
#2. Process case bsed on priority and time constraint
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print("Take some time out but get back to it cause its of high priority")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} is a medium priority task that requires attention today!")
        else:
            print(f"You still have some time to finsh {task}")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: {task} is of low  priority but still attend to it today!")
        else:
            print(f"Read a book {task} a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid response")