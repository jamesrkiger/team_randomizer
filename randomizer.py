import random

roster_init = "Linus, Cletus, Clement, Sixtus, Cornelius, Cyprian, Lawrence, Chrysogonus, John, Paul, Cosmas, Damian, Stephen, Matthias, Barnabas, Ignatius, Alexander, Marcellinus, Peter, Felicitas, Perpetua, Agatha, Lucy, Agnes, Cecilia, Anastasia"

print ("Welcome to the Academy Pittsburgh random team generator. Let's get teamed up.\n")

print ("Please review the roster and see if anyone is absent:\n" + roster_init + "\n")

print ("Please review the roster and see if anyone is absent:\n" + roster_init + "\n")
print ("Enter the names of any absent students as they appear above, separated by commas and spaces. If no one is absent, press enter.\n")
absentees = str(input())
roster = roster_init.split(", ")

#remove absentees, if any
if (len(absentees) > 0):
    absentees = absentees.split(", ")
    for name in absentees:
        roster.remove(name)

student_num = len(roster)
print ("There are currently " + str(student_num) + " students here today. How many teams would you like to create?.\n")
number_of_teams = int(input())
default_team_size = len(roster) // number_of_teams
team_remainder = len(roster) % number_of_teams

#generate an array of team sizes (I think this could also be done without a loop using numpy split)
team_sizes = []

for team in range(number_of_teams):
    team_sizes.append(default_team_size)
    if (team_remainder > 0):
        team_sizes[team] += 1 
        team_remainder -= 1

#randomly shuffle roster list
for name in range(len(roster)):
    ran_spot = random.randint(0,name + 1)

    roster[name],roster[ran_spot] = roster[ran_spot], roster[name]

#print out a team from the beginning of the roster, then delete those names from the roster 
print()
for team in range(number_of_teams):
    print ("Team " + str(team + 1))
    for name in range(team_sizes[team]):
        print(roster[name])    
    del roster[:team_sizes[team]]
    print()






