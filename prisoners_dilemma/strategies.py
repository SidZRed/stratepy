import random


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
