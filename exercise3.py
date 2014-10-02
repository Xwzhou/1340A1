#!/usr/bin/env python3
# Does collaboration work?
#lets see if it works
rps_results = {}
rps_results[("Rock", "Paper")] = 2
rps_results[("Rock", "Scissors")] = 1
rps_results[("Paper", "Rock")] = 1
rps_results[("Paper", "Scissors")] = 2
rps_results[("Scissors", "Paper")] = 1
rps_results[("Scissors", "Rock")] = 2

def decide_rps(player1, player2):
    if type(player1) and type(player2) ==str:
        if (player1, player2) in rps_results:
            return rps_results.get((player1, player2))
        elif player1 == player2:
            return 0
        else:
            raise ValueError ("Not Rock, Paper, Scissors")
    else:
        raise TypeError ("Not String")
