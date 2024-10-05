# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
csv_file = "/users/nickvoltin/Python_Challenge/PyBank/Resources/budget_data.csv"  # Input file path
budget_data = os.path.join("PyBank", "analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
average_change = 0
greatest_increase = {"month": "", "amount": 0}
greatest_decrease = {"month": "", "amount": 0}
months = []
net_changes = []
previous_net = None

# Open and read the csv
with open(csv_file) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract the first row
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_net = int(first_row[1])

    # Loop through the rest of the rows
    for row in reader:
        # Track the total months and net amount
        total_months += 1
        total_net += int(row[1])

        # Calculate net change from the previous month
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_changes.append(net_change)
        months.append(row[0])

        # Track the greatest increase and decrease
        if net_change > greatest_increase["amount"]:
            greatest_increase = {"month": row[0], "amount": net_change}

        if net_change < greatest_decrease["amount"]:
            greatest_decrease = {"month": row[0], "amount": net_change}

# Calculate the average change
average_change = sum(net_changes) / len(net_changes)

# Output the results
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['month']} (${greatest_increase['amount']})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['month']} (${greatest_decrease['amount']})\n"
)

# Print the results
print(output)

# Save the results to the text file
with open(budget_data, "w") as txt_file:
    txt_file.write(output)