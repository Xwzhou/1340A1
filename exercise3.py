#!/usr/bin/env python3
# Does collaboration work?
# lets see if it works
def decide_rps(player1, player2):
    """(str,str)->int
    get players' input
    validate input type and value
    :param player1 and player2 are input by users as strings
    :signs is a list for possible inputs
    :result is a list for pairs regarding on winning decision

    """
    signs = ["Rock", "Paper", "Scissors"]

    #catergorizing results by adding up strings
    result = player1 + player2
    player1_win=["RockScissors","ScissorsPaper","PaperRock"]
    player2_win=["RockPaper","ScissorsRock","PaperScissors"]
    tie=["RockRock","ScissorsScissors","PaperPaper"]

    # check input type and value
    if type(player1) == str and type(player2) == str:
        if player1 in signs and player2 in signs:
            if result in player1_win:
                return 1
            elif result in player2_win:
                return 2
            elif result in tie:
                return 0
        else:
            raise ValueError("the value of input is not valid")
         #decision making

    else:
        raise TypeError("the type of input is not valid")


    # get input into pair



