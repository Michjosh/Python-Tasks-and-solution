
class Entry:
    def __init__(self, entry_id, entry_title, entry_body, entry_date):
        self.entry_id = entry_id
        self.entry_title = entry_title
        self.entry_body = entry_body
        self.entry_date = entry_date

    def get_entry_id(self):
        return self.entry_id

    def get_entry_title(self):
        return self.entry_title

    def get_entry_body(self):
        return self.entry_body

    def get_entry_date(self):
        return self.entry_date

    def __str__(self):
        return f"""
                =============================
                Entry Number: {self.entry_id}
                Entry Title: {self.entry_title}
                Entry Body: {self.entry_body}
                Entry Date: {self.entry_date}
                =============================
                """
