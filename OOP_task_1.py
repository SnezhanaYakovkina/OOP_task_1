# Функция для расчёта средней оценки
def  average_grade():
    sum_ex = 0  # создадим счётчик, в котором будем наращивать суммы всех значений
    for student in Student:
        # print(student)
        sum_ex += student['exam']  # по итогу работы цикла будет сумма всех значений за экзамен
    return round(sum_ex / len(Student), 2)


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Cравнение между собой студентов по средней оценке за домашние задания.
    def _lt_(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self.grades < other.grades


    # Переопределяем метод _str_
    def _str_(self):
        res_1 = f'Имя:{self.name}'
        res_2 = f'Фамилия:{self.surname}'
        res_3 = f'Средняя оценка за лекции:{average_grade}
        res_4 = f'Курсы в процессе изучения:{self.courses_in_progress}
        res_5 = f'Завершенные курсы: {self.finished_courses}
        return res_1, res_2, res_3, res_4, res_5

    some_student = Student('Ruoy', 'Eman', 9.9)
    some_student.courses_in_progress += ['Python', 'Git']
    some_student.finished_courses = ['Введение в программирование']

    # print(some_student)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    self.grades = {}

    # Cравнение между собой лекторов по средней оценке за лекции.
    def _lt_(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return self.average_grade < other.average_grade

    # Переопределяем метод _str_
    def _str_(self):
        res_1 = f'Имя:{self.name}'
        res_2 = f'Фамилия:{self.surname}'
        res_3 = f'Средняя оценка за лекции:{average_grade}'
        return res_1, res_2, res_3

    some_lecturer = Lecturer('Some', 'Buddy', 9.9)

    # print(some_lecturer)


class Reviewer (Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Переопределяем метод _str_
        def _str_(self):
            res_1 = f'Имя:{self.name}'
            res_2 = f'Фамилия:{self.surname}'
            res_3 = f'Средняя оценка за лекции:{average_grade}
            return res_1, res_2, res_3

        some_reviewer = Reviewer('Some', 'Buddy')

        # print(some_reviewer)


# задание №4

students_list = [
    {"name": "Василий", "surname": "Теркин", "gender": "м", "grade": [8, 8, 9]},
    {"name": "Мария", "surname": "Павлова", "gender": "ж", "grade": [7, 8, 9, 7]},
    {"name": "Ирина", "surname": "Андреева", "gender": "ж", "grade": [10, 9, 8, 10, 10]},
    {"name": "Татьяна", "surname": "Сидорова", "gender": "ж", "grade": [7, 8, 8, 9, 8]},
    {"name": "Иван", "surname": "Васильев", "gender": "м", "grade": [9, 8, 9, 6, 9]},
    {"name": "Роман", "surname": "Золотарев", "gender": "м", "grade": [8, 9, 9, 6, 9]}
]

lecturers_list = [
    {"name": "Пётр", "surname": "Сергеев", "lecturer_grades": [8, 8, 9, 10, 9, 8]},
    {"name": "Анна", "surname": "Антонова", "lecturer_grades": [7, 8, 9, 7, 8, 10]},
    {"name": "Ульяна", "surname": "Семёнова", "lecturer_grades": [10, 9, 8, 10, 10, 10]},
    {"name": "Кристина", "surname": "Шпак", "lecturer_grades": [7, 8, 8, 9, 8, 9]},
    {"name": "Антон", "surname": "Петров", "lecturer_grades": [9, 8, 9, 6, 9, 7],
    {"name": "Евгений", "surname": "Иванченко", "lecturer_grades": [8, 9, 9, 6, 9, 9]}
]

# Функция, которая будет считать среднюю оценку за домашние задания у всех студентов:
def get_hw_grade(students_list,courses_in_progress):
  sum_ex = 0  # создадим счётчик, в котором будем наращивать суммы всех значений
  for student in Students:
    # print(student)
    sum_hw += student['hw']  # по итогу работы цикла будет сумма всех значений за домашние задания
  return round(sum_hw / len(students), 2)

# print(get_hw_grade(students_list,courses_in_progress))

# Функция, которая будет считать среднюю оценку за лекции всех лекторов:
def get_lecture_grade(lecturers_list,courses_attached):
  sum_ex = 0  # создадим счётчик, в котором будем наращивать суммы всех значений
  for lecturer in Lecturer:
    # print(lecturer)
    sum_lecture += lecturer['lecture']  # по итогу работы цикла будет сумма всех значений за экзамен
  return round(sum_lecture / len(lecturer), 2)

# print(get_lecture_grade(lecturers_list,courses_attached)