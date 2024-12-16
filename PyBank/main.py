"""
PyBank Homework Budget Analysis
Justin Zisholtz
Due: December 16th, 2024
"""

#Dependencies
import csv
import os

#Files to load and output
files_to_load = os.path.join("Resources", "budget_data.csv")
files_to_output = os.path.join("analysis", "budget_analysis.txt")

#Define variables and set them up
total_months = 0
net_pl = 0
greatest_increase = ["",0]
greatest_dec = ["",0]
sumchange = 0

# Track the total and net change
totalchange = []
netchange = None

# lines 12/11 just set the file paths, now
# we need to open and read the csv in line 12
#So, set the path to a string var and set the var to 
with open(files_to_load) as financial_data:
    reader = csv.reader(financial_data)

    #indent because everything we are doing now is within this open csv file.
    #skip header row, 'next' allows you to go to the next row.
    header = next(reader)

    #Extract first row to avoid appending to net_change_list
    firstrow = next(reader)
    total_months += 1
    net_pl = net_pl + int(firstrow[1])
    followingrow_pl = int(firstrow[1])

    # Process each row of data
    for row in reader:
       #Tracking the total
       total_months += 1
       #Track the net change profit and loss
       net_pl = net_pl + int(row[1])
        #calculating the total change: each row - the one before
       change = int(row[1]) - (followingrow_pl)
       followingrow_pl = int(row[1])
       totalchange.append(change)
       #calculate average change
       avgchange = sum(totalchange)/(total_months -1)
       roundedAvgChange = round(avgchange, 2)

      # Calculate the greatest increase in profits (month and amount)
       if change > int(greatest_increase[1]):
         greatest_increase[0] = row[0]
         greatest_increase[1] = change
         #calc greatest decrease:
       if change < int(greatest_dec[1]):
         greatest_dec[0] = row[0]
         greatest_dec[1] = change
         

#create a txt file and save the output there:
with open("analysis/PyBankAnalysis.txt", "w") as txt_file:
   txt_file.write("Financial Analysis\n")
   txt_file.write("----------------------------\n")
   txt_file.write(f"Total Months: {total_months}\n")
   txt_file.write(f"Total: ${net_pl}\n")
   txt_file.write(f"Average Change: ${roundedAvgChange}\n")
   txt_file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
   txt_file.write(f"Greatest Decrease in Profits: {greatest_dec[0]} (${greatest_dec[1]})\n")
#print results
   print("Financial Analysis")
   print("----------------------------")
   print(f"Total Months: {total_months}")
   print(f"Total: ${net_pl}")
   print(f"Average Change: ${roundedAvgChange}")
   print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
   print(f"Greatest Decrease in Profits: {greatest_dec[0]} (${greatest_dec[1]})")