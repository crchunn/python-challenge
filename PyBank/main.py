
import os

import csv

import statistics

print("Financial Analysis")

csvpath = os.path.join("Resources/budget_data.csv")



    #months = str(profit_loss[0])
    #amounts = int(profit_loss[1])
   


    #changes_in_profits = average(months)




#def print_percentages(profit_loss):

#data1 = [1, 3, 4, 5, 7, 9, 2] 
  
#x = statistics.mean(profit_loss) 
  
# Printing the mean 
#print("Mean is :", x) 

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    greatestincrease = ["", 0]
    greatestdecrease = ["", 999999]
    avg_of_profit = []
    total_months = 1
    #print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")


    net = next(csvreader)
    net = int(net[1])
    #print(net)
    changes_in_profits = net

    for row in csvreader:
        #print(row)

        total_months = total_months + 1
        changes_in_profits = changes_in_profits + int(row[1])
        monthchange = int(row[1]) - net

        avg_of_profit.append(monthchange)
        net = int(row[1])
        if(greatestincrease[1] < monthchange):
            greatestincrease[1] = monthchange
            greatestincrease[0] = row[0]

        if(greatestdecrease[1] > monthchange):
            greatestdecrease[1] = monthchange
            greatestdecrease[0] = row[0]

profitavg = sum(avg_of_profit)/len(avg_of_profit)


print("Total Months:")
print(total_months)
print(changes_in_profits)
print(f"{profitavg:.2f}")

print(greatestincrease)
print(greatestdecrease)

#output = (
    #"Financial Analysis/n"
   # "--------------------------------------/n"
   # "Total Months" + str(total_months) + "/n"
    #"Total: $" + (changes_in_profits) + "/n"
   # "Average Change:" + (f"{profitavg:.2f}") + "/n"
   # "Greatest Increase in Profits:" + (greatestincrease) + "/n"
  #  "Greatest Decrease in Profits:" + (greatestdecrease) + "/n")

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

#with open(output, "w") as textfile:
    #textfile.write(output)
