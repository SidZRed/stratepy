# Prisoner's Dilemma Game Library

## Overview

This Python library provides a framework for simulating the classic game of Prisoner's Dilemma. The game allows two players to repeatedly choose to cooperate or defect, with varying payoff outcomes based on their choices.

## Files

- `game.py`: Contains the `PrisonersDilemma` class which manages the game logic, player strategies, and scoring.
- `strategies.py`: Defines various player strategies that can be used in the game.

## How to Use

1. **Import the Library**:

    ```python
    from game import PrisonersDilemma
    import strategies
    ```

2. **Instantiate the Game**:

    Create an instance of the `PrisonersDilemma` class.

    ```python
    game = PrisonersDilemma()
    ```

3. **Set Player Names**:

    Set the names of the two players.

    ```python
    game.set_players("Player 1", "Player 2")
    ```

4. **Set Payoff Weights**:

    Define the payoff weights for different outcomes of the game. These weights determine the score each player receives based on their moves.

    ```python
    game.set_payoffs(3, 0, [5, 0], [0, 5])
    ```

    Here, the parameters represent:
    - Weight for cooperation (3)
    - Weight for defection (0)
    - Payoff for mutual cooperation ([5, 0])
    - Payoff for mutual defection ([0, 5])

5. **Set Player Strategies**:

    Choose the strategies for each player from the provided strategies in `strategies.py`.

    ```python
    game.set_strategies(strategies.tit_for_tat, strategies.always_defect)
    ```

6. **Play the Game**:

    Specify the number of iterations and let the game run.

    ```python
    game.play(10)  # Play 10 iterations
    ```

7. **Display Scores**:

    After playing, you can retrieve the scores of both players.

    ```python
    player1_score, player2_score = game.display_scores()
    print(f"Player 1 Score: {player1_score}, Player 2 Score: {player2_score}")
    ```

## Available Strategies

The following strategies are available in `strategies.py`:
- Tit For Tat
- Suspicious Tit For Tat
- Always Cooperate
- Always Defect
- Random Strategy
- Probable Cooperation
- Grim
- Pavlov
- N-Pavlov
- Reactive
- Memory One

## Customization

You can customize the game by defining new strategies or modifying existing ones in `strategies.py`. Additionally, you can adjust the parameters of strategies in `game.py` to experiment with different gameplay dynamics.

## Example

```python
from game import PrisonersDilemma
import strategies

# Create game instance
game = PrisonersDilemma()

# Set player names
game.set_players("Alice", "Bob")

# Set payoff weights
game.set_payoffs(3, 0, [5, 0], [0, 5])

# Set player strategies
game.set_strategies(strategies.tit_for_tat, strategies.random_strategy)

# Play the game
game.play(5)

# Display scores
player1_score, player2_score = game.display_scores()
print(f"Alice's Score: {player1_score}, Bob's Score: {player2_score}")
