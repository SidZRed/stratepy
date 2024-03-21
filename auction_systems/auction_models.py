def first_price_sealed_bid(bids):
    return max(bids)


def second_price_sealed_bid(bids):
    sorted_bids = sorted(bids, reverse=True)
    return sorted_bids[1] if len(sorted_bids) > 1 else sorted_bids[0]


def open_ascending_bid(bids):
    return max(bids)


def open_descending_bid(bids):
    return min(bids)
