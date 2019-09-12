import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

months = []
cash = []

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

for row in csvreader:
        months.append(row[0])
        cash.append(int(row[1]))

total_months = len(months) 
total_cash = 0
avg_change= round((total_cash)/(total_months), 2)
greatest_profit = cash[0]
greatest_loss = cash[0]

for csvpath in range (len(cash)):
    if cash >= greatest_profit:
       greatest_profit = cash
       greatest_month = months
    elif cash <= greatest_loss:
       greatest_loss = cash
       least_month = months
    total_cash += cash

new_csv = zip(total_months, total_cash, avg_change, greatest_profit, greatest_loss)

output_path = os.path.join( 'Resources', 'Financial Analysis.csv')

with open(output_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow("Financial Analysis")
    writer.writerows(new_csv)
    
print(csvfile)



    
