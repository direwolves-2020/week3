from models.Model import User

class View:

    def __init__(self):
        pass

    def get_new_user_details(self):
        print("Logic to gather information about user registration")

        return  User('sample_username', 'sample_password')

    def display_entitlement_error(self):
        print("Sorry, not permitted")
