print("===Temperature convert===")
print("1.celsius to fahrenheit")
print("2.faherenheit to celsius")

choice=input("kya convert karna hai ? 1,2:")
temp=float(input("Temperature daalo :"))
if choice=="1":
	result=(temp*9/5)+32
	print(f"{temp}•c={result:.2f}•f")
elif choice=="2":
	result=(temp-32)*5/9
	print(f"{temp}•f={result:.2f}•c")
else:
	print("galat option!")