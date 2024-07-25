import random
from collections import Counter

def voting_simulation(candidates, num_voters):
    votes = []
    candidate_count = Counter({candidate: 0 for candidate in candidates})
    predicted_winner = random.choice(candidates)
    print(f"Initially Predicted Winner (based on uniform probability): {predicted_winner}\n")

    for i in range(num_voters):
        vote = random.choice(candidates)
        votes.append(vote)
        candidate_count[vote] += 1
        total_votes = sum(candidate_count.values())
        probabilities = {candidate: count / total_votes for candidate, count in candidate_count.items()}
        print(f"After {i+1} votes: {dict(candidate_count)}")
        print(f"Probabilities: {probabilities}\n")

    actual_winner = max(candidate_count, key=candidate_count.get)
    print(f"Actual Winner: {actual_winner}")
    print(f"Was the predicted winner correct? {'Yes' if predicted_winner == actual_winner else 'No'}")

names = input("Enter names of candidates: ").split(',')
candidates = [name.strip() for name in names]
num_voters = int(input("ENter number of voters: "))

voting_simulation(candidates, num_voters)
