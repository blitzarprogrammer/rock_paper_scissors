import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = ''' 
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to the rock/paper/scissors GAME!")
print("The Game is you vs the COMPUTER. HAHAHAHA")
game_images = [rock,paper,scissors]

user_choice = int(input("Choose 0.Rock 1.Paper 2.Scissors.\n Enter the number not the word:"))
print(game_images[user_choice])

computer_choice = random.randint(0,2)
print(game_images[computer_choice])

print(f"Computer chose {computer_choice}")

if user_choice==0 and computer_choice==2:
    print("YOU WIN")

elif user_choice==2 and computer_choice==0:
    print("Computer Wins")

elif user_choice==2 and computer_choice==1:
    print("YOU WIN")

elif user_choice==1 and computer_choice==0:
    print("YOU WIN")

elif computer_choice>user_choice:
    print("Computer Wins")

elif computer_choice == user_choice:
    print("Its a tie")
else:
    print("You typed an invalid number, YOU LOSER")