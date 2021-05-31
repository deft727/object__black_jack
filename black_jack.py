import random


class Card:
    def __init__(self, rank:str, suit:str) -> None:
        self.rank = rank
        self.suit = suit
    
    def get_value(self) -> int:
        if self.rank in "ТВДК":
            return 10
        else:
            return " A23456789".index(self.rank)
        
    def get_rank(self) -> str:
        return f"{self.suit} {self.rank}"
    

class DeskCard:
    def __init__(self) -> None:
        _rank = "A23456789ТВДК"
        _suit = "ПБЧК"
        self.__cards = [Card(r,s) for s in _suit for r in _rank]
        random.shuffle(self.__cards)
    
    def get_card(self) -> Card:
        return self.__cards.pop()
    

class Player:
    def __init__(self,name:str) -> None:
        self._hand = []
        self.count = 0
        self.name = name
    
    @property
    def hand(self) -> str:
        return f" Карты в руке {self.name}: {self._hand}; очков - {self.count}"

    @hand.setter
    def hand(self, card:Card) -> None:
        self.count += card.get_value()
        self._hand.append(card.get_rank())


class Dealer(Player):
    def get_cards(self, cards: DeskCard):
        while self.count < 18:
            self.hand = cards.get_card()

    
class Game:
    def __init__(self,player_name:str) -> None:
        self.cards = DeskCard()
        self.player = Player(name=player_name)
        self.dealer = Dealer(name = "Dealer")

    def print(self) -> str:
        return f'\n{self.player.name}:\n{self.player.hand}\n{self.dealer.name}:\n{self.dealer.hand}'

    def check_count(self) -> None:
        if self.player.count > 21:
            print('Вы проиграли ', self.print())
        elif self.dealer.count > 21 and self.player.count <= 21:
            print('Вы победили ', self.print())
        elif self.dealer.count == self.player.count:
            print ('НИЧЬЯ' ,self.print())
        elif self.dealer.count > self.player.count:
            print ('Вы проиграли' ,self.print())
        elif self.dealer.count < self.player.count:
            print ('Вы победили' ,self.print())

    def start(self):
        self.player.hand = self.cards.get_card() 
        self.player.hand = self.cards.get_card() 

        self.dealer.hand = self.cards.get_card() 
        self.dealer.hand = self.cards.get_card() 

        print(self.player.hand)

        while self.player.count < 21:
            answer = input('Карту ннада? y/n: ')
            if answer == 'y':
                self.player.hand = self.cards.get_card()
                print(self.player.hand)
            elif answer == 'n':
                self.dealer.get_cards(self.cards)
                break
            self.check_count()

def main() -> None:
    name = input("Ваше имя: ")
    game = Game(name)
    game.start()


if __name__ == '__main__':
    main()
