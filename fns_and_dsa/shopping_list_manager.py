def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
def add_item():
    item_name = input("Enter the item to add: ")
    shopping_list.append(item_name)
def remove_item():
    item_name += input("Enter the item to remove: ")
    shopping_list.remove(item_name)
def view_item():
    print(shopping_list)
shopping_list = []
is_running = True
while is_running:
    display_menu()
    choice = (input("Enter your choice(1-4): "))
    if choice == "1":
        add_item()
    elif choice == "2":
        view_item()
    elif choice =="3":
        remove_item()
    elif choice =="4":
        is_running = False
        print("Goodbye")
    else:
        print("Invalid choice. Please try again!")

        
    