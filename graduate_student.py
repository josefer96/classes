from student import Student

class Graduate_Student(Student):
    
    #initializar
    def __init__(self, first_name, last_name, grade, student_id=None, degree_program="Masters"):
        #super() calls a method in the parent calls.
        super().__init__(first_name, last_name, grade, student_id)
        self.degree_program = degree_program
        
    def print_student_data(self):
        super().print_studen_data()
        print(f"\tDegree programe: {self.degree_program}")