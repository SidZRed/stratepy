from auction_models import *


class Auction:
    def __init__(self, auction_type):
        self.auction_type = auction_type
        self.bids = []

    def submit_bid(self, bid):
        self.bids.append(bid)

    def conduct_auction(self):
        if self.auction_type == "First price sealed bid":
            winner_bid = first_price_sealed_bid(self.bids)
        elif self.auction_type == "Second price sealed bid":
            winner_bid = second_price_sealed_bid(self.bids)
        elif self.auction_type == "Open ascending bid":
            winner_bid = open_ascending_bid(self.bids)
        elif self.auction_type == "Open descending bid":
            winner_bid = open_descending_bid(self.bids)
        else:
            raise ValueError("Invalid auction type")

        return winner_bid
