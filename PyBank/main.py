import os
import csv

# initiating path to CSVfile
cwd = os.path.dirname(os.path.abspath(__file__))
csvpath = os.path.join(cwd, "Resources", "budget_data.csv")

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    row_count = 0
    next(csvreader)
    for row in csvreader:
        row_count += 1

print("\nFinancial Analysis\n")

print("----------------------------")

print(f"\nTotals month: {row_count}\n")

cwd = os.path.dirname(os.path.abspath(__file__))
csvpath = os.path.join(cwd, "Resources", "budget_data.csv")

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

     #skipping header row
    header = next(csvreader)
    #setting variable
    total_sum = 0
    
    for row in csvreader: #looping through list to get total value
        value = int(row[1])
        total_sum += value
print(f'Total : ${total_sum}\n')

cwd = os.path.dirname(os.path.abspath(__file__))

csvpath = os.path.join(cwd, "Resources", "budget_data.csv")

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") 
     #skipping header row
    header = next(csvreader)
    #setting variables
    values = []
    changes = []
    average_change = 0 
    for row in csvreader:  # looping to get each value
        value = float(int(row[1]))
        values.append(value)
    for i in range(1, len(values)): #calculating change
        change = values[i] - values[i - 1]  
        changes.append(change)
average_change = sum(changes) / len(changes)
print(f"Average Change: ${average_change:.2f}")


cwd = os.path.dirname(os.path.abspath(__file__))

csvpath = os.path.join(cwd, "Resources", "budget_data.csv")

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #setting variables
    dates = []
    changes2 = []
    
    #skipping header row
    next(csvreader)

    for row in csvreader: # looping through table to populate list : dates
        date = row[0]
        dates.append(date)

    for i in range(0, len(changes)): #calculating change
        change = values[i] - values[i - 1] 
        changes2.append(change)
        
        max_change = max(changes2) # using index to correspond values in output. 
        min_change = min(changes2)

        max_index = changes2.index(max_change)
        min_index = changes2.index(min_change)
        
        max_date = dates[max_index]
        min_date = dates[min_index]
       
print(f'\nGreatest Increase in Profits: {max_date} (${max_change:.0f})\n')
print(f'Greatest Decrease in Profits: {min_date} (${min_change:.0f})\n')



 
      



    













    

 
    