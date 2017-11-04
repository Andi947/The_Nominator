# Defines the variables of a User object and the requirements to create/initialise a User object.
class User(object):

# variables that will make up a User object (currently global variables - accessible by other classes calling this class)
    userID = 0
    username = ""
    user_email = ""
    user_password = ""

# Initialisation method for the User object (when creating a User object the variables userID, username, email and password need to be passed)
    def __init__(self, userID, username, email, password):
        self.userID = userID
        self.username = username
        self.user_email = email
        self.user_password = password

# Various Getter methods to get access to the value of the local variables in User object (currently they are global and don't require these methods)
    def get_username(self):
        return self.username

    def get_user_email(self):
        return self.user_email

    def get_user_password(self):
        return self.user_password

    def get_userID(self):
        return self.userID

# Various Setter methods to set the values of the local variables in the User object (currently they are global and can be set without these methods)
    def set_username(self, username):
        self.username = str(username)

    def set_user_email(self, email):
        self.user_email = str(email)

    def set_user_password(self, password):
        self.user_password = str(password)
