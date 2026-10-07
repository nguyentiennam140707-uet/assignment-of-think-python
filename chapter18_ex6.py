# %%add_method_to Deck

def __str__(self):
    return '\n'.join(str(card) for card in self.cards)