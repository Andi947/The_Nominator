from user import *

# Object that contains the static user data used in the program. Going forward, this will be where the Users Database logic will be where users can be added to or accessed from the DB

class UsersData(object):
    # empty list generated
    usersList = []

    # Each static user is created as a User Object
    admin = User(0, "admin","andi.goldsworthy@gmail.com", "password")
    nick = User(1, "nick","nick@mobalistic.com", "nick")
    andi = User(2, "andi","ayjaynaylor@gmail.com", "andi")
    lucy = User(3, "lucy", "lucymehrabyan@gmail.com", "lucy")
    sarah = User(4, "sarah", "sarahnusher@gmail.com", "sarah")

    # Each user is added to the list
    usersList.append(admin)
    usersList.append(nick)
    usersList.append(andi)
    usersList.append(lucy)
    usersList.append(sarah)

# a getter to get the list of users
    def get_list(self):
        return self.usersList
