from user import *
import user
from data_storage import *
import data_storage

class UsersData(object):

    dict_users = DataStorage()
    nominator_users = {}
    listData = []

    admin = User(0, "admin","andi.goldsworthy@gmail.com", "password")
    nick = User(1, "nick","nick@mobalistic.com", "nick")
    andi = User(2, "andi","ayjaynaylor@gmail.com", "andi")
    lucy = User(3, "lucy", "lucymehrabyan@gmail.com", "lucy")
    sarah = User(4, "sarah", "sarahnusher@gmail.com", "sarah")

    selfnominator_users = dict_users.add_data(admin)
    nominator_users = dict_users.add_data(nick)
    nominator_users = dict_users.add_data(andi)
    nominator_users = dict_users.add_data(lucy)
    nominator_users = dict_users.add_data(sarah)

    listData.append(admin)
    listData.append(nick)
    listData.append(andi)
    listData.append(lucy)
    listData.append(sarah)

    def get_list(self):
        return self.listData

    def get_nominator_users(self):
        return self.nominator_users
    # for i in nominator_users:
    #     myUser = nominator_users[i];
    #     print myUser.get_username()

    # print nominator_users

    # for i in nominator_users[admin.User()]:
    #     print nominator_users[admin.User()(i)]

    # def get_user_username(dummy_users):
    #     for i in dummy_users:
    #         return i.get_username()
    #
    # def get_user_password(dummy_users):
    #     for i in dummy_users:
    #         return i.get_user_password
# nominees = {"Alice":"She leads the way", "Ashleigh": "She champions the client", "Eduardo":"He loves what he does"}
# print
# print "break"
# print

# def create_nomination_dic(username, reason):
#     hero={}
#     hero[str(username)] = str(reason)
#     return hero
#
# def update_nominees(hero):
#     nominees.update(hero)
#     return nominees

    # dummy_nominations.add_nomination(your_username, your_email, nominee_username, reason)
