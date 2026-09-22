cbudget=0
cregular=0
cpremium=0
cluxury=0
for i in range(1,9):
    product=input("Enter price")
    if product<500:
        cbudget+=1
        print("Budget")
    elif 500<=product<2000:
        cregular+=1
        print("Regular")
    elif 2000<=product<5000:
        cpremium+=0
        print("Premium")
    else:
        cluxury+=1
        print("Luxury")
print(f"number of product in budget -> {cbudget}")
print(f"number of products in regular -> {cregular}")
print(f"number of products in premium -> {cpremium}")
print(f"number of product in luxury -> {cluxury}")