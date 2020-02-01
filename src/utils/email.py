import sys


class SendEmail():
     
    def __init__(self, name, email):
        self.name = name
        self.email = email

        if not self.validate_data():
            print(Common.ERROR_EMAIL_MESSAGE)
            sys.exit()

    def validate_data(self):
        return self.name is not None and self.email is not None

    @staticmethod
    def validate_list(list_data):
        return len(list_data) == 4