class Contacts:

    def __init__(self, contact_id, contact_name, contact_number, email_address, home_address, creation_date):
        self.contact_id = contact_id
        self.contact_name = contact_name
        self.contact_number = contact_number
        self.email_address = email_address
        self.home_address = home_address
        self.creation_date = creation_date

    def get_contact_id(self):
        return self.contact_id

    def get_contact_name(self):
        return self.contact_name

    def get_contact_number(self):
        return self.contact_number

    def get_email_address(self):
        return self.email_address

    def get_home_address(self):
        return self.home_address

    def get_creation_date(self):
        return self.creation_date

    def __str__(self):
        return f"""
        =============================
        Contact ID: {self.contact_id}
        Contact Name: {self.contact_name}
        Contact Number: {self.contact_number}
        Email Address: {self.contact_number}
        Home Address: {self.home_address}
        Creation date: {self.creation_date}
        =============================
        """
