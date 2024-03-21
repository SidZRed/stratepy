class Voting:
    def __init__(self, candidates):
        self.candidates = candidates
        self.votes = {candidate: 0 for candidate in candidates}

    def plurality_voting(self, voter_preferences):
        for preference in voter_preferences:
            if preference in self.candidates:
                self.votes[preference] += 1
                break

    def instant_runoff_voting(self, voter_preferences):
        while True:
            for preference in voter_preferences:
                if preference in self.candidates:
                    self.votes[preference] += 1
                    break
            lowest_candidate = min(self.votes, key=self.votes.get)
            if self.votes[lowest_candidate] > sum(self.votes.values()) / 2:
                break
            del self.votes[lowest_candidate]

    def approval_voting(self, voter_preferences):
        for preference in voter_preferences:
            for candidate in preference:
                if candidate in self.candidates:
                    self.votes[candidate] += 1

    def borda_count_voting(self, voter_preferences):
        for i, preference in enumerate(voter_preferences):
            for j, candidate in enumerate(preference):
                if candidate in self.candidates:
                    self.votes[candidate] += len(preference) - j
