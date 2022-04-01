class Student:
    '''
    Methods:
    add_class()
    get_num_classes()
    summary()
    '''

    def __init__(self, name, year, courses, school = "Ada Developers Academy"):
        self.name = name
        self.year = year
        self.courses = courses
        self.school = school
    
    def add_class(self, course_name):
        if course_name:
            self.courses.append(course_name)
        return self.courses

    def get_num_classes(self):
        return len(self.courses)
    
    def summary(self):
        print(f"{self.name} is a {self.year} taking {self.get_num_classes()} classes this semester.")
    