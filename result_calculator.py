from collections import defaultdict
import unicodedata

class CalculatorResult(object):

# Takes an object (list of users) and returns a list of nominee userID numbers
    def list_of_nomineeIDs(self, object):
        nomineeID_list = []
        for i in object:
            nominee = int(i.nomineeID)
            nomineeID_list.append(nominee)
        return nomineeID_list

# Takes an object(list of nominee userID numbers) and provides the total number
# of votes stored in the list
    def total_votes(self, object):
        count = int(len(object))
        return count

# Takes an object (list of nominee userID numbers) and counts the number of
# times that ID was chosen in the list and assigns the count to that
# nominee userID
    def nomination_per_nominee(self, object):
        counts = dict()
        for i in object:
            counts[i] = counts.get(i, 0) + 1
        return counts

# Takes the dictionary of no. of nominations per nominee and returns the userID
 # that got the largest number.
# In future, add logic to deal with equal votes
    def calculate_winning_nomineeID(self, object):
        maximum = max(object, key=object.get)
        return maximum

# Takes the dictionary of no. of nominations per nominee and returns the number
#  of votes associated with the winning UserID
    def no_of_votes(self, object):
        maximum = max(object, key=object.get)
        return object[maximum]

# Takes the users list and runs the nominee userID against the list to return
#  the username of the winning nominee
    def winnerID(self, object, int):
        winner = ""
        for i in object:
            user = i
            userID = user.get_userID()
            if userID == int:
                winner = user.get_username()
                return winner
            else:
                continue
