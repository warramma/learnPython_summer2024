from Course import Course

class CSCourse(Course):
    def display_cs_course(self):
        self.display_course()
        print('There is a sale on CS textbooks from now until August 9! See the bookstore website for more details!\n')