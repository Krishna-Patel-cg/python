amount=int(input("Enter your ammount and ckeck your discount"))
if amount<500:
    print(f"{amount} discount is 0%")
elif amount>=500 and amount<1000:
    print(f"{amount} dicount is 5%")
elif amount>=1000 and amount<1999:
    print(f"{amount} dicount is 10%")
elif amount>=2000 and amount<4999:
    print(f"{amount} dicount is 15%")
else:
    print(f"{amount} discount is 20%")