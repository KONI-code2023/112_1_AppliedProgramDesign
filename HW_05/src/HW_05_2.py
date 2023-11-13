import random 

class Poker:
    __SUIT = ('♠', '♥', '♦', '♣')
    __RANK = ('A', 'K', 'Q', 'J', '10', '9', 
             '8', '7', '6', '5', '4', '3', '2')
    
    def __init__(self):
        self.cards = []
        for suit in self.__SUIT:
            for rank in self.__RANK:
                self.cards.append(rank + suit)
        self.TC = len(self.cards)                   #總牌數
        random.shuffle(self.cards)                  #洗牌

    def show(self):
        return f"重新洗牌: {self.cards}"
    
    def distribute(self, TPP, p):
        if self.TC % TPP != 0:                      #讓所有玩家手牌數一致
            self.TC -= self.TC % TPP
        return self.cards[int(0+p * (self.TC/TPP)) : int((self.TC/TPP) * (p+1))]

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def show(self):
        return f"{self.name}: {self.cards}"
    
def main():
    path = '..\\docs\\output.txt'

    with open(path,'a',encoding="utf-8-sig") as f:               
            f.truncate(0)                #清空txt檔案內所有內容

    poker = Poker()

    players = [
                Player("玩家1"), 
                Player("玩家2"), 
                Player("玩家3"),
                Player("玩家4")
              ]
    
    TPP = len(players)                  #玩家人數

    for i in range(TPP):
        players[i].cards = (poker.distribute(TPP, i))
        print(players[i].show())
        with open(path,'a',encoding="utf-8-sig") as f:
            f.writelines(players[i].show())
            f.writelines("\n")
        
    f.closed 

if __name__ == "__main__":
        main()