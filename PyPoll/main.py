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

print("Election Results\n\n")
print("----------------------------------------------------\n\n")
print(f"Total Votes: {row_count}\n\n")
print("----------------------------------------------------\n")

output = "Election Results\n\n"
output += "----------------------------------------------------\n\n"
output += f"Total Votes: {row_count}\n\n"
output += "----------------------------------------------------\n"



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

    for i in csvreader: #looping through second column to count votes for each candidate and add them to respective list using if condition
        vote = i[2]
        if vote == 'Charles Casper Stockham':
            charles.append(vote)
        elif vote == 'Diana DeGette':
            diana.append(vote)
        elif vote == 'Raymon Anthony Doane':
            raymon.append(vote)
        vote_count += 1


print(f'\nCharles Casper Stockham : {len(charles)/int(vote_count)*100:.03f}% ({len(charles)})\n\n') 
print(f'Diana DeGette : {len(diana)/int(vote_count)*100:.03f}% ({len(diana)})\n\n') 
print(f'Raymon Anthony Doane : {len(raymon)/int(vote_count)*100:.03f}% ({len(raymon)})\n\n') 
print("----------------------------------------------------\n\n")

output += f'\nCharles Casper Stockham : {len(charles)/int(vote_count)*100:.03f}% ({len(charles)})\n\n' 
output += f'Diana DeGette : {len(diana)/int(vote_count)*100:.03f}% ({len(diana)})\n\n'
output += f'Raymon Anthony Doane : {len(raymon)/int(vote_count)*100:.03f}% ({len(raymon)})\n\n' 
output += "----------------------------------------------------\n\n"

#using IF and ELIF conditions to determine winner
if len(charles) > len(diana) and len(raymon):
    print("Winner : Charles Casper Stockham\n")
    output += "Winner : Charles Casper Stockham\n"
elif len(diana) > len(charles) and len(raymon):
    print("Winner : Diana DeGette\n")
    output += "Winner : Diana DeGette\n"
elif len(raymon) > len(charles) and len(diana):
    print("Winner : Raymon Anthony Doane\n")
    output += "Winner : Raymon Anthony Doane\n"

print("\n----------------------------------------------------\n")
output += "\n----------------------------------------------------\n"
    
cwd = os.path.dirname(os.path.abspath(__file__))

csvpath = os.path.join(cwd, "Analysis", "output.txt")

# with clause for write priveleges to add results in text file. 
with open(csvpath, "w") as file:
    file.write(output)

print("Output file 'output.txt' created successfully!")          


    

    