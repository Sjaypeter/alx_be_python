def add_item():
    item_name = input("Enter the item: ")
    shopping_list.append(item_name)
def remove_item():
    item_name += input("Enter the name of the item")
    shopping_list.remove(item_name)
def view_item():
    print(shopping_list)
shopping_list = []
is_running = True
while is_running:
    print("----SHOPPING CART----")
    print("1.Add item")
    print("2.View item")
    print("3.Remove item")
    print("4.Exit")
    choice = (input("Enter your choice(1-4): "))
    if choice == "1":
        add_item()
    elif choice == "2":
        view_item()
    elif choice =="3":
        remove_item()
    elif choice =="4":
        is_running = False
        print("Thank you for shopping")
    else:
        print("Invalid choice")

        
    