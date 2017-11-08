from user import *

# what it is and how you're currently using it (usig it for static data) - going forward plan (add database logic to save or get the user)

class UsersData(object):

    usersList = []

    admin = User(0, "admin","andi.goldsworthy@gmail.com", "password")
    nick = User(1, "nick","nick@mobalistic.com", "nick")
    andi = User(2, "andi","ayjaynaylor@gmail.com", "andi")
    lucy = User(3, "lucy", "lucymehrabyan@gmail.com", "lucy")
    sarah = User(4, "sarah", "sarahnusher@gmail.com", "sarah")

    usersList.append(admin)
    usersList.append(nick)
    usersList.append(andi)
    usersList.append(lucy)
    usersList.append(sarah)

# a getter to get the list of user
    def get_list(self):
        return self.usersList
