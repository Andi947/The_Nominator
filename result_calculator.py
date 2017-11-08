from collections import defaultdict
import unicodedata

class CalculatorResult(object):

    def list_of_nomineeIDs(self, object):
        nomineeID_list = []
        for i in object:
            nominee = i.nomineeID
            nominee = int(nominee)
            nomineeID_list.append(nominee)
        return nomineeID_list

    def total_votes(self, object):
        count = 0
        for i in object:
            count += 1
        return count

    def calculate_nominee_nominations(self, object):
        counts = dict()
        for i in object:
            counts[i] = counts.get(i, 0) + 1
        return counts

    def calculate_winning_nomineeID(self, object):
        maximum = max(object, key=object.get)
        return maximum

    def no_of_votes(self, object):
        maximum = max(object, key=object.get)
        return object[maximum]

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
