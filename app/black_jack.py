import random
from typing import Tuple, List, Dict

class BlackJack:
    suits = '♠ ♥ ♦ ♣'.split()
    cards = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    card = Tuple[str, str]
    pack = List[card]

    def make_pack(self, aleatory: bool = False) -> pack:
        pack = [(card, suit) for card in self.cards for suit in self.suits]
        if aleatory:
            random.shuffle(pack)
        return pack
    
    def share_pack(self, pack: pack) -> Tuple[pack, pack, pack, pack]:
        return (pack[0::4], pack[1::4], pack[2::4], pack[3::4])
    
    def play(self) -> None:
        cards = self.make_pack(aleatory=True)
        players: List[str] = 'p1 p2 p3 p4'.split()
        hands: Dict [str, self.make_pack()] = {player: hand for player, hand in zip(players, self.share_pack(cards))}

        for player, cards in hands.items():
            card = ' '.join(f'{player}{card}' for (player, card) in cards)
            print(f'{player}: {card}')



back_jack = BlackJack().play()
