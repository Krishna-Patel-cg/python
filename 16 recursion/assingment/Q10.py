def power(n,m):
    if n==0:
        return 1
    print(n**m)
power(2,3)



def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)
print(power(3, 3))