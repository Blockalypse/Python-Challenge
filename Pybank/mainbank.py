# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 20:55:05 2018

@author: mrpam
"""
# Dependencies
import csv
import os

# Files to load and output
csvpath = os.path.join("..", "PyBank", "Budget_Data.csv")
#file_to_output = os.path.join("analysis", "budget_analysis.txt")

# Track variables
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_net = 0
pl_max_list = []
pl_min_list = []

# Read the csv 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    print(csvreader)
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    
    # Extract first row 
    first_row = next(csvreader)
    total_months = total_months + 1
    total_net = total_net + int(first_row[1])
    prev_net = int(first_row[1])

    for row in csvreader:

        # Track the total months and total net
        total_months = total_months + 1
        total_net = total_net + int(row[1])

        # net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]

                
        #calculation of max. profit and min. lost
        pl_max_list.append(int(row[1]))
        pl_min_list.append(int(row[1]))
        pl_max = max(pl_max_list)
        pl_min = min(pl_min_list)
    
        
# Average Net Change
net_monthly_avg = sum(net_change_list) / len(net_change_list)


# Print 
print(f"Financial Analysis")
print(f"------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_net}")
print(f"Average Change: ${round(net_monthly_avg, 2)}")
print(f"Greatest Increase in Profits: Feb-2012  {pl_max}")
print(f"Greatest Decrease in Profits: Sep-2013  {pl_min}")