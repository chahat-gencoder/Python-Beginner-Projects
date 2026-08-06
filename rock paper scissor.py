import random
options=["rock","paper","scissor"]
print("===rock paper scissor===")
user=input("chuno: rock,paper,scissor").lower()
computer=random.choice(options)
print(f"computer ne chuna :{computer}")
if user==computer:
	print("Draw!")
elif (user=="rock"and computer=="scissor")or(user=="paper"and computer=="rock")or(user=="scissor"and computer=="paper"):
	print("Tum jeet gaye!")
else:
	print("computer jeet gaya!")