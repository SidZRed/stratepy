import random


class PrisonersDilemma:
    def __init__(self):
        self.player1_name = None
        self.player2_name = None
        self.player1_score = 0
        self.player2_score = 0
        self.player1_strategy = None
        self.player2_strategy = None

    def set_players(self, name1, name2):
        self.player1_name = name1
        self.player2_name = name2

    def set_(self, weight1: int, weight2: int, weight3: list, weight4: list):
        self.cooperate = weight1
        self.defect = weight2
        self.coop_def = weight3
        self.def_coop = weight4

    def set_strategies(self, strategy1, strategy2):
        self.player1_strategy = strategy1
        self.player2_strategy = strategy2

    def play(self, iterations):
        history = []
        for i in range(iterations):
            move1 = self.player1_strategy(history, 0)
            move2 = self.player2_strategy(history, 1)

            history.append((move1, move2))

            if move1 == 'C' and move2 == 'C':
                self.player1_score += 3
                self.player2_score += 3
            elif move1 == 'C' and move2 == 'D':
                self.player1_score += 0
                self.player2_score += 5
            elif move1 == 'D' and move2 == 'C':
                self.player1_score += 5
                self.player2_score += 0
            elif move1 == 'D' and move2 == 'D':
                self.player1_score += 1
                self.player2_score += 1

    def display_scores(self):
        return (self.player1_score, self.player2_score)


def tit_for_tat(history, player):
    # Start with cooperate, then mimic opponent's last move
    if not history:
        return 'C'
    return history[-1][1-player]


def susp_tit_for_tat(history, player):
    if not history:
        return 'D'
    return history[-1][1-player]


def always_cooperate(history, player):
    return 'C'


def always_defect(history, player):
    return 'D'


def random(history, player):
    a = random.random()
    if a >= 0.5:
        return 'C'
    return 'D'


def probable_coop(history, player):
    # Accept the probability from the user
    prob = int(input("Enter the probability"))
    a = random.random()
    if a <= prob:
        return 'C'
    return 'D'


if __name__ == "__main__":
    game = PrisonersDilemma()
    game.set_players("P1", "P2")
    # You can set different strategies here
    game.set_strategies(always_cooperate, tit_for_tat)
    game.play(10)  # Number of iterations
    print(game.display_scores())
