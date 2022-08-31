#data needed to be retrieve 
#1. Total number of votes cast
#2. A complete list of candidiates who recevied votes
#3. The percetage of votes each cadidate won
#4. The total number of votes each candidate won
#5. The winnder of the election based on popular vote


import csv
import os

file_to_load = os.path.join('Resources','election_results.csv')
file_to_save = os.path.join('analysis','election_results.txt')

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
    election_data.close()
with open(file_to_save,"w") as txt_file:

    txt_file.write("Counties in the Election\n-------------------\nArapahoe\nDenver\nJefferson")
    txt_file.close()

