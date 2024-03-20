import random


class PrisonersDilemma:
    def __init__(self):
        # Initialize variables
        self.player1_name = None
        self.player2_name = None
        self.player1_score = 0
        self.player2_score = 0
        self.player1_strategy = None
        self.player2_strategy = None
        self.history = []
        self.current_player = 0  # 0 for player 1, 1 for player 2

        # Strategy-specific parameters
        self.grim = 0
        self.pav_prob = 1
        self.reactive = 0
        self.reactive_c = 0
        self.reactive_d = 0
        self.memory_one = [0, 0, 0, 0]

    def set_players(self, name1, name2):
        # Set player names
        self.player1_name = name1
        self.player2_name = name2

    def set_payoffs(self, weight1: int, weight2: int, weight3: list, weight4: list):
        # Set payoff weights
        self.cooperate = weight1
        self.defect = weight2
        self.coop_def = weight3
        self.def_coop = weight4

    def set_strategies(self, strategy1, strategy2):
        # Set player strategies
        self.player1_strategy = strategy1
        self.player2_strategy = strategy2

    def set_reactive(self, y, p, q):
        # Set reactive strategy parameters
        self.reactive = y
        self.reactive_c = p
        self.reactive_d = q

    def set_memory_one(self, a, b, c, d):
        # Set memory-one strategy parameters
        self.memory_one[0] = a
        self.memory_one[1] = b
        self.memory_one[2] = c
        self.memory_one[3] = d

    def play(self, iterations):
        # Play the game for a certain number of iterations
        for i in range(iterations):
            move1 = self.player1_strategy(self)
            move2 = self.player2_strategy(self)

            self.history.append((move1, move2))

            # Update scores based on moves
            if move1 == 'C' and move2 == 'C':
                self.player1_score += self.cooperate
                self.player2_score += self.cooperate
            elif move1 == 'C' and move2 == 'D':
                self.player1_score += self.coop_def[0]
                self.player2_score += self.coop_def[1]
            elif move1 == 'D' and move2 == 'C':
                self.player1_score += self.def_coop[0]
                self.player2_score += self.def_coop[1]
            elif move1 == 'D' and move2 == 'D':
                self.player1_score += self.defect
                self.player2_score += self.defect

            self.current_player = 1 - self.current_player

    def display_scores(self):
        # Return scores of both players
        return (self.player1_score, self.player2_score)


# Strategies for player actions
def tit_for_tat(game):
    # Cooperate if opponent cooperated in the last round, otherwise defect
    if not game.history:
        return 'C'
    return game.history[-1][1 - game.current_player]


def susp_tit_for_tat(game):
    # Defect initially, then mimic opponent's previous move
    if not game.history:
        return 'D'
    return game.history[-1][1 - game.current_player]


def always_cooperate(game):
    # Always cooperate
    return 'C'


def always_defect(game):
    # Always defect
    return 'D'


def random_strategy(game):
    # Randomly choose between cooperation and defection
    if random.random() >= 0.5:
        return 'C'
    return 'D'


def probable_coop(game):
    # Cooperate with a given probability
    prob = int(input("Enter the probability"))
    if random.random() <= prob:
        return 'C'
    return 'D'


def grim(game):
    # Cooperate until opponent defects, then always defect
    if game.grim == 1:
        return 'D'
    game.grim = 1
    return 'C'


def pavlov(game):
    # Cooperate if last round had the same moves, otherwise defect
    if game.history[-1][0] == game.history[-1][1]:
        return 'C'
    return 'D'


def n_pavlov(game):
    # Adjust probability based on previous round's outcome
    if game.history[-1] == ('D', 'D'):
        game.pav_prob = max(0, game.pav_prob - 2/len(game.history))
    if game.history[-1] == ('C', 'C'):
        game.pav_prob = min(1, game.pav_prob + 1/len(game.history))
    if game.history[-1][game.current_player] == 'D':
        game.pav_prob = min(1, game.pav_prob + 2/len(game.history))
    if game.history[-1][game.current_player] == 'C':
        game.pav_prob = max(0, game.pav_prob - 1/len(game.history))


def reactive(game):
    # Randomly cooperate with a reactive chance, otherwise defect
    a = random.random()
    if not game.history:
        if a <= game.reactive:
            return 'C'
        return 'D'
    if game.history[-1][1-game.current_player] == 'C':
        if a <= game.reactive_c:
            return 'C'
        return 'D'
    if a <= game.reactive_d:
        return 'D'
    return 'C'


def memory_one(game):
    # Mimic opponent's last move with probabilities based on previous outcomes
    a = random.random()
    if not game.history:
        return 'C'
    if game.history[-1] == ('C', 'C'):
        if a <= game.memory_one[0]:
            return 'C'
        return 'D'
    if game.history[-1] == ('D', 'D'):
        if a <= game.memory_one[1]:
            return 'C'
        return 'D'
    if game.history[-1] == ('C', 'D'):
        if a <= game.memory_one[2]:
            return 'C'
        return 'D'
    if a <= game.memory_one[3]:
        return 'C'
    return 'D'


if __name__ == "__main__":
    # Initialize the game
    game = PrisonersDilemma()
    game.set_players("P1", "P2")
    # Set strategies for players
    game.set_strategies(always_cooperate, tit_for_tat)
    # Play the game for a certain number of iterations
    game.play(10)
    # Display scores
    print(game.display_scores())
