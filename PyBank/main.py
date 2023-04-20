import os
import csv

#set path for file
budget_data_cvs = os.path.join

#output of the text file
txt_path = "output.txt"

#variables 
total_months = 0
total_rev = 0
rev = []
previous_rev = 0
month_of_change = 0
rev_change = 0
greatest_decrease = ["",9999999]
greatest_increase = ["",0]
rev_change_list = []
rev_avg = 0
counter = 0
diff = []

#open the csv file
with open('budget_data.csv') as csvfile:
    csvreader = csv.DictReader(csvfile)

    #loop to find total months
    for row in csvreader:

    #total number of months 
        total_months += 1

        #total revenue over the entire period 
        total_rev = total_rev + int(row["Profit/Losses"])

        rev.append(int(row["Profit/Losses"]))

        #average change in revenue between months
        rev_change = float(row["Profit/Losses"])- previous_rev
        previous_rev = float(row["Profit/Losses"])
        rev_change_list = rev_change_list + [rev_change]
        month_of_change = [month_of_change] + [row["Date"]]

       #greatest increase in revenue 
        if rev_change > greatest_increase[1]:
            greatest_increase[1] = rev_change
            greatest_increase[0] = row['Date'] 

      #greatest decrease in revenue 
        if rev_change<greatest_decrease[1]:
            greatest_decrease[1] = rev_change
            greatest_decrease[0] = row['Date'] 
           

diff = [rev[x]-rev[x-1] for x in range(1,len(rev))]        
rev_avg = sum(diff)/len(diff)

#change t0 csv
with open(txt_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("------------------------\n")    
    file.write("Total Months: %d\n" % total_months)
    file.write("Total Revenue: $%d\n" % total_rev)
    file.write("Average Revenue Change: $%d\n" % rev_avg)
    file.write("Greatest Increase in Revenue: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1]))
    file.write("Greatest Decrease in Revenue: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))



