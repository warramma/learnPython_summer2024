#6-23-24
#create Student objects using Student class

from Student import Student

cs140_class = {
    'Harry Potter' : Student('Harry', 'Potter', 3.5, 'Defense Against the Dark Arts', 5, False),
    'Hermione Granger' : Student('Hermione', 'Granger', 4.0, 'Multiple majors - All', 5, False),
    'Ron Weasley' : Student('Ronald', 'Weasley', 3.0, 'Communications', 5, False),
    'Tom Riddle' : Student('Tom', 'Riddle', 4.0, 'Dark arts', 7, True)
}

for student in cs140_class:
    cs140_class[student].print()
