#!/usr/bin/env python3
# Does collaboration work?
#lets see if it works

def decide_rps(player1, player2):
    '''
    Rock Paper Scissors Program.
    Gets Both player's selection, ocmpare and return either
    0 for tie, 1 for player 1 win, 2 for player 2 win.
    :param player1:String Either Rock, Paper, or Scissors
    :param player2:String Either Rock, Paper, or Scissors 
    :return:Integer, either 0, 1, or 2

    '''

    #Dictionary for RPS Results
    rps_results = {}
    rps_results[("Rock", "Paper")] = 2
    rps_results[("Rock", "Scissors")] = 1
    rps_results[("Paper", "Rock")] = 1
    rps_results[("Paper", "Scissors")] = 2
    rps_results[("Scissors", "Paper")] = 1
    rps_results[("Scissors", "Rock")] = 2

    #check if input is both string
    if type(player1) and type(player2) ==str:
        #check if input string is either "Rock, Paper, or Scissors"
        if (player1, player2) in rps_results:
            return rps_results.get((player1, player2))
        elif player1 == player2:
            return 0
        else:
            raise ValueError ("Not Rock, Paper, Scissors")
    else:
        raise TypeError ("Not String")
