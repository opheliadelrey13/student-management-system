students = {}

def load_students():
    try:
        with open("students.txt", "r") as file:
            for line in file:
                name, surname, grade = line.strip().split(",")
                students[f"{name} {surname}"] = grade


    except FileNotFoundError:
        print("Student file not found.")
    except Exception as e:
        print("Error loading student file!\n ", f"{type(e)}: {e}")


def save_students():
    with open("students.txt","w") as file:
        for student,grade in students.items():
            name, surname = student.split(" ")
            file.write(f"{name},{surname},{grade}\n")



def add_student():
    try:
        name = input("Enter student name: ").upper()
        surname = input("Enter student surname: ").upper()
        grade = input("Enter student grade: ")
        students[f"{name} {surname}"] = grade
        save_students()

        print("Student added.")

    except:
        print("Something went wrong.")



def update_grade():
    name = input("Enter student name: ").upper()
    surname = input("Enter student surname: ").upper()
    full_name = f"{name} {surname}"
    if full_name not in students:
        print("Student not found.")
        return

    new_grade = input("Enter new grade: ")
    students[full_name] = new_grade
    save_students()
    print("Student updated.")


def show_students():
    if not students:
        print("No students found.")
        return
    for name,grade in students.items():
        print(f"{name} - Grade: {grade}")





def show_menu():
    print("\n---Student Management System---")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Show Students")
    print("4. Exit")
    running = True
    while running:
        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            update_grade()
        elif choice == "3":
            show_students()
        elif choice == "4":
            print("Thank you for using this program!")
            running = False
        else:
            print("invalid choice.")


print("Program started")
load_students()
show_menu()