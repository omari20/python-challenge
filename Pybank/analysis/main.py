# Import the os and csv modules to create univeral file paths and perform read and write functions respectively
import os
import csv

# Specify the CSV file within the directory
# file_name = 'budget_data.csv'
path = r"C:\Users\omari\Documents\GitHub\python-challenge\Pybank\Resources"
file_path = os.path.join(path, 'budget_data.csv')

# print(f'this is it: {file_path}')

with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # for row in csvreader:
    #     print(row)

#skip first row
    next(csvreader)

#create a variable that will store the number of months (rows)
    
    total_months = 0
    total_net_profit = 0
    previous_net_profit = None 
    total_changes = 0
    highest_positive_change = 0
    date_highest_positive_change = ""
    highest_negative_change = 0
    date_highest_negative_change = ""


#itirate over the rest of the data set to make the calculations  
    for row in csvreader:

    #Total number of months (The count of rows)  
        total_months +=1

    #current Net profit in the iteration
        current_net_profit = int(row[1])
 
    #Add the current change to total change
        if previous_net_profit is not None:
            changes = current_net_profit - previous_net_profit
            total_changes += changes
    
    # Using this formula to add up to give the highest & lowest changes
            if changes > highest_positive_change:
                highest_positive_change = changes
                date_highest_positive_change = row[0]
            elif changes < highest_negative_change:
                highest_negative_change = changes
                date_highest_negative_change = row[0]


    # Update previous net profit for the iteration
        previous_net_profit = current_net_profit

    # Add current net profit to the total net profit
        total_net_profit += current_net_profit

# Average Change in profits (subtract one to remove header)
average_Change = round((total_changes / (total_months - 1)),2)

print("Financial Analysis")


print('-------------------------------------------')


print(f'Total months: {total_months}')


print(f'Total: ${total_net_profit}')


print(f'Total: ${average_Change}')


print(f'Greatest Increase in Profits: {date_highest_positive_change} (${highest_positive_change})')


print(f'Greatest Decrease in Profits: {date_highest_negative_change} (${highest_negative_change})')

   
# Write results to a text file called results.txt
file_path1 = r'C:\Users\omari\Documents\GitHub\python-challenge\Pybank\analysis'
path2 = os.path.join(file_path1, 'results.txt')

with open(path2, 'w') as output_file:

    output_file.write('Financial Analysis\n')
    output_file.write('--------------------------\n')
    output_file.write(f'Total: {total_net_profit}\n')
    output_file.write(f'Total: ${average_Change}\n')
    output_file.write(f'Greatest Increase in Profits: {date_highest_positive_change} (${highest_positive_change})\n')  
    output_file.write(f'Greatest Decrease in Profits: {date_highest_negative_change} (${highest_negative_change})')