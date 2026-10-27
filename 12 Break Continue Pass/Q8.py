str= input("Enter your name: ").strip().lower()
index = 0
while index < len(str):
    if str[index] == "o":
        print("Found")
        break
    index += 1
else:
    print("Not found")