from nomination import *
import nomination
from data_storage import *
import data_storage

class NominationsData(object):

    list_nominations = DataStorage()
    nominationsList = []

    nomination1 = Nomination(1, 4, "She knows what she's doing")
    nomination2 = Nomination(2, 0, "He knows what he's doing")
    nomination3 = Nomination(3, 1, "She tries her best")
    nomination4 = Nomination(4, 2, "He loves what he does")
    nomination5 = Nomination(0, 3, "Runs the place")


    nominationsList.append(nomination1)
    nominationsList.append(nomination2)
    nominationsList.append(nomination3)
    nominationsList.append(nomination4)
    nominationsList.append(nomination5)

    def get_list(self):
        return self.nominationsList

    def get_nominationsList(self):
        return self.nominationsList

    # list_length = len(nominator_nominations)
    # for i in nominator_nominations:
    #     myNomination = i.get_reason()
    #     print myNomination

    # print nominator_nominations
