import random

elements = {
    0: "rock",
    1: "paper",
    2: "scissors",
}

def draw_rock():
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    
def draw_paper():
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    
def draw_scissors():
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

def draw_element(element):
    if element == "rock":
        draw_rock()
    if element == "paper":
        draw_paper()
    if element == "scissors":
        draw_scissors()

def logic(user_choice, rand_choice):
    if user_choice == rand_choice:
        return 2
    if user_choice == "rock" and rand_choice == "paper":
        return 0
    if user_choice == "paper" and rand_choice == "rock":
        return 1
    if user_choice == "rock" and rand_choice == "scissors":
        return 1
    if user_choice == "scissors" and rand_choice == "rock":
        return 0
    if user_choice == "paper" and rand_choice == "scissors":
        return 0
    if user_choice == "scissors" and rand_choice == "paper":
        return 1

def get_choice(message):
    choice = 3
    while choice > 2 or choice < 0:
        choice = int(input(message))
    return elements[choice]


play = int(input("For how many points you want to play: "))
user_Points = 0
system_Points = 0

while user_Points < play and system_Points < play:
    rand_pick = random.choice(elements)
    print("0 - Rock\n1 - Paper\n2 - Scissors")
    user_choice = get_choice("Enter your Choice: ")
    print("your choice")
    draw_element(user_choice)
    print("my choice")
    draw_element(rand_pick)
    func_out = logic(user_choice, rand_pick)

    if func_out == 1:
        print("You Won")
        user_Points += 1
    elif func_out == 0:
        print("You lose")
        system_Points += 1
    else:
        print("Draw!")
        user_Points += 1
        system_Points += 1

    print("Your Points: ", user_Points, "Opponent Points: ", system_Points)

if user_Points == play:
    print("YOU WON THE BATTLE :) ")
else:
    print("YOU LOST THE BATTLE :(")
