class PokerHand(Hand):
    '''Represents a poker hand.'''
    def __init__(self, cards):
        self.cards = cards

    def get_suit_counts(self):
        counter = {}

        for card in self.cards:
            key = card.suit
            counter[key] = counter.get(key, 0) + 1
        return counter
    
    def get_rank_counts(self):
        counter = {}

        for card in self.cards:
            key = card.rank
            counter[key] = counter.get(key, 0) + 1
        return counter
    
    # Codeveloped with the Virtual Assistant(Copilot)
    def has_flush(self):
        suit_count = self.get_suit_counts()

        return any(count == 5 for count in suit_count.values())
    
    def has_straight(self):
        cards = [card.rank for card in self.cards]
        cards.sort()

        count = 0
        rank = cards[0]

        for i in range(len(cards)):
            card_rank = cards[i]
            if card_rank == rank + 1:
                count += 1
                rank = card_rank
                if count >= 4:
                    return True
            else:
                count = 0
                rank = card_rank
        
        return False
    
    def has_straight_flush(self):
        if self.has_straight() and self.has_flush():
            return True
        return False
    
    def has_pair(self):
        rank_counts = self.get_rank_counts()
        return any(count == 2 for count in rank_counts.values())
    
    def has_full_house(self):
        rank_count = self.get_rank_counts()
        return any(count == 2 for count in rank_count.values()) and any(count == 3 for count in rank_count.values())