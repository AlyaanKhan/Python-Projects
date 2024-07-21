import random
from collections import Counter
def voting_simulation(candidates, num_voters):
    votes = []
    candidate_count = Counter({candidate: 0 for candidate in candidates})
    #print(candidate_count)
    for i in range(num_voters):
        vote = random.choice(candidates)
        votes.append(vote)
        candidate_count[vote] += 1
        total_votes = sum(candidate_count.values())
        probabilities = {candidate: count / total_votes for candidate, count in candidate_count.items()}
        print(f"After {i+1} votes: {dict(candidate_count)}")
        print(f"Probabilities: {probabilities}")
names = input("Enter names of candidates: ").split(',')
candidates = []
candidates.extend(names)
num_voters = 5
voting_simulation(candidates, num_voters)
