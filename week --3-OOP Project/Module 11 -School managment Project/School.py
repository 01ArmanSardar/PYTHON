class School:
    def __init__(self,name,address) -> None:
        self.name=name
        self.address=address
        self.teachers={}
        #composition, school has student
        self.classrooms={}
    def add_classroom(self,classroom):
        self.classrooms[classroom.name]=classroom

    def add_teacher(self,subject,teacher):
        self.teachers[subject]=teacher

    def student_admission(self,student,classroom_name):
        if classroom_name in self.classrooms:
            self.classrooms[classroom_name].add_student(student)
        else:
            print(f'no classroom as named {classroom_name}')
    
    def __repr__(self) -> str:
        print ('---------all classrooms----------')
        for key,value in self.classrooms.items():
            print(key)

        return ''


class ClassRoom:
    def __init__(self,name) -> None:
        self.name=name
        #composition ,class has student
        self.students=[]
    def add_student(self,student):
        serial_id =f'{self.name}-{len(self.students)+1}'
        student=serial_id
        student.classroom=self.name
        self.students.append(student)
    def __str__(self) -> str:
        return f'{self.name}-{len(self.students)}'
    
    def get_top_studnets(self):
        pass