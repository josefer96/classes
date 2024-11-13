#Class is a blueprint of an object
class Student:
    #class level attribute. Shared by all instances of the class
    school_name = "Weber State University"
    
    #constructor initializer
    #attributes
    def __init__(self, first_name, last_name, grade):
        self.first = first_name
        self.last = last_name
        self.grade = grade
        self.email = first_name + last_name + '@weber.edu'

    def print_student_data(self):
                print (f"student info \n,",
                       f"\tFirst Name:{self.first_name} \n",
                       f"\tLast name: {self.last_name} \n",
                       f"\tGrade: {self.grade}\n",
                       f"\tEmail: {self.email}\n",
                       f"\tSchool name:{Student.school_name}")
                
                def change_grade(self, new_grade_level):
                    self.grade = new_grade_level
                    
                    def __str__(self):
                    #Magic method __str__ is a user-friend string representation of the object
#jay_pike is an instance of the student class
    return (f"Name:{"self.first_name} {self.last Name} Email: {self.email}"
                       f"\tSchool name:{Student.school_name}")
jay_pike = Student("Jay", "Pike", "Sophomore") #Object of the student class
jane_doe = Student("Jane", "Doe", "Senior") #object of the student class
Waldo_Wildcat = Student("Wald", "Wildcat", "Senior")

jay_pike.print_student_data()
jane_doe.print_student_data()
Waldo_Wildcat.print_student_data()

jay_pike.change_grade("Junior")
jane_doe.change_grade("Graduated")
Waldo_Wildcat.change_grade("Freshman")

jay_pike.print_student_data()
jane_doe.print_student_data()
Waldo_Wildcat.print_student_data()


print("Printing out object")
print(jay_pike)
print(jane_doe)
print(Waldo_Wildcat)
#Created the OOP Branch