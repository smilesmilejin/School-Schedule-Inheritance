from .student import Student
# This one works too
# from school_schedule.student import Student
class HighSchoolStudent(Student):
    def __init__(self, name, grade, classes,
        has_parking_privileges=False, clubs=None):

        super().__init__(name, grade, classes)
        self.has_parking_privileges = has_parking_privileges
        self.clubs = clubs if clubs is not None else []

    def join_club(self, club_name):
        self.clubs.append(club_name)

    def summary(self):
        student_summary = super().summary()
        parking_message = self.display_parking_message()
        club_message = self.display_clubs()

        return "\n".join((student_summary, parking_message, club_message))

    def display_parking_message(self):
        has_message = "has" if self.has_parking_privileges else "doesn't have"
        return f"{self.name} {has_message} parking privileges"

    def display_clubs(self):
        club_str = ", ".join(self.clubs)

        if club_str:
            return f"{self.name} is a member of: {club_str}"
    
        return f"{self.name} hasn't joined a club yet."