students = []


class Student:

    school_name = "Silverstream Primary"

    def __init__(self, name: object, student_id: object = 332) -> object:
        """

        :rtype: object
        """
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name