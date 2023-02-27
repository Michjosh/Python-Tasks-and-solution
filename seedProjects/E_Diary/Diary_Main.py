import sys

from seedProjects.E_Diary.Diary import Diary


def exit_app():
    print("Thank you for using our application")
    sys.exit(1)


class E_diary:
    my_diary = Diary()

    def __init__(self):
        self.username = "mike"
        self.password = "1234"

    def login(self):
        try:
            print("Kindly enter your password and username to login")
            username_input = input("Enter username: ")
            password_input = input("Enter password: ")
            if username_input != self.username or password_input != self.password:
                raise ValueError("Incorrect Password or Username")
        except ValueError as e:
            print(e)
            print()
            self.login()
        else:
            print("Access Granted")
            self.the_main_menu()

    def the_main_menu(self):
        main_menu = """
    ===================================
        Welcome to Your Smart E-diary
        1 -> Create New Entry
        2 -> View Entry
        3 -> View All entries
        4 -> Delete Entry
        5 -> Count Entries
        6 -> Edit Entry
        7 -> Exit
    ===================================
         """
        user_input = input(main_menu)
        if user_input == '1':
            self.create_new_entry()
        elif user_input == '2':
            self.view_entry()
        elif user_input == '3':
            self.view_all_entry()
        elif user_input == '4':
            self.delete_new_entry()
        elif user_input == '5':
            self.count_entry()
        elif user_input == '6':
            self.edit_entry()
        elif user_input == '7':
            exit_app()
        else:
            self.the_main_menu()

    def edit_entry(self):
        try:
            entry_number = int(input("Enter your entry number: "))
            title = input("Enter Title Of Entry: ")
            body = input("Enter body of diary: ")
            self.my_diary.edit_entry(entry_number, title, body)
            raise ValueError
        except ValueError as e:
            print(e)
            self.the_main_menu()

    def count_entry(self):
        try:
            print("Your Entry(ies) is(are): ", end='')
            self.my_diary.count_entries()
            self.the_main_menu()
            raise ValueError
        except ValueError as e:
            print(e)
            self.the_main_menu()

    def delete_new_entry(self):
        try:
            entry_number = int(input("Enter your entry number: "))
            self.my_diary.delete_entry(entry_number)
            self.the_main_menu()
            raise ValueError
        except ValueError as e:
            print(e)
            self.the_main_menu()

    def view_all_entry(self):
        try:
            self.my_diary.view_all_entries()
            self.the_main_menu()
            raise ValueError
        except ValueError as e:
            print(e)
            self.the_main_menu()

    def view_entry(self):
        try:
            entry_number = int(input("Enter your entry number: "))
            self.my_diary.view_entry(entry_number)
            self.the_main_menu()
            raise ValueError
        except ValueError as e:
            print(e)
            self.the_main_menu()

    def create_new_entry(self):
        try:
            title = input("Enter Title Of Entry: ")
            body = input("Enter body of diary: ")
            E_diary.my_diary.create_entry(title, body)
            print("Entry created successfully: ")
            self.the_main_menu()
            raise ValueError
        except ValueError as e:
            print(e)
            self.the_main_menu()


if __name__ == "__main__":
    ed = E_diary()
    ed.login()
