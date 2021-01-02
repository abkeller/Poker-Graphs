# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 14:47:39 2020

@author: Andy
"""
import pandas as pd
import time
import pygal

def player_data():


    file = 'HH2020-08-17 Poker.txt'

    with open(file, mode='r') as f:
        game = f.read()
        hands = game.split('Hand #')[1:]
        players = {}
        number_of_hands = 0
        for hand in hands:
            number_of_hands += 1
            for x in range(1,11):
                try:
                    player = hand.split('Seat {}: '.format(x))[1].split('(')[0]
                    if player not in players:
                        players[player] = []
                except:
                    pass

        #df = pd.DataFrame(index=players)
        

        for hand in hands:

            for x in range(1,11):
                try:
                    
                    player = hand.split('Seat {}: '.format(x))[1].split('(')[0]
                    chips = int(hand.split('Seat {}: '.format(x))[1].split('(')[1].split(')')[0])
                    players[player].append(chips)

                except:
                   pass

    return  (players, number_of_hands)

    #make_graph()

# def make_graph(line_chart):
#     return line_chart.render_response()

#             #time.sleep(1)
#             hand_number = int(hand.split('-')[1])
#             if hand_number <= 20: 
#                 line_chart.x_labels = map(str, range(0, hand_number))
#             else:
#                 line_chart.x_labels = map(str, range(hand_number - 20, hand_number))
#         line_chart = pygal.Line()
#         line_chart.title = "Chips by Hand"
# # if __name__ == "__main__":
# #     main()