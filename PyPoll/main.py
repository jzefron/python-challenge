import csv
import os


csvpath = os.path.join('source','Instructions','PyPoll','Resources','election_data.csv')
vote_data = []
candidates = []
totVotes =0
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    csv_header = next(csvreader)
    print(csv_header)
    for row in csvreader:
        totVotes +=1
        #print(row[2])
        vote = row[2]
        if vote in candidates:
            #print("in try")
            vote_data[candidates.index(row[2])] += 1
        else:
           # print("exception")
            candidates.append(row[2])
            vote_data.append(1)

print("Election Results") 
print("-------------------------")

print("Total Votes:",totVotes)
print("-------------------------")

for i,candidate in enumerate(candidates):
    vote = vote_data[i]

    print (candidate +" recieved:",  str(round(vote/totVotes*100))+"% (" +str(vote) +")")