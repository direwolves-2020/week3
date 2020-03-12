class UserDAO:

    def __init__(self):
        pass


    def save_user(self, user):
        """Takes in a user object and stores it to the db"""
        conn = sql()

        conn.commit()


class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password
    