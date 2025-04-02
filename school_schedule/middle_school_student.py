from .student import Student

# add MiddleSchoolStudent here
class MiddleSchoolStudent(Student):
    def __init__(self, name, grade, classes,
        gets_transportation=False):

        super().__init__(name, grade, classes)
        self.gets_transportation = gets_transportation

    def summary(self):
        student_summary = super().summary()
        transpotation_message = self.display_transportation_message()
        return "\n".join((student_summary, transpotation_message))

    def display_transportation_message(self):
        has_message = (
            "does get" if self.gets_transportation else "does not get"
            )
        return f"{self.name} {has_message} transportation"
