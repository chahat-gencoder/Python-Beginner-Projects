import random
n=random.randint(1,10)
g=int(input("1 se 10 tak number guess karo:"))
if g==n:
	print("shabash ! sahi jawab")
else:
	print("galat.sahi number:",n)