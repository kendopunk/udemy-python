import os

running = True
bids = {}


def handle_bid(name, bid):
    bids[name] = bid


def get_auction_winner():
    keys = bids.keys()
    mx = max(bids.values())
    for k in keys:
        if bids[k] == mx:
            print("%s is the auction winner with a bid of $%s" %
                  (k, '{:.2f}'.format(bids[k])))


print("Welcome to the secret auction program.")
while running:
    name = input("$> What is your name?: ")
    bid = float(input("$> What's your bid?: $"))
    handle_bid(name, bid)

    additional = input("$> Are there any other bidders? y/n: ")
    if (additional == 'n'):
        running = False
    os.system('clear')

get_auction_winner()
