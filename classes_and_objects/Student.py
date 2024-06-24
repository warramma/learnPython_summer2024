#6-23-24
#create a Student class that keeps track of the Student's current GPA, major(s), year in school, age, first and last name, and whether or not they are on academic probation
#then, use this class to create Student objects and print students

class Student:
    
    def __init__(self, first_name, last_name, gpa, major, year, probation): 
        self.first_name = first_name
        self.last_name = last_name
        self.gpa = gpa
        self.major = major
        self.year = year
        self.probation = probation
    def print(self):
        if(self.probation == True):
            print('Full name: ' + self.first_name + ' ' + self.last_name)
            print('This student is currently on academic probation. All records are locked and require proper authorization...\n\n')
        else:
            print('Full name: ' + self.first_name + ' ' + self.last_name)
            print('Major: ' + self.major)
            print('Year: ' + str(self.year))
            print('GPA: ' + str(self.gpa) + '\n\n')
            