import random

from PycharmProjects.inputfileconversion.venv.uno import wild_cards


class UnoGame:
    def __init__(self, players):
        self.players = players  # all players in the game
        self.deck = self.generate_deck()  # creates draw pile
        self.current_player = random.choice(players)  # whose turn is it?
        self.current_card = self.draw_card()  # the current card at the top of the pile
        self.direction = 1  # moves the order of play forward
        self.winner = None  # no one wins at the start of the turn

    def generate_deck(self):
        colors = ['Red', 'Blue', 'Green', 'Yellow']
        values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Skip', 'Reverse', 'Draw Two']
        wild_cards_set = ['Wild', 'Wild Draw Four']
        uno_deck = [(colors, values) for _ in colors for _ in values] + [(wild_card,) for wild_card in wild_cards_set]
        random.shuffle(uno_deck)
        return uno_deck

    def draw_card(self):
        if len(self.deck) == 0:
            return None
        return self.deck.pop()  # pops out the top card from the draw pile deck at the start of the turn

    def play_turn(self, player, card):  # what happens when a player plays a valid card
        if self.is_valid_card(card):
            self.current_card = card
            self.deck.append(card)
            self.current_player.remove_card(card)
            if len(player.hand) == 1:
                uno_input: str = input('Are you forgetting something? ')
                while uno_input != "uno":
                    penalty_card = self.draw_card()
                    self.current_player.add_card(penalty_card)
                    uno_input = input()
            elif len(player.hand) == 0:
                self.winner = player

    def is_valid_card(self, card):  # checking whether the card played matches the current card on top of the pile or
        # is wild
        return card[0] == self.current_card[0] or card[1] == self.current_card[1] or card[0] == 'Wild' or card[
            0] == 'Wild Draw Four'

    def play_game(self):
        while not self.winner:
            print(f'Current card on top of draw pile is {self.current_card}')
            self.current_player.show_hand()
            print(f"It is now {self.current_player}'s turn. Would you like to play a card from your hand or draw?")
            chosen_card = self.current_player.choose_card(self.current_card)
            if chosen_card is None:
                drawn_card = self.draw_card()  # cheats a little, the drawn card is from the same pile as the current
                # card but is not the same one so that is ok
                if drawn_card:
                    print(f"{self.current_player} drew {drawn_card}")
                    print(f"Would you like to play this card?")
                    if self.is_valid_card(drawn_card):
                        print(f"{self.current_player} played {drawn_card}")
                        self.play_turn(self.current_player, drawn_card)
                    else:
                        self.current_player.add_card(drawn_card)
            elif chosen_card == 'Skip':
                pass
            #elif chosen_card == 'Reverse'
            else:
                if self.play_turn(self.current_player, chosen_card):
                    if self.is_valid_card(chosen_card):
                        print(f"{self.current_player} played {chosen_card}")
            self.current_player = self.get_next_player()
        print(f"Congratulations! {self.current_player} is the winner!")


class UnoPlayer:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def remove_card(self, card):
        self.hand.remove(card)

    def choose_card(self, current_card):
        print(f'Play a card from your hand (color,value):')
        player_input = tuple(x for x in input().split(","))
        valid_cards = [player_input for card in self.hand if
                       card[0] == current_card[0] or card[1] == current_card[1] or card[0] == 'Wild' or card[
                           0] == 'Wild Draw Four']
        if valid_cards:
            return player_input
        else:
            print(f"Not a valid card. Try again: {player_input}")


    def show_hand(self):
        print(f"{self.name}'s hand is: {self.hand}")


class ReverseCard:
    def __init__(self, color):
        self.color = color

    def apply_effect(self, game):
        game.direction *= -1
        print(
            f"{game.current_player} played Reverse {self.color}. Direction is now {'forward' if game.direction == 1 else 'reverse'}.")

    def __str__(self):
        return f"Reverse {self.color}"


class WildCard:
    def __init__(self, chosen_color):
        self.chosen_color = chosen_color

    def apply_effect(self, game):
        self.chosen_color = game.current_player.choose_wild_color()
        print(f"{game.current_player} played Wild. Chose color: {self.chosen_color}.")

    def __str__(self):
        return f"Wild"


class WildDrawFourCard(WildCard):
    def apply_effect(self, game):
        self.chosen_color = game.current_player.choose_wild_color()
        print(f"{game.current_player} played Wild Draw Four. Chose color: {self.chosen_color}.")
        next_player = game.get_next_player()
        next_player.draw_cards(4)
        print(f"{next_player} had to draw 4 cards.")


