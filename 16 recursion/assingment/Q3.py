def count(n):
    if n == 4:
        print("End")
        return
    print("Start",n)
    count(n + 1)
    print("Back",n)
count(2)