import random


class PrisonersDilemma:
    def __init__(self):
        self.player1_name = None
        self.player2_name = None
        self.player1_score = 0
        self.player2_score = 0
        self.player1_strategy = None
        self.player2_strategy = None
        self.history = []
        self.current_player = 0  # 0 for player 1, 1 for player 2
        self.grim = 0
        self.pav_prob = 1
        self.reactive = 0
        self.reactive_c = 0
        self.reactive_d = 0
        self.memory_one = [0, 0, 0, 0]

    def set_players(self, name1, name2):
        self.player1_name = name1
        self.player2_name = name2

    def set_payoffs(self, weight1: int, weight2: int, weight3: list, weight4: list):
        self.cooperate = weight1
        self.defect = weight2
        self.coop_def = weight3
        self.def_coop = weight4

    def set_strategies(self, strategy1, strategy2):
        self.player1_strategy = strategy1
        self.player2_strategy = strategy2

    def set_reactive(self, y, p, q):
        self.reactive = y
        self.reactive_c = p
        self.reactive_d = q

    def set_memory_one(self, a, b, c, d):
        self.memory_one[0] = a
        self.memory_one[1] = b
        self.memory_one[2] = c
        self.memory_one[3] = d

    def play(self, iterations):
        for i in range(iterations):
            move1 = self.player1_strategy(self)
            move2 = self.player2_strategy(self)

            self.history.append((move1, move2))

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
        return (self.player1_score, self.player2_score)


def tit_for_tat(game):
    if not game.history:
        return 'C'
    return game.history[-1][1 - game.current_player]


def susp_tit_for_tat(game):
    if not game.history:
        return 'D'
    return game.history[-1][1 - game.current_player]


def always_cooperate(game):
    return 'C'


def always_defect(game):
    return 'D'


def random_strategy(game):
    a = random.random()
    if a >= 0.5:
        return 'C'
    return 'D'


def probable_coop(game):
    # Accept the probability from the user
    prob = int(input("Enter the probability"))
    a = random.random()
    if a <= prob:
        return 'C'
    return 'D'


def grim(game):
    if game.grim == 1:
        return 'D'
    game.grim = 1
    return 'C'


def pavlov(game):
    if game.history[-1][0] == game.history[-1][1]:
        return 'C'
    return 'D'


def n_pavlov(game):
    if game.history[-1] == ('D', 'D'):
        game.pav_prob = max(0, game.pav_prob - 2/len(game.history))
    if game.history[-1] == ('C', 'C'):
        game.pav_prob = min(1, game.pav_prob + 1/len(game.history))
    if game.history[-1][game.current_player] == 'D':
        game.pav_prob = min(1, game.pav_prob + 2/len(game.history))
    if game.history[-1][game.current_player] == 'C':
        game.pav_prob = max(0, game.pav_prob - 1/len(game.history))


def reactive(game):
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


# Add more strategies ...
if __name__ == "__main__":
    game = PrisonersDilemma()
    game.set_players("P1", "P2")
    # You can set different strategies here
    game.set_strategies(always_cooperate, tit_for_tat)
    game.play(10)  # Number of iterations
    print(game.display_scores())
