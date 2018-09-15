# import modules
import os
import csv


#import data source
budgetCSV = os.path.join("budget_data.csv")

#set up data storage variable to parse it out
months = []
earnings = []

#read the csv data, seperate it into rows to manipulate, skip the header
with open(budgetCSV, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

#fill the variable with the two data categories
    for row in csvreader:
        months.append(row[0])
        earnings.append(row[1])

earnings = [int(x) for x in earnings]
tot_earn = sum(earnings)

#find the averge change over the period
next_month = earnings.copy()
next_month.pop(0)
next_month = [int(x) for x in next_month]
earnings_delta = []


for period in range(len(next_month)):
    if earnings[period] > 0 and next_month[period] > 0:
        delta = next_month[period]-earnings[period]
        earnings_delta.append(delta)
    elif earnings[period] > 0 and next_month[period] < 0:
        delta = next_month[period] + earnings[period]
        earnings_delta.append(delta)
    elif earnings[period] < 0 and next_month[period] > 0:
        delta = earnings[period] + next_month[period]
        earnings_delta.append(delta)
    elif earnings[period] < 0 and next_month[period] < 0:
        delta= next_month[period] - earnings[period]
        earnings_delta.append(delta)



avg_delta = round(sum(earnings_delta)/len(next_month),)
great_increase = max(earnings_delta)
great_decrease = min(earnings_delta)
great_inc_index = earnings_delta.index(925441)
#print(great_inc_index)
great_dec_index = earnings_delta.index(-927228)
#print(great_dec_index)
great_inc_month = months[great_inc_index]
great_dec_month = months[great_dec_index]



#call our calculations
 
#script output

print("Financial Analysis")
print("-----------------------")
print(f"Total Months:   {len(months)}")
print(f"Total:   ${tot_earn}")
print(f"Average Change:  ${avg_delta}")
print(f"Greatest Icrease in Profits: {great_inc_month} ${great_increase}")
print(f"Greatest Decrease in Profits: {great_dec_month} ${great_decrease}")