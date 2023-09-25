# Modules
import os
import csv
import sys
# Set path for file
csvpath = os.path.join(os.getcwd(),"Resources", "budget_data.csv")

# Declaring variables
total_months = 0
net_change = 0
prev_profLossValue = 0
greatIncreaseinProfit = 0 
greatIncreaseinProfitMonth = ("") 
currProfitORLoss = 0 
greatDecreaseInLoss = 0
greatDecreaseInLossMonth = ("")
net_total = 0


# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile)
    # Loop through
    for col in csvreader:
 
  
        # Condition Execute after 1st row only
        if total_months > 0:
            # Calcuating change in profit/Loss
            currProfitORLoss =  int(col[1]) - prev_profLossValue
            net_change = net_change + currProfitORLoss
    
        # Calculating greatest increase in profit
        if greatIncreaseinProfit < currProfitORLoss:
            greatIncreaseinProfit = currProfitORLoss
            greatIncreaseinProfitMonth = col[0]

        # Calculating greatest decrease in profit        
        if greatDecreaseInLoss > currProfitORLoss:
            greatDecreaseInLoss = currProfitORLoss
            greatDecreaseInLossMonth = col[0]

        # Stroing previsous row profit/loss value to calculate change
        prev_profLossValue = int(col[1]) 

        total_months = total_months + 1
        net_total = net_total+int(col[1])


    # Creating txt file and redirecting output to it
    old_print = print
    log_file = open("output.txt", "w")
    print = lambda *args, **kw: old_print(*args, **kw) or old_print(*args, file=log_file, **kw)


    # Displaying results
    print("Financial Analysis\n")
    print("----------------------------\n")    
    print ("Total Months: "+str(total_months)+"\n")
    print ("Total: $"+str(net_total)+"\n")
    print("Average Change: $"+str(net_change/(total_months-1))+"\n")
    print("Greatest increase in Profits: "+str(greatIncreaseinProfitMonth)+" ($"+str(greatIncreaseinProfit)+")\n")
    print("Greatest Decrease in Profits: "+str(greatDecreaseInLossMonth)+" ($"+str(greatDecreaseInLoss)+")")

    # Closing File
    log_file.close()
