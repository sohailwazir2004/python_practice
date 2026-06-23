# Build a flashcard quiz using a class! A flashcard has information on both sides,
#  used to help you remember things — usually a question on one side and an answer on the other.
# 1.	Create a class named FlashCard.
# 2.	Inside __init__(), create a dictionary named fruits, 
# where each key is a fruit name and each value is that fruit's color, for example {"Banana": "yellow", "Strawberries": "pink"}.
# 3.	Use the random module to randomly choose one fruit-color pair,
#  and store the fruit name in a variable called fruit and the color in a variable called color.
# 4.	Ask the player to type the color of the chosen fruit.
# 5.	If the answer is correct, print "Correct answer." If it is wrong, print "wrong."
# 6.	Let the player keep playing by asking them to enter 0 to play again.

import random
class FlashCard:
    def __init__(self):
        self.fruits = {
            "Banana": "Yellow",
            "Strawberries": "Pink",
            "Apple": "Red",
            "Orange": "Orange",
            "Grapes": "Green"
        }

    def rand(self):
        fruit,color = random.choice(list(self.fruits.items()))
        print(fruit)
        user_input = input("enter the color of the selected fruit: ")

        if user_input.lower() == color.lower():
            print("correct")
        else:
            print("wrong color for the given fruit!")


obj = FlashCard()

choice = 0
while choice == 0:
    obj.rand()
    choice = int(input("enter 0 to play again! else any number to abort the game!"))

print("game over!")
