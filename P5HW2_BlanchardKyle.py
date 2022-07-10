# Let a user select either addition, subtraction, or exit from a menu. The Addition option asks the user to add two numbers together and tracks guesses until the user guesses correct. The Subtraction option does the same with subtraction instead of addition. Both will ask the user if they want to play again. The exit option will terminate the program.
# 07/10/2022
# CTI-110 P5HW2 - Math Quiz
# Kyle Blanchard

import random

def add_game():
    guesses = 0
    num1 = random.randint(100,999)
    num2 = random.randint(100,999)
    print(f" {num1}",f"+{num2}","____",sep="\n")
    while(True):
        guesses += 1
        answer = int(input("Enter answer: "))
        if(answer == num1+num2):
            print(f"Correct answer! It took you {guesses} guess(es)!")
            break
        elif(answer > num1-num2):
            print("Your answer was too high")
        elif(answer < num1-num2):
            print("Your answer was too low")
            
def sub_game():
    guesses = 0
    num1 = random.randint(100,999)
    num2 = random.randint(100,999)
    print(f" {num1}",f"-{num2}","____",sep="\n")
    while(True):
        guesses += 1
        answer = int(input("Enter answer: "))
        if(answer == num1-num2):
            print(f"Correct answer! It took you {guesses} guess(es)!")
            break
        elif(answer > num1-num2):
            print("Your answer was too high")
        elif(answer < num1-num2):
            print("Your answer was too low")
            
def play_again():
    print("Would you like to play again?")
    while(True):
        answer = input("y/n: ")
        if(answer=="n"):
            return False
        elif(answer=="y"):
            return True
        else:
            print("ERROR: Invalid input, please enter 'y' or 'n'")
            
if __name__=='__main__':
    print("MAIN MENU\n__________________________________________\n1. Adding Random Numbers\n2. Subtracting Random Numbers\n3. Exit\n")
    while(True):
        choice = input("Please choose one of the menu options: ")
        if(choice=="1"):
            add_game()
            if(play_again() == False): 
                break
        elif(choice=="2"):
            sub_game()
            if(play_again() == False):
                break
        elif(choice=="3"):
            break
        else:
            print("ERROR: Choose a valid menu option.")
