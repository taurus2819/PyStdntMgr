students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student.get("name").title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("could not open file")


def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            # add_student(student)
            print(student)
        f.close()
    except Exception:
        print("Could not open files")


def add_student(name, student_id=332):
        student = {"name": name, "student_id": student_id}
        students.append(student)


def start():
    choice = True

    while choice:
        student_name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        add_student(student_name, student_id)
        save_file(student_name)
        decision = input("Do you want to continue : Enter y or n \n")
        if decision == "y":
            choice = True
        elif decision == "n":
            choice = False
            break


def print_student_list():
    read_file()
    print_students_titlecase()


start()
print_student_list()
