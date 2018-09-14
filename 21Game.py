import random
import sys
import time

class Card:
    
    #定义扑克牌类，每个对象代表一张扑克盘
    
    def __init__(self,card_type,card_text,card_value):
          
          #card_type str 类型 红桃等
          #card_text str 文本
          #card_value  int 实际点数

          self.card_type = card_type
          self.card_text = card_text
          self.card_value = card_value

class Role: 

    def __init__(self):

        self.cards = []

    def show_card(self):

        for card in self.cards:
            print(card.card_type,card.card_text,sep="",end="")
        print()
    
    def get_value(self,min_or_max):
        
        #最小值判断是否爆牌
        #记录点数和
        sum2 = 0
        #记录A的数量
        A = 0

        for card in self.cards:
            sum2 += card.card_value
            #累计A的数量
            if card.card_type == "A":
                A+=1

        if min_or_max == "max":
            for i in range(A):
                value = sum2 - i *10
                if value <= 21:
                    return value
        return sum2 - A * 10

    def burst(self):
        
        return self.get_value("min") > 21

class CardManage:
        #扑克盘管理类
    def __init__(self):

        self.cards = []
        
        all_card_type="♥♦♠♣"
        
        all_card_text=["A","k","Q","j","10","9","8","7","6","5","4","3","2"]

        all_card_value=[11,10,10,10,9,8,7,6,5,4,3,2]

        for index,card_type in enumerate(all_card_type):
            for card_text in all_card_text:
                card=Card(card_type,card_text,all_card_value[index])
                self.cards.append(card)
        #洗盘
        random.shuffle(self.cards)

    def send_card(self,role,num=1):
         
         for i in range(num):
             role.cards.append(self.cards.pop)