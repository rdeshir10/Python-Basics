import os
import csv

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

    header = next(csvreader)
    total_sum = 0
    
    for row in csvreader: 
        value = int(row[1])
        total_sum += value
print(f'Total : ${total_sum}\n')

cwd = os.path.dirname(os.path.abspath(__file__))

csvpath = os.path.join(cwd, "Resources", "budget_data.csv")

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") 
    
    header = next(csvreader)

    values = []
    changes = []
    average_change = 0 
    for row in csvreader:  
        value = float(int(row[1]))
        values.append(value)
    for i in range(1, len(values)):
        change = values[i] - values[i - 1]  
        changes.append(change)
average_change = sum(changes) / len(changes)
print(f"Average Change: ${average_change:.2f}")

cwd = os.path.dirname(os.path.abspath(__file__))

csvpath = os.path.join(cwd, "Resources", "budget_data.csv")

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    dates = []
    changes = []
    
    next(csvreader)
  
    max_change = float('-inf')  
    min_change = float('inf')   
    max_date = ""
    min_date = ""

   
    for row in csvreader:
        date = row[0]
        try:
            value = float(row[1])  
        except ValueError:
            continue  
        
        
        dates.append(date)
        changes.append(value)
    
    
    for i in range(1, len(changes)):
        change = changes[i] - changes[i - 1]
        
        if change > max_change:
            max_change = change
            max_date = dates[i]
        elif change < min_change:
            min_change = change
            min_date = dates[i]
print(f'\nGreatest Increase in Profits: {max_date} (${max_change:.0f})\n')
print(f'Greatest Decrease in Profits: {min_date} (${min_change:.0f})\n')




 
      



    













    

 
    