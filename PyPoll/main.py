# main.py 
# pypoll assignment - Python module -Pradip Raodeo 7/1/2022
# This will allow us to create file paths across operating systems


import os

# Module for reading CSV files
import csv
csvpath = os.path.join('.', 'Resources', 'election_data.csv')


v_county_candidates = []
v_total_vote_count = 0
with open(csvpath, encoding='utf-8') as inputdata:
#with open("Resources/election_data.csv") as inputdata:
    reader = csv.reader(inputdata)
    next(reader) #skip the first header row
    for row in reader:
        v_county = row[1]
        v_candidate = row[2]
        v_ballot_dict = {"county": v_county, "candidate": v_candidate}
        v_county_candidates.append(v_ballot_dict)  

v_total_vote_count = len(v_county_candidates) #length of list will give us count for votes

#print("total vote counts "+ str(v_total_vote_count))
#v_county_candidates[0:100]
#v_county_candidates[9]["candidate"]
v_unique_candidates = [] #unique candidates list with names
v_votes_for_candidates = [] #vote counts for each candidates

#Get the unique candidate list from all the votes
for v_vote in range(v_total_vote_count):
    if v_county_candidates[v_vote]["candidate"] not in v_unique_candidates:
        v_unique_candidates.append(v_county_candidates[v_vote]["candidate"])
        
#print(v_unique_candidates)
#print(v_unique_candidates[0])
v_candidate_cnt = len(v_unique_candidates) # we got three unique candidates 
#print( v_candidate_cnt)
#x = 0

#initializing list for candidate vote counts
for x in range(v_candidate_cnt):
    v_votes_for_candidates.append(0) 

# vote grouping by candidate, we already know how many candidates and we stored in list v_unique_candidates
for v_vote in range(v_total_vote_count):
    for x in range(v_candidate_cnt):
        if v_county_candidates[v_vote]["candidate"] == v_unique_candidates[x]:
            v_votes_for_candidates[x] += 1

#print(v_votes_for_candidates)  
print("Election Results")
print("-------------------------")
print("Total Votes: "+ str(v_total_vote_count))
print("-------------------------")

# for output file
output = ""
output += f"\nElection Results\n"
output += f"-------------------------\n"
output += f"Total Votes: "+ str(v_total_vote_count) +"\n"
output += f"-------------------------\n"

for x in range(v_candidate_cnt):
    v_percent_votes = (v_votes_for_candidates[x]/v_total_vote_count) * 100
    #print(v_unique_candidates[x] +" "+ str((v_votes_for_candidates[x]/v_total_vote_count) * 100) + " ("+ str(v_votes_for_candidates[x]) + ") " )
    print(f"{v_unique_candidates[x]}  {v_percent_votes:.3f}%  {v_votes_for_candidates[x]} " )
    output += f"{v_unique_candidates[x]}  {v_percent_votes:.3f}%  {v_votes_for_candidates[x]}\n "
print("-------------------------")
output += f"-------------------------\n"

#select the winner record
v_max_votes = 0
for x in range(v_candidate_cnt):
    if v_votes_for_candidates[x] > v_max_votes:
        v_max_votes = v_votes_for_candidates[x]
#print(v_max_votes)

#search for index for max votes and print it
for x in range(v_candidate_cnt):
    if v_votes_for_candidates[x] == v_max_votes:
        print("Winner: "+ v_unique_candidates[x] + " with "+ str(v_max_votes) + " votes!!" )
        print(" -------------------------")
        output += f"Winner: "+ v_unique_candidates[x] + " with "+ str(v_max_votes) + " votes!!\n" 
        output += f"-------------------------\n"

output_file = os.path.join('.', 'analysis',"pypoll_analysis.txt")
with open(output_file, "w") as textFile:
    textFile.write(output)
  