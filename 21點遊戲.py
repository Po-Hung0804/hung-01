import random
from sys import exit


class Poke:
    def __init__(self):
        self.cards=[[suit,rank]for suit in "♦♣♥♠" for rank in [1,2,3,4,5,6,7,8,9,10,'J','Q','K']]
        random.shuffle(self.cards)


class Dealer:
    def __init__(self):
        self.cards=Poke().cards
    def give_one_card(self):
        if not self.cards:
            self.cards.append(Poke().cards)
        return self.cards.pop()

class Player:
    def __init__(self,name):
        self.name=name
        self.score=0
        self.points=0
        self.cards_in_hand=[]

    def init(self):
        self.cards_in_hand=[]
        self.points=0

    def now_count(self):
        point=0
        for suit,rank in self.cards_in_hand:
            if rank in ['J','Q','K']:
                rank=10
            point +=rank
        for card in self.cards_in_hand:
            if card[1]==1 and point+10<21:
                self.points=point+10
            else:
                self.points=point
    def is_win(self,player):
        s1=self.points
        s2=player.points
        if s1>s2:
            print(f"玩家{self.name}點數為{s1}電腦玩家{player.name}點數為{s2},玩家{self.name}獲勝!")
            self.score+=1
        elif s1==s2:
            print("平局")
        else:
            print(f"玩家{self.name}點數為{s1}電腦玩家{player.name}點數為{s2},電腦玩家{player.name}獲勝!")
            player.score+=1
    def get(self, *cards):
        for card in cards:
            self.cards_in_hand.append(card)
        self.now_count()


def main(dealer: Dealer,computer: Player,human: Player):


    count = 0
    try:
        while True:
            count+=1
            print(f"比賽第{count}輪開始")
            flag = False
            human.init()
            computer.init()
            for i in range(2):
                human.get(dealer.give_one_card())
                computer.get(dealer.give_one_card())
            print(f"玩家{human.name}手中的牌是{human.cards_in_hand[-2]},{human.cards_in_hand[-1]}")
            print(f"電腦{computer.name}手中的牌是{computer.cards_in_hand[-2]},  ? ")
            if human.points ==21== computer.points:
                print(f"玩家{human.name}和電腦{computer.name}平局")
            elif human.points==21:
                print(f"玩家{human.name}點數為21點, 獲勝!")
                human.score+=1
            else:
                while True:
                    next_card=input("請問是否還要牌, (y/n)")
                    if next_card in ['n','N']:
                        break
                    elif next_card in ['y','Y']:
                        human.get(dealer.give_one_card())
                        print(f"玩家{human.name}得到一張牌{human.cards_in_hand[-1]},玩家手中的牌是{human.cards_in_hand}")
                        if human.points>21:
                            print(f"玩家{human.name}爆掉, 輸了")
                            computer.score+=1
                            flag = True
                            break
                if not flag:
                    while computer.points<17:
                       computer.get(dealer.give_one_card())
                       print(f"電腦{computer.name}得到一張牌{computer.cards_in_hand[1]},電腦手中的牌{computer.cards_in_hand}")
                    if computer.points>21:
                        print(f"玩家{human.name}獲勝!")
                        human.score+=1
                    else:
                        human.is_win(computer)
            print("="*30)
            play_again=input("請輸入,(y/n)")
            if play_again  in ['y','Y']:
                    print(f"玩家{human.name},電腦{computer.name}, 總比分為{human.score}:{computer.score}")
            elif  play_again in ['n','N']:
                print(f"玩家{human.name},電腦{computer.name}, 總比分為{human.score}:{computer.score}")
                if human.score>computer.score:
                  print(f"玩家{human.name} 獲勝!")
                elif human.score<computer.score:
                     print(f"電腦{computer.name}獲勝")
                else:
                    print("平手")
                print("遊戲結束")
                exit(0)
            else:
                print("輸入錯誤, 請從新輸入")
    except Exception:
        print("bug")

    


dealer=Dealer()
computer=Player('Robot')
human=Player('Benson')
main(dealer,computer,human)
          




                


                    
                    

                   
                

    
        








        




        
            



