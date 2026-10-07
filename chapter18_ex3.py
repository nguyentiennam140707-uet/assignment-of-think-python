from collections import defaultdict
def partition(self):
    hands = defaultdict(PokerHand)
    for card in self.cards:
        hands[card.suit].add_card(card)
    return hands