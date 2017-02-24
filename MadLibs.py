#Python Mad Libs
#Coded by Adin Biederman on 2/24/17
import time #get sleep dependencies
print("Welcome to Mad Libs, Python Edition!")
print("Please select a story. A: What's For Dinner?, B: Story2, C: Story3")
story = raw_input("Type A, B, or C:   ") #Choose story
print("Story " + story + " selected! Please wait... ")
time.sleep(1)
if story == 'A': #Get word values
    anoun1 = raw_input("Noun: ")
    aperson1 = raw_input("Person in Room: ")
    averb1 = raw_input("Verb: ")
    abody1 = raw_input("Body Part (plural): ")
    aadjective1 = raw_input("Adjective: ")
    anoun2 = raw_input("Noun: ")
    anoun3 = raw_input("Noun: ")
    aplnoun1 = raw_input("Plural Noun: ")
    aliquid1 = raw_input("Liquid type: ")
    aadjective2 = raw_input("Adjective: ")
    anoun4 = raw_input("Noun: ")
    anoun5 = raw_input("Noun: ")
    anoun6 = raw_input("Noun: ")
    aplnoun2 = raw_input("Plural Noun: ")
    aperson2 = raw_input("Person in Room (Female): ")
    anoun7 = raw_input("Noun: ")
    abody2 = raw_input("Body Part (Plural): ")
    print("Done! Preparing your story...")
    time.sleep(1)
    print("It was Thanksgiving, and the scent of succulent roast" + anoun1 + " wafted through my house.") 
    print("'" aperson1 + " it's time to " + averb1 + " !' My mother called. I couldn't wait to get my " + abody1 + " on that " + aadjective1 + " Thanksgiving meal.")
    print("My family sat around the dining-room " + anoun2 + ". The table was laid out with every kind of " + anoun3 + " imaginable.")
    print("
