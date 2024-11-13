#Class is a blueprint of an object
class Student:
    #class level attribute. Shared by all instances of the class
    school_name = "Weber State University"
    all_students = [] # class attributes store all instances of the class
    
    #constructor initializer
    #attributes
    def __init__(self, first_name, last_name, grade, student_id=None):
        self.first = first_name
        self.last = last_name
        self.grade = grade
        self.email = first_name + last_name + '@weber.edu'
        self.student_id = self.format_student_id(Student_id)
        
        Student.all_students.append(self)
    #Class method is a method that belongs to the class rather than the instance
    
    
    @classmethod #python decorator
    def from_fullname(cls, full_name, grade, student_id):
            firstname, lastname = full_name.split() # "ose Fernandez" first Jose, second Fernandez
            return cls(firstname, lastname, grade, student_id)
            
            
    def print_student_data(self):
                print (f"student info \n,",
                       f"\tFirst Name:{self.first_name} \n",
                       f"\tLast name: {self.last_name} \n",
                       f"\tGrade: {self.grade}\n",
                       f"\tEmail: {self.email}\n",
                       f"\tSchool name:{Student.school_name}\n")
                       f"\tID: {self.student_id")
                
                def change_grade(self, new_grade_level):
                    self.grade = new_grade_level
                    
                    
                    def __str__(self):
                    #Magic method __str__ is a user-friend string representation of the object
#jay_pike is an instance of the student class
    return (f"Name:{"self.first_name} {self.last Name} Email: {self.email}"
                       f"School name:{Student.school_name}") ID: {self.student_id}
                       
    @staticmethod # does not have access to class level attributes or instance attributes
    def format_student_id(Student_id)
        #format 
        return f"WSU-{studen_id}" if Student_id else "no ID assigned"
    @classmethod
    def get_all_students(cls)
        # Class method to access the lsit of all students
        return cls.all_students
jay_pike = Student.from_fullname("Jay", "Pike", "Sophomore",3456) #Object of the student class
jane_doe = Student("Jane", "Doe", "Senior", 1234) #object of the student class
Waldo_Wildcat = Student("Wald", "Wildcat", "Senior")

# jay_pike.print_student_data()
# jane_doe.print_student_data()
# Waldo_Wildcat.print_student_data()

# jay_pike.change_grade("Junior")
# jane_doe.change_grade("Graduated")
# Waldo_Wildcat.change_grade("Freshman")

# jay_pike.print_student_data()
# jane_doe.print_student_data()
# Waldo_Wildcat.print_student_data()


# print("Printing out object")
# print(jay_pike)
# print(jane_doe)
# print(Waldo_Wildcat)
#Created the OOP Branch

all_students_in_class = Student.get_all_students()
for Student in all_students_in_class:
        Student.print_student_data()