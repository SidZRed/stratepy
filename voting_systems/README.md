# Voting Models Library

## Overview

This Python library provides implementations of different voting systems, including plurality voting, instant-runoff voting, approval voting, and Borda count voting.

## Files

- `voting_models.py`: Contains the `Voting` class which defines the various voting systems.
- `voting_sim.py`: Provides a function `simulate_voting` to simulate the voting process using a specified voting system.

## How to Use

1. **Import the Library**:

    ```python
    from voting_models import Voting
    ```

2. **Instantiate the Voting System**:

    Create an instance of the `Voting` class by passing a list of candidates.

    ```python
    voting_system = Voting(['Candidate1', 'Candidate2', 'Candidate3'])
    ```

3. **Simulate Voting**:

    Use the `simulate_voting` function from `voting_sim.py` to simulate the voting process.

    ```python
    from voting_sim import simulate_voting

    num_voters = int(input("Enter the number of voters: "))
    simulate_voting(voting_system.plurality_voting, num_voters)
    ```

    Replace `voting_system.plurality_voting` with the desired voting system method (`instant_runoff_voting`, `approval_voting`, or `borda_count_voting`).

    Each voter's preferences should be entered as a comma-separated list of candidate names.

4. **View Results**:

    After simulating the voting process, the results will be printed, showing the number of votes each candidate received.

## Available Voting Systems

The following voting systems are available in `voting_models.py`:

- Plurality Voting
- Instant Runoff Voting
- Approval Voting
- Borda Count Voting

## Customization

You can customize the library by modifying the voting methods in `voting_models.py` or by adding new voting systems. Additionally, you can adjust the simulation process in `voting_sim.py` to include additional features or functionalities.

## Example

```python
from voting_models import Voting
from voting_sim import simulate_voting

# Create voting system instance
voting_system = Voting(['Candidate1', 'Candidate2', 'Candidate3'])

# Simulate plurality voting
num_voters = int(input("Enter the number of voters: "))
simulate_voting(voting_system.plurality_voting, num_voters)
