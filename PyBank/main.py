
import os

import csv

import statistics

csvpath = os.path.join("Resources/budget_data.csv")

def print_percentages(profit_loss):
    months = str(profit_loss[0])
    amounts = int(profit_loss[1])

    total_months = sum(months)

    changes_in_profits = average(months)





#data1 = [1, 3, 4, 5, 7, 9, 2] 
  
x = statistics.mean(profit_loss) 
  
# Printing the mean 
print("Mean is :", x) 


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)





#total number of months included in dataset

#net total amount of profit/loss over entire period

    #df["Profit/Losses"].sum()
    #csvreader.next() 
    # to skip the header 

    #numbers = (float(row[2]) for row in csvreader)
    #total = sum(numbers)

    #print (total)
#average of changes in profits (date and amount) over period

#greatest increase in profits (date and amount) over period

#greatest decrease in losses (date and amount) over entire period


