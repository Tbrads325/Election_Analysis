# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import os

#Assign a variable for the file to load and the path
#file_to_load = 'Election_Analysis/Resources/election_results.csv'
file_to_load = os.path.join("Resources","election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter
total_votes = 0
# Candidate Options
candidate_options = []
# Declare empty dictionary
candidate_votes = {}

# Winning Candidate and winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

#Print the header row
    headers = next(file_reader)
    print(headers)
#Print each row in the CSV file:
    for row in file_reader:
        # 2. Add to the total vote count
        total_votes += 1
        #Print the candidate name from each row
        candidate_name = row[2]
        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
        #Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
        #Begin tracking the candidate's vote count
            candidate_votes[candidate_name] = 0
        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
#Save the results to our txt file
with open(file_to_save, "w") as txt_file:
    #Print final vote count in terminal.
    election_results = (
        f"\nElection Results\n"
        f"-----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------\n")
    print(election_results, end="")
    #Save the final vote count to the txt file
    txt_file.write(election_results)
    # 3. Print the total votes
    print(total_votes)
    print(candidate_options)
    print(candidate_votes)

    #Determine the percentage of votes for each candidate by looping through the counts
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print the candidate name and percentage of votes
        #print(f"{candidate_name}: recieved {vote_percentage:.1f}% of the vote.")
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        #Determine winning vote count and candidate
        #Determine if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #If true then set winning_count = votes and winning_percentage = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #And, set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name
    winning_candidate_summary = (
        f"-----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-----------------------------\n")
    print(winning_candidate_summary)
    #Save Winning Candidate's Results to txt file
    txt_file.write(winning_candidate_summary)   
    #Using the open() function with the "w" mode we will write data to the file
    #####open(file_to_save,"w")
    # with open(file_to_save, "w") as txt_file:
        
    #Write some data to the file
    #####outfile = open(file_to_save, "w")
    ##### outfile.write("Hello World")

    # #Close File
    ##### outfile.close()
    # Write 3 counties to the file
        # txt_file.write("Counties in the Election\n-------------------------\n")
        # txt_file.write("Arapahoe\nDenver\nJefferson")
