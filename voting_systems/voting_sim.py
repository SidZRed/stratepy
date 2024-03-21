from voting_models import Voting

def simulate_voting(voting_system, num_voters):
    for _ in range(num_voters):
        voter_preferences = input("Enter voter preferences (comma-separated list): ").split(',')
        voting_system(voter_preferences)
    print("Voting Results:")
    print(voting_system.votes)