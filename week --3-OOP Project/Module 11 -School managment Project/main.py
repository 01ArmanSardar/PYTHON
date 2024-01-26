""" from School import School,ClassRoom,Subject
from person import Student,Teacher
def main():
    school=School('ARun chandra ','maijdee')

    eight=ClassRoom('eight')
    school.add_classroom(eight)
    nine=ClassRoom('nine')
    school.add_classroom(nine)
    ten=ClassRoom('ten')
    school.add_classroom(ten)
    
#add students
    abul=Student('abul',eight)
    school.student_admission(abul)

    pabul=Student('pabul',eight)
    school.student_admission(pabul)

    cabul=Student('cabul',eight)
    school.student_admission(cabul)
#subject addd
    physics_teacher=Teacher('Shajahan Tapon Rana',physics)
    physics=Subject('physics',physics_teacher)
    eight.add_subject(physics)

    chemistry_teacher=Teacher('haradhon nagh sir',chemistry)
    chemistry=Subject('chemistry',chemistry_teacher)
    eight.add_subject(chemistry)

    Biology_teacher=Teacher('Azmol sir',Biology)
    Biology=Subject('Biology',Biology_teacher)
    eight.add_subject(Biology)

    print(school)
if __name__ =='__main__':
    main() 
     #module 11.5 projntoh korchi
    """

from School import School, ClassRoom, Subject
from person import Student, Teacher

def main():
    school = School('Adam Jee', 'U TT RA')

    eight = ClassRoom('eight')
    school.add_classroom(eight)
    nine = ClassRoom('nine')
    school.add_classroom(nine)
    ten = ClassRoom('ten')
    school.add_classroom(ten)

    # add students
    abul = Student('Abul Khan', eight)
    school.student_admission(abul)
    babul = Student('Babul Khan', eight)
    school.student_admission(babul)
    cabul = Student('Cabul Khan', eight)
    school.student_admission(cabul)

    # subjects
    physics_teacher = Teacher('Shahjahan Tapon Rana')
    physics = Subject('physics', physics_teacher)
    eight.add_subject(physics)

    chemistry_teacher = Teacher('Haradon Nag')
    chemistry = Subject('chemistry', chemistry_teacher)
    eight.add_subject(chemistry)
    
    biology_teacher = Teacher('Azmal Sir')
    biology = Subject('biology', biology_teacher)
    eight.add_subject(biology)

    eight.take_semester_final()


    print(school)

if __name__ == '__main__':
    main()