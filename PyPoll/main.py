# Creates file paths across operating systems 
import os

# Module for reading CSV files
import csv

# importing the path file to join
input_file = os.path.join('PyPoll','Resources','election_data.csv')

#Input Variables
candidates = set()
votes_total = 0
khan = 0
correy = 0
li = 0
otooley = 0

# Using r in order to "read" the csv file 
with open(input_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for vote in csvreader:
        votes_total += 1

    candidates.add(vote[2])

if (vote[2] == "khan"):
    khan += 1
elif (vote[2] == "correy"):
    correy += 1
elif (vote[2] == "li"):
    li += 1
else:
    otooley += 1

candidates = ["khan", "correy", "li", "otooley"]
votes = [khan, correy, li, otooley]

khan_percent = (khan / votes_total)
correy_percent = (correy / votes_total)
li_percent = (li / votes_total)
otooley_percent = (otooley / votes_total)


vote_cast_dict = dict(zip(candidates, votes))
key = max(vote_cast_dict, key=vote_cast_dict.get)




print("Total Number of Votes Casted: " + str(votes_total))
print("khan: " + "{:.3%}".format(khan_percent) + " " + (str(khan)))
print("correy: " + "{:.3%}".format(correy_percent) + " " + (str(correy)))
print("li: " + "{:.3%}".format(li_percent) + " " + (str(li)))
print("otooley: " + "{:.3%}".format(otooley_percent) + " " + (str(otooley)))
print("winner: " + key)
