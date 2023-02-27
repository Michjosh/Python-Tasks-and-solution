from seedProjects.E_Diary.Diary import Diary


class EDiary:
    # entry = input("Kindly enter your password and username to login\n")
    my_diary = Diary()

    # @staticmethod
    # def main():
    #     EDiary.login()

    @staticmethod
    def the_main_menu():
        main_menu = """
                      =========================
                      Welcome to Your Smart E-diary
                      1 -> Create New Entry
                      2 -> View Entry
                      3 -> View All entries
                      4 -> Delete Entry
                      5 -> Count Entries
                      6 -> Edit Entry
                      7 -> Exit
                      =========================
                """
        user_input = input(main_menu)
        if user_input == '1':
            EDiary.create_new_entry()
        elif user_input == '2':
            EDiary.view_entry()
        elif user_input == '3':
            EDiary.view_all_entry()
        elif user_input == '4':
            EDiary.delete_new_entry()
        elif user_input == '5':
            EDiary.count_entry()
        elif user_input == '6':
            EDiary.edit_entry()
        elif user_input == '7':
            EDiary.exit()
        else:
            EDiary.the_main_menu()

    @staticmethod
    def exit():
        print("Thank you for using our application")
        exit(1)

    @staticmethod
    def edit_entry():
        entry_number = int(input("Enter your entry number"))
        title = input("Enter New Title Of Entry")
        body = input("Enter New Body of diary")

        EDiary.my_diary.edit_entry(entry_number, title, body)
        EDiary.the_main_menu()

    @staticmethod
    def count_entry():
        print("Your Entries Are: ", end="")
        EDiary.my_diary.count_entries()
        EDiary.the_main_menu()

    @staticmethod
    def delete_new_entry():
        entry_number = int(input("Enter your entry number"))
        EDiary.my_diary.delete_entry(entry_number)
        EDiary.the_main_menu()

    @staticmethod
    def view_entry():
        entry_number = int(input("Enter your entry number"))
        EDiary.my_diary.view_entry(entry_number)
        EDiary.the_main_menu()

    @staticmethod
    def view_all_entry():
        EDiary.my_diary.view_all_entries()
        EDiary.the_main_menu()

    @staticmethod
    def create_new_entry():
        title = input("Enter Title Of Entry")
        body = input("Enter Body of Diary")

        EDiary.my_diary.create_entry(title, body)
        print("Entry Created Successfully")
        EDiary.the_main_menu()

    @staticmethod
    def login(self):
        print("Kindly enter your password and username to login")
        username_input = input("Enter username: ")
        password_input = input("Enter password: ")

        if username_input == self.username and password_input == self.password:
            print("Access Granted")
            self.the_main_menu()

        else:
            print("Incorrect Password or Username")


if __name__ == '__main__':
    EDiary.the_main_menu()


# def login():
#     user_name_input = input("Enter Username: ")
#     password_input = input("Enter Password: ")
#     try:
#         if my_diary["username"].lower() == user_name_input.lower() and my_diary[
#             "password"].lower() == password_input.lower():
#             print("Access granted.")
#             the_main_menu()
#         else:
#             raise Exception("Incorrect username or password.")
#     except Exception as e:
#         print(e)
#         print()
#         login()
