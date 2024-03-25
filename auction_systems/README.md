# Auction Models Library

## Overview

This Python library provides implementations of various auction models, including first-price sealed bid, second-price sealed bid, open ascending bid, and open descending bid.

## Files

- `auction_models.py`: Contains functions implementing different auction models.
- `auction_sim.py`: Defines the `Auction` class to conduct auctions using the specified auction type.

## How to Use

1. **Import the Library**:

    ```python
    from auction_models import *
    ```

2. **Instantiate the Auction**:

    Create an instance of the `Auction` class by specifying the auction type.

    ```python
    auction_type = "First price sealed bid"
    auction = Auction(auction_type)
    ```

    Replace `auction_type` with the desired auction type ("First price sealed bid", "Second price sealed bid", "Open ascending bid", or "Open descending bid").

3. **Submit Bids**:

    Use the `submit_bid` method to submit bids to the auction.

    ```python
    auction.submit_bid(100)
    auction.submit_bid(150)
    auction.submit_bid(200)
    ```

    Bids should be submitted as numerical values representing the bid amount.

4. **Conduct the Auction**:

    Call the `conduct_auction` method to determine the winner bid based on the specified auction type.

    ```python
    winner_bid = auction.conduct_auction()
    print("Winner Bid:", winner_bid)
    ```

## Available Auction Types

The following auction types are available in `auction_models.py`:

- First Price Sealed Bid
- Second Price Sealed Bid
- Open Ascending Bid
- Open Descending Bid

## Customization

You can customize the library by modifying the auction models in `auction_models.py` or by adding new auction types. Additionally, you can extend the `Auction` class in `auction_sim.py` to include additional features or functionalities.

## Example

```python
from auction_models import *
from auction_sim import Auction

# Create auction instance
auction_type = "First price sealed bid"
auction = Auction(auction_type)

# Submit bids
auction.submit_bid(100)
auction.submit_bid(150)
auction.submit_bid(200)

# Conduct the auction
winner_bid = auction.conduct_auction()
print("Winner Bid:", winner_bid)
