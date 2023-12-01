import csv
import os
import sys

# Function to record vote in a CSV file.
def record_vote(name: str, vote: str) -> None:
    """
    Records voter name and their vote.

    Args:
        name: Voter name
        vote: Candidate chosen (John or Jane)
    """
    with open('vote_results.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, vote]) # Writing name and vote into CSV file.

# Function to calculate and summarize the votes, then exit the application.
def finish_vote() -> None:
    """
    Finish the voting process, creates summary file.
    """
    with open('vote_results.csv', 'r') as file:
        reader = csv.reader(file)
        votes = list(reader)
        # Count votes for John and Jane as well as total votes
        person1_votes = sum(1 for row in votes if row[1] == 'John')
        person2_votes = sum(1 for row in votes if row[1] == 'Jane')
        total_votes = len(votes)

        # Writing the summary to a new CSV file.
        with open('vote_summary.csv', 'w', newline='') as summary_file:
            writer = csv.writer(summary_file)
            writer.writerow(['Candidate ', 'Total Votes'])
            writer.writerow(['John ', person1_votes])
            writer.writerow(['Jane ', person2_votes])
            writer.writerow(['Total Votes ', total_votes])
    
    # Clean up and remove the individual votes file
    if os.path.exists('vote_results.csv'):
        """
        Deletes the results
        """
        os.remove('vote_results.csv')

    # Exiting the application
    sys.exit()


