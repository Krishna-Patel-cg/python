bill=int(input("Enter your electric bill unit"))
if bill>=1 and bill<100:
    eb1=bill*5
    print(f"Under 100units  {eb1}")
elif bill<=200:
    eb3=500+(bill-100)*7
    print(f"Under 200units  {eb3}")
elif bill<=300:
    eb3=1200+(bill-200)*10
    print(f"Under 300units  {eb3}")
