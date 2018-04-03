students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student.get("name").title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def start():
    choice = True

    while choice:
        student_name = input("Enter student name: ")
        student_id = input("Enter student ID: ")

        def add_student(name, student_id=332):
            student = {"name": name, "student_id": student_id}
            students.append(student)

        add_student(student_name, student_id)
        decision = input("Do you want to continue : Enter y or n \n")
        if decision == "y":
            choice = True
        elif decision == "n":
            choice = False
            break


    print_students_titlecase()

start()