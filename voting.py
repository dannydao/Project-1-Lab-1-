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
    # Check if the file exists to prevent rewriting the header
    write_header = not os.path.exists('vote_results.csv')

    with open('vote_results.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        if write_header:
            writer.writerow(['Voter Name', 'Candidate'])

        writer.writerow([name, vote])

# Function to calculate and summarize the votes, then exit the application.
def finish_vote() -> None:
    """
    Finish the voting process, creates summary file.
    """
    with open('vote_results.csv', 'r') as file:
        reader = csv.reader(file)
        votes = list(reader)

        # Exclude header row from count
        total_votes = len(votes) -1 if votes else 0

        # Count votes for John and Jane as well as total votes
        person1_votes = sum(1 for row in votes if row[1] == 'John')
        person2_votes = sum(1 for row in votes if row[1] == 'Jane')

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


