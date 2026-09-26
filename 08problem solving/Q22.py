account_balence,withdrawal_balence=map(int,input("Enter your ammount").split()[:2])
if account_balence>withdrawal_balence and withdrawal_balence>0 and withdrawal_balence%100==0 and account_balence-withdrawal_balence>=500:
    remain=account_balence-withdrawal_balence
    print(f"""Withdrawal successful
    Remaining balence {remain}""")
else:
    print("Withdrawal unsuccessful")