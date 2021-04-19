import os
import csv

# joining path 
csvpath = os.path.join("Resources", "election_data.csv")

#Initializing Variable Values
votes = 0
voteCount = []
candidates = []

# open and read csv file
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    next(csv_reader)

    # read through each row of data after header
    for row in csv_reader:
        #Tally votes
        votes = votes + 1
        #Candidates
        candidate = row[2]

        #if/else statements to get votes per candidate
        if candidate in candidates:
           candidate_index = candidates.index(candidate)
           voteCount[candidate_index] = voteCount[candidate_index] + 1
        else:
           candidates.append(candidate)
           voteCount.append(1)

# Calculate candidate/vote percentages
percentages = []
greatestVotes = voteCount[0]
greatestVotes_index = 0
for count in range(len(candidates)):
    votePercentage = voteCount[count]/votes*100
    percentages.append(votePercentage)
    if voteCount[count] > greatestVotes:
        print(greatestVotes)
        greatestVote_index = count
winner = candidates[greatestVotes_index]
percentages = [round (i,2) for i in percentages]
#Print the results           
print()
print("Election Results")
print("--------------------------------")
print(f"Total Votes: {votes}")
print("--------------------------------")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({voteCount[count]})")
print("--------------------------------")
print(f"Winner:  {winner}")
print("--------------------------------")


# output to text file. '\n' represents a new line to be written

file = open("output.txt", "w" )

file.write("Election Results" + "\n")
file.write("\n__________________________" + "\n")

file.write("\nTotal Votes" + str(votes))
file.write("\n_________________________" + "\n")

for count in range(len(candidates)):
    file.write(f"\n{candidates[count]}: {percentages[count]}% ({voteCount[count]})" +"\n")
file.write("\n__________________________" + "\n")
file.write(f"\nWinner: {winner}")
file.write("\n_____________________________" + "\n")
