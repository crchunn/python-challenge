
import os

import csv

csvpath = os.path.join("Resources/budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)

import statistics

#def print_percentages(profit_loss)

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


