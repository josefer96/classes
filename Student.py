#Class is a blueprint of an object
class Student:
    #class level attribute. Shared by all instances of the class
    school_name = "Weber State University"
    all_students = [] # class attribute stor all instances of the class
   
    #constructor initializer
    #attributes
    def __init__(self, first_name, last_name, grade, student_id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade
        self.email = first_name + last_name + '@weber.edu'
        self.student_id = self.format_student_id(student_id)
       
        Student.all_students.append(self)
   
    #class method is a method that belongs to the class rather than the instance
   
    @classmethod #python decorator
    def from_fullname(cls, full_name, grade, student_id):
        firstname, lastname = full_name.split() # "Scott Hadzik" first Scott second Hadzik
        return cls(firstname, lastname, grade, student_id)
   
    def print_student_data(self):
        print (f"Student info \n",
               f"\tFirst Name: {self.first_name} \n",
               f"\tLast Name: {self.last_name} \n",
               f"\tGrade: {self.grade}\n",
               f"\tEmail: {self.email}\n",
               f"\tSchool Name: {Student.school_name}\n",
               f"\tID: {self.student_id}")
   
    def change_grade(self, new_grade_level):
        self.grade = new_grade_level
       
    def __str__(self):
        # Magic method __str__ is a user-friendly string representation of the object
        return (f"Name: {self.first_name} {self.last_name} Email: {self.email}"
               f"School Name: {Student.school_name} ID: {self.student_id}")
   
   
    @staticmethod #does not have access to class level attributes or instance attributes
    def format_student_id(student_id):
        #format the student id so that it starts with WSU
        return f"WSU-{student_id}" if student_id else "No ID assigned"
   
    @classmethod
    def get_all_students(cls):
        # Class method to access the list of all students
        return cls.all_students
       
#jay_pike is an instance of the student class
jay_pike = Student.from_fullname("Jay Pike", "Sophomore", 3456) #Object of the student class
jane_doe = Student("Jane", "Doe", "Senior", 1234) #object of the student class
waldo_wildcat = Student("Waldo", "Wildcat", "Senior")

# jay_pike.print_student_data()
# jane_doe.print_student_data()
# waldo_wildcat.print_student_data()

# jay_pike.change_grade("Junior")
# jane_doe.change_grade("Graduated")
# waldo_wildcat.change_grade("Freshman")

# jay_pike.print_student_data()
# jane_doe.print_student_data()
# waldo_wildcat.print_student_data()

# print("Printing out object")
# print(jay_pike)
# print(jane_doe)
# print(waldo_wildcat)
# We created the OOP branch

all_students_in_class = Student.get_all_students()
for student in all_students_in_class:
    student.print_student_data()