import os
import time
from time import sleep
from banner import *
from function import *
from color import white, blue, green, red, reset

def main_menu():
    show_banner()
    while True:
        print(f"{blue}[1]{white} Add Teacher")
        print(f"{blue}[2]{white} Add Student")
        print(f"{blue}[3]{white} Add Attendance")
        print(f"{blue}[4]{white} View Teachers")
        print(f"{blue}[5]{white} View Students")
        print(f"{blue}[6]{white} View Attendance")
        print(f"{blue}[7]{white} Find Student Details")
        print(f"{blue}[8]{white} Find Teacher Details")
        print(f"{blue}[9]{white} Count Total Present Days")
        print(f"{blue}[10]{white} Edit Teacher")
        print(f"{blue}[11]{white} Edit Student")
        print(f"{blue}[12]{white} Delete Teacher")
        print(f"{blue}[13]{white} Delete Student")
        print(f"{blue}[14]{white} Exit{reset}")

        try:
            choice = int(input(f"{blue}[?] Enter your choice: {white}"))
        except ValueError:
            print(f"{red}[-] Invalid input. Please enter a number between 1 and 14.{reset}")
            time.sleep(1)
            show_banner()
            continue
        except KeyboardInterrupt:
            print("\nExiting program.")
            break
        
        if choice == 1:
            show_banner ()
            add_teacher()
        elif choice == 2:
            show_banner ()
            add_student()
        elif choice == 3:
            show_banner ()
            add_attendance()
        elif choice == 4:
            show_banner ()
            view_teachers()
        elif choice == 5:
            show_banner ()
            view_students()
        elif choice == 6:
            show_banner ()
            view_attendance()
        elif choice == 7:
            show_banner ()
            find_student_details()
        elif choice == 8:
            show_banner ()
            find_teacher()
        elif choice == 9:
            show_banner ()
            find_total_present()
        elif choice == 10:
            show_banner ()
            edit_teacher()
        elif choice == 11:
            show_banner ()
            edit_student()
        elif choice == 12:
            show_banner ()
            delete_teacher()
        elif choice == 13:
            show_banner ()
            delete_student()
        elif choice == 14:
            break
        else:
            print(f"{red}[-] Invalid choice, please try again.{reset}")
            time.sleep(3)
            show_banner()
            continue
        
        user_choice = input(f"{blue}Do you want to return to the main menu? (yes/no): {white}").strip().lower()
        if user_choice not in ['yes', 'y']:
            break
        else:
            show_banner()

if __name__ == "__main__":
    main_menu()