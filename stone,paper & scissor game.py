import random

a = input("Enter your choice: ")
x = ["s", "p", "sc"]
y = random.choice(x)

print("mychoice:",y)

if a==y:
    print("its a tie")
elif (a== "sc" and y=="p" or a=="s" and y=="p"):
    print("you win")
elif (a=="p" and y=="sc" or a=="p" and y=="s"):
    print("you win")
else:
    print("invalid choice. please enter s,sc and p")