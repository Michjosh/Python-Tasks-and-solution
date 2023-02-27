import sys

from seedProjects.E__PhoneBook.PhoneBook import PhoneBook


def exit_app():
    print("Thank you for using our phonebook")
    sys.exit(1)


class phone_book:
    my_contact = PhoneBook()

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
        Welcome to Your Smart E-PhoneBook
        1 -> Create New Contact
        2 -> Search Contact by ID
        3 -> Search Contact by Name
        4 -> View All Contact
        5 -> Delete Contact
        6 -> Count Contact
        7 -> Edit Contact
        8 -> Exit
    ===================================
         """
        user_input = input(main_menu)
        if user_input == '1':
            self.create_new_contact()
        elif user_input == '2':
            self.view_contact_by_id()
        elif user_input == '3':
            self.search_contact_by_name()
        elif user_input == '4':
            self.view_all_contacts()
        elif user_input == '5':
            self.delete_contact()
        elif user_input == '6':
            self.count_contact()
        elif user_input == '7':
            self.edit_contact()
        elif user_input == '8':
            exit_app()
        else:
            self.the_main_menu()

    def edit_contact(self):
        try:
            contact_id = int(input("Enter contact ID number: "))
            name = input("Enter new contact name: ")
            number = input("Enter new contact number: ")
            email = input("Enter new email: ")
            home = input("Enter new home address: ")
            self.my_contact.edit_contacts(contact_id, name, number, email, home)
            raise ValueError

        except ValueError as e:
            print(e)
            self.the_main_menu()

    def count_contact(self):
        try:
            print("Your Contact(s) are: ", end='')
            self.my_contact.count_contacts()
            self.the_main_menu()
            raise ValueError
        except ValueError as e:
            print(e)
            self.the_main_menu()

    def delete_contact(self):
        try:
            contact_id = int(input("Enter contact ID number: "))
            self.my_contact.delete_contact(contact_id)
            self.the_main_menu()
            raise ValueError
        except ValueError as e:
            print(e)
            self.the_main_menu()

    def view_all_contacts(self):
        try:
            self.my_contact.view_all_contacts()
            self.the_main_menu()
            raise ValueError
        except ValueError as e:
            print(e)
            self.the_main_menu()

    def search_contact_by_name(self):
        try:
            contact_name = input("Enter contact name: ")
            self.my_contact.search_contact_by_name(contact_name)
            self.the_main_menu()
            raise ValueError
        except ValueError as e:
            print(e)
            self.the_main_menu()

    def view_contact_by_id(self):
        try:
            contact_id = int(input("Enter contact ID number: "))
            self.my_contact.view_contact_by_id(contact_id)
            self.the_main_menu()
            raise ValueError
        except ValueError as e:
            print(e)
            self.the_main_menu()

    def create_new_contact(self):
        try:
            name = input("Enter contact name: ")
            number = input("Enter contact number: ")
            email = input("Enter contact email address: ")
            home = input("Enter contact home address: ")
            self.my_contact.create_contacts(name, number, email, home)
            print("Entry created successfully: ")
            self.the_main_menu()
            raise ValueError
        except ValueError as e:
            print(e)
            self.the_main_menu()


if __name__ == "__main__":
    pb = phone_book()
    pb.login()
