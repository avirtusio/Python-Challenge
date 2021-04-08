# Creates file path across operating system
import os

# Module for reading CSV files
import csv

# Importing the path to the file to join
input_file = os.path.join('PyPoll', 'Resources', 'election_data.csv')

# My list of input variables
candidates = set()
votes_total = 0
khan = 0
correy = 0
li = 0
otooley = 0

# Obtaining the total amount of votes and the sum of each of the votes for each candidate
with open(input_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for vote in csvreader:
        votes_total += 1
        candidates.add(vote[2])

        if(vote[2] == "Khan"):
            khan += 1
        elif(vote[2] == "Correy"):
            correy += 1
        elif(vote[2] == "Li"):
            li += 1
        else:
            otooley += 1

# Formula to calculate the percentage amount for each of the candidates
percent_khan = (khan/votes_total)
percent_correy = (correy/votes_total)
percent_li = (li/votes_total)
percent_otooley = (otooley/votes_total)

# Creation of lists
candidate_list = ["Khan", "Correy", "Li", "Otooley"]
votes = [khan, correy, li, otooley]

# Use of dictionaries in order to recall the list and information 
vote_cast_dict = dict(zip(candidate_list, votes))
key = max(vote_cast_dict, key=vote_cast_dict.get)

# Print statments for the given input to outputs
# Using the .3% formula in order to show percentage and roundage after the decimal point
print("Total Amount of Votes Casted: " + str(votes_total))
print("Khan: " + "{:.3%}".format(percent_khan) + " " + (str(khan)))
print("Correy: " + "{:.3%}".format(percent_correy) + " " + (str(correy)))
print("Li: " + "{:.3%}".format(percent_li) + " " + (str(li)))
print("Otooley: " + "{:.3%}".format(percent_otooley) + " " + (str(otooley)))

print("Winner: " + key)

# Writing the text file into the Analysis folder 
output_path = os.path.join('PyPoll','Analysis','new_file.txt')
# Using \n to create a new line 
with open(output_path, 'w') as file:
    file.write("Total Amount of Votes Casted: " + str(votes_total))
    file.write("\nKhan: " + "{:.3%}".format(percent_khan) + " " + (str(khan)))
    file.write("\nCorrey: " + "{:.3%}".format(percent_correy) + " " + (str(correy)))
    file.write("\nLi: " + "{:.3%}".format(percent_li) + " " + (str(li)))
    file.write("\nOtooley: " + "{:.3%}".format(percent_otooley) + " " + (str(otooley)))
    file.write("\nWinner: " + key)
