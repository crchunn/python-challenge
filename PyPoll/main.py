import os

import csv
import string
import statistics
print("Election Results")

csvpath = os.path.join("Resources/election_data.csv")


candidate1 = str("Khan")
candidate2 = str("Correy")
candidate3 = str("Li")
candidate4 = str("O'Tooley")
#temp = {}
#name = ["Candidate"[3]]


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    cvotes = []
    total_votes = 0
    
    


    for row in csvreader:
        candidate_name = row[2]
        total_votes = total_votes + 1
        candidate_votes = 0
        #cvotes = int(row[1])
        cvotes.append(candidate_votes)


        if (candidate_name == candidate_name):
            candidate_name = candidate_votes + 1
            candidate_name = row[2]
        if (candidate_name != candidate_name):
            candidate_name = candidate_name + 1
            candidate_name = row[2]
        

           
        print(candidate_name)
        
        #if(candidate[2] = candidate):
            #candidate[2] = candidate + int(1)
        
    
        #for candidate[0] in csvreader:
            #name = name.lower()

           # if name in csvreader:
            #    temp[name] += 1
     #       else:
     #           temp[name] = 1
     #           countnames = {}
     #   for key, value in temp.items():
      #      if value in countnames:
    #            countnames[value].append(key)
     #       else:
     #           countnames[value] = [key]
#print(countnames)

        #if row[1] == candidate1:
            #candidate1 = candidate1 + 1
        #if row[1] == candidate2:
           # candidate2 = candidate2 + 1
        #if row[1] == candidate3:
           # candidate3 = candidate3 + 1
        #if row[1] == candidate4:
           # candidate4 = candidate4 + 1

   # print(candidate1 + "had" + "of the vote.")

#A complete list of candidates who received votes


#The percentage of votes each candidate won


#The total number of votes each candidate won
   #Khan = str(candidate_list[3])

        #if (candidate_list[3] = Khan):
            #candidate_list[3] = candidate
            #candidate_list[0] = row[0] """


#The winner of the election based on popular vote.


    

       # print(csvreader)(5)

    #csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #for row in csvreader:
        #print(row)(5)

print("Total Votes:") 
print(total_votes)