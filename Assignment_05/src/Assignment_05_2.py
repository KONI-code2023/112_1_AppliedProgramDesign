import random

class Poker:
    SUITS = ('♠', '♥', '♦', '♣')
    RANKS = ('A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2')

    def __init__(self):
        self.cards = [rank + suit for suit in self.SUITS for rank in self.RANKS]
        self.total_cards = len(self.cards)
        random.shuffle(self.cards)

    def show(self):
        return f"牌堆: {self.cards}"

    def distribute(self, total_players, player_index):
        if self.total_cards % total_players != 0:
            self.total_cards -= self.total_cards % total_players
        start_index = int(player_index * (self.total_cards / total_players))
        end_index = int((self.total_cards / total_players) * (player_index + 1))
        return self.cards[start_index:end_index]

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def show(self):
        return f"{self.name}: {self.cards}"

def main():
    output_path = '..\\docs\\output.txt'

    with open(output_path, 'w', encoding="utf-8-sig") as file:
        file.truncate(0)  # 清空檔案內所有內容

    poker = Poker()

    players = [Player(f"玩家{i+1}") for i in range(4)]
    total_players = len(players)

    for i in range(total_players):
        players[i].cards = poker.distribute(total_players, i)
        print(players[i].show())
        with open(output_path, 'a', encoding="utf-8-sig") as file:
            file.write(players[i].show() + "\n")

if __name__ == "__main__":
    main()
