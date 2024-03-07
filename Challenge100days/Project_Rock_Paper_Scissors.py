rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
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

#Write your code below this line 👇
import random

player=input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n")

player=int(player)
computer=random.randint(0,2)

game=[rock, paper, scissors]


print(game[player])
#Rock wins against scissors.
#Scissors win against paper.
#Paper wins against rock.
print(f"Computer chose: {game[computer]}")

if (player==0 and computer==2) or (player==2 and computer==1) or (player==1 and computer==1):
  print("You win")
elif (player==computer):
  print ("Tie")
else:
  print ("You lose")