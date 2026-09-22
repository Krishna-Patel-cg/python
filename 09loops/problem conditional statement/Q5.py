cshort=0
cmedium=0
clong=0
for i in range(0,5):
    para=input("Write a paragraph")

    if len(para)<=3:
        cshort+=1
        print("Short" ,end="")
    elif 4<= (len(para)) <=6:
        cmedium+=1
        print("Medium",end="")
    else:
        clong+=1
        print("Long",end="")
print(f"number of short paragraph -> {cshort}")
print(f"number of medium paragraph -> {cmedium} ")
print(f"number of long paragraph ->{clong}")