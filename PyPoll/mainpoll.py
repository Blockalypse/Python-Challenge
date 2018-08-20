# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 22:20:39 2018

@author: mrpam
"""
#PyPoll Election
import csv
import os

csvpath = os.path.join("..", "PyPoll", "election_data.csv")

votes = [0,0,0,0]
candidates = ["Khan", "Correy", "Li", "O'Tooley" ]

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    for row in csvreader:
        
        Khan_vote = 0
        Correy_vote = 1
        Li_vote = 2
        OTooley_vote = 3

        if  row[2] == "Khan":
            Khan_index = int(Khan_vote)
            votes[Khan_index] += 1
            
        elif row[2] == "Correy":
            Correy_index = int(Correy_vote)
            votes[Correy_index] += 1
            
        elif row[2] == "Li":
            Li_index = int(Li_vote)
            votes[Li_index] += 1
            
        else: 
            row[2] == "O'Tooley"
            OTooley_index = int(OTooley_vote)
            votes[OTooley_index] += 1
        
       
    # Total votes of each Candidates    
    #print(votes)
    
    # Sum of all votes 
    vote_total = sum(votes)
    
    
    #function for percentages
    def percentage(a, b):
        return round(a / b * 100, 2)
    #Percentages
    Khan_percentage = percentage(votes[0], vote_total)
    Correy_percentage = percentage(votes[1], vote_total)
    Li_percentage = percentage(votes[2], vote_total)
    OTooley_percentage = percentage(votes[3], vote_total)
    
    #Summary
    print(f"Election Results")
    print(f"---------------------------")
    print(f"Total Votes: {vote_total}")
    print(f"---------------------------")
    print(f"{candidates[0]}:     {Khan_percentage}% ({votes[0]})")
    print(f"{candidates[1]}:   {Correy_percentage}% ({votes[1]})")
    print(f"{candidates[2]}:       {Li_percentage}% ({votes[2]})")
    print(f"{candidates[3]}:  {OTooley_percentage}% ({votes[3]})")
    print(f"---------------------------")
    print(f"Winner: {candidates[0]}")