def num(n):
    if n==0:
        print("Done!")
        return
    print(n)
    num(n-1)
num(3)