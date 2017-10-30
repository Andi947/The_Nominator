import users_data
from users_data import *
import nominations_data
from nominations_data import *
from result_calculator import *

users = UsersData().get_nominator_users()
nominations = NominationsData().get_nominator_nominations()
calculate = CalculatorResult()

nomineeID_count = []
nominee_counts = {}

nomineeID_count = calculate.list_of_nomineeIDs(nominations)
print nomineeID_count

nominee_counts = calculate.calculate_nominee_nominations(nomineeID_count)
print nominee_counts

winning_userID = calculate.calculate_winning_nomineeID(nominee_counts)
print winning_userID

winner_name = calculate.winnerID(users, winning_userID)
print winner_name

number_of_votes = calculate.no_of_votes(nominee_counts)
print number_of_votes

total_votes = calculate.total_votes(nomineeID_count)
print total_votes

print "Congratulation to " + str(winner_name) + " who got a total of " + str(number_of_votes) + " out of " + str(total_votes) + " votes!"
