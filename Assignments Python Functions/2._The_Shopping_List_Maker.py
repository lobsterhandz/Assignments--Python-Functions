# Task 1: Function to add items to the shopping list
shopping_list = []

def add_item(item):
    shopping_list.append(item)
    print(f"{item} added to the shopping list.")

# Task 2: Function to remove items from the shopping list
def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from the shopping list.")
    else:
        print(f"{item} is not in the shopping list.")

# Task 3: Function to print the entire shopping list
def print_list():
    if not shopping_list:
        print("The shopping list is empty.")
    else:
        print("Shopping List:")
        for item in shopping_list:
            print(f"- {item}")

# Create w1hile loop to let the user continue adding, removing, and printing until they quit
while True:
    print("\nWelcome to the Shopping List Maker:")
    print("1. Add item")
    print("2. Remove item")
    print("3. Print list")
    print("4. Quit")
    
    choice = input("Enter your choice (1/2/3/4): ") 

    if choice == "1":
        item = input("Enter the item to add: ")
        add_item(item)
    
    elif choice == "2":
        item = input("Enter the item to remove: ")
        remove_item(item)

    elif choice == "3":
        print_list()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")

