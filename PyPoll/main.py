import os
import csv

# initiating path to CSVfile
cwd = os.path.dirname(os.path.abspath(__file__))

csvpath = os.path.join(cwd, "Resources", "election_data.csv")

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")    
    
    #skipping header row
    next(csvreader)
    #setting variable
    row_count = 0
    for row in csvreader: #looping to get total count of votes
        row_count += 1

print("Election Results")

print("----------------------------------------------------")

print(f"Total Votes: {row_count}")

print("----------------------------------------------------")
cwd = os.path.dirname(os.path.abspath(__file__))

csvpath = os.path.join(cwd, "Resources", "election_data.csv")

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skipping header row
    next(csvreader)
    #setting variables
    charles = []
    diana = []
    raymon = []
    vote_count = 0
    winner = []

    for i in csvreader: #looping through second column to count votes for each candidate using if condition
        vote = i[2]
        if vote == 'Charles Casper Stockham':
            charles.append(vote)
        elif vote == 'Diana DeGette':
            diana.append(vote)
        elif vote == 'Raymon Anthony Doane':
            raymon.append(vote)
        vote_count += 1


print(f'\nCharles Casper Stockham : {len(charles)/int(vote_count)*100:.03f}% ({len(charles)})\n') 
print(f'Diana DeGette : {len(diana)/int(vote_count)*100:.03f}% ({len(diana)})\n') 
print(f'Raymon Anthony Doane : {len(raymon)/int(vote_count)*100:.03f}% ({len(raymon)})\n') 
print("----------------------------------------------------")
#using IF and ELIF conditions to determine winner
if len(charles) > len(diana) and len(raymon):
    print("Winner : Charles Casper Stockham")
elif len(diana) > len(charles) and len(raymon):
    print("Winner : Diana DeGette")
elif len(raymon) > len(charles) and len(diana):
    print("Winner : Raymon Anthony Doane")

print("----------------------------------------------------")
    
            


    

              
















# def count_of_votes(election_data):
#     header = next(csvreader)
#     candidate = row[2]

   
    