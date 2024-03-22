# stratepy: A Python Library for Game Theory Simulations
![image](https://github.com/SidZRed/stratepy/assets/141948050/e2d1c151-3ad7-4500-b544-f3c6a04fcc42)



stratepy is a Python library designed to facilitate simulations of strategies in Game Theory. With a variety of built-in strategies and customizable parameters, it allows for the exploration and analysis of different decision-making scenarios.


[Library](https://pypi.org/project/stratepy/)

## Features

-   Simulate game theory scenarios such as the Prisoner's Dilemma.
-   Implement various strategies for players to adopt.
-   Analyse simulation results to understand the outcomes of different strategies.

## Installation

You can install stratepy via pip:

``` 
$ pip install stratepy
```
## Getting Started

To start using stratepy, you can follow these steps:

1.  **Import the Library**: Import stratepy in your Python script.
#### Python
`import stratepy` 

3.  **Initialize the Game**: Create an instance of the game you want to simulate. Currently, stratepy supports Prisoner's Dilemma.

#### Python
`game = stratepy.PrisonersDilemma()` 

3.  **Set Players and Strategies**: Set the players' names and their strategies.

#### Python

`game.set_players("Player 1", "Player 2")
game.set_strategies(stratepy.always_cooperate, stratepy.tit_for_tat)` 

4.  **Play the Game**: Run the simulation for a specified number of iterations.

#### Python

`game.play(10)` 

5.  **Display Scores**: Retrieve and display the scores of both players.

#### Python

`print(game.display_scores())` 

## Available Strategies

stratepy comes with several predefined strategies for players to adopt:

-   `always_cooperate`: Always cooperate regardless of the opponent's move.
-   `always_defect`: Always defect regardless of the opponent's move.
-   `tit_for_tat`: Cooperate if the opponent cooperated in the last round, otherwise defect.
-   `susp_tit_for_tat`: Defect initially, then mimic the opponent's previous move.
-   `random_strategy`: Randomly choose between cooperation and defection.
-   `probable_coop`: Cooperate with a given probability.
-   `grim`: Cooperate until the opponent defects, then always defect.
-   `pavlov`: Cooperate if the last round had the same moves, otherwise defect.
-   `reactive`: Randomly cooperate with a reactive chance, otherwise defect.
-   `memory_one`: Mimic the opponent's last move with probabilities based on previous outcomes.

## Example

#### Python

`import stratepy`

# Initialize the game

    game = stratepy.PrisonersDilemma()
    game.set_players("P1", "P2")

# Set strategies for players

    game.set_strategies(stratepy.always_cooperate, stratepy.tit_for_tat)

# Play the game for a certain number of iterations

    game.play(10)

# Display scores

    print(game.display_scores())` 

## Created by:
Siddharth Reddy [(@SidZRed)](https://github.com/SidZRed)

## License

This library is released under the Apache-2.0 License. See the LICENSE file for more details.

## Support

For any questions, bug reports, or feature requests, please contact [@SidZRed].


