'''
snake, water gun game
1 = snake,
-1 = water,
0 = Gun

The Rules:
Snake vs. Water: Snake drinks water, so the player who chose snake wins. 
Water vs. Gun: Gun drowns in water, so the player who chose water wins. 
Gun vs. Snake: Gun shoots the snake, so the player who chose gun wins. 
Tie: If both players choose the same option, it's a tie, and the round is replayed. 
'''
import random
your_choice = input("Enter your choice: ")
computer_choice = random.choice([-1, 0, 1])

dict = {"s": 1, "w": -1, "g": 0}
rev_dict = {1: "snake", -1: "water", 0: "gun"}

your_choice_int = dict[your_choice]
print(f"Your choise is {rev_dict[your_choice_int]}")
print(f"Computer choise is {rev_dict[computer_choice]}")

if your_choice_int == computer_choice:
    print("It's a tie!")
else:
    if your_choice_int == 1 and computer_choice == -1:
        print("You Win!")
    elif your_choice_int == 1 and computer_choice == 0:
        print("You Lose!")
    elif your_choice_int == 0 and computer_choice == 1:
        print("You Win!")
    elif your_choice_int == 0 and computer_choice == -1:
        print("You Lose!")
    elif your_choice_int == -1 and computer_choice == 1:
        print("You Lose!")
    elif your_choice_int == -1 and computer_choice == 0:
        print("You Win!")
    else:
        print("Something went wrong")