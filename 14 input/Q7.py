
balance = 5000.0
withdrawal = float(input("Enter withdrawal amount (₹): "))

while withdrawal <= 0 or withdrawal > balance:
    if withdrawal <= 0:
        print("Invalid amount! Withdrawal must be greater than zero.")
    else:
        print(f"Insufficient funds! Available balance is ₹{balance:.2f}.")
    withdrawal = float(input("Enter withdrawal amount (₹): "))
balance -= withdrawal
print(f"\nWithdrawal successful! Amount withdrawn: ₹{withdrawal:.2f}")
print(f"Remaining balance: ₹{balance:.2f}")

    
