import random
small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','*','(',')','+']

print("Welcome to the PyPassword Generator!")
nr_s_letters = int(input("How many Small letters would you like your password_list?\n"))
nr_c_letters= int(input("How many Capital letters would you like your password_list?\n"))
nr_symbols = int(input("How many symbols would you like your password_list?\n"))
nr_numbers = int(input("How many Numbers would you like your password_list?\n"))

password_list=[]
password = ""

for char in range(0, nr_s_letters):
    password_list.append(random.choice(small_letters))
for char in range(0, nr_c_letters):
    password_list.append(random.choice(capital_letters))
for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
for char in password_list:
    password += char

print(password)


