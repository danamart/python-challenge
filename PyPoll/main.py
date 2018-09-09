# Module for reading CSV files
import os
import csv

#locate file to read
csvpath = os.path.join('election_data.csv')

#Variable
TotalVotes = 0 
KhanVotes = 0
CorreyVotes = 0
LiVotes = 0
OtooleyVotes = 0

#open the csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") 

    #Read the header row first
    header = next(csvreader)     

    #loop through data
    for row in csvreader: 

        #Count the total number of voters by unique voter ID and keep
        TotalVotes +=1

        #Count and store number of votes for each of the 4 candidtaes ***INDENT
        if row[2] == "Khan": 
            KhanVotes +=1
        elif row[2] == "Correy":
            CorreyVotes +=1
        elif row[2] == "Li": 
            LiVotes +=1
        elif row[2] == "O'Tooley":
            OtooleyVotes +=1
            
#Create a list for the candidates and votes to store
Candidates = ["Khan", "Correy", "Li","O'Tooley"]
Votes = [KhanVotes, CorreyVotes,LiVotes,OtooleyVotes]

#Put Candidates and Votes list together to create a dictonary - ZIP
dictCandidateVote = dict(zip(Candidates,Votes))
key = max(dictCandidateVote, key=dictCandidateVote.get)

# Print a the summary of the analysis
KhanPercent = (KhanVotes/TotalVotes) *100
CorreyPercent = (CorreyVotes/TotalVotes) * 100
LiPercent = (LiVotes/TotalVotes)* 100
OtooleyPercent = (OtooleyVotes/TotalVotes) * 100

# Print the summary table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {TotalVotes}")
print(f"----------------------------")
print(f"Khan: {KhanPercent:.3f}% ({KhanVotes})")
print(f"Correy: {CorreyPercent:.3f}% ({CorreyVotes})")
print(f"Li: {LiPercent:.3f}% ({LiVotes})")
print(f"O'Tooley: {OtooleyPercent:.3f}% ({OtooleyVotes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

# create new txt file
file = open("ElectionResults.txt","w")

# Write methods to print to Elections_Results_Summary 
file.write(f"Election Results")
file.write("\n")
file.write(f"----------------------------")
file.write("\n")
file.write(f"Total Votes: {TotalVotes}")
file.write("\n")
file.write(f"----------------------------")
file.write("\n")
file.write(f"Khan: {KhanPercent:.3f}% ({KhanVotes})")
file.write("\n")
file.write(f"Correy: {CorreyPercent:.3f}% ({CorreyVotes})")
file.write("\n")
file.write(f"Li: {LiPercent:.3f}% ({LiVotes})")
file.write("\n")
file.write(f"O'Tooley: {OtooleyPercent:.3f}% ({OtooleyVotes})")
file.write("\n")
file.write(f"----------------------------")
file.write("\n")
file.write(f"Winner: {key}")
file.write("\n")
file.write(f"----------------------------")

#close file
file.close()