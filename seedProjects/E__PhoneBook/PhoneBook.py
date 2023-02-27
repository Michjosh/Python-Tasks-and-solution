from datetime import datetime

from seedProjects.E__PhoneBook.Contacts import Contacts


class PhoneBook:
    def __init__(self):
        self.contacts = []
        self.contact_id = 1

    def create_contacts(self, contact_name, contact_number, email_address, home_address):
        contact = Contacts(self.contact_id, contact_name, contact_number, email_address, home_address, datetime.now())
        self.contacts.append(contact)
        self.contact_id += 1

    def count_contacts(self):
        return print(len(self.contacts))

    def edit_contacts(self, contact_id, new_contact_name, new_contact_number, new_email_address, new_home_address):
        for contact in self.contacts:
            if contact.get_contact_id() == contact_id:
                contact.contact_name = new_contact_name
                contact.contact_number = new_contact_number
                contact.email_address = new_email_address
                contact.home_address = new_home_address
                print("Entry has been successfully edited.")
                return
            print("Entry not found")

    def view_contact_by_id(self, contact_id: int):
        for contact in self.contacts:
            if contact.get_contact_id() == contact_id:
                print(contact)
                return
        print("Entry not found")

    def view_all_contacts(self):
        if len(self.contacts) == 0:
            print("No Contact to display")
        else:
            for contact in self.contacts:
                print(contact)

    def delete_contact(self, contact_id):
        for i, contact in enumerate(self.contacts):
            if contact.get_contact_id() == contact_id:
                self.contacts.pop(i)
                print("Contact has been successfully deleted.")
                return
        print("Contact not found")

    def search_contact_by_name(self, contact_name):
        for contact in self.contacts:
            if contact.get_contact_name() == contact_name:
                print(contact)
                return
            print("Contact not found")
