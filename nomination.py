class Nomination(object):

    userID_nominating = ""
    nomineeID = ""
    reason = ""

    def __init__(self, userID, nomineeID, reason):
        self.userID_nominating = userID
        self.nomineeID = nomineeID
        self.reason = reason

    def get_userID(self):
        return self.userID_nominating

    def get_nomineeID(self):
        return self.nomineeID

    def get_reason(self):
        return self.reason

    def set_userID(self, userID):
        self.userID_nominating = userID

    def set_nomineeID(self, nomineeID):
        self.nomineeID = nomineeID

    def set_reason(self, reason):
        self.reason = str(reason)
