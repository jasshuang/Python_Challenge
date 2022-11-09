import csv
import os

rowcount = 0
total = 0 
changes = []
#prev_revenue = 0
month = []

#open csv file
with open('budget_data.csv', 'r') as file:
    reader = csv.reader(file, delimiter= ",")

    #skip and print the header
    header = next(reader)

    firstrow = next(reader)

    prev_revenue = int(firstrow[1])

    
    for row in reader:
        #get the number of total months
        rowcount +=1 

        print(f"{row}")

        #get sum of profit /loss
        total = total + int(row[1]) 

        #get revenue change from the previous month
        revenue_change = int(row[1])-prev_revenue
    

        # set previou revenue to the current  month
        prev_revenue = int(row[1]) 

        #add revenue changes to the list
        changes.append(revenue_change) 

        #create a month list for calculating the greatest increase/decrease months
        month.append(row[0])


        
average = sum(changes)/len(changes)
max_profit = max(changes)
max_month = month[changes.index(max(changes))]
min_profit = min(changes)
min_month = month[changes.index(min(changes))]


#print out the output lines 
print("Finalcial Analysis")
print("----------------------------------------")
print(f'Total Months: {rowcount}')
print(f'Total: {total}')
print(f'Average: {average}')
print(f"Greatest Increase in Profits: {max_month} , {max_profit}" ) 
print(f"Greatest Decrease in Profits: {min_month} , {min_profit}" )



 # save the output file path
output_file = os.path.join("output.txt")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w") as pypoll_output:
    writer = csv.writer(pypoll_output)

    writer.writerow(["Finalcial Analysis"])
    writer.writerow(["----------------------------------------"])
    writer.writerow([f'Total Months: {rowcount}'])
    writer.writerow([f'Total: {total}'])
    writer.writerow([f'Average: {average}'])
    writer.writerow([f"Greatest Increase in Profits: {max_month} , {max_profit}" ]) 
    writer.writerow([f"Greatest Decrease in Profits: {min_month} , {min_profit}" ])



