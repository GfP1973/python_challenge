import os
import csv

#set up definition for finding percentages

def vote_percentages(x):
    if x > 0:
        return (round(float((x)/total_vote)*100))
    else:
        print("No Votes")

#create path to data set
electionCSV = os.path.join("election_data.csv")

voter_id = []
cand_name = []

with open(electionCSV, newline="") as csvfile:

    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)

   
#prep the data in the columns
    for row in csvreader:
        voter_id.append(row[0])
        cand_name.append(row[2])


#print(len(voter_id))
#print(len(cand_name))

khan_vote = []
li_vote = []
correy_vote = []
otooley_vote = []

#tally votes

for vote in cand_name:
    if vote == "Khan":
        khan_vote.append(int(1))
    elif vote == "Li":
        li_vote.append(int(1))
    elif vote == "Correy":
        correy_vote.append(int(1))
    elif vote == "O'Tooley":
        otooley_vote.append(int(1))

#get totals for each candidate

sum_khan = sum(khan_vote)
sum_li = sum(li_vote)
sum_correy = sum(correy_vote)
sum_otooley = sum(otooley_vote)
total_vote = int(sum_khan + sum_li+ sum_correy + sum_otooley)

#Output

print("Election Results:")
print("-------------------------------")
print(f"Total Votes:  {total_vote}")
print("-------------------------------")
print(f"Khan:  {vote_percentages(sum_khan)}% ( {sum_khan} )" )
print(f"Li:  {vote_percentages(sum_li)}% ( {sum_li} )" )
print(f"Correy:  {vote_percentages(sum_correy)}% ( {sum_correy} )" )
print(f"O'Tooley:  {vote_percentages(sum_otooley)}% ( {sum_otooley} )" )
print("-------------------------------")

print("Winner:  Khan!")







