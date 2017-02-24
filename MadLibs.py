#Python Mad Libs
import time
print("Welcome to Mad Libs, Python Edition!")
print("Please select a story. A: Story1, B: Story2, C: Story3")
story = raw_input("Type A, B, or C:   ")

print("Story " + story + " selected! Please wait... ")
time.sleep(1)
if story == 'A':
    noun1 = raw_input("Noun? ")
    verb1 = raw_input("Verb? ")
    print("So, you are already " + verb1 + " years old, " + noun1 + "!")
