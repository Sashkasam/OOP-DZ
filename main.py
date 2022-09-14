
from re import A


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course,grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grade_hw(self):
        result = sum(*self.grades.values()) / len(*self.grades.values())
        return result

    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {self._average_grade_hw()}\n'
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
            f'Завершенные курсы: {", ".join(self.finished_courses)}')
        return res

    def __lt__(self,other):
        if not isinstance(other,Student):
            print('Not a Student!')
            return
        return self._average_grade_hw() < other._average_grade_hw()
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
     
    
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res
    
    

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.grades = {}

    def _average_rating(self):
        result = round(sum(*self.grades.values()) / len(*self.grades.values()),1)
        return result
    
    def __str__(self):
      res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_rating()}'
      return res  
        
    def __lt__(self,other):
        if not isinstance(other,Lecturer):
            print('Not a Lecturer!')
            return
        return self._average_rating() < other._average_rating()

# Создаем студентов и определяем для них изучаемые и завершенные курсы
first_student = Student('Polina', 'Samoilova', 'female')
first_student.courses_in_progress += ['Python','Java']
first_student.finished_courses += ['Введение в программирование']

second_student = Student('Alexsander', 'Samoilov', 'male')
second_student.courses_in_progress += ['Python','Java']
second_student.finished_courses += ['Введение в программирование']

third_student = Student('Ksenia', 'Samoilova', 'female')
third_student.courses_in_progress += ['Python','Java']
third_student.finished_courses += ['Введение в программирование']

# Создаем лекторов и закрепляем за ними курсы
first_lecturer = Lecturer('Pavel', 'Ivanov')
first_lecturer.courses_attached += ['Python']

second_lecturer = Lecturer('Anna', 'Gorodilova')
second_lecturer.courses_attached += ['Java']

third_lecturer = Lecturer('Alex', 'Petrov')
third_lecturer.courses_attached += ['Python']

# Создаем ревьюеров и закрепляем за ними курсы
first_reviewer = Reviewer('Ivan', 'Ivanov')
first_reviewer.courses_attached += ['Python']

second_reviewer = Reviewer('Nikolai', 'Smirnov')
second_reviewer.courses_attached += ['Java']

# Выставляем студентами оценки лекторам за лекции
first_student.rate_lecturer(first_lecturer, 'Python', 10)
first_student.rate_lecturer(first_lecturer, 'Python', 9)
first_student.rate_lecturer(second_lecturer, 'Java', 9)
first_student.rate_lecturer(second_lecturer, 'Java', 8)
first_student.rate_lecturer(third_lecturer, 'Python', 8)
first_student.rate_lecturer(third_lecturer, 'Python', 10)

second_student.rate_lecturer(first_lecturer, 'Python', 9)
second_student.rate_lecturer(first_lecturer, 'Python', 9)
second_student.rate_lecturer(second_lecturer, 'Java', 10)
second_student.rate_lecturer(second_lecturer, 'Java', 9)
second_student.rate_lecturer(third_lecturer, 'Python', 9)
second_student.rate_lecturer(third_lecturer, 'Python', 7)

third_student.rate_lecturer(first_lecturer, 'Python',8)
third_student.rate_lecturer(first_lecturer, 'Python',9)
third_student.rate_lecturer(second_lecturer, 'Java',9)
third_student.rate_lecturer(second_lecturer, 'Java',10)
third_student.rate_lecturer(third_lecturer, 'Python',7)
third_student.rate_lecturer(third_lecturer, 'Python',8)

# Выставляем  ревьюерами оценки студентам за домашние задания

first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(first_student, 'Python', 9)
first_reviewer.rate_hw(second_student, 'Java', 9)
first_reviewer.rate_hw(second_student, 'Java', 7)
first_reviewer.rate_hw(third_student, 'Python', 9)
first_reviewer.rate_hw(third_student, 'Python', 10)

second_reviewer.rate_hw(first_student, 'Python', 9)
second_reviewer.rate_hw(first_student, 'Python', 7)
second_reviewer.rate_hw(second_student, 'Java', 8)
second_reviewer.rate_hw(second_student, 'Java', 9)
second_reviewer.rate_hw(third_student, 'Python', 8)
second_reviewer.rate_hw(third_student, 'Python', 7)


students_list = [first_student,second_student,third_student]
lectures_list = [first_lecturer,second_lecturer,third_lecturer]

students_grades_list = []
def average_students(students_list,course):
    for student in students_list:
        for key,value in student.grades.items():
            if key is course:
                students_grades_list.extend(value)
    result = round(sum(students_grades_list) / len(students_grades_list),1)
    print(f'Средний бал по всем студентам курса {course}: {result}')

lectures_grades_list = []
def average_lectures(lectures_list,course):
    for lecturer in lectures_list:
        for key,value in lecturer.grades.items():
            if key is course:
                lectures_grades_list.extend(value)
    result = round(sum(lectures_grades_list) / len(lectures_grades_list),1)
    print(f'Средний бал по всем лекторам курса {course}: {result}')




print(f'Список всех студентов: \n\n{first_student}\n\n{second_student}\n\n{third_student}')
print()
print(f'Список всех лекторов: \n\n{first_lecturer}\n\n{second_lecturer}\n\n{third_lecturer}')
print()
print(f'Список ревьюеров: \n\n{first_reviewer}\n\n{second_reviewer}')
print()
print(first_student < second_student)
print(second_student < third_student)
print(first_lecturer < third_lecturer)
print(second_lecturer > first_lecturer)
print()
average_students(students_list,'Python')
average_students(students_list,'Java')
print()
average_lectures(lectures_list, 'Python')
average_lectures(lectures_list, 'Java')