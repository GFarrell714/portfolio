import os
import csv

#joining path
csvpath = os.path.join("Resources", "budget_data.csv")

# open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    # skip header row
    print(f"Header: {csv_header}")

    # Initializing Variable Values
    Profit = []
    Date = []

    #read through each row of data after header
    for rows in csvreader:
        Profit.append(int(rows[1]))
        Date.append(rows[0])

    # find revenue change
    revenue_change = []

    for i in range(1, len(Profit)):
        revenue_change.append((int(Profit[i]) - int(Profit[i-1])))
    
    # calculate average revenue change
    revenue_average = sum(revenue_change) / len(revenue_change)
    
    # calculate total length of months
    total_months = len(Date)

    # greatest increase in revenue
    greatest_increase = max(revenue_change)
    # greatest decrease in revenue
    greatest_decrease = min(revenue_change)


    # print the Results
print("Financial Analysis")

print("....................................................................................")

print(f"Total months: {total_months}")

print(f"Total: ${sum(Profit)}")

print(f"Average Change: ${round(revenue_average)}")

print(f"Greatest Increase in Profits: {Date[revenue_change.index(max(revenue_change))]} ${greatest_increase}")

print(f"Greatest Decrease in Profits: {Date[revenue_change.index(min(revenue_change))]} ${greatest_decrease}")


# output to a text file. '\n' represents a new line to be written

file = open("output.txt","w")

file.write("Financial Analysis" + "\n")

file.write("\n...................................................................................." + "\n")

file.write("\ntotal months: " + str(total_months))

file.write("\nTotal: " + "$" + str(sum(Profit)))

file.write("\nAverage change: " + "$" + str(revenue_average))

file.write("\nGreatest Increase in Profits: " + str(Date[revenue_change.index(max(revenue_change))]) + " " + "$" + str(greatest_increase) + ")")

file.write("\nGreatest Decrease in Profits: " + str(Date[revenue_change.index(min(revenue_change))]) + " " + "$" + str(greatest_decrease) + ")")

file.close()







		



			




