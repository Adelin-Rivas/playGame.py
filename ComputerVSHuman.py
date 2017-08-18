// create  rpogram that use a dicctionary
// to play a game agaist a human.
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
          But if no hand was played, output "You have not played a hand yet. 
          Please play a new hand first!"
        
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    isfirsthand=False
    hand={}
    hand2={}
     
    isfirsthand=False
    hand={}
    hand2={}
    ask=True
     
    while(True):
        if(ask):
            print("") 
            handtype=input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
             
            if( not isfirsthand and (handtype== "r") ):
                print("You have not played a hand yet. Please play a new hand first!")

            elif (isfirsthand and (handtype=="r")):
                hand=hand2
                ask=False
                
                
            
            elif(handtype=="n"):
                hand=dealHand(HAND_SIZE)
                hand2=hand.copy()
                isfirsthand=True
                ask=False
            elif(handtype=="e"):
                break
                 
            else:
                print("Invalid command.")
            


        if( isfirsthand and (handtype in "nre") and (not ask) ):
            
            
            playertype=input("Enter u to have yourself play, c to have the computer play:")

            if(playertype=="u"):
                playHand(hand, wordList, HAND_SIZE)
                ask=True
            elif(playertype=="c"):
                compPlayHand(hand, wordList,HAND_SIZE )
                ask=True
            else:
                print("Invalid command.")
