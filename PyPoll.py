#data needed to be retrieve 
#1. Total number of votes cast
#2. A complete list of candidiates who recevied votes
#3. The percetage of votes each cadidate won
#4. The total number of votes each candidate won
#5. The winnder of the election based on popular vote


import csv
import os

#assign a variable to load a file from a path
file_to_load = os.path.join('Resources','election_results.csv')
#assigna  varaible to save a file to a path
file_to_save = os.path.join('analysis','election_results.txt')

total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#open the election result and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    for i in file_reader:
        total_votes += 1
        candidate_name = i[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            
            #track each candidate's total votes 
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name] += 1

    print(total_votes)
    print(candidate_options)
    print(candidate_votes)
    can_percentage = []
    for j in candidate_options:
        can_percentage.append(candidate_votes[j]/total_votes*100)
        print(f"{j}vote count of {candidate_votes[j]/total_votes*100:.2f}")
        if (candidate_votes[j] > winning_count) and (candidate_votes[j]/total_votes*100>winning_percentage):
            winning_count = candidate_votes[j]
            winning_percentage = candidate_votes[j]/total_votes*100
            winning_candidate = j
    winning_summary = (
        f"______________________\n"
        f"Winner: {winning_candidate}\n"
        f"Winning vote count: {winning_count}\n"
        f"winning percentage: {winning_percentage:.2f}%\n"
        f"_______________________\n"
    )
    print(winning_summary)


    election_data.close()
