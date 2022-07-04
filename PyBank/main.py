# main.py 
# pybank assignment - Python module -Pradip Raodeo 7/1/2022
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

# expected path .\Resources\budget_data.csv
#print(csvpath)
v_total_months = 0
v_total_amount = 0
v_average_change = 0
v_total_change = 0
v_prev_row_amount = 0
v_greatest_increase = 0
v_greatest_increase_month = " "
v_greatest_decrease = 0
v_greatest_decrease_month = " "
# Open the CSV
with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip first row as data set has header
    csv_header = next(csvreader)
    v_row_count = 0
    # Loop through and count # of months, also total amount 
    for row in csvreader:
        v_total_months += 1
        v_total_amount += int(row[1])
        v_row_count += 1
        if v_row_count == 1: # for the first row total change will be zero but store row amount
            v_total_change = 0
            v_prev_row_amount = int(row[1])
            v_greatest_increase = int(row[1])
            v_greatest_increase_month = row[0]
            v_greatest_decrease = int(row[1])
            v_greatest_decrease_month = row[0]
        else: 
            # for rows > 1 store the cumulative values of differnces CurrentRow minus PreviousRow
            v_total_change +=  (int(row[1]) - v_prev_row_amount )
            if v_greatest_increase <   (int(row[1]) - v_prev_row_amount ):
                v_greatest_increase = (int(row[1]) - v_prev_row_amount )
                v_greatest_increase_month = row[0]

            if v_greatest_decrease >   (int(row[1]) - v_prev_row_amount ):
                v_greatest_decrease = (int(row[1]) - v_prev_row_amount )
                v_greatest_decrease_month = row[0]

            v_prev_row_amount = int(row[1])

            #print("average change for row " + str(v_row_count) + " is " + str(v_total_change ))  

    v_average_change = v_total_change/(v_row_count-1) # calculate average change , you have count one row less
    
    print("Financial Analysis")
    print("-------------------")
    print("Total Months: "+ str(v_total_months))
    print("Total: " + str(round(v_total_amount,2)))
    print(f"Average Change:  {v_average_change:.2f}" )  
    print("Greatest Increase in Profits: " + v_greatest_increase_month + " ($ " + str(v_greatest_increase)+")" )
    print("Greatest Decrease in Profits: " + v_greatest_decrease_month + " ($ " + str(v_greatest_decrease)+")" )

# write analysis to file
# Set variable for output file
output_file = os.path.join('.', 'analysis',"pybank_analysis.txt")

#expected out put file path .\analysis\pybank_analysis.txt
#print(output_file)

#  Open the output file
with open(output_file, "w") as datafile:
    print("Financial Analysis", file=datafile)
    print("-------------------", file=datafile)
    print("Total Months: "+ str(v_total_months), file=datafile)
    print("Total: " + str(round(v_total_amount,2)), file=datafile)
    print(f"Average Change:  {v_average_change:.2f}" , file=datafile)  
    print("Greatest Increase in Profits: " + v_greatest_increase_month + " ($ " + str(v_greatest_increase)+")" , file=datafile )
    print("Greatest Decrease in Profits: " + v_greatest_decrease_month + " ($ " + str(v_greatest_decrease)+")" , file=datafile)


