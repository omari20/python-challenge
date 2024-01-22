# Import the os and csv modules to create univeral file paths and perform read and write functions respectively

import os
import csv

# create a variable for the file path and use the os module to make sure that it works on every operating system
path = r'C:\Users\omari\Documents\GitHub\python-challenge\PyPoll\Resources'

file_path = os.path.join(path, 'election_data.csv')

with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the first row
    next(csvreader)

    # initialize variables
    total_votes = 0

    # Set candidate votes to dictionary so the key is the unique candidate name, and the value will be the votes
    candidates_votes = {}

    # Creating a dictionary to track the winner
    winner = {"name": "", "votes": 0}

    for row in csvreader:
    
    # Total votes casted (count of all rows)
        total_votes += 1

    # Set the candidate name found in col 2
        candidate_name = row[2]
    
    # Check if the candidate name is already in the dictionary 
        if candidate_name in candidates_votes:
            # If yes, add a count in the iteration
            candidates_votes[candidate_name] += 1
        # If not, add the candidate to the dictionary    
        else:
            candidates_votes[candidate_name] = 1

    # Check if the current candidate has more votes than the current winner
        if candidates_votes[candidate_name] > winner['votes']:
            winner['name'] = candidate_name
            winner['votes'] = candidates_votes[candidate_name]


print('Election Results')

print('-----------------------------------')

print(f'Total votes: {total_votes}')

print('-----------------------------------')

# create 2 variables (candidates, votes) in the forloop to input the key, value pair into a tuple created by the items() function
for candidate, votes in candidates_votes.items():
    vote_percentage = (votes / (total_votes - 1)) * 100 
    print(f'{candidate}: {vote_percentage:.3f}% ({votes})')

print('-----------------------------------')


print(f'Winner: {winner['name']}')

print('-----------------------------------')

# create a variable for the file path and use the os module to make sure that it works on every operating system
file_path2 = r'C:\Users\omari\Documents\GitHub\python-challenge\PyPoll\analysis'
path2 = os.path.join(file_path2, 'results.txt')

# Write results to a text file called results.txt
with open(path2, 'w') as output_file:
    output_file.write('Election Results\n')
    output_file.write('-----------------------------------\n')
    output_file.write(f'Total votes: {total_votes}\n')
    output_file.write('-----------------------------------\n')
# fixed the iteration here as well so the code writes to the txt file per candidate    
    for candidate, votes in candidates_votes.items():
        vote_percentage = (votes / total_votes) * 100 
        output_file.write(f'{candidate}: {vote_percentage:.3f}% ({votes})\n')
    output_file.write('-----------------------------------\n')
    output_file.write(f'Winner: {winner['name']}\n')
    output_file.write('-----------------------------------')