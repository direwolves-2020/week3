from View import View
from models.Model import UserDAO

class Controller:

    def __init__(self):
        self.view = View()
        self.modeldao = UserDAO()
        self.validator = Validator()

    def register_new_user(self):
        user = self.view.get_new_user_details()

        if self.validator.is_entitled(user, "create_new"):
            self.modeldao.save_user(user)
        else:
            self.view.display_entitlement_error()

    def list_users(self):
        pass

    def update_user(self):
        pass
    

class Validator:

    def __init__(self):
        pass

    def is_entitled(self, user, action):
        """Checks whether user is entitled to perform action"""
        return False



controller = Controller()
controller.register_new_user()