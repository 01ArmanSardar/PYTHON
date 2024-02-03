class Student:
    def __init__(self,name,current_class,id):
        self.name=name
        self.id=id
        self.current_class=current_class
    def __repr__(self):
        return f'student with name :{self.name},class{self.current_class},id: {self.id}'
        
class Teacher:
    def __init__(self,name,subject,id):
        self.name=name
        self.subject=subject
        self.id=id
    def __repr__(self):
        return f'teacher name is {self.name} subject {self.subject} teacher id is {self.id}'

class School:
    def __init__(self,name):
        self.name=name
        self.teachers=[]
        self.students=[]
    def add_teacher(self,name,subject):
        id=len(self.teachers)+101# teacher dher id gulah 101 er por tekhe suru kortechi
        teacher=Teacher(name,subject,id) #teacher aktah variable nie tr vitor Teacher class keh call koreh name subject id passed kore dilam,poreh teacher variable takhe jeh instance attributes teachers list vanailam tr vitor append koreh dibho
        self.teachers.append(teacher)
    def enroll (self,name,fee):
        if fee<6500:
            print('not enough money')
        else:
            id=len(self.students)+1
            student=Student(name,'C',id)
            self.students.append(student)
            print( f'{name} is enrolled with id : {id} ,extra money {fee-6500}')
    def __repr__(self):
        print('welcome to',self.name)
        print('\n..........OUR Teachers.........\n')
        for teacher in self.teachers:
            print(teacher)
        print('\n........OUR Students........\n')
        for student in self.students:
            print(student)
        return '\nAll Done for Now'

        
              
# arman=Student('arman sardar',9,12)
# print(arman)
# rahat=Teacher('rahat sir','data strcuture',32)
# print(rahat)
phitron=School('Phitron')
phitron.enroll('arman',5300)
phitron.enroll('rakib',7000)

phitron.add_teacher('rahat sir','data structure')
phitron.add_teacher('farhan sir','data_base')
print(phitron)