from nomination import *
import nomination
from data_storage import *
import data_storage

class NominationsData(object):

    list_nominations = DataStorage()
    nominator_nominations = []

    nomination1 = Nomination(1, 4, "She knows what she's doing")
    nomination2 = Nomination(2, 1, "He knows what he's doing")
    nomination3 = Nomination(3, 2, "She tries her best")
    nomination4 = Nomination(4, 1, "He loves what he does")


    nominator_nominations = list_nominations.add_to_list(nomination1)
    nominator_nominations = list_nominations.add_to_list(nomination2)
    nominator_nominations = list_nominations.add_to_list(nomination3)
    nominator_nominations = list_nominations.add_to_list(nomination4)

    def add_to_list(self, object):
        self.nominator_nominations.append(object)
        return self.nominator_nominations

    def get_nominator_nominations(self):
        return self.nominator_nominations

    # list_length = len(nominator_nominations)
    # for i in nominator_nominations:
    #     myNomination = i.get_reason()
    #     print myNomination

    # print nominator_nominations
