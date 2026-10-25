num = list(map(int, input("Enter number: ").split()))
i = 0
while i < len(num):
    if num[i] < 0:
        break
    print(num[i], end=" ")
    i += 1