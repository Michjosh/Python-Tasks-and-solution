from datetime import datetime

from seedProjects.E_Diary.Entry import Entry


class Diary:
    def __init__(self):
        self.entries = []
        self.entry_number = 1

    def create_entry(self, entry_title, entry_body):
        entry = Entry(self.entry_number, entry_title, entry_body, datetime.now())
        self.entries.append(entry)
        self.entry_number += 1

    def view_entry(self, entry_id: int):
        for entry in self.entries:
            if entry.get_entry_id() == entry_id:
                print(f"ID: {entry.get_entry_id()}")
                print(f"Title: {entry.get_entry_title()}")
                print(f"Body: {entry.get_entry_body()}")
                print(f"Date: {entry.get_entry_date()}")
                return
        print("Entry not found")

    def view_all_entries(self):
        if len(self.entries) == 0:
            print("No entries to display")
        else:
            for entry in self.entries:
                print(entry)

    def edit_entry(self, entry_id, new_title, new_body):
        for entry in self.entries:
            if entry.get_entry_id() == entry_id:
                entry.entry_title = new_title
                entry.entry_body = new_body
                print("Entry has been successfully edited.")
                return
        print("Entry not found")

    def delete_entry(self, entry_id):
        for i, entry in enumerate(self.entries):
            if entry.get_entry_id() == entry_id:
                self.entries.pop(i)
                print("Entry has been successfully deleted.")
                return
        print("Entry not found")

    def count_entries(self):
        return print(len(self.entries))
