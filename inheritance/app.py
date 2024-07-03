from Course import Course
from MathCourse import MathCourse
from CSCourse import CSCourse

courses = [
    CSCourse('CS210','Computer Network Architecture', 'Fall', 2024, 3),
    CSCourse('CS360', 'Fundamentals of Data Science', 'Fall', 2024, 3),
    MathCourse('MTH120', 'Discrete Math', 'Fall', 2024, 3)
]

print('Here are your current enrollments:')
for course in courses:
    if(isinstance(course,CSCourse)):
        course.display_cs_course()
    if(isinstance(course,MathCourse)):
        course.display_math_course()
