"""
PyPoll - Election Data Analysis
Justin Zisholtz
Module Challenge 3
"""
import csv
import os

file_to_load = os.path.join("Resources", "election_data.csv")
files_to_output = os.path.join("analysis", "election_analysis.txt")

# variables:
total_votes = 0
candidate_votes = {}
PercentVote = {}
winningVotes = 0
winningCand = ""



with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

#skip header
    header = next(reader)

#The total number of votes cast
    for row in reader:
        total_votes += 1
#A complete list of candidates who received votes
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
    
# The percentage of votes each candidate won
    for candidate, votes in candidate_votes.items():
        PercentVote[candidate] = (votes/total_votes) * 100
# The total number of votes each candidate won
    #This answer is in the "[candidate_votes]" dict already.
# The winner of the election based on popular vote
    for winner, votes in candidate_votes.items():
        if votes > winningVotes:
            winningVotes = votes
            winningCand = winner
# Export Results to txt file
with open(files_to_output, "w") as txtF:
    txtF.write("Election Results\n")
    txtF.write("-------------------------\n")
    txtF.write(f"Total Votes: {total_votes}\n")
    txtF.write("-------------------------\n")
    for candidate in candidate_votes:
        txtF.write(f"{candidate}: {PercentVote[candidate]:.3f}% ({candidate_votes[candidate]})\n")
    txtF.write(f"-------------------------\n")
    txtF.write(f"Winner: {winningCand}\n")
    txtF.write("-------------------------\n")
#Print Results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidate_votes:
    print(f"{candidate}: {PercentVote[candidate]:.3f}% ({candidate_votes[candidate]})")
print(f"-------------------------")
print(f"Winner: {winningCand}")
print("-------------------------")