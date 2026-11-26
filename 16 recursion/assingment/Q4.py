def answer(n):
    if n == 0:
        return n + answer(n - 1)
    print(n)
print(answer(3))