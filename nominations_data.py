from nomination import *

# Object that contains the static nomination data used in the program. Going
# forward, this will be where the Database logic will go where nominations can
# be added to or accessed from the  Database

class NominationsData(object):
    # empty list created
    nominationsList = []

    # Each static nomination is created as a Nomination Object
    nomination1 = Nomination(1, 4, "She knows what she's doing")
    nomination2 = Nomination(2, 0, "He knows what he's doing")
    nomination3 = Nomination(3, 1, "She tries her best")
    nomination4 = Nomination(4, 2, "He loves what he does")
    nomination5 = Nomination(0, 3, "Runs the place")

    # Each nomination is added to the list
    nominationsList.append(nomination1)
    nominationsList.append(nomination2)
    nominationsList.append(nomination3)
    nominationsList.append(nomination4)
    nominationsList.append(nomination5)

#a getter to get the list of nominations
    def get_list(self):
        return self.nominationsList
