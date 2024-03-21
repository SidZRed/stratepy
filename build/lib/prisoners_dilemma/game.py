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
