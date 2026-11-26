def mystery(n):
    if n <= 1:
        return n

    return mystery(n - 1) + mystery(n - 2)
print(mystery(7))
print(mystery(2))
print(mystery(1))