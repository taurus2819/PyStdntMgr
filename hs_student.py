from student import Student


class HighSchoolStudent(Student):

    school_name = "Silverstream High"

    def get_school_name(self):
        return self.school_name

    def get_name(self):
        return super().get_name_capitalize()