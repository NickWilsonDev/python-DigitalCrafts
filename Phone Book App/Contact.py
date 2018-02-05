#Contact.py

class Contact():
    def __init__(self, first, last, phone, email):
        self.first = first
        self.last  = last
        self.phone = phone
        self.email = email

    def to_string(self):
        return self.first + ' ' + self.last + ' ' +  self.phone + ' ' + self.email


