print("Program started")


def show_menu():
    print("\n---Student Management System---")
    print("1. Add Student")
    print("2. Add Grade")
    print("3. Show Students")
    print("4. Exit")
    running = True
    while running:
        choice = input("Choose an option: ")

        if choice == "4":
            print("Thank you for using this program!")
            running = False
        else:
            print("Option selected:", choice)


show_menu()