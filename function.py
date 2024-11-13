from tabulate import tabulate
from classes import CollegeManagementSystem
from color import red, green, reset, blue
from datetime import datetime

cms = CollegeManagementSystem()

def add_teacher():
    name = input(f"{blue}[?] Enter teacher's name: {reset}")
    nickname = input(f"{blue}[?] Enter teacher's nickname: {reset}")
    phone_number = input(f"{blue}[?] Enter teacher's phone number: {reset}")
    cms.add_teacher(name, nickname, phone_number)
    print(f"{green}[+] Teacher added successfully.{reset}")

def add_student():
    name = input(f"{blue}[?] Enter student's name: {reset}")
    father_name = input(f"{blue}[?] Enter father's name: {reset}")
    mother_name = input(f"{blue}[?] Enter mother's name: {reset}")
    department = input(f"{blue}[?] Enter department: {reset}")
    shift = input(f"{blue}[?] Enter shift: {reset}")
    group = input(f"{blue}[?] Enter group: {reset}")
    class_roll = input(f"{blue}[?] Enter class roll: {reset}")
    registration = input(f"{blue}[?] Enter registration number: {reset}")
    session = input(f"{blue}[?] Enter session: {reset}")
    cms.add_student(name, father_name, mother_name, department, shift, group, class_roll, registration, session)
    print(f"{green}[+] Student added successfully.{reset}")

def add_attendance():
    date = input(f"{blue}[?] Enter date (YYYY-MM-DD): {reset}")
    class_roll = input(f"{blue}[?] Enter class roll: {reset}")
    status = input(f"{blue}[?] Enter attendance status (present/absent or p/a): {reset}").strip().lower()
    if status in ["present", "p"]:
        status = "present"
    elif status in ["absent", "a"]:
        status = "absent"
    else:
        print(f"{red}[-] Invalid input for attendance status. Please enter 'present', 'absent', 'p', or 'a'.{reset}")
        return
    
    cms.add_attendance(date, class_roll, status)
    print(f"{green}[+] Attendance added successfully.{reset}")

def view_teachers():
    teachers = cms.get_teachers()
    if teachers:
        print(f"\n{green}TEACHERS LIST:{reset}")
        headers = [f"{blue}{header.upper()}{reset}" for header in teachers[0].keys()]
        rows = [[f"{green}{value}{reset}" for value in teacher.values()] for teacher in teachers]
        print(tabulate(rows, headers, tablefmt="pretty"))
    else:
        print(f"{red}[-] NO TEACHERS FOUND.{reset}")

def view_students():
    students = cms.get_students()
    if students:
        print(f"\n{green}STUDENTS LIST:{reset}")
        headers = [f"{blue}{header.upper()}{reset}" for header in students[0].keys()]
        rows = [[f"{green}{value}{reset}" for value in student.values()] for student in students]
        print(tabulate(rows, headers, tablefmt="pretty"))
    else:
        print(f"{red}[-] NO STUDENTS FOUND.{reset}")

def view_attendance():
    date = input(f"{blue}Enter date to view attendance (YYYY-MM-DD): {reset}")
    attendance_records = cms.get_attendance(date)
    if attendance_records:
        print(f"\nAttendance for {date}:")
        headers = attendance_records[0].keys()
        rows = [record.values() for record in attendance_records]
        print(tabulate(rows, headers, tablefmt="pretty"))
    else:
        print(f"{red}[-] No attendance records found for {date}.{reset}")

def find_student_details():
    class_roll = input(f"{blue}[?] Enter the class roll number of the student: {reset}")
    student = cms.get_student_details(class_roll)
    if student:
        headers = [f"{red}{header.upper()}{reset}" for header in student.keys()]
        rows = [[f"{green}{value}{reset}" for value in student.values()]]
        print(f"\n{green}STUDENT DETAILS:{reset}")
        print(tabulate(rows, headers=headers, tablefmt="pretty"))
    else:
        print(f"{red}[-] Student not found.{reset}")

def find_teacher():
    name_or_nickname = input(f"{blue}[?] Enter teacher's name or nickname: {reset}")
    teachers = cms.find_teacher(name_or_nickname)
    if teachers:
        print(f"\n{green}FOUND TEACHERS:{reset}")
        headers = [f"{red}{header.upper()}{reset}" for header in teachers[0].keys()]
        rows = [[f"{green}{value}{reset}" for value in teacher.values()] for teacher in teachers]
        print(tabulate(rows, headers=headers, tablefmt="pretty"))
    else:
        print(f"{red}[-] No teachers found.{reset}")

def find_total_present():
    class_roll = input(f"{blue}[?] Enter the class roll number: {reset}")
    month = input(f"{blue}[?] Enter month (YYYY-MM): {reset}")
    present_count = cms.count_present_days(class_roll, month)
    print(f"{blue}[i] Total present days for roll number {class_roll} in {month}: {present_count}{reset}")

def edit_teacher():
    nickname = input(f"{blue}[?] Enter teacher's nickname to edit: {reset}")
    name = input(f"{blue}[?] Enter new name (leave blank to keep current): {reset}")
    phone_number = input(f"{blue}[?] Enter new phone number (leave blank to keep current): {reset}")
    cms.edit_teacher(nickname, name if name else None, phone_number if phone_number else None)
    print(f"{green}[+] Teacher updated successfully.{reset}")

def edit_student():
    class_roll = input(f"{blue}[?] Enter class roll number to edit: {reset}")
    name = input(f"{blue}[?] Enter new name (leave blank to keep current): {reset}")
    father_name = input(f"{blue}[?] Enter new father's name (leave blank to keep current): {reset}")
    mother_name = input(f"{blue}[?] Enter new mother's name (leave blank to keep current): {reset}")
    department = input(f"{blue}[?] Enter new department (leave blank to keep current): {reset}")
    shift = input(f"{blue}[?] Enter new shift (leave blank to keep current): {reset}")
    group = input(f"{blue}[?] Enter new group (leave blank to keep current): {reset}")
    registration = input(f"{blue}[?] Enter new registration number (leave blank to keep current): {reset}")
    session = input(f"{blue}[?] Enter new session (leave blank to keep current): {reset}")

    cms.edit_student(
        class_roll,
        name if name else None,
        father_name if father_name else None,
        mother_name if mother_name else None,
        department if department else None,
        shift if shift else None,
        group if group else None,
        registration if registration else None,
        session if session else None
    )
    print(f"{green}[+] Student updated successfully.{reset}")

def delete_teacher():
    nickname = input(f"{blue}[?] Enter teacher's nickname to delete: {reset}")
    cms.delete_teacher(nickname)
    print(f"{green}[+] Teacher deleted successfully.{reset}")

def delete_student():
    class_roll = input(f"{blue}[?] Enter class roll number to delete: {reset}")
    cms.delete_student(class_roll)
    print(f"{green}[+] Student deleted successfully.{reset}")