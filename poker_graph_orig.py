# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 14:47:39 2020

@author: Andy
"""
import pandas as pd

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
        hand_number = hand.split('-')[1]
        df[hand_number] = 0
        for x in range(1,11):

    
            try:
                
                player = hand.split('Seat {}: '.format(x))[1].split('(')[0]
                chips = hand.split('Seat {}: '.format(x))[1].split('(')[1].split(')')[0]
                df.at[player, hand_number] = chips
                
            except:
                pass
    print (df)