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
    signs = ["rock", "paper", "scissors"]

    player1 = input("Hi,player 1,please input your sign")
    player2 = input("Hi,player 2,please input your sign")

    # check input type and value
    if type(player1) == str:
        if player1 in signs:
            if type(player2) == str:
                if player2 in signs:


                else:
                     raise ValueError("the value of input is not valid")
            else:
                raise TypeError("the type of input is not valid")
        else:
            raise ValueError("the value of input is not valid")
    else:
        raise TypeError("the type of input is not valid")


    # get input into pair

    result = player1 + player2
    player1_win=["rockscissors","scissorspaper","paperrock"]
    player2_win=["rockpaper","scissorsrock","paperscissors"]
    tie=["rockrock","scissorsscissors","paperpaper"]

    #decision making
    if result in player1_win:
        return 1
    elif result in player2_win:
        return 2
    elif result in tie:
        return 0
