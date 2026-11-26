add=1
def addition(n):
    global add
    add *=n
    if (n==5):
        return add
    return addition(n+1)
print(addition(1))