from __future__ import annotations
import random


class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = []


class Card:
    def __init__(self, color: str, value: str):
        self.color = color
        self.value = value

    def play_card(self, card: Card) -> bool:
        return self.color == card.color or self.value == card.value

    def __str__(self) -> str:
        return f"{self.color}{self.value}"

    def __repr__(self) -> str:
        return f"{self.color}{self.value}"



class Deck:
    def __init__(self):
        self.colors = ['🟥', '🟦', '🟩', '🟨']
        self.default_cards = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🚫', '🔄', '➕2️⃣']
        self.special_cards = ['🌈', '➕4️⃣']
        self.cards_in_deck = self._generate_deck()

    def _generate_zeros(self) -> list[Card]:
        return [(Card(color=color, value='0️⃣')) for color in self.colors]


    def _generate_special_cards(self) -> list[Card]:
        cards = []
        for card in self.special_cards:
            for n in range(4):
                cards.append(Card(color='⬜️', value=card))

        return cards

    def _generate_default_cards(self) -> list[Card]:
        cards = []
        for n in range(2):
            for card in self.default_cards:
                for color in self.colors:
                    cards.append(Card(color=color, value=card))

        return cards

    def _generate_deck(self) -> list[Card]:
        cards = []
        cards.extend(self._generate_zeros())
        cards.extend(self._generate_special_cards())
        cards.extend(self._generate_default_cards())

        random.shuffle(cards)

        return cards

    @property
    def amount(self) -> int:
        return len(self.cards_in_deck)


    def deal_cards(self, players: list[Player], amount: int=7) -> None:
        for i in range(amount):
            for player in players:
                card_from_deck = self.cards_in_deck.pop(0)
                player.hand.append(card_from_deck)

deck = Deck()

rick = Player('Rick')
anke = Player('Anke')

deck.deal_cards([rick, anke])

print(rick.hand)
print(anke.hand)
print(f"Dealt cards, cards remaining: {deck.amount}")
