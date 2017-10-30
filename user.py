class User(object):

    userID = 0
    username = ""
    user_email = ""
    user_password = ""

    def __init__(self, userID, username, email, password):
        self.userID = userID
        self.username = username
        self.user_email = email
        self.user_password = password

    def get_username(self):
        return self.username

    def get_user_email(self):
        return self.user_email

    def get_user_password(self):
        return self.user_password

    def get_userID(self):
        return self.userID

    def set_username(self, username):
        self.username = str(username)

    def set_user_email(self, email):
        self.user_email = str(email)

    def set_user_password(self, password):
        self.user_password = str(password)

    # def set_userID(self):
    #     self.userID =
