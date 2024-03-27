num = (input("Enter a number: "))

a = int(num[0])
b = int(num[1])
c = int(num[2])

if a+c > b:
	print(">")

elif a+c == b:
	print("=")

else:
	print("<")
	