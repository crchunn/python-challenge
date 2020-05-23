import os

import csv
import string
import statistics
# print("Election Results")

csvpath = os.path.join("Resources/election_data.csv")


# """ candidate1 = str("Khan")
# candidate2 = str("Correy")
# candidate3 = str("Li")
# candidate4 = str("O'Tooley")
# #temp = {} """
#name = ["Candidate"[3]]


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    cvotes = []
    total_votes = 0
    unique = []
    percent = []
    candidatecount = []

    
    


    for row in csvreader:
        # candidate_name = row[2]
        total_votes = total_votes + 1
        # candidate_votes = 0
        #cvotes = int(row[1])
        # cvotes.append(candidate_votes)


        # if (candidate_name == candidate_name):
        #     candidate_name = candidate_votes + 1
        #     candidate_name = row[2]
        # if (candidate_name != candidate_name):
        #     candidate_name = candidate_name + 1
        #     candidate_name = row[2]

        if row[2] not in unique:
            unique.append(row[2])

        cvotes.append(row[2])

    for candidate in unique:
        candidatecount.append(cvotes.count(candidate))
        percent.append(round(cvotes.count(candidate)/total_votes*100,3))

    winner = unique[candidatecount.index(max(candidatecount))]

print("Election Results")
print("----------------------------")
print(f"Total Results: {total_votes}")
print("----------------------------")
for i in range(len(unique)):
    print(f"{unique[i]}: {percent[i]}% {candidatecount[i]}")
print("----------------------------")
print(f"Winner: {winner}")

poll_output_file = os.path.join("PyPoll.txt")        
with open(poll_output_file, 'w') as txtfile:

    txtfile.write("Election Results")
    txtfile.write("\n----------------------------")
    txtfile.write(f"\nTotal Results: {total_votes}")
    txtfile.write("----------------------------")
    for i in range(len(unique)):
        txtfile.write(f"\n{unique[i]}: {percent[i]}% {candidatecount[i]}")
    txtfile.write("\n----------------------------")
    txtfile.write(f"Winner: {winner}")

#with open(pypoll_csv, newline="") as csvfile:
    #csvreader = csv.reader(csvfile, delimiter=",")

           
        # print(candidate_votes)
        
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

# print("Total Votes:") 
# print(total_votes)