import json
import os
from typing import List, Dict
from datetime import datetime

ASSETS_DIR = "assets"
TEACHERS_FILE = os.path.join(ASSETS_DIR, "teachers.json")
STUDENTS_FILE = os.path.join(ASSETS_DIR, "students.json")
ATTENDANCE_FILE = os.path.join(ASSETS_DIR, "attendance.json")

if not os.path.exists(ASSETS_DIR):
    os.makedirs(ASSETS_DIR)

def load_data(filename: str):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(filename: str, data):
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))
        
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

class Teacher:
    def __init__(self, name, nickname, phone_number):
        self.name = name
        self.nickname = nickname
        self.phone_number = phone_number

    def to_dict(self):
        return {
            "name": self.name,
            "nickname": self.nickname,
            "phone_number": self.phone_number
        }

class Student:
    def __init__(self, name, father_name, mother_name, department, shift, group, class_roll, registration, session):
        self.name = name
        self.father_name = father_name
        self.mother_name = mother_name
        self.department = department
        self.shift = shift
        self.group = group
        self.class_roll = class_roll
        self.registration = registration
        self.session = session

    def to_dict(self):
        return {
            "name": self.name,
            "father_name": self.father_name,
            "mother_name": self.mother_name,
            "department": self.department,
            "shift": self.shift,
            "group": self.group,
            "class_roll": self.class_roll,
            "registration": self.registration,
            "session": self.session
        }

class Attendance:
    def __init__(self, date, class_roll, status):
        self.date = date
        self.class_roll = class_roll
        self.status = status

    def to_dict(self):
        return {
            "date": self.date,
            "class_roll": self.class_roll,
            "status": self.status
        }

class CollegeManagementSystem:
    def __init__(self):
        self.teachers = load_data(TEACHERS_FILE)
        self.students = load_data(STUDENTS_FILE)
        self.attendance = load_data(ATTENDANCE_FILE)

    def add_teacher(self, name, nickname, phone_number):
        teacher = Teacher(name, nickname, phone_number)
        self.teachers.append(teacher.to_dict())
        save_data(TEACHERS_FILE, self.teachers)

    def add_student(self, name, father_name, mother_name, department, shift, group, class_roll, registration, session):
        if any(student['class_roll'] == class_roll for student in self.students):
            print(f"Student with roll number {class_roll} already exists.")
            return

        student = Student(name, father_name, mother_name, department, shift, group, class_roll, registration, session)
        self.students.append(student.to_dict())
        save_data(STUDENTS_FILE, self.students)
        print(f"Student {name} added successfully.")

    def add_attendance(self, date, class_roll, status):
        if not any(student['class_roll'] == class_roll for student in self.students):
            print(f"Student with roll number {class_roll} does not exist.")
            return

        if any(record['date'] == date and record['class_roll'] == class_roll for record in self.attendance):
            print(f"Attendance for roll number {class_roll} on {date} already exists.")
            return

        attendance_record = Attendance(date, class_roll, status)
        self.attendance.append(attendance_record.to_dict())
        save_data(ATTENDANCE_FILE, self.attendance)
        print(f"Attendance for roll number {class_roll} on {date} added successfully.")

    def edit_teacher(self, nickname, name=None, phone_number=None):
        for teacher in self.teachers:
            if teacher['nickname'] == nickname:
                if name:
                    teacher['name'] = name
                if phone_number:
                    teacher['phone_number'] = phone_number
                save_data(TEACHERS_FILE, self.teachers)
                print(f"Teacher {nickname} updated successfully.")
                return
        print(f"Teacher with nickname {nickname} not found.")

    def edit_student(self, class_roll, name=None, father_name=None, mother_name=None, department=None, shift=None, group=None, registration=None, session=None):
        for student in self.students:
            if student['class_roll'] == class_roll:
                if name:
                    student['name'] = name
                if father_name:
                    student['father_name'] = father_name
                if mother_name:
                    student['mother_name'] = mother_name
                if department:
                    student['department'] = department
                if shift:
                    student['shift'] = shift
                if group:
                    student['group'] = group
                if registration:
                    student['registration'] = registration
                if session:
                    student['session'] = session
                save_data(STUDENTS_FILE, self.students)
                print(f"Student {class_roll} updated successfully.")
                return
        print(f"Student with roll number {class_roll} not found.")

    def delete_teacher(self, nickname):
        self.teachers = [teacher for teacher in self.teachers if teacher['nickname'] != nickname]
        save_data(TEACHERS_FILE, self.teachers)
        print(f"Teacher {nickname} deleted successfully.")

    def delete_student(self, class_roll):
        self.students = [student for student in self.students if student['class_roll'] != class_roll]
        save_data(STUDENTS_FILE, self.students)
        print(f"Student with roll number {class_roll} deleted successfully.")

    def get_attendance_summary(self, class_roll: str, month: str) -> List[Dict]:
        return [record for record in self.attendance if record['class_roll'] == class_roll and record['date'].startswith(month)]

    def get_student_details(self, class_roll: str) -> Dict:
        for student in self.students:
            if student['class_roll'] == class_roll:
                return student
        return None

    def find_teacher(self, name_or_nickname):
        found_teachers = [
            teacher for teacher in self.teachers
            if teacher['name'].lower() == name_or_nickname.lower() or 
               teacher['nickname'].lower() == name_or_nickname.lower()
        ]
        return found_teachers

    def count_present_days(self, class_roll: str, month: str) -> int:
        present_count = 0
        for record in self.attendance:
            record_date = datetime.strptime(record['date'], "%Y-%m-%d")
            if record['class_roll'] == class_roll and record_date.strftime("%Y-%m") == month and record['status'] == "present":
                present_count += 1
        return present_count

    def get_teachers(self):
        return self.teachers

    def get_students(self):
        return self.students

    def get_attendance(self, date):
        return [record for record in self.attendance if record['date'] == date]