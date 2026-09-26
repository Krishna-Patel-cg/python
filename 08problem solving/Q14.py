cost_price,sell_price =map(int,input("Enter please price").split())
if cost_price<sell_price:
    print("Profit")
elif cost_price>sell_price:
    print("Loss")
else:
    print("No profit and no loss")