import random
print("Welcome to Rock Paper Scissors Game.")

computer = ["Rock","Paper","Scissors"]
num = random.randint(0,2)
user = input("Enter Your Choice Rock, Paper or Scissor\n").capitalize()
if user == "Rock" and computer[num]== "Rock":
    print(f"Computer : {computer[num]}")
    print("Drow")
elif user == "Rock" and computer[num]== "Paper":
    print(f"Computer : {computer[num]}")
    print("Lose")
elif user == "Rock" and computer[num]== "Scissor":
    print(f"Computer : {computer[num]}")
    print("Win!")
elif user == "Paper" and computer[num]== "Rock":
    print(f"Computer : {computer[num]}")
    print("Win!")
elif user == "Paper" and computer[num]== "Paper":
    print(f"Computer : {computer[num]}")
    print("Drow")
elif user == "Paper" and computer[num]== "Scissor":
    print(f"Computer : {computer[num]}")
    print("Lose!")
elif user == "Scissor" and computer[num]== "Rock":
    print(f"Computer : {computer[num]}")
    print("Lose")
elif user == "Scissor" and computer[num]== "Paper":
    print(f"Computer : {computer[num]}")
    print("Win!")
elif user == "Scissor" and computer[num]== "Scissor":
    print(f"Computer : {computer[num]}")
    print("Drow!")

print(f"final : {computer[num]}")

