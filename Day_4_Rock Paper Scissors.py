import random
print("Welcome to Rock, Paper or Scissor Game.")

Computers = [0,1,2]
poster =[
        '''
            _______
        ---'    ___)_
                _____)
                _____)
                (___)
        ---.___(__)
        '''
        ,'''
            ______
        ---'   ___)_____
                   _____)
                    _____)
                    ___)
        ---._________)
        '''
        ,'''
            _______
        ---'    ___)___
                  _____)
                ________)
                (___)
        ---.___(__)
        '''
]


num = random.randint(0,2)
user = int(input("Enter Your Choice 0 for 0, 1 for 1 and 2 for 2: "))
print(poster[user])
if user == num:
    print("Computer Chose:")
    print(poster[num])
    print("Drow")
elif user == 0 and num== 1:
    print("Computer Chose:")
    print(poster[num])
    print("You Lose")
elif user == 0 and num== 2:
    print("Computer Chose:")
    print(poster[num])
    print("You Win!")
elif user == 1 and num== 0:
    print("Computer Chose:")
    print(poster[num])
    print("You Win!")
elif user == 1 and num== 2:
    print("Computer Chose:")
    print(poster[num])
    print("You Lose!")
elif user == 2 and num== 0:
    print("Computer Chose:")
    print(poster[num])
    print("You Lose")
elif user == 2 and num== 1:
    print("Computer Chose:")
    print(poster[num])
    print("You Win!")



