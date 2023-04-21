import os
import csv

#set path for file
election_data_csv = os.path.join("election_data.csv")



#open csv file
with open(election_data_csv,newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # total number of votes
    csv_header = next(csvreader)
    data = list(csvreader)
    row_count = len(data)

    #create new list from csv column to get a complete list of candidates
    candidate_list = list()
    tally = list()
    for i in range (0, row_count):
        candidate = data[i][2]
        tally.append(candidate)
        if candidate not in candidate_list:
            candidate_list.append(candidate)
    candidate_count = len(candidate_list)

    #total number of votes & percent 
    votes = list()
    percentage = list()
    for j in range(0,candidate_count):
        name = candidate_list[j]
        votes.append(tally.count(name))
        vote_percent = votes[j]/row_count
        percentage.append(vote_percent)

    #winner of election
    winner = votes.index(max(votes))

    #print analysis and terminal export
    #print results to terminal
    print("Election Results")
    print("------------------------")
    print(f"Total Votes: {row_count:,}")
    print("------------------------")
    for k in range (0,candidate_count):
        print(f"{candidate_list[k]:.3} ({votes[k]:,})")
    print("-------------------------")
    print(f"Winner: {candidate_list[winner]}")

    #print results in pypoll.txt file
    print("Election Results", file=open("Pypoll,txt", "a"))
    print("--------------------------", file = open("Pypoll.txt", "a"))
    print(f"Total Votes: {row_count:,}", file = open("Pypoll.txt", "a"))
    print("------------------------", file = open("Pypoll.txt", "a"))
    for k in range (0,candidate_count):
        print(f"{candidate_list[k]}:{percentage[k]:.3} ({votes[k]:,})" , file = open("Pypoll.txt", "a"))
    print("-------------------------", file = open("Pypoll.txt", "a"))
    print(f"Winner: {candidate_list[winner]}", file = open("Pypoll.txt", "a"))




                                        
       






