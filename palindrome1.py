num=int(input("enter the number:"))
temp=num,#original number save kar diya
reverse=0

while num>10:
	digit=num%10  #last digit niklena
	reverse=reverse*10+digit  #reverse banana
	num=num//10  #last digit hata dena 
print(f"original :{temp}")
print(f"ulta :{reverse}")

if temp==reverse:
	print("ye palindrome number hai !")
else:
	print("ye palindrome number nahi hai !")