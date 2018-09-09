#Module for reading CSV files
import os
import csv

#locate file to read
csvpath = os.path.join('budget_data.csv')

#list to track total months
TotalMonths = []

#list to track total Profit/Loss
TotalPL = []

#list to track change in Profit/Loss
PLChange = []

#open the csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    next(csvreader)

    #loop through data
    for row in csvreader:

        #Append the total months and total profit/ losses
        TotalMonths.append(row[0])
        TotalPL.append(int(row[1]))

    # Iterate through the profits/ losses
    for i in range(len(TotalPL)-1):
        
        #subtract the PL from the previous list and then sum
        PLChange.append(TotalPL [i+1]-TotalPL[i])
        
#find the max of the PL change
MaxChangeAmt = max(PLChange)

#find the min of the PL change
MinChangeAmt = min(PLChange)

#find the max change month
MaxChangeMonth = PLChange.index(max(PLChange)) + 1

#find the min change month
MinChangeMonth = PLChange.index(min(PLChange)) + 1 

#print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(TotalMonths)}")
print(f"Total: ${sum(TotalPL)}")
print(f"Average Change: {round(sum(PLChange)/len(PLChange),2)}")
print(f"Greatest Increase in Profits: {TotalMonths[MaxChangeMonth]} (${(str(MaxChangeAmt))})")
print(f"Greatest Decrease in Profits: {TotalMonths[MinChangeMonth]} (${(str(MinChangeAmt))})")   

# create new txt file
file = open("FinancialAnalysis.txt","w")
    
#print results to txt file
file.write("Financial Analysis")
file.write("\n")
file.write("----------------------------")
file.write("\n")
file.write(f"Total Months: {len(TotalMonths)}")
file.write("\n")
file.write(f"Total: ${sum(TotalPL)}")
file.write("\n")
file.write(f"Average Change: {round(sum(PLChange)/len(PLChange),2)}")
file.write("\n")
file.write(f"Greatest Increase in Profits: {TotalMonths[MaxChangeMonth]} (${(str(MaxChangeAmt))})")
file.write("\n")
file.write(f"Greatest Decrease in Profits: {TotalMonths[MinChangeMonth]} (${(str(MinChangeAmt))})")

#close
file.close()