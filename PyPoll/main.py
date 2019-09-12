import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

candidate = []
candidate_name = []
candidate_votes = 0
total_candidate_votes = 0
winner_votes = 0
total_votes = 0
total_candidates = len(candidate)
winner = ""

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
        candidate.append(row[2])
    for unique in candidate:

        if  unique not in candidate_name:    
            candidate_name.append(unique)
            candidate_votes = 1
            total_votes = total_votes + 1
        else:
            percentage_won = float(candidate_votes/total_votes) * 100   
            winning_candidate = candidate_name
            win_count = candidate_votes
            candidate_votes = candidate_votes + 1
            total_votes = total_votes + 1

output_path = os.path.join( 'Resources', 'Election Results.csv')

with open(output_path, 'w', newline='') as txtfile:
    writer = text.writer(txtfile)
    writer.write('Election Results')
    writer.write(txtfile)
    
print(txtfile)