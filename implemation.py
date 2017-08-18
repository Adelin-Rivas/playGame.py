def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
   
    isfirsthand=False
    hand={}
    hand2={}
     
    while(True):
        print("") 
        handtype=input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if(handtype in "nre"):
             
            if(handtype=="n"):
                hand=dealHand(HAND_SIZE)
                hand2=hand.copy()
                isfirsthand=True
            elif("e"==handtype):
                break
            else:
                if(handtype=="r" and isfirsthand==False):
                    print("You have not played a hand yet. Please play a new hand first!")
                elif((handtype=="r" and isfirsthand==True)):
                    hand=hand2
             
            if(isfirsthand):
                
                playHand(hand, wordList,HAND_SIZE)     
             
        else:
            print("Invalid command.")
