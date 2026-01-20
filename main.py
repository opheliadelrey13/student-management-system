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

def get_valid_name(context):
    while True:
        name = input(context).strip()
        if not name:
            print("Name is required.")
            continue
        if not name.isalpha():
            print("Must contain only letters.")
            continue

        return name.upper()
def get_valid_grade():
    while True:
        grade = input("Enter student grade (0-100): ")

        if not grade.isdigit():
            print("Grade must be a number.")
            continue
        grade = int(grade)
        if 0 <= grade <= 100:
            return str(grade)
        print("Grade must be between 0 and 100.")


def add_student():
    try:
        name = get_valid_name("Enter student name: ")
        surname = get_valid_name("Enter Student Surname: ")
        grade = get_valid_grade()
        full_name = f"{name} {surname}"
        if full_name in students:
            print("Student with that name already exists.")
            return

        students[full_name] = grade
        save_students()

        print("Student added.")

    except:
        print("Something went wrong.")



def update_grade():
    name = get_valid_name("Enter student name: ")
    surname = get_valid_name("Enter Student Surname: ")
    full_name = f"{name} {surname}"
    if full_name not in students:
        print("Student not found.")
        return

    new_grade = get_valid_grade()
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