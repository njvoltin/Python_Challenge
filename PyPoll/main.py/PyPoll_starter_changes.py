# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = "/Users/nickvoltin/Python_Challenge/PyPoll/Resources/election_data.csv"  # Input file path
file_to_output = "/Users/nickvoltin/Python_Challenge/PyPoll/Analysis/election_data.txt"  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates = []  
candidate_votes = {}  


# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0.0
Election_Results = ("Election Results")

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
          
        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1 

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0
        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1


# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print(f"Election_Results")
    txt_file.write(Election_Results + "\n")
    print(". " * 50)
    txt_file.write("." *50 + "\n")
    print(f"Total Votes: {total_votes}")

    # Write the total vote count to the text file
    txt_file.write(f"Total Votes: {total_votes}\n")
    print(". " * 50)
    txt_file.write("." *50 + "\n")

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidate_votes:

        # Get the vote count and calculate the percentage
        votes=candidate_votes[candidate]
        vote_percentage=(votes / total_votes) * 100

        # Update the winning candidate if this one has more votes
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate

        # Print and save each candidate's vote count and percentage
        print(f"{candidate}: {vote_percentage:.3f}% ({votes})")
        txt_file.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")
    print(". " * 50)
    txt_file.write("." *50 + "\n")

    # Generate and print the winning candidate summary

    winning_summary = (
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count}\n"
        f"Winning Percentage: {winning_percentage:.3f}%\n"
        )
    print(winning_summary)
    txt_file.write(winning_summary)
