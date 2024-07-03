#7-3-24

class Course:
    def __init__ (self, code, name, semester, year, credits):
        self.code = code
        self.name = name
        self.semester = semester
        self.year = year
        self.credits = credits
    
    def display_course(self):
        print(self.code + ' ' + self.name)
        print(self.semester + ' ' + str(self.year) + ' ' + str(self.credits) + ' credit hours\n')
