# 90 points and above (A),
# 80-89 (B),
# 70-79 (C),
# 60-69 (D),
# below 60 (F).

g = int(input("Enter a number: "))

if g >= 90:
	print("A")

elif g < 90 and g > 79:
	print("B")

elif g < 80 and g > 69:
	print("C")

elif g < 70 and g > 59:
	print("D")

else:
	print("F")