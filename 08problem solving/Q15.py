cost_price,sell_price =map(int,input("Enter please price").split())
if cost_price<sell_price:
    profit=sell_price-cost_price
    profit_per=(profit/cost_price)*100
    print(f"Busnessman profit {profit_per}%")
elif cost_price>sell_price:
    loss=cost_price-sell_price
    profit_per=(loss/cost_price)*100
    print(f"Busnessman loss {profit_per}%")
else:
    print("p")