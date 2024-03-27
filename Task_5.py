

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
print(max(a))
if min(a) == 0:
    print("Yes")
else:
    print("No")