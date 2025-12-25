from datetime import date
from typing import List, Optional

class University:
    def __init__(self):
        self.faculties: List['Faculty'] = []

    def add_faculty(self, faculty: 'Faculty'):
        self.faculties.append(faculty)

class Faculty:
    def __init__(self, name: str):
        self.name = name
        self.dean: Optional['Dean'] = None
        self.institutes: List['Institute'] = []

    def set_dean(self, dean: 'Dean'):
        self.dean = dean

    def add_institute(self, institute: 'Institute'):
        self.institutes.append(institute)

class Institute:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address

class Employee:
    counter = 0

    def __init__(self, ss_no: int, name: str, email: str):
        self.ss_no = ss_no
        self.name = name
        self.email = email
        Employee.counter += 1

class AdministrativeEmployee(Employee):
    def __init__(self, ss_no: int, name: str, email: str):
        super().__init__(ss_no, name, email)

class ResearchEmployee(Employee):
    def __init__(self, ss_no: int, name: str, email: str, field_of_study: str, institute: Institute):
        super().__init__(ss_no, name, email)
        self.field_of_study = field_of_study
        self.institute = institute
        self.projects: List['Participation'] = []
        self.courses: List['Course'] = []

    def add_project(self, participation: 'Participation'):
        self.projects.append(participation)

    def add_course(self, course: 'Course'):
        self.courses.append(course)

class Lecturer(ResearchEmployee):
    def __init__(self, ss_no: int, name: str, email: str, field_of_study: str, institute: Institute):
        super().__init__(ss_no, name, email, field_of_study, institute)

class Dean(AdministrativeEmployee):
    def __init__(self, ss_no: int, name: str, email: str):
        super().__init__(ss_no, name, email)

class Project:
    def __init__(self, name: str, start_date: date, end_date: date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date

class Participation:
    def __init__(self, hours: int, employee: ResearchEmployee, project: Project):
        self.hours = hours
        self.employee = employee
        self.project = project

class Course:
    def __init__(self, course_id: int, name: str, weekly_duration: float):
        self.course_id = course_id
        self.name = name
        self.weekly_duration = weekly_duration


if __name__ == "__main__":
    uni = University()

    faculty = Faculty("ФКН")
    uni.add_faculty(faculty)

    institute = Institute("Кафедра ИТВЦД", "ул. Университетская, 1")
    faculty.add_institute(institute)

    dean = Dean(12345, "Крыловецкий А.А.", "dean@mail.ru")
    faculty.set_dean(dean)

    researcher = ResearchEmployee(67890, "Дедов П.Д.", "dedov@mail.tu", "IT", institute)
    lecturer = Lecturer(13579, "Соколов В.А.", "sokolov@mail.ru", "IT", institute)

    project = Project("Проект бебра", date(2024, 1, 1), date(2024, 12, 31))
    participation = Participation(100, researcher, project)
    researcher.add_project(participation)

    course = Course(101, "МИСПИС", 4.0)
    lecturer.add_course(course)

    print(f"Университет содержит факультет: {uni.faculties[0].name}")
    print(f"Декан факультета: {faculty.dean.name}")
    print(f"Научный сотрудник: {researcher.name}, область: {researcher.field_of_study}")
    print(f"Преподаватель ведёт курс: {lecturer.courses[0].name}")
    print(f"Общее число сотрудников: {Employee.counter}")