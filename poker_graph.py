# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 14:47:39 2020

@author: Andy
"""
import pandas as pd
import time
import pygal

def main():


    file = 'HH2020-08-17 Poker.txt'

    with open(file, mode='r') as f:
        game = f.read()
        hands = game.split('Hand #')[1:]
        players = []
        for hand in hands:
            for x in range(1,11):
                try:
                    player = hand.split('Seat {}: '.format(x))[1].split('(')[0]
                    if player not in players:
                        players.append(player)
                except:
                    pass
            

        df = pd.DataFrame(index=players)
        
        for hand in hands:
           #time.sleep(1)
            hand_number = hand.split('-')[1]
            df[hand_number] = 0
            for x in range(1,11):

        
                try:
                    
                    player = hand.split('Seat {}: '.format(x))[1].split('(')[0]
                    chips = hand.split('Seat {}: '.format(x))[1].split('(')[1].split(')')[0]
                    df.at[player, hand_number] = chips
                    
                except:
                    pass

            #print  (df)

    make_graph()

def make_graph():
    line_chart = pygal.HorizontalLine()
    line_chart.title = 'Browser usage evolution (in %)'
    line_chart.x_labels = map(str, range(2002, 2013))
    line_chart.add('Firefox', [None, None,    0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
    line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
    line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
    line_chart.range = [0, 100]
    line_chart.render()



    print(__name__)
if __name__ == "__main__":
    main()