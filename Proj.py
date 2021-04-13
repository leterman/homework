
class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []
        self.teachers = {}
        self.grade = []
        #self.avgg = (sum(self.grade) / len(self.grade))
    def avg(self,grade1, grade2, grade3):
        x = (grade1 + grade2 + grade3)/3
        self.average = format(x,'.1f')

    def strip(self, coarse):
        x = coarse.strip('')
        self.stripp = x

    def strip2(self,coarse,coarse2):
        x = coarse.strip('')
        y = coarse2.strip('')
        self.strip2 = x+","+y

    def rate_hw(self, reviewer, course, grade):
        if isinstance(reviewer, Reviewers) and course in self.finished_courses and course in reviewer.courses_attached:
            if course in reviewer.gradess:
                reviewer.gradess[course] += [grade]
            else:
                reviewer.gradess[course] = [grade]
        else:
            return 'Ошибка'

    def avgrade(self,student,course):
        student = self.name = name, self.surname
        course = self.finished_courses
        if isinstance(student, Student) and course in self.finished_courses:
            print(self.average)

    def ave_homework(self, student_lits, course_name):

        #list = [best_student, student1]
        #course_name = 'Введение в програмирование'

        a = []
        for obj in student_lits:
            if course_name in obj.stripp:
                a.append(obj.grade)
        suum = [sum(x) for x in zip(*a)]
        count = 0
        for z in a:
            count += len(z)

        suum1 = sum(suum)/ count
        print(course_name, suum1, sep=' ')




    # Задание 3.2
    def __gt__(self, other):
        if self.average > other.average:
            return f'Лучший студент: {self.name} с рейтингом: {self.average}'
        else:
            return f'Лучший студент: {other.name} с рейтингом: {other.average}'

    # Задание 3.1
    def __str__(self):
        return 'Имя:{self.name} \nФамилия:{self.surname} \nСредняя оценка за Д/З:{self.average}\nКурсы' \
               ' в процессе изучения:{self.strip2}\nЗавершённые курсы:{self.stripp}'.format(self=self)
#Задание 4.1
class Student2:
    def count_mark(self, students, mark):
        print("name".ljust(15), "group".ljust(8), "marks".ljust(20))
        for student in students:
            marks_list = student['marks']
            number_list = marks_list
            from numpy import mean
            avg = mean(number_list)
            result = (sum(marks_list) / len(marks_list))
            if result >= zero:
                print(student["name"].ljust(15), student["group"].ljust(8), round(avg, 2))




class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.gradess = {}
        self.average = {}

    # Задание 3.1
    def __str__(self):
        return 'Имя:{self.name} \nФамилия:{self.surname}'.format(self=self)
#Задание 2
class Reviewers(Mentor):


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

        print(str(grade))

    # Задание 3.1
    def __str__(self):
        return 'Имя:{self.name} \nФамилия:{self.surname}'.format(self=self)

#Задание 2
class Lecturer(Mentor):

    def avg(self,grade1, grade2, grade3):
        x = (grade1 + grade2 + grade3)/3
        self.average = format(x,'.1f')

    # Задание 3.2
    def __gt__(self, other):
        if self.average > other.average:
            return f'Лучший лектор: {self.name} с рейтингом: {other.average}'
        else:
            return f'Лучший лектор: {other.name} с рейтингом: {other.average}'

    # Задание 3.1
    def __str__(self):
        return 'Имя:{self.name} \nФамилия:{self.surname} \nСредняя оценка за лекции:{self.average}'.format(self=self)

#Задание 4.2
class Lecturer1:
    def count_mark(self, lecturers, mark):
        print("name".ljust(15), "group".ljust(8), "marks".ljust(20))
        for lecturer in lecturers:
            marks_list = lecturer['marks']
            number_list = marks_list
            from numpy import mean
            avg = mean(number_list)
            result = (sum(marks_list) / len(marks_list))
            if result >= zero:
                print(lecturer["name"].ljust(15), lecturer["group"].ljust(8), round(avg, 2))

#Задание 3.1
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.strip2('Python', 'Git')
best_student.strip('Введение в програмирование')
best_student.courses_in_progress += ['Python']
best_student.teachers['Python'] = [10]
best_student.avg(4, 9, 6)
best_student.grade = [1, 9, 6]
print(best_student)

#Задание 3.1
cool_mentor = Reviewers('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
print(cool_mentor)

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

best_student.rate_hw(cool_mentor, 'Python', 10)

#Задание 3.1
cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.avg(10, 9, 10)
print(cool_lecturer)
bad_lecturer = Lecturer('Some', 'Buddy')
bad_lecturer.avg(10, 9, 10)

#Задание 3.2
print(cool_lecturer > bad_lecturer)

student1 = Student('Plom', 'Render', 'your_gender')
student1.strip2('Python', 'Git')
student1.strip('Введение в програмирование')
student1.teachers['Python'] = [10]
student1.avg(10, 9, 10)
student1.grade = [10, 5, 6]
#Задание 3.2
print(student1 > best_student)

print(type(best_student))
student_list = [best_student, student1]
course_name = ['Введение в програмирование']


list = [best_student, student1]
course_name1 = 'Введение в програмирование'
student1.ave_homework(list, course_name1)

#Задача 4.1
groupmates = [
  {
    "name": "StudentOne",
    "group": "Python",
    "marks": [4, 3, 5, 5, 4]
  },
  {
    "name": "StudenTwo",
    "group": "Python",
    "marks": [3, 2, 3, 4, 3]
  },
  {
    "name": "StudentThree",
    "group": "Python",
    "marks": [3, 5, 4, 3, 5]
  },
  {
    "name": "StudentFour",
    "group": "Python",
    "marks": [5, 5, 5, 4, 5]
  },
  {
    "name": "StudentFive",
    "group": "Python",
    "marks": [5, 5, 5, 5, 5]
  }
]
#Задание 4.2
lecturers = [
  {
    "name": "Lector1",
    "group": "Python",
    "marks": [4, 3, 5, 5, 4]
  },
  {
    "name": "Lector2",
    "group": "Python",
    "marks": [3, 2, 3, 4, 3]
  },
  {
    "name": "Lector3",
    "group": "Python",
    "marks": [3, 5, 4, 3, 5]
  },
  {
    "name": "Lector4",
    "group": "Python",
    "marks": [5, 5, 5, 4, 5]
  },
  {
    "name": "Lector5",
    "group": "Python",
    "marks": [5, 5, 5, 5, 5]
  }
]


zero = 0

mate = Student2()
mate.count_mark(groupmates,zero)
lector = Lecturer1()
lector.count_mark(lecturers,zero)

