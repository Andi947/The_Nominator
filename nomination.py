# Defines the variables of a Nomination object and the requirements to create/initialise a Nomination object.
class Nomination(object):

# variables that will make up a Nomination object (currently global variables - accessible by other classes calling this class)
    userID_nominating = 0
    nomineeID = 0
    reason = ""

# Initialisation method for the Nomination object (when creating a Nomination object the variables userID, nomineeID and reason need to be passed)
    def __init__(self, userID, nomineeID, reason):
        self.userID_nominating = userID
        self.nomineeID = nomineeID
        self.reason = reason

# Various Getter methods to get access to the value stored in the local variables in a Nomination object (currently they are global and don't require these methods)
    def get_userID(self):
        return self.userID_nominating

    def get_nomineeID(self):
        return self.nomineeID

    def get_reason(self):
        return self.reason

# Various Setter methods to set the value of the local variables in the Nomination object (currently they are global and can be set without these methods)
    def set_userID(self, userID):
        self.userID_nominating = userID

    def set_nomineeID(self, nomineeID):
        self.nomineeID = nomineeID

    def set_reason(self, reason):
        self.reason = str(reason)
