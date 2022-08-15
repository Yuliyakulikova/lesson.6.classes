class Student:
    student_list = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.student_list.append(self)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def all_grades(self):
        # функция возвращения всех оценок
        sum_grades = []
        for value_item in self.grades.values():
            for new_list in value_item:
                sum_grades += [new_list]

        return sum_grades

    def average(self):
        # функция подсчета среднего арифметического числа
        average_grade = sum(Student.all_grades(self)) / len(Student.all_grades(self))
        return round(average_grade, 1)

    def __lt__(self, other):
        # функция сравнения студентов по средней оценки за домашнее задание
        if self.average() >= other.average():
            return f"{self.name} {self.surname} средняя оценка больше, равно {self.average()}"
        else:
            return f"{self.name} {self.surname} средняя оценка меньше, равно {self.average()}"

    def __str__(self):
        try:
            print(
                f"Имя: {self.name}\nФамилия:{self.surname}\nСредняя оценка за домашние задания: {Student.average(self)}"
                f"\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}")
        except ZeroDivisionError:
            print("нет курсов")

    def lecturer_grades(self, lecturer, course, grade):
        # функция добавления лекторам оценок
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lecturer_list = []

    def __init__(self, name, surname):
        Lecturer.lecturer_list.append(self)
        self.grades = {}
        super().__init__(name, surname)

    def all_grades(self):
        # функция возвращения всех оценок
        sum_grades = []
        for value_item in self.grades.values():
            for new_list in value_item:
                sum_grades += [new_list]

        return sum_grades

    def average(self):
        # функция подсчета среднего арифметического числа
        average_grade = sum(Lecturer.all_grades(self)) / len(Lecturer.all_grades(self))
        return round(average_grade, 1)

    def __lt__(self, other):
        if self.average() >= other.average():
            return f"{self.name} {self.surname} средняя оценка больше, равно {self.average()}"
        else:
            return f"{self.name} {self.surname} средняя оценка меньше, равно {self.average()}"

    def __str__(self):
        try:
            print(f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {Lecturer.average(self)}")
        except ZeroDivisionError:
            print("нет лекций")

    def show_grades(self):
        # просмотр всех оценок у лекторов
        for key_course, value_grades in self.grades.items():
            print(f"Курс: {key_course} Оценка: {value_grades}")


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        print(f"Имя: {self.name}\nФамилия: {self.surname}")

    def rate_hw(self, student, course, grade):
        # функция добавления студентам оценок
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def courses_average_students(student_list, course):
    # подсчет средней оценки за домашние задания по всем студентам в рамках конкретного курса
    # в качестве аргументов принимаем список студентов и название курса

    for student in student_list:
        for k, v in student.grades.items():
            if course == k:
                sum_average = sum(v) / len(v)
                print(f"Студент: {student.name} {student.surname}\nКурс: {k}\n"
                      f"Cредняя оценка за домашние задания: {round(sum_average, 1)}\n")


def courses_average_lecturer(lecturer_list, course):
    # подсчет средней оценки за лекции всех лекторов в рамках конкретного курса
    # в качестве аргументов принимаем список лекторов и название курса
    for lecturer in lecturer_list:
        for k, v in lecturer.grades.items():
            if course == k:
                sum_average = sum(v) / len(v)
                print(f"Лектор: {lecturer.name} {lecturer.surname}\nКурс: {k}\n"
                      f"Cредняя оценка за курс: {round(sum_average, 1)}\n")


# студенты
vasya_student = Student('Vasya', 'Pupkin', 'man')
masha_student = Student('Masha', 'Zinina', 'girl')
olga_student = Student('Olga', 'Gorgeeva', 'girl')
# курсы студентов в прогрессе
vasya_student.courses_in_progress += ['Python']
vasya_student.finished_courses += ['Git']
masha_student.courses_in_progress += ['Python']
masha_student.courses_in_progress += ['Git']
olga_student.courses_in_progress += ['C++']
olga_student.courses_in_progress += ['Git']
# ******
ilya_reviewer = Reviewer('Ilya', 'Dnisov')
vitaly_reviewer = Reviewer('Vitaly', 'Glazov')
ilya_reviewer.courses_attached += ['Python']
vitaly_reviewer.courses_attached += ['Git']
vitaly_reviewer.courses_attached += ['C++']
# ******
ilya_reviewer.rate_hw(vasya_student, 'Python', 0)
ilya_reviewer.rate_hw(vasya_student, 'Python', 9)
ilya_reviewer.rate_hw(vasya_student, 'Python', 6)
ilya_reviewer.rate_hw(masha_student, 'Python', 10)
ilya_reviewer.rate_hw(masha_student, 'Python', 10)
ilya_reviewer.rate_hw(masha_student, 'Python', 10)
vitaly_reviewer.rate_hw(masha_student, 'Git', 9)
vitaly_reviewer.rate_hw(masha_student, 'Git', 9)
vitaly_reviewer.rate_hw(masha_student, 'Git', 9)
vitaly_reviewer.rate_hw(olga_student, 'Git', 7)
vitaly_reviewer.rate_hw(olga_student, 'Git', 7)
vitaly_reviewer.rate_hw(olga_student, 'Git', 7)
vitaly_reviewer.rate_hw(olga_student, 'C++', 9)
vitaly_reviewer.rate_hw(olga_student, 'C++', 9)
vitaly_reviewer.rate_hw(olga_student, 'C++', 9)
vasya_student.__str__()
# olga_student.comparison_student(vasya_student)
# лектора
alex_lecturer = Lecturer('Alex', 'Eratov')
igor_lecturer = Lecturer('Igor', 'Kyzin')
anton_lecturer = Lecturer('Anton', 'Orlov')
# выставление оценок лекторам
vasya_student.lecturer_grades(alex_lecturer, 'Python', 10)
vasya_student.lecturer_grades(alex_lecturer, 'Python', 10)
vasya_student.lecturer_grades(alex_lecturer, 'Python', 10)
masha_student.lecturer_grades(alex_lecturer, 'Python', 10)
masha_student.lecturer_grades(alex_lecturer, 'Python', 10)
masha_student.lecturer_grades(alex_lecturer, 'Python', 10)
masha_student.lecturer_grades(igor_lecturer, 'Git', 8)
masha_student.lecturer_grades(igor_lecturer, 'Git', 5)
masha_student.lecturer_grades(igor_lecturer, 'Git', 6)
olga_student.lecturer_grades(igor_lecturer, 'Git', 7)
olga_student.lecturer_grades(igor_lecturer, 'Git', 7)
olga_student.lecturer_grades(igor_lecturer, 'Git', 7)
olga_student.lecturer_grades(alex_lecturer, 'Git', 9)
olga_student.lecturer_grades(alex_lecturer, 'Git', 9)
olga_student.lecturer_grades(alex_lecturer, 'Git', 9)
olga_student.lecturer_grades(anton_lecturer, 'C++', 10)
olga_student.lecturer_grades(anton_lecturer, 'C++', 10)
olga_student.lecturer_grades(anton_lecturer, 'C++', 10)
# __str()__
ilya_reviewer.__str__()
alex_lecturer.__str__()
vasya_student.__str__()
# подсчет средней оценки за домашние задания
print("")
courses_average_students(Student.student_list, 'Git')
courses_average_lecturer(Lecturer.lecturer_list, 'Git')
# сравнение студентов и лекторов
print(igor_lecturer > alex_lecturer)
print(vasya_student < olga_student)