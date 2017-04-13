#Python Text-Based adventure game
#By Adin Biederman
import time #get sleep dependencies
print("Welcome to the mystical Python adventure!")
playername = raw_input("Please enter your name: ")
print("Hello" + playername + ". This game will take you through a series of puzzles and challenges.")
beginq = raw_input("Are you ready to begin? Say yes or no: ")
  if beginq == 'yes' or beginq == 'Yes':
    print("OK, then let's go!")
    print("You enter a large cavern, that is completely black.")
    cavern1 = raw_input("Which way do you go? Say North or South: ")
      if cavern1 == 'North' or 'north':
    
  else:
    print("Sorry to hear that. Goodbye!")
    return
