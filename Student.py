#Class is a blueprint of an object
class Student:
    #constructor initializer
    #attributes
    def __init__(self, first_name, last_name, grade):
        self.first = first_name
        self.last = last_name
        self.grade = grade
        self.email = first_name + last_name + '@weber.edu'

    def print_student_data(self):
                print ("student info \n,",
                       "\tFirst Name:{self.first_name} \n",
                       "\tLast name: {self.last_name} \n",
                       "\tGrade: {self.grade}\n",
                       "\tEmail: {self.email}")
                
                def change_grade(self, new_grade_level):
                    self.grade = new_grade_level
                    
#jay_pike is an instance of the student class
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

#Created the OOP Branch