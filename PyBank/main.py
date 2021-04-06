# Creates file paths across operating systems 
import os

# Module for reading CSV files
import csv

# importing the path file to join
input_file = os.path.join('PyBank','Resources','budget_data.csv')

#Input Variables
total_months = []
total_amount = []
monthly_profit_change = []

#Obtaining the total for months, amount (Profit/Losses), and greatest increase and decrease for the given periods.
with open(input_file, newline='\n') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader: 
        total_months.append(row[0])
        total_amount.append(int(row[1]))

    for r in range(len(total_amount)-1):
        monthly_profit_change.append(total_amount[r+1]-total_amount[r])

        greatest_increase = max(monthly_profit_change)
        greatest_decrease = min(monthly_profit_change)

        greatest_increase_profit = monthly_profit_change.index(max(monthly_profit_change))+1
        greatest_decrease_losses = monthly_profit_change.index(min(monthly_profit_change))+1

# Print Statments for the given inputs to outputs
print(f"Total Months: {len(total_months)}")
print(f"Total Net Amount: ${sum(total_amount)}")
print(f"Average of Changes: ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[greatest_increase_profit]} (${str(greatest_increase)})")
print(f"Greatest Decrease in Losses: {total_months[greatest_decrease_losses]} (${str(greatest_decrease)})")


output_path = os.path.join('PyBank','Analysis','new_file.txt')

with open(output_path, 'w') as file:
    file.write(f"Total Months: {len(total_months)}\n")
    file.write(f"Total Net Amount: ${sum(total_amount)}\n")
    file.write(f"Average of Changes: ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}\n")
    file.write(f"Greatest Increase in Profits: {total_months[greatest_increase_profit]} (${str(greatest_increase)})\n")
    file.write(f"Greatest Decrease in Losses: {total_months[greatest_decrease_losses]} (${str(greatest_decrease)})\n")
