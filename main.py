import random

def ROCK():
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

def PAPER():
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

def SCISSOR():
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")


num = int(input("\n\n\n1 for Rock, 2 for Paper, 3 for Scissor >>> "))
rand = random.randint(1,3)

if (num == 1 and rand == 1) or (num == 2 and rand == 2) or (num == 3 and rand == 3) : result = "It's tied"
if (num == 1 and rand == 3) or (num == 2 and rand == 1) or (num == 3 and rand == 2) : result = "You won"
if (num == 1 and rand == 2) or (num == 2 and rand == 3) or (num == 3 and rand == 1) : result = "You lost"

def SIGN(a):
    if a == 1: ROCK()
    elif a == 2: PAPER()
    else: SCISSOR()

print("You do")
SIGN(num)
print("Computer do")
SIGN(rand)
print(result)
